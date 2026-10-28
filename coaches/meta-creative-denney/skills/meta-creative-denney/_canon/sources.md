# Sources, corpus and accuracy notes (meta-creative-denney, v0.1)

## Tag legend
- [YT:<id>] → https://www.youtube.com/watch?v=<id>
- (YYYY-MM) = upload month (exact upload dates pulled from YouTube).
- NOW = evidence from a 2026 video ("working now"). EVERGREEN = a 2025 top performer. BOTH = said in both years.
- DTC = depends on a physical product, purchase, discount, catalog or unboxing. GEN = any advertiser. LEADGEN = services / lead gen. APP = apps.
- [quote src: YT:<id>] = the quoted words were found verbatim in that video rather than in the bullet's main sources.
- [caption-fixed] = an obvious auto-caption error was corrected inside the quote.
- (guest: Name) / (speaker unclear) = technique only; never voice it as one of the five.

## What the corpus is (pulled Oct 6, 2026)
- 124 videos, 52.6 hours, 675K caption words, 3,277 sourced items (992 rules, 461 ad examples, 378 frameworks, 368 opinions, 291 analysis moves, 217 data points, 133 "what changed" items).
- Dara Denney: 28 videos (18 from 2026, 10 top 2025), 632 items. Primary voice.
- Fraser Cottrell: 50 videos (36 / 14), 970 items.
- Sarah Levinger: 24 videos (22 / 2), 735 items.
- Alex Cooper: 16 videos (12 / 4), 419 items.
- Barry Hott: 6 videos led by him plus appearances on Denney's and Cooper's channels (4 / 2), 307 items.
- Guests (Harry Delmege, Mirella Crespi, Anze Mikac, Danil Saliukov, Taylor Holiday and others): 195 items; speaker unclear: 19.
- Era split: 2,214 items from 2026 videos, 1,063 from 2025 top performers.
- Vertical split: 2,070 GEN, 1,188 DTC, 17 LEADGEN, 2 APP. Lead-gen-specific evidence is thin.

## Selection rules
- Long-form only (3 min+), no Shorts. Topics: ad creative (formats, statics, video/UGC, hooks, copy, testing, creative strategy, AI ad production). Skipped: career/hiring, pure media buying, CRO/landing pages, business vlogs (list in catalog.tsv, column skip_reason).
- 2026: every qualifying video. 2025: top third per creator by views per day since upload (minimum 3).

## Accuracy notes
- Transcripts are YouTube auto-captions without speaker labels. In interviews and panels, items were attributed by context; unclear lines are marked.
- Every quoted fragment was machine-checked against the transcripts (2,119 quotes, all found; 15-word cap). Quotes that could not be found were turned into paraphrase.
- "What converts" here is creator-reported, mostly from DTC client accounts. Not verified data, not controlled tests.
- Tool and model claims change month to month; every one carries its date.
- Not in the corpus: courses, paid communities, newsletters, X/LinkedIn posts, the ads shown on screen (only what was said about them).

## Database
On Ivan's Mac: ~/ultimate coach pack/meta-creative-corpus/ — catalog.tsv (all 208 candidate videos, selection, reason), items.tsv (3,277 items: theme, type, speaker, vertical, video, date, era, content), raw/ (124 transcripts), extract/ (per-bundle evidence), themes/L1/ (consolidated digests).
