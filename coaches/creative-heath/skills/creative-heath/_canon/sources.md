# Sources — Ben Heath coach

Corpus pulled Oct 6–7, 2026. Tags: era NOW = 2026, EVERGREEN = 2025, ALLTIME = before 2025. Cite as [YT:id] = youtube.com/watch?v=id.

## This coach's numbers
- Videos with transcripts: 24 (7.3 h, 98,760 words); 24 on own channel, 0 guest appearances. Dates 2019-07-09 to 2026-07-20.
- By era (videos): NOW 6, EVERGREEN 7, ALLTIME 11.
- Sourced items spoken by Ben Heath: 341 (NOW 78, EVERGREEN 114, ALLTIME 149); 32 VISUAL (on-screen ad descriptions).
- By vertical: GEN 230, DTC 45, LEADGEN 62, APP 4.
- By theme: TEST 54, COPY 52, FORMAT 48, VIDEO 33, AI 27, STRAT 27, STATIC 24, PLATFORM 21, HOOK 19, BIO 14, PROD 13, VOICE 9.

## How the corpus was built
- Selection: every 2026 upload (era NOW), the top 2025 uploads by views-per-day (EVERGREEN), and the all-time top uploads before 2025 (ALLTIME) from each creator's own channel; plus guest appearances on Motion and other channels where the creator is the main speaker. Shorts, livestream replays without topic, and off-topic videos skipped.
- Metadata: exact dates, views and durations from YouTube's own player data (pulled Oct 2026).
- Transcripts: YouTube auto-captions (English). Pulled via yt-dlp; when YouTube blocked the workspace, caption URLs were resolved on Ivan's Mac and downloaded from the workspace. Auto-captions mis-hear names and numbers; items marked [caption-fixed] were corrected from context.
- Extraction: each transcript read in full by a model and split into sourced items `[THEME|TYPE|SPEAKER|VERTICAL] content — [YT:id]`. Types include CLAIM, FRAMEWORK, STEP, EXAMPLE, RESULT, NUMBER, SCRIPT, HOOK, OPINION, VISUAL.
- VISUAL items: for the top breakdown videos, YouTube storyboard frames (320x180 thumbnails, every few seconds) were read alongside the transcript to describe the ads shown on screen. Low resolution: layouts, text overlays and shot types are reliable; small print is not.
- Canon: items consolidated by theme, then drafted into canon files. Every quoted fragment (in double quotes) was checked word-for-word against the raw transcript of the cited video; quotes that failed were corrected or turned into paraphrase. Quotes are capped at 15 words.

## Accuracy notes
- "Converts", "won", "scaled" are creator-reported results from their own or client accounts. Not audited, rarely with spend context.
- Platform behavior (Andromeda, GEM, Lattice, Advantage+) and AI tools change month to month. Every such claim is dated by the video date.
- The corpus is DTC-heavy (3,425 DTC items vs 272 lead-gen items across all 7,797). Lead-gen transfer is an inference unless an item is tagged LEADGEN.
- Not in the corpus: courses, paid communities, newsletters, X/LinkedIn posts, podcasts not on YouTube. Absence from the canon is not proof a creator never said something.

## Database
- Ivan's Mac: `~/ultimate coach pack/meta-creative-corpus/` — `meta/catalog.tsv` (every candidate video, why selected or skipped), `meta/items.tsv` (all 7,797 sourced items, filterable by theme/type/speaker/vertical/era), `raw/` (transcripts), `extract/` (per-bundle extraction), `visual/notes/` (storyboard reads), `coaches/` and `aggregate/` (canon).

The counts above cover the 24 videos where this creator is a listed main speaker. The list below also includes 0 videos on other channels where items are attributed to them, and 4 videos cited only for another speaker's position (disagreements, guests).

