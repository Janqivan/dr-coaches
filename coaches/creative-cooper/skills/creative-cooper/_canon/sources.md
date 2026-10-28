# Sources — Alex Cooper coach

Corpus pulled Oct 6–7, 2026. Tags: era NOW = 2026, EVERGREEN = 2025, ALLTIME = before 2025. Cite as [YT:id] = youtube.com/watch?v=id.

## This coach's numbers
- Videos with transcripts: 27 (18.3 h, 219,742 words); 27 on own channel, 0 guest appearances. Dates 2023-11-24 to 2026-08-19.
- By era (videos): NOW 12, EVERGREEN 6, ALLTIME 9.
- Sourced items spoken by Alex Cooper: 711 (NOW 350, EVERGREEN 167, ALLTIME 194); 48 VISUAL (on-screen ad descriptions).
- By vertical: GEN 423, DTC 282, LEADGEN 6, APP 0.
- By theme: AI 171, STATIC 104, STRAT 96, VIDEO 76, TEST 62, PROD 61, COPY 49, FORMAT 45, BIO 19, HOOK 14, VOICE 8, PLATFORM 6.

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

The counts above cover the 27 videos where this creator is a listed main speaker. The list below also includes 2 videos on other channels where items are attributed to them, and 9 videos cited only for another speaker's position (disagreements, guests).

