#!/usr/bin/env python3
"""Coach corpus search. Stdlib only.

Searches two layers shipped with the coach:
  items   - sourced, attributed extract items (rules, moves, stories, numbers)
  raw     - full transcript passages (~250 words), may include other speakers

First run builds a SQLite FTS5 index in a cache dir (one-time, ~10-60 s on big corpora).

Usage:
  python3 search.py "value based pricing objection too expensive"
  python3 search.py "hierarchy squint test" --layer items --k 15
  python3 search.py "logo critique" --layer raw --k 8 --chars 1400
  python3 search.py --doc YT_ID                       # first 6000 chars of one transcript
  python3 search.py --doc YT_ID --around "too expensive"   # text around a phrase
  python3 search.py --doc YT_ID --offset 6000         # next page
  python3 search.py '"exact phrase" other words'      # quoted phrase is required
  python3 search.py --stats
"""
import argparse, gzip, json, os, re, sqlite3, sys, tempfile, hashlib

HERE = os.path.dirname(os.path.abspath(__file__))
CORPUS = os.path.join(os.path.dirname(HERE), "corpus")


def cache_path():
    sig = hashlib.md5(CORPUS.encode()).hexdigest()[:10]
    for f in ("items.jsonl.gz", "passages.jsonl.gz"):
        p = os.path.join(CORPUS, f)
        if os.path.exists(p):
            sig += str(int(os.path.getmtime(p))) + str(os.path.getsize(p))
    sig = hashlib.md5(sig.encode()).hexdigest()[:12]
    base = os.environ.get("COACH_CACHE") or tempfile.gettempdir()
    return os.path.join(base, f"coach-index-{sig}.db")


def build(db):
    tmp = f"{db}.{os.getpid()}.part"
    if os.path.exists(tmp):
        os.remove(tmp)
    c = sqlite3.connect(tmp)
    c.execute("CREATE VIRTUAL TABLE t USING fts5(body, layer UNINDEXED, src UNINDEXED, "
              "title UNINDEXED, date UNINDEXED, tags UNINDEXED, tokenize='porter unicode61')")
    n = 0
    for layer, fn in (("items", "items.jsonl.gz"), ("raw", "passages.jsonl.gz")):
        p = os.path.join(CORPUS, fn)
        if not os.path.exists(p):
            continue
        rows = []
        with gzip.open(p, "rt", encoding="utf-8") as f:
            for line in f:
                r = json.loads(line)
                rows.append((r["text"], layer, r.get("id", ""), r.get("title", ""),
                             r.get("date", ""), r.get("tags", "")))
                if len(rows) >= 5000:
                    c.executemany("INSERT INTO t VALUES (?,?,?,?,?,?)", rows); n += len(rows); rows = []
        if rows:
            c.executemany("INSERT INTO t VALUES (?,?,?,?,?,?)", rows); n += len(rows)
    c.commit(); c.close()
    os.replace(tmp, db)
    return n


def connect():
    db = cache_path()
    if not os.path.exists(db):
        sys.stderr.write("Building search index (one-time)...\n")
        # another process may be building it: the rename is atomic, so a finished db is always complete
        n = build(db)
        sys.stderr.write(f"Indexed {n} rows.\n")
    return sqlite3.connect(db)


STOP = set("the a an and or of to in on for with is are be it this that i you we my our your how what why do does".split())


def fts_query(q):
    words = [w for w in re.findall(r"[A-Za-z0-9']+", q.lower()) if w not in STOP]
    if not words:
        words = re.findall(r"[A-Za-z0-9']+", q.lower())
    phrases = re.findall(r'"([^"]+)"', q)
    q2 = re.sub(r'"[^"]+"', ' ', q)
    words = [w for w in re.findall(r"[A-Za-z0-9']+", q2.lower()) if w not in STOP] or words
    ors = " OR ".join(f'"{w}"' for w in words) if words else ""
    req = " AND ".join(f'"{p}"' for p in phrases)
    if req and ors:
        return f"({req}) AND ({ors})"
    return req or ors


