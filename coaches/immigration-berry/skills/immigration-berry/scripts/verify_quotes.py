#!/usr/bin/env python3
"""Check every quoted line in a draft against the coach's transcripts before delivery.

Usage: python3 verify_quotes.py draft.md
Finds text inside "double quotes" or “curly quotes” with 5+ words and checks it appears in the corpus
(case, punctuation and filler-insensitive). Prints OK / NOT FOUND per quote, and which [YT:id] holds it.
Any NOT FOUND quote must be removed or turned into an unquoted paraphrase before the reply goes out.
"""
import gzip, json, os, re, sys

HERE = os.path.dirname(os.path.abspath(__file__))
CORPUS = os.path.join(os.path.dirname(HERE), "corpus")


def norm(s):
    s = s.lower().replace("’", "'")
    s = re.sub(r"\b(um+|uh+|like|you know)\b", " ", s)
    return " ".join(re.findall(r"[a-z0-9']+", s))


def main():
    if len(sys.argv) < 2 or sys.argv[1] in ("-h", "--help") or not os.path.isfile(sys.argv[1]):
        print(__doc__); sys.exit(0 if len(sys.argv) > 1 and sys.argv[1] in ("-h", "--help") else 2)
    text = open(sys.argv[1], encoding="utf-8").read()
    # only attributed quotes: a [YT:id] or [canon] tag within 160 chars after the closing quote,
    # or a "says/said/calls it/in his words/in her words" marker just before it. Ad copy in quotes is skipped.
    quotes = []
    spans = list(re.finditer(r'“([^“”\n]{12,400})”', text)) + list(re.finditer(r'"([^"\n]{12,400})"', text))
    for m in spans:
        q = m.group(1)
        after, before = text[m.end():m.end() + 160], text[max(0, m.start() - 60):m.start()].lower()
        if len(q.split()) >= 4 and (re.search(r"\[(YT:|canon)", after) or
                                    re.search(r"(says|said|calls it|puts it|in (his|her|their) words|quote)\W*$", before)):
            quotes.append(q)
    if not quotes:
        print("No quotes to verify."); return
    docs = {}
    for fn in ("passages.jsonl.gz", "items.jsonl.gz"):
        p = os.path.join(CORPUS, fn)
        if not os.path.exists(p):
            continue
        for line in gzip.open(p, "rt", encoding="utf-8"):
            r = json.loads(line)
            docs.setdefault(r.get("id", "") or "canon", []).append(r["text"])
    joined = {k: norm(" ".join(v)) for k, v in docs.items()}
    bad = 0
    for q in quotes:
        nq = norm(q.strip(" .,…"))
        hit = next((k for k, t in joined.items() if nq and nq in t), None)
        if hit:
            print(f"OK         [YT:{hit}] \"{q[:80]}\"")
        else:
            bad += 1
            print(f"NOT FOUND  \"{q[:80]}\"  -> if attributed to the coach: drop the quote marks or the line; if it is draft copy for Ivan: fine")
    print(f"\n{len(quotes) - bad}/{len(quotes)} quotes verified.")
    sys.exit(1 if bad else 0)


if __name__ == "__main__":
    main()