## Video list (newest first)
| Date | Era | Channel | Role | YT id | Title |
|---|---|---|---|---|---|
| 2026-08-19 | NOW | Alex Cooper | main | 9O3-AdYpwyQ | The Facebook Ads Shift Only The Top 1% of Marketers Understand |
| 2026-07-30 | NOW | Alex Cooper | main | XQwJRuN8p-Q | The ULTIMATE Guide to Static Ads in 2026 |
| 2026-07-16 | NOW | Alex Cooper | main | aD7vKl1nkcE | I Turned Claude Code into the Ultimate Creative Strategist |
| 2026-06-30 | NOW | Alex Cooper | main | GdYGUirdZYQ | I Analyzed $1B in Facebook Adspend…here’s what’s working right now |
| 2026-06-11 | NOW | Alex Cooper | main | KSm0pvevV9k | I Asked a $1M Ad Copywriter Why Most Brands’ Ads Fail |
| 2026-06-04 | NOW | Alex Cooper | main | 79doYBhLLFU | The REAL Reason Your Facebook Ads Won’t Scale |
| 2026-05-01 | NOW | Alex Cooper | main | A29szOW7YDE | How to Make AI Animation Ads in Kling 3.0 |
| 2026-04-07 | NOW | Alex Cooper | main | mpj0A4Prxu4 | The Biggest Mistakes Facebook Advertisers Make in 2026 (with Barry Hott) |
| 2026-03-27 | NOW | Alex Cooper | main | Ugd7a2sPgZk | How to Make Killer Facebook Ads Creatives in 2026 (with Harry Delmege) |
| 2026-03-12 | NOW | Alex Cooper | main | ibzfKRRSHhU | How to Create UNLIMITED Image Ads with AI (Nano Banana 2) |
| 2026-03-05 | NOW | Alex Cooper | main | OzkRU3Wx_1w | The ‘Ugly Ads’ Formula That Is Replacing UGC (Ugly Ads Masterclass) |
| 2026-02-26 | NOW | Alex Cooper | main | vD8eLrjAxEM | I Built an AI Tool That Makes Facebook Ads Briefs on Autopilot (Full Parker Demo) |
| 2026-02-15 | NOW | Fraser Cottrell | cited for another speaker | cv9GbhtGLCc | I Made This Pixar Style Ad in 30 Minutes Using AI (MaxFusion) |
| 2025-12-21 | EVERGREEN | Fraser Cottrell | cited for another speaker | 7c0aEpo8-bg | Can You Spot the Winning Ad? (Most People Can’t) |
| 2025-10-17 | EVERGREEN | Fraser Cottrell | cited for another speaker | opWKMc6iavo | I made 10,000 Ads, These are the Money Making Hooks |
| 2025-10-09 | EVERGREEN | Motion (Creative Analytics) | cited for another speaker | kFtv5VDkRSg | AI Ads vs Human Creators: Which Performs Better? (UGC Expert & AI Engineer Reveal Data) |
| 2025-08-14 | EVERGREEN | Alex Cooper | main | fls5dwYVY1M | How to Make Facebook Ads That Actually Work in 2025 |
| 2025-07-03 | EVERGREEN | Fraser Cottrell | cited for another speaker | tVXjXJSEjeA | How to Make Meta Ad Creatives (even if you are a beginner) |
| 2025-05-28 | EVERGREEN | Motion (Creative Analytics) | speaks (other channel) | ITM4faRVzF8 | Creative Strategy AI Mastery: Prompting to Producing (2025 Guide) |
| 2025-04-29 | EVERGREEN | Barry Hott | cited for another speaker | RVRRGf746Bw | Unlock the Hidden Systems Behind $1B+ in Ad Spend with Charles Tichenor IV |
| 2025-04-17 | EVERGREEN | Alex Cooper | main | EOZp34uDIc4 | The EXACT Systems I Use to Make 1,000+ Facebook Ads/mo in 2025 |
| 2025-03-26 | EVERGREEN | Alex Cooper | main | c_6XsMe9eXE | The ULTIMATE Guide to using AI to make Facebook Ads (Full Step-by-Step Walkthrough) |
| 2025-02-28 | EVERGREEN | Fraser Cottrell | cited for another speaker | 3Aw5-kVfufc | Do THIS To Make Founder Ads That Actually Convert |
| 2025-02-20 | EVERGREEN | Alex Cooper | main | nOj-4ZQsSqI | making ugc ads with AI is literally cheating |
| 2025-01-16 | EVERGREEN | Alex Cooper | main | _9f0rTKKIOY | How to Make Facebook Ads Creative That Converts in 2025 (feat. Mirella Crespi) |
| 2025-01-06 | EVERGREEN | Alex Cooper | main | Oj-KGCw7K1g | Facebook Ads Expert Reveals Advertising Secrets in 2025 (Q&A with Barry Hott) |
| 2024-11-21 | ALLTIME | Alex Cooper | main | SmNpVtfIRHw | The ULTIMATE Guide to Facebook Image Ads |
| 2024-10-17 | ALLTIME | Alex Cooper | main | MAwkpQWEQS8 | How to Use Psychology to Make WINNING Facebook Ads (with Sarah Levinger) |
| 2024-09-20 | ALLTIME | Motion (Creative Analytics) | speaks (other channel) | Be9YLcOory4 | 10x Your Creative Output with AI for Advertising [2024] |
| 2024-09-12 | ALLTIME | Alex Cooper | main | fawsUmNeCkg | Facebook Ads HOT TAKES 🌶 (with Barry Hott and Archit Batlaw) |
| 2024-05-25 | ALLTIME | Alex Cooper | main | 7htwuw0zO0Y | How to Use Midjourney to make Facebook Ads |
| 2024-05-16 | ALLTIME | Alex Cooper | main | qhVdp32ebWM | How to Test Facebook Ads Creative (OCTOBER 2024) |
| 2024-03-29 | ALLTIME | Alex Cooper | main | 3wLk3D99JyA | Watch Me Write a Facebook Ads Creative Script |
| 2024-03-15 | ALLTIME | Alex Cooper | main | gWNtOqesF4Q | How to Use AI to Make UGC for Facebook Ads |
| 2024-03-06 | ALLTIME | Alex Cooper | main | Z82ehPFBY54 | The BEST Facebook Ad Creative Style |
| 2023-11-24 | ALLTIME | Alex Cooper | main | 9ikhnQi2ghE | How to Make Winning Facebook Ad Creatives (Step-by-Step Guide) |
| 2022-12-16 | ALLTIME | Dara Denney | cited for another speaker | M2ObOuFQSv0 | LIVE: Let's analyze some ads with FireTeam and Barry Hott! |
| 2020-04-24 | ALLTIME | The Social Savannah | cited for another speaker | PvjkCV9WelU | How To Make Great Video Ads for eCommerce Facebook Ads |
