# /voss _canon — Index (v2, URL-verified)

This folder holds the canonical reference material AIVoss loads on demand. SKILL.md is the lean router; this folder is the depth.

**v2 changes:** public_corpus_excerpts.md is now URL-verified — every Voss quote in it ties back to a live link on his own company blog or an official long-form interview page. Added `free_authored_articles.md` as a working URL catalogue of all Voss-authored free public content.

---

## Files in this folder

| File | What it contains | Source type | When to load |
|------|-----------------|-------------|--------------|
| `never_split_the_difference_frameworks.md` | Chapter-by-chapter framework map for NSTD (2016). Mechanism + execution rule + failure mode for each of 11 named frameworks. Own-words descriptions. | Book-derived framework summary (facts, not reproduction) | Framework deep-dive, diagnostic decisions, prep work |
| `full_fee_agent_frameworks.md` | Framework map for The Full Fee Agent (Voss + Shull, 2022). Service-business pricing applications of NSTD tactics. | Book-derived framework summary (facts, not reproduction) | Agency pricing, retainer defense, discount pushback, full-fee positioning |
| `public_corpus_excerpts.md` *(v2)* | Short fair-use quotes from Voss's own blog (blackswanltd.com) and verified long-form interview pages, each with URL. Voice-calibration reference. | Author-owned blog content (fair-use short quotes) + verified interview episode pages | Voice calibration when responding "as Voss"; sourcing publishable quotes |
| `free_authored_articles.md` *(new in v2)* | URL catalogue of all verified free Voss content — BSG blog by topic, Lex Fridman / Huberman episode pages, TED, MasterClass, major podcast appearances. | Working URL catalogue | Whenever Ivan asks "where does Voss say X?" — surface the URL |
| `_index.md` | This file. | Index | Read first if unsure which file to load |

---

## Framework → file mapping

Use this table to know which canon file to load for which incoming Ivan question.

| If Ivan asks about... | Load this file |
|----------------------|----------------|
| Tactical empathy, mirrors, labels | `never_split_the_difference_frameworks.md` (Frameworks 1-3), then `public_corpus_excerpts.md` (sections A1-A5) |
| Accusation audit, preempting objections | `never_split_the_difference_frameworks.md` (Framework 4), then `public_corpus_excerpts.md` (section A4) |
| Yes vs No, "no" as safety | `never_split_the_difference_frameworks.md` (Framework 5) |
| "That's right" vs "you're right" | `never_split_the_difference_frameworks.md` (Framework 6), then `public_corpus_excerpts.md` (section A1) |
| Loss aversion, anchoring, non-round numbers | `never_split_the_difference_frameworks.md` (Framework 7) |
| Calibrated questions ("how", "what") | `never_split_the_difference_frameworks.md` (Framework 8), then `public_corpus_excerpts.md` (section A6) |
| 7-38-55 rule, Rule of Three, Pinocchio Effect | `never_split_the_difference_frameworks.md` (Framework 9) |
| Ackerman Model (price bargaining math) | `never_split_the_difference_frameworks.md` (Framework 10), then `public_corpus_excerpts.md` (section A9 — note: bargaining is Plan B, not Plan A) |
| Black Swans (unknown unknowns hunt) | `never_split_the_difference_frameworks.md` (Framework 11), then `public_corpus_excerpts.md` (section A8) |
| The word "fair" being thrown at Ivan | `public_corpus_excerpts.md` (section A7) — primary load |
| Discount pushback / fee defense / Case Flow pricing | `full_fee_agent_frameworks.md` (Frameworks A-D), then `public_corpus_excerpts.md` (section A9) |
| ICP / positioning / "fishing where the fish are" | `full_fee_agent_frameworks.md` (Framework E) |
| Existing client cancel / pause / renegotiate | `full_fee_agent_frameworks.md` (Framework F) |
| Voice / cadence / verbal style | `public_corpus_excerpts.md` (section C) |
| "Where can I read Voss on X?" | `free_authored_articles.md` (surface the URL) |
| Quoting Voss in published DR material | `public_corpus_excerpts.md` (find candidate quote) + `free_authored_articles.md` (verify URL) |

---

## Sourcing standards

**What's in these files:**
- Framework structures (NAMES, STEPS, MECHANISMS, FAILURE MODES) — facts, described in own words
- Chapter references for NSTD and Full Fee Agent — so Ivan can read Voss's own prose
- Short fair-use quotes from Voss's author-owned blog at `blackswanltd.com` and `blog.blackswanltd.com`, each with URL attribution
- URLs to verified free public sources (BSG blog, Lex Fridman page, Huberman Lab page, TED, MasterClass)
- Mechanical applications calibrated to DR's business

**What's NOT in these files:**
- Reproduced book paragraphs, chapters, or sections
- Paraphrased book content presented as Voss's own words
- Long verbatim transcript excerpts beyond fair use
- Pirated PDF / audiobook content from any source

**If Ivan asks for "the actual book chapter":** the answer is buy the book and use `free_authored_articles.md` for the free supplementary content. These files are operator-grade framework maps. Voss's prose is in his books and his recorded talks.

---

## Load policy

Default: load nothing at session start. Load on demand based on the framework→file table above.

If multiple files are needed, load in this order:
1. `_index.md` (this file)
2. The specific framework file (NSTD or Full Fee Agent)
3. `public_corpus_excerpts.md` for voice + verified quote sourcing
4. `free_authored_articles.md` only when surfacing a URL for Ivan to read

Do not load all four files unless explicitly asked to.

---

## Version notes

**v1 (initial build):** Framework files + public_corpus_excerpts.md with pattern-attributed signature phrases.

**v2 (URL-verified enrichment):**
- Replaced pattern-attributed phrases in public_corpus_excerpts.md with short fair-use quotes from verified Voss-authored blog content, each citing a live URL
- Added `free_authored_articles.md` as a working URL catalogue of all verified free Voss content
- Updated this index to reflect the new file and the v2 mapping

**Future:** when more Voss content becomes accessible (new book, new keynote, new long-form interview), update `free_authored_articles.md` with the URL, and add a short fair-use quote to `public_corpus_excerpts.md` if the new content introduces a new framework or signature phrase.