def search(q, layer, k, chars, tag, _loose=False):
    c = connect()
    sql = "SELECT body, layer, src, title, date, tags, bm25(t) FROM t WHERE t MATCH ?"
    args = [" OR ".join(f'"{p}"' for p in re.findall(r'"([^"]+)"', q)) if _loose else fts_query(q)]
    if layer != "both":
        sql += " AND layer = ?"; args.append(layer)
    if tag:
        sql += " AND tags LIKE ?"; args.append(f"%{tag.upper()}%")
    sql += " ORDER BY bm25(t) LIMIT ?"; args.append(k * 3)
    seen, out, heads, canon = {}, [], set(), 0
    has_primary = c.execute("SELECT count(*) FROM t WHERE layer='raw' OR tags NOT LIKE '%CANON%'").fetchone()[0] > 0
    for body, lay, src, title, date, tags, score in c.execute(sql, args):
        if lay == "raw" and seen.get(src, 0) >= 2:  # max 2 passages per video
            continue
        h = re.sub(r"[^a-z0-9]", "", body.lower())[:70]
        if h in heads:
            continue
        if has_primary and "CANON" in (tags or ""):
            if canon >= 2:
                continue
            canon += 1
        heads.add(h)
        seen[src] = seen.get(src, 0) + 1
        out.append((body, lay, src, title, date, tags))
        if len(out) >= k:
            break
    for i, (body, lay, src, title, date, tags) in enumerate(out, 1):
        ref = f"[YT:{src}]" if src else "[canon]"
        head = f"[{i}] {lay.upper()} {ref} {title}" + (f" ({date})" if date else "")
        if tags:
            head += f" {{{tags}}}"
        txt = body if len(body) <= chars else body[:chars] + " ..."
        print(head + "\n" + txt + "\n")
    if not out and '"' in q and not _loose:
        print("(no row has the exact phrase together with the other words; showing matches for the phrase alone)\n")
        return search(q, layer, k, chars, tag, _loose=True)
    if not out:
        print("No hits. Rephrase with the creator's own words (concrete nouns, not abstractions).")


def doc(yid, around=None, chars=6000, offset=0):
    p = os.path.join(CORPUS, "passages.jsonl.gz")
    parts = []
    with gzip.open(p, "rt", encoding="utf-8") as f:
        for line in f:
            r = json.loads(line)
            if r.get("id") == yid:
                parts.append((r.get("seq", 0), r))
    if not parts:
        print("Not found."); return
    parts.sort(key=lambda x: x[0])
    r0 = parts[0][1]
    full = " ".join(r["text"] for _, r in parts)
    print(f"[YT:{yid}] {r0.get('title','')} ({r0.get('date','')}) — {len(full.split())} words total\n")
    if around:
        hits = [m.start() for m in re.finditer(re.escape(around.lower()), full.lower())]
        if not hits:
            print(f"Phrase not found: {around}"); return
        for i, h in enumerate(hits[:5], 1):
            a, b = max(0, h - chars // 2), min(len(full), h + chars // 2)
            print(f"--- match {i}/{len(hits)} at char {h} ---\n...{full[a:b]}...\n")
        return
    seg = full[offset:offset + chars]
    print(seg)
    if offset + chars < len(full):
        print(f"\n[... {len(full) - offset - chars} more chars; continue with --offset {offset + chars}]")


def stats():
    c = connect()
    for lay, n in c.execute("SELECT layer, count(*) FROM t GROUP BY layer"):
        print(lay, n)


if __name__ == "__main__":
    import signal
    signal.signal(signal.SIGPIPE, signal.SIG_DFL)
    ap = argparse.ArgumentParser()
    ap.add_argument("query", nargs="?")
    ap.add_argument("--layer", default="both", choices=["both", "items", "raw"])
    ap.add_argument("--k", type=int, default=12)
    ap.add_argument("--chars", type=int, default=900)
    ap.add_argument("--tag", default="")
    ap.add_argument("--doc")
    ap.add_argument("--around", help="with --doc: show text around this phrase")
    ap.add_argument("--offset", type=int, default=0, help="with --doc: start char")
    ap.add_argument("--stats", action="store_true")
    a = ap.parse_args()
    if a.stats:
        stats()
    elif a.doc:
        doc(a.doc, a.around, a.chars if a.chars != 900 else 6000, a.offset)
    elif a.query:
        search(a.query, a.layer, a.k, a.chars, a.tag)
    else:
        ap.print_help()