## Video list (newest first)
| Date | Era | Channel | Role | YT id | Title |
|---|---|---|---|---|---|
| 2026-08-13 | NOW | Dara Denney | cited for another speaker | KmbEjy0UBT8 | I Ranked 51 Meta Ad Creative Types (Tier List) |
| 2026-07-20 | NOW | Ben Heath | main | wwdvrZBjock | Meta's CMO on AI Ads and Rising Meta Ad Costs |
| 2026-07-14 | NOW | Ben Heath | main | TpZrPY6jTE8 | How To Make AI Ads With Claude X Meta |
| 2026-03-24 | NOW | Ben Heath | main | mMKLLRTk-7c | How To Use Creative Enhancements on Your Facebook Ads |
| 2026-03-10 | NOW | Ben Heath | main | bAo6SICFyIE | Copy This EXACT Facebook Ad, It'll Blow Up Your Results |
| 2026-03-03 | NOW | Ben Heath | main | 8dJxOaZrK1M | Copy This Meta Ads Testing Strategy for Better Results |
| 2026-02-10 | NOW | Ben Heath | main | onFwSud9C2Y | The NEW WAY To Test Facebook Ads (Post Andromeda) |
| 2025-11-04 | EVERGREEN | Ben Heath | main | _MIWfyD91yc | I found a BETTER way to create Meta video ads (using AI) |
| 2025-10-17 | EVERGREEN | Ben Heath | main | M2VReAjHiN8 | I found an AI tool that makes winning Facebook Ad ideas! |
| 2025-09-23 | EVERGREEN | Ben Heath | main | IRyR9PzSnM8 | Copy This Meta Ads Strategy, It'll Blow Up Your Business |
| 2025-06-03 | EVERGREEN | Motion (Creative Analytics) | cited for another speaker | lf0Y4hBVih8 | How to Use AI for UGC Content Creation - The COMPLETE 2025 Framework |
| 2025-05-27 | EVERGREEN | Ben Heath | main | D6Sxk8Mbkq4 | How I Made £2.7M with Facebook Ads in 90 Days (Full Breakdown) |
| 2025-05-20 | EVERGREEN | Ben Heath | main | fBrC1_VPTRU | How To Use The NEW Creator Marketplace For Meta Ads |
| 2025-05-13 | EVERGREEN | Ben Heath | main | M36tVQD26TY | This Facebook Ad Format Gets Insane Results (and nobody uses it!) |
| 2025-04-29 | EVERGREEN | Barry Hott | cited for another speaker | RVRRGf746Bw | Unlock the Hidden Systems Behind $1B+ in Ad Spend with Charles Tichenor IV |
| 2025-02-04 | EVERGREEN | Ben Heath | main | GPp8Y-lKzJw | The BEST Facebook Ads Format (Based On Data) |
| 2024-10-22 | ALLTIME | Ben Heath | main | z3LiJ0PbY-0 | The NEW Facebook Ad Creative Strategy that DOUBLES Results |
| 2024-03-14 | ALLTIME | Fraser Cottrell | cited for another speaker | NNg9-TDiFDA | My Ultimate Meta Ad Creative Framework / Unlimted Creative Ideas |
| 2023-11-07 | ALLTIME | Ben Heath | main | Tkl3hhNu8_I | New AI Tools That Make Facebook Ads EASY! |
| 2023-09-20 | ALLTIME | Ben Heath | main | KgO_J6pwv9I | The EASY Way To Create Facebook Ads That Convert (Full Tutorial) |
| 2023-02-21 | ALLTIME | Ben Heath | main | N3X8CuD_VQk | The BEST Facebook Ad FORMAT (NEW DATA) |
| 2022-02-22 | ALLTIME | Ben Heath | main | 4mZ3F77dNdI | Copy This Facebook Ad To Guarantee Success |
| 2021-03-30 | ALLTIME | Ben Heath | main | sxQwH4kjGW4 | Should You Use Dynamic Creative with Facebook Ads? |
| 2021-03-11 | ALLTIME | Ben Heath | main | dwUxmlgWfxQ | How To Test New Facebook Ad Creative The RIGHT Way! |
| 2021-01-21 | ALLTIME | Ben Heath | main | 1EQrp8MJRek | 7 Facebook Ad Copy Techniques That WORK |
| 2020-07-28 | ALLTIME | Ben Heath | main | E0lbvr71wR8 | Facebook Advertising Psychology - How To Guarantee Success |
| 2020-07-06 | ALLTIME | Ben Heath | main | HzDJpKu7vew | Get 50% More Conversions With THIS Facebook Ad Creative Strategy |
| 2019-07-09 | ALLTIME | Ben Heath | main | WeQrKeAwZDg | 6 SUCCESSFUL FACEBOOK ADS TO COPY |
