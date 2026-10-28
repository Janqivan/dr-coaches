# Sources — Facebook Creative Coach (aggregate)

Corpus pulled Oct 6–7, 2026. Tags: NOW = 2026, EVERGREEN = 2025, ALLTIME = before 2025. Cite as [YT:id] = youtube.com/watch?v=id.

## Corpus numbers
- Candidate videos catalogued: 369; selected: 317; with transcripts: 297 (141.6 h, 1,689,730 words).
- Videos by era: NOW 109, EVERGREEN 90, ALLTIME 98.
- Videos by channel owner: cottrell 78, denney 53, motion 40, hott 36, cooper 27, levinger 25, heath 24, savannah 14.
- Sourced items: 7,797 (NOW 2879, EVERGREEN 2564, ALLTIME 2354); VISUAL 900.
- Items by speaker: Cottrell 1557, Denney 1300, Hott 1095, Levinger 837, Cooper 711, Savannah 561, Heath 341, Unclear 162, GUEST:Mirella Crespi, Creative Milkshake 73, GUEST:Harry Delmege 51, GUEST:Motion host 49, GUEST:Mirella Crespi 48; other guests 1012.
- Items by vertical: GEN 3998, DTC 3425, LEADGEN 272, APP 102.
- Selected but no transcript (YouTube rate-limited): 20.
- Consensus rule: a play is called consensus only when 3+ of the 7 practitioners state it independently; otherwise it is attributed to whoever said it.

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

## Video list (newest first)
| Date | Era | Channel | Role | YT id | Title |
|---|---|---|---|---|---|
| 2026-10-03 | NOW | Fraser Cottrell | main | RExPkxyRB6o | The New Era of Meta Ads Has Just Begun |
| 2026-09-28 | NOW | Dara Denney | main | 4wM-i1cxtAM | Give me 15 Minutes, I'll Fix Your Meta Ads |
| 2026-09-26 | NOW | Fraser Cottrell | main | Mqj05tYuDI0 | I Made 10,000+ Ads. Only 6 Hooks Kept Winning |
| 2026-09-19 | NOW | Fraser Cottrell | main | 5R2grcV0WzY | Our Best Performing Static Ads Right Now |
| 2026-09-19 | NOW | Sarah Levinger | main | in1l2TPFc1c | How to Build Behavior-Based Marketing Avatars from Scratch (Full Tutorial) |
| 2026-09-14 | NOW | Dara Denney | main | pMbN-RefgUk | The New Era of Meta Ads is Here |
| 2026-09-13 | NOW | Fraser Cottrell | main | 1FpqxqbHxVQ | The Ultimate Guide to Static Image Ads (copy & scale) |
| 2026-09-03 | NOW | Dara Denney | main | xTMrZlvAEmM | 7 Claude CoWork Workflows Every Creative Strategist Needs in 2026 |
| 2026-08-26 | NOW | Dara Denney | main | p4yXXdnCgWg | The Easiest Way To Make Winning Meta Ads (in 2026) |
| 2026-08-23 | NOW | Fraser Cottrell | main | n_EyIK5eSWY | I Made This VIRAL AI Ad in 15 Min (Claude + Arcads Tutorial) |
| 2026-08-19 | NOW | Alex Cooper | main | 9O3-AdYpwyQ | The Facebook Ads Shift Only The Top 1% of Marketers Understand |
| 2026-08-16 | NOW | Fraser Cottrell | main | nUTzR9ilTts | How to Make Meta Ads So Good People Can’t Stop Watching |
| 2026-08-13 | NOW | Dara Denney | main | KmbEjy0UBT8 | I Ranked 51 Meta Ad Creative Types (Tier List) |
| 2026-08-09 | NOW | Fraser Cottrell | main | xIpMOTNFvkY | Claude + Arcads MCP / Fastest Way to Make Iterations Meta Ad Creatives |
| 2026-08-02 | NOW | Fraser Cottrell | main | DNI5NI2-lSk | Creative Volume / How Many Ads You Actually Need at Each Spend Level |
| 2026-08-01 | NOW | Dara Denney | main | _VtpfVeB2Kc | How to Work With the Best Creators & Influencers |
| 2026-07-30 | NOW | Alex Cooper | main | XQwJRuN8p-Q | The ULTIMATE Guide to Static Ads in 2026 |
| 2026-07-25 | NOW | Dara Denney | main | yRgPbqywUJ8 | How I Build an Elite Creative Strategy for a Brand in One Sitting |
| 2026-07-25 | NOW | Sarah Levinger | main | _iMPT2SsjeU | How I Get Ad Ideas AI Can't Copy (Psychology Backed Method) |
| 2026-07-20 | NOW | Ben Heath | main | wwdvrZBjock | Meta's CMO on AI Ads and Rising Meta Ad Costs |
| 2026-07-19 | NOW | Fraser Cottrell | main | Lkx7nOGIslw | 15 Years of Meta Ads Knowledge in 11 Minutes |
| 2026-07-19 | NOW | Sarah Levinger | main | vBotjaDGNQI | Watch Me Rebuild a Winning Ad From Scratch (1 video, 2 statics, 1 GIF + Carousel) |
| 2026-07-16 | NOW | Alex Cooper | main | aD7vKl1nkcE | I Turned Claude Code into the Ultimate Creative Strategist |
| 2026-07-14 | NOW | Ben Heath | main | TpZrPY6jTE8 | How To Make AI Ads With Claude X Meta |
| 2026-07-12 | NOW | Sarah Levinger | main | OiKpEOXY4zc | How to Find Winning Meta Ads (post Andromeda) |
| 2026-07-12 | NOW | Fraser Cottrell | main | RSa4wUuw_2k | My Complete Meta Ads Process (copy & scale) |
| 2026-07-05 | NOW | Fraser Cottrell | main | cvk-SxErSF8 | Claude Just Changed Meta Ads Forever (Arcads MCP) |
| 2026-07-04 | NOW | Sarah Levinger | main | a5ruZB-Urlw | I Made 50,000 Ads / These Are the 5 Formats That Keep Winning! |
| 2026-07-03 | NOW | Motion (Creative Analytics) | main | M-zOOiG5GLw | Should B2B Run a DTC Playbook? Manychat & Wispr Flow's Creative Strategy |
| 2026-07-03 | NOW | Motion (Creative Analytics) | main | ILTXC1L8te8 | Emily Hickey's "Motivator Map": The Creative Framework Behind $1B in Meta Ad Spend |
| 2026-07-03 | NOW | Motion (Creative Analytics) | main | TQnMTUoXKmA | 3 Creative Strategy Leaders on What's Actually Working in 2026 (Everyday Dose, Arrae, Harry's) |
| 2026-06-30 | NOW | Alex Cooper | main | GdYGUirdZYQ | I Analyzed $1B in Facebook Adspend…here’s what’s working right now |
| 2026-06-27 | NOW | Sarah Levinger | main | cO1wlDtG5TY | Stop Letting AI Do Your Research (Do This Instead!) |
| 2026-06-27 | NOW | Fraser Cottrell | main | 505rIrOKhWI | How I Write Winning Meta Ad Scripts (from my course) |
| 2026-06-25 | NOW | Dara Denney | main | 5C5VhqW9HCc | How I Make AI Static Ads (in minutes) |
| 2026-06-22 | NOW | Motion (Creative Analytics) | main | -E9sjb2msjo | How to Diagnose a Brand & Prioritize Your Ideas / Dara Denney |
| 2026-06-22 | NOW | Motion (Creative Analytics) | main | DqFjak694PQ | What Is Creative Strategy? The Foundations Every Creative Strategist Needs / Evan Lee, Motion |
| 2026-06-22 | NOW | Motion (Creative Analytics) | main | CVWHkhUA5Ms | Scaling UGC Ads Post-Andromeda: One Winner, Many Formats |
| 2026-06-22 | NOW | Motion (Creative Analytics) | main | v-BQQk1B3k0 | How to Make AI Video Ads with Claude, Nano Banana & Veo / Will Sartorius, SelfMade |
| 2026-06-22 | NOW | Motion (Creative Analytics) | main | pV0tM1gSJiU | Customer & Audience Research for Ads: Sarah Levinger's System For Winning Creative |
| 2026-06-20 | NOW | Sarah Levinger | main | vrBYS4-Gr4o | The Creative Strategy (Full Guide) |
| 2026-06-20 | NOW | Fraser Cottrell | main | IX-2-uSJDk8 | How I Write Winning Meta Ad Scripts (without AI) |
| 2026-06-17 | NOW | Dara Denney | main | 9UBSGSS2Yuo | Meta's New Plan Will End Performance Marketing |
| 2026-06-14 | NOW | Sarah Levinger | main | ukbQeecMU60 | Why AI Just Made Good Marketing Worthless (What you should do) |
| 2026-06-14 | NOW | Fraser Cottrell | main | y7TFcfgwhP8 | I Ranked Every Meta Ad Creative Type (Tier List) |
| 2026-06-12 | NOW | Dara Denney | main | I8tXqqfjIX4 | 9 Meta Ad Hooks That Are Printing $$$ Right Now (45%+ Hook Rates) |
| 2026-06-11 | NOW | Alex Cooper | main | KSm0pvevV9k | I Asked a $1M Ad Copywriter Why Most Brands’ Ads Fail |
| 2026-06-07 | NOW | Fraser Cottrell | main | SJi5todbhJg | The New Way to Make AI Static Ads in 2026 (Canva Layers Update) |
| 2026-06-07 | NOW | Sarah Levinger | main | DEoj28QXUYE | Why Every Ad Hook Sounds the Same And How to Break the Pattern |
| 2026-06-05 | NOW | Dara Denney | main | Uh0TE6nZs5A | How I Built an AI Creative Strategist |
| 2026-06-04 | NOW | Alex Cooper | main | 79doYBhLLFU | The REAL Reason Your Facebook Ads Won’t Scale |
| 2026-05-30 | NOW | Sarah Levinger | main | qUn6OV_70fQ | 5 Things Marketers Believe That Consumers Are Begging Us to STOP Doing |
| 2026-05-30 | NOW | Fraser Cottrell | main | zpUsN6xQSGQ | How to Make Winning Meta Ad Creatives (copy & scale) |
| 2026-05-28 | NOW | Dara Denney | main | eFyvp0mu7UQ | The only 10 brands worth copying for creative strategy... |
| 2026-05-24 | NOW | Fraser Cottrell | main | y4ZvZXacSxE | I Made This VIRAL AI Claymation Ad in 15 Minutes (Arcads Tutorial) |
| 2026-05-23 | NOW | Sarah Levinger | main | RpRSFn5pznc | Why Your Brain Ignores Vague Ads (And What To Write Instead) |
| 2026-05-17 | NOW | Fraser Cottrell | main | QKRd7FTZ7vM | How to use AI to Copy Winning Ads (Step by Step) |
| 2026-05-17 | NOW | Sarah Levinger | main | vXA7E1lcbaU | My 3 Question Framework to Find Winning Ad Creatives |
| 2026-05-10 | NOW | Fraser Cottrell | main | QoGFOGEqijw | Copy This Meta Ads Strategy (Creative Diversity Post Andromeda) |
| 2026-05-09 | NOW | Sarah Levinger | main | 6ZBccBr5AV4 | I Made 50,000 Ads / These are the Money Makers |
| 2026-05-07 | NOW | Dara Denney | main | UGiN8aVy2l8 | How I Use Claude Cowork as a Creative Strategist |
| 2026-05-05 | NOW | Barry Hott | main | s4mLWmECoKI | Ad Relevance: What Everyone Still Gets Wrong |
| 2026-05-03 | NOW | Fraser Cottrell | main | qZhOnITrN0Q | I've Made 10,000 Ads / Here's Why Yours Don't Win |
| 2026-05-01 | NOW | Alex Cooper | main | A29szOW7YDE | How to Make AI Animation Ads in Kling 3.0 |
| 2026-05-01 | NOW | Sarah Levinger | main | ZMXFvjYZoE0 | Why Your Meta Ads Are So Expensive (It's Not Your Creative) |
| 2026-04-28 | NOW | Fraser Cottrell | main | QdNIajKiC2s | What $300M in Ad Spend Taught Me About Scaling ($1M vs $10M Brand) |
| 2026-04-23 | NOW | Dara Denney | main | ePcEcT2PH8E | I've created 20,000+ ads. Here's what's converting NOW. |
| 2026-04-23 | NOW | Sarah Levinger | main | po85BKDTG-Y | The NEW Meta Ad Creative Strategy in 2026 (Post Andromeda) |
| 2026-04-20 | NOW | Motion (Creative Analytics) | main | 0QE6OifIlIM | Meta Ad Hooks & Formats that NEVER MISS ($500k Creative Strategy Study) |
| 2026-04-19 | NOW | Fraser Cottrell | main | WX2fDjp9f4I | Claude + Seedance 2.0 to Create AI UGC Creators Holding the Product |
| 2026-04-16 | NOW | Dara Denney | main | R3Z1VvvgtzU | How Pact Acquires 50K New Customers per Month (with no creative strategist or media buyer) |
| 2026-04-12 | NOW | Fraser Cottrell | main | PuQ2TvXrWg4 | BRUTAL Meta Ads Advice No One Tells You (10 mistakes costing you $$$) |
| 2026-04-09 | NOW | Motion (Creative Analytics) | main | mprXXGL42oU | The Complete Guide To Making UGC Ads - Every Step From Creative Brief to Final Ad |
| 2026-04-08 | NOW | Barry Hott | main | Hh4zkUdRVzg | Who cares about ad hit rate?! |
| 2026-04-08 | NOW | Sarah Levinger | main | RCrvd8pTUzo | How to Write Headlines That Convert (Using Social Judgement Theory) |
| 2026-04-07 | NOW | Alex Cooper | main | mpj0A4Prxu4 | The Biggest Mistakes Facebook Advertisers Make in 2026 (with Barry Hott) |
| 2026-04-06 | NOW | Sarah Levinger | main | cJlBabiKX9k | How I Use Claude to Generate 20 Fresh Ad Concepts Every Monday (Full Setup) |
| 2026-04-05 | NOW | Fraser Cottrell | main | KlhBwk1kmzI | Watch Me Create 3 Static Ads With AI (From Scratch) |
| 2026-03-29 | NOW | Fraser Cottrell | main | wXe0B2XZTGI | How I Make High-Performing Ads Faster Using AI (Poppy Ai) |
| 2026-03-27 | NOW | Alex Cooper | main | Ugd7a2sPgZk | How to Make Killer Facebook Ads Creatives in 2026 (with Harry Delmege) |
| 2026-03-24 | NOW | Ben Heath | main | mMKLLRTk-7c | How To Use Creative Enhancements on Your Facebook Ads |
| 2026-03-23 | NOW | Motion (Creative Analytics) | main | 1BAn7dDmn6E | Meta Ads in 2026: How Many Creatives Do You Actually Need to Launch? |
| 2026-03-19 | NOW | Ecomm Cowboy | main | EgnN83jIsj8 | I Ate a Bag of Chips for 3 Minutes. That Ad Ran for Years. / Barry Hott Interview |
| 2026-03-18 | NOW | Ecomm Cowboy | main | m8dbcF407H8 | World Premiere: Prophit Engine / Andromeda is Awesome / Taylor Holiday, Barry Hott, Danil Saliukov |
| 2026-03-17 | NOW | Sarah Levinger | main | LxWwRykBtfc | How to Use the Feelings Wheel to Build Higher-Converting Ad Hooks |
| 2026-03-15 | NOW | Fraser Cottrell | main | ahwbstiCVpQ | The New Way to Make Ai UGC in 2026 |
| 2026-03-12 | NOW | Alex Cooper | main | ibzfKRRSHhU | How to Create UNLIMITED Image Ads with AI (Nano Banana 2) |
| 2026-03-11 | NOW | Sarah Levinger | main | HuI3o3TBI4A | Full Winning Ad Breakdown: How to Iterate Winning Ads Using the 12-Combination System |
| 2026-03-10 | NOW | Ben Heath | main | bAo6SICFyIE | Copy This EXACT Facebook Ad, It'll Blow Up Your Results |
| 2026-03-09 | NOW | Motion (Creative Analytics) | main | cSm2NPvKLHo | We Analyzed 5000+ Meta Ads: The 2026 Creative Benchmarks Report |
| 2026-03-08 | NOW | Fraser Cottrell | main | oZFiSUkJEPE | This Ad Format Is Secretly CRUSHING (But Not for the Reason You Think) |
| 2026-03-05 | NOW | Alex Cooper | main | OzkRU3Wx_1w | The ‘Ugly Ads’ Formula That Is Replacing UGC (Ugly Ads Masterclass) |
| 2026-03-03 | NOW | Ben Heath | main | 8dJxOaZrK1M | Copy This Meta Ads Testing Strategy for Better Results |
| 2026-03-01 | NOW | Fraser Cottrell | main | 93gJ8_qvOQg | My $450M Hook Strategy (copy and scale) |
| 2026-02-26 | NOW | Alex Cooper | main | vD8eLrjAxEM | I Built an AI Tool That Makes Facebook Ads Briefs on Autopilot (Full Parker Demo) |
| 2026-02-22 | NOW | Fraser Cottrell | main | _BuCO3Jf-K0 | Static Ads vs UGC in 2026 / What Actually Scales Now |
| 2026-02-15 | NOW | Fraser Cottrell | main | cv9GbhtGLCc | I Made This Pixar Style Ad in 30 Minutes Using AI (MaxFusion) |
| 2026-02-10 | NOW | Ben Heath | main | onFwSud9C2Y | The NEW WAY To Test Facebook Ads (Post Andromeda) |
| 2026-02-08 | NOW | Fraser Cottrell | main | TouPE2n7mzo | I Tested 500 Static Ads, Here’s What Actually Scales in 2026 |
| 2026-02-06 | NOW | Sarah Levinger | main | gRQ1y0fLpWY | Why $100k/mo Brands Are Ditching Literal Ads for "Implicit" Creative |
| 2026-02-02 | NOW | Sarah Levinger | main | CwSAZdtqemk | Building Strong 2-Second Hooks: How to Hijack Visual Tension from Organic Content to Use in Your Ads |
| 2026-02-01 | NOW | Fraser Cottrell | main | CPWoW09WCCo | Copy This NEW Meta Ads Strategy (Post Andromeda) |
| 2026-01-30 | NOW | Motion (Creative Analytics) | main | MT2MzrTGC5w | How I Make 200+ Winning Meta Ads Per Week (Full Production Process) |
| 2026-01-29 | NOW | Dara Denney | main | GbXeAYTXhP4 | I Spent $100 on Ads and Built a $35 Million Brand |
| 2026-01-26 | NOW | Fraser Cottrell | main | _FMXAlfgYQo | The Only Meta Ad Creative Workflow You’ll Ever Need |
| 2026-01-20 | NOW | Dara Denney | main | gJrKogm75xg | This AI Creative Company is INSANE |
| 2026-01-18 | NOW | Fraser Cottrell | main | GCugREdurJk | Why Some Ads Are IMPOSSIBLE to Skip |
| 2026-01-11 | NOW | Fraser Cottrell | main | xB4jykCt_yU | How to Find the Right UGC Creators in 2026 |
| 2026-01-04 | NOW | Fraser Cottrell | main | KKp3rA0QK9A | How to Write Winning Meta Ad Scripts ($450M Spent) |
| 2025-12-21 | EVERGREEN | Dara Denney | main | x1b4h42HTG8 | Meta's Andromeda & GEM: Clearly Explained |
| 2025-12-21 | EVERGREEN | Fraser Cottrell | main | 7c0aEpo8-bg | Can You Spot the Winning Ad? (Most People Can’t) |
| 2025-12-19 | EVERGREEN | Motion (Creative Analytics) | main | 3zZiKZUJmms | Motion's 2026 Creative Trends (Full Event) |
| 2025-12-19 | EVERGREEN | Motion (Creative Analytics) | main | uy7f44INEOw | Oren John's 2026 Creative Trend Predictions (HOOKS+VIRALITY+STORYTELLING) |
| 2025-12-19 | EVERGREEN | Motion (Creative Analytics) | main | Lhl4o7yyuDQ | Dara Denney Reveals the BIGGEST Creative Analysis Mistake in 2026 (Most Strategists Do This) |
| 2025-12-19 | EVERGREEN | Motion (Creative Analytics) | main | WuOzOG0H-7U | The Creator-Led Strategy Boosting B2B Ad Efficiency 32% (Meta Study) |
| 2025-12-18 | EVERGREEN | Sarah Levinger | main | sBS1vy-5Be0 | Closed Sessions: How to Build a Scroll-Stopping Story in 15 Seconds (or less) |
| 2025-12-18 | EVERGREEN | Dara Denney | main | ZydGeio1DGQ | The 5 Levels of Creative Diversity (most brands miss this) |
| 2025-12-15 | EVERGREEN | Motion (Creative Analytics) | main | 8WRS3-y4K98 | How To Script Micro Movie Ads That Scale in 2026 (Step-by-Step) |
| 2025-12-14 | EVERGREEN | Fraser Cottrell | main | Ry7KQFZaPGA | How to make Founder Ads that actually convert in 2026 |
| 2025-12-08 | EVERGREEN | Sarah Levinger | main | sdEV9rZ70BY | Why Your Ads Are Failing in 2026: The Algorithm Nobody Told You About |
| 2025-12-07 | EVERGREEN | Fraser Cottrell | main | lDtQRWhLXn4 | How I Make Ai UGC Creatives That Look Real (Arcads + Sora 2) |
| 2025-11-30 | EVERGREEN | Fraser Cottrell | main | FWWp6NcVo3Q | Every Ad Creative Type EXPLAINED |
| 2025-11-23 | EVERGREEN | Fraser Cottrell | main | A_e_9v_Sy0I | The Ai UGC Bubble Was NOT Real (you've been lied to) |
| 2025-11-16 | EVERGREEN | Fraser Cottrell | main | -q2lqfNysUs | My $300M Meta Ads Strategy (copy & scale) |
| 2025-11-09 | EVERGREEN | Fraser Cottrell | main | gP-68LmgAQ4 | How to make Meta Ad Creatives (in 2026) |
| 2025-11-04 | EVERGREEN | Ben Heath | main | _MIWfyD91yc | I found a BETTER way to create Meta video ads (using AI) |
| 2025-10-17 | EVERGREEN | Ben Heath | main | M2VReAjHiN8 | I found an AI tool that makes winning Facebook Ad ideas! |
| 2025-10-17 | EVERGREEN | Fraser Cottrell | main | opWKMc6iavo | I made 10,000 Ads, These are the Money Making Hooks |
| 2025-10-10 | EVERGREEN | Motion (Creative Analytics) | main | UAvSFd3qF8c | 2026 Creative Strategy: What Top Experts Wish You Knew |
| 2025-10-10 | EVERGREEN | Fraser Cottrell | main | bNMeFhW6YmA | I made 10,000+ Ads (These Are the Money Makers) |
| 2025-10-09 | EVERGREEN | Motion (Creative Analytics) | main | kFtv5VDkRSg | AI Ads vs Human Creators: Which Performs Better? (UGC Expert & AI Engineer Reveal Data) |
| 2025-09-23 | EVERGREEN | Ben Heath | main | IRyR9PzSnM8 | Copy This Meta Ads Strategy, It'll Blow Up Your Business |
| 2025-09-19 | EVERGREEN | Fraser Cottrell | main | q_PsIjZl6e4 | Whitelisting Ads vs Partnership Ads (EXPLAINED) |
| 2025-09-12 | EVERGREEN | Fraser Cottrell | main | PRKp0sSUb2c | I Audited 7 Worst Ad Creatives (Don't make these mistakes) |
| 2025-09-02 | EVERGREEN | Fraser Cottrell | main | BkNZVaQboQQ | Google's Nano Banana Update Changed Ai Ad Creatives Forever |
| 2025-08-29 | EVERGREEN | Fraser Cottrell | main | RpNcnKS2WYc | How I Turn Reddit Threads Into High-Converting Ad Ideas |
| 2025-08-28 | EVERGREEN | Dara Denney | main | t-Xf12o4jt4 | I tested over 1000 ads. Here are the hooks ACTUALLY making MONEY |
| 2025-08-25 | EVERGREEN | Motion (Creative Analytics) | main | HIUqsMLp7sc | How AI Transformed Creative Strategy for Winning Facebook Ads (The 2025 Evolution) |
| 2025-08-15 | EVERGREEN | Fraser Cottrell | main | HXox1I6QQvQ | Static Ads Ultimate Guide / The Easiest Ads to Scale FAST |
| 2025-08-14 | EVERGREEN | Alex Cooper | main | fls5dwYVY1M | How to Make Facebook Ads That Actually Work in 2025 |
| 2025-08-08 | EVERGREEN | Fraser Cottrell | main | hxfTY7nkmHA | How I Make Ai UGC Creatives FAST (with Arcads) |
| 2025-07-26 | EVERGREEN | Fraser Cottrell | main | DPvFnflNEYQ | I Ranked Every Meta Ad Creative Type (stop wasting $$$) |
| 2025-07-25 | EVERGREEN | Fraser Cottrell | main | z_IcHzPUoGA | Breaking Down the Ad Format That Keeps Winning for This Brand |
| 2025-07-25 | EVERGREEN | Barry Hott | main | 4BOtccKnC2Q | AI Ads: No Going Back |
| 2025-07-10 | EVERGREEN | Fraser Cottrell | main | 20QsbmSTst8 | Breaking Down a Product Ad That Turns Tradition Into Conversion |
| 2025-07-03 | EVERGREEN | Fraser Cottrell | main | mVb5HKHsC3w | Breaking Down a Perfect Example of UGC That Sells |
| 2025-07-03 | EVERGREEN | Fraser Cottrell | main | tVXjXJSEjeA | How to Make Meta Ad Creatives (even if you are a beginner) |
| 2025-07-02 | EVERGREEN | Motion (Creative Analytics) | main | KALGyNhfrVU | The 30 Ad Formats Every Top Brand is Stealing in 2025 |
| 2025-06-24 | EVERGREEN | Dara Denney | main | ToTQBWHm38I | Why I'd Choose Founder Ads on Meta Over Everything |
| 2025-06-13 | EVERGREEN | Fraser Cottrell | main | fn8NQVpiMe8 | Breaking Down What Actually Makes a Good UGC Ad |
| 2025-06-09 | EVERGREEN | Fraser Cottrell | main | 2BrGawWj1aI | Static Ads Masterclass 2026 (Full Guide) / The Easiest Ads to Scale FAST |
| 2025-06-04 | EVERGREEN | Motion (Creative Analytics) | main | J3TiyuWqYng | The #1 AI Creative Strategy That Helped This Agency Scale to 2k+ Ads Per Month |
| 2025-06-03 | EVERGREEN | Motion (Creative Analytics) | main | lf0Y4hBVih8 | How to Use AI for UGC Content Creation - The COMPLETE 2025 Framework |
| 2025-06-01 | EVERGREEN | Dara Denney | main | NsHk8o3jVvM | How to Make Meta Ads Creative (even if you are wildly unqualified) |
| 2025-05-29 | EVERGREEN | Fraser Cottrell | main | oVpT0GnGY8Q | 10 Psychological Triggers to Get Your Ads Watched |
| 2025-05-28 | EVERGREEN | Dara Denney | main | hGCdGNP5oGE | How Seed Does Creative Testing on Meta Ads (and Why It Works) |
| 2025-05-28 | EVERGREEN | Motion (Creative Analytics) | main | 6jvIXIjieyA | How to Make AI Native Ads Look Human (Barry Hott Method) |
| 2025-05-28 | EVERGREEN | Motion (Creative Analytics) | main | ITM4faRVzF8 | Creative Strategy AI Mastery: Prompting to Producing (2025 Guide) |
| 2025-05-27 | EVERGREEN | Ben Heath | main | D6Sxk8Mbkq4 | How I Made £2.7M with Facebook Ads in 90 Days (Full Breakdown) |
| 2025-05-23 | EVERGREEN | Dara Denney | main | 2tD7h42zwxE | How I Use ChatGPT to Make Meta Ads That Look Real (Image Generation) |
| 2025-05-21 | EVERGREEN | Fraser Cottrell | main | EqhboKbkESQ | How I Make Ai Ads That Actually Work (My Exact Workflow) |
| 2025-05-20 | EVERGREEN | Ben Heath | main | fBrC1_VPTRU | How To Use The NEW Creator Marketplace For Meta Ads |
| 2025-05-15 | EVERGREEN | Barry Hott | main | VtEoAOfQsCU | 5 Psychology Tactics for Winning Meta Ads in 2025 with Sarah Levinger |
| 2025-05-13 | EVERGREEN | Ben Heath | main | M36tVQD26TY | This Facebook Ad Format Gets Insane Results (and nobody uses it!) |
| 2025-05-13 | EVERGREEN | Barry Hott | main | 2jVcLu3Earg | Dead Simple SOPs That Convert Like Crazy on Meta Ads with Dara Denney |
| 2025-05-02 | EVERGREEN | Barry Hott | main | u4B0GGBBDXY | This 1 NEW Line in Ads Manager Could Save You Thousands |
| 2025-05-02 | EVERGREEN | Fraser Cottrell | main | 2cT3ccIzLTU | Top Meta Ad Creatives You Need to Run in 2025 |
| 2025-04-29 | EVERGREEN | Barry Hott | main | RVRRGf746Bw | Unlock the Hidden Systems Behind $1B+ in Ad Spend with Charles Tichenor IV |
| 2025-04-21 | EVERGREEN | Fraser Cottrell | main | ofZxTu1SkQ0 | How This Ad Got 41% Hook Rate (COPY THIS) |
| 2025-04-17 | EVERGREEN | Alex Cooper | main | EOZp34uDIc4 | The EXACT Systems I Use to Make 1,000+ Facebook Ads/mo in 2025 |
| 2025-04-08 | EVERGREEN | Barry Hott | main | FTotRZL9vAg | I turned these advertisers into ad machines |
| 2025-04-02 | EVERGREEN | Fraser Cottrell | main | 4o46eGI6XwQ | How to Write Winning Meta Ad Scripts ($300M Spent) |
| 2025-03-28 | EVERGREEN | Dara Denney | main | 7knQyPYLmfo | How to Test Facebook Ads Creatives at Every Budget (2026) |
| 2025-03-26 | EVERGREEN | Alex Cooper | main | c_6XsMe9eXE | The ULTIMATE Guide to using AI to make Facebook Ads (Full Step-by-Step Walkthrough) |
| 2025-03-20 | EVERGREEN | Dara Denney | main | yNTlVKvuX0o | The UGC Ad Formula That Converts in 2026 |
| 2025-03-14 | EVERGREEN | Motion (Creative Analytics) | main | EgJgQ4EsJ5c | Generate 100s of Winning AI Ads For Facebook -- Discover How! |
| 2025-03-13 | EVERGREEN | The Social Savannah | main | EHiXurAZPj0 | AI Ad Creatives: Yay or Nay? Live Webinar |
| 2025-03-06 | EVERGREEN | foreplay | main | 3TzdwzAG1X8 | Make Facebook Ads Ads for Apps & Games with Social Savannah |
| 2025-02-28 | EVERGREEN | Dara Denney | main | wfENnO7PA5Q | The Best Hooks for Meta Ads 2026 |
| 2025-02-28 | EVERGREEN | Fraser Cottrell | main | 3Aw5-kVfufc | Do THIS To Make Founder Ads That Actually Convert |
| 2025-02-27 | EVERGREEN | Motion (Creative Analytics) | main | jAc63K9lRIQ | Savannah Sanchez Shares Her TOP 43 Ad Hooks for Apps and Services |
| 2025-02-27 | EVERGREEN | The Social Savannah | main | j9d6j0B3W6U | Apps & Services: Top Ad Creative Formats |
| 2025-02-20 | EVERGREEN | Alex Cooper | main | nOj-4ZQsSqI | making ugc ads with AI is literally cheating |
| 2025-02-20 | EVERGREEN | Motion (Creative Analytics) | main | 2gH-KD0eNBs | Best Way To Make Lo-Fi UGC Ads in 2025 (3 Pro Examples) |
| 2025-02-20 | EVERGREEN | Fraser Cottrell | main | SMZyaVvw76c | The 3 Facebook Ad Creatives Every ECOM Brand Needs |
| 2025-02-04 | EVERGREEN | Motion (Creative Analytics) | main | JEEhqMNvu80 | Watch Me Break Down These Mind Blowing AI Ads (And AI Tools)! |
| 2025-02-04 | EVERGREEN | Ben Heath | main | GPp8Y-lKzJw | The BEST Facebook Ads Format (Based On Data) |
| 2025-02-04 | EVERGREEN | Motion (Creative Analytics) | main | MQfMNLipE9o | 23 Meta Ad Ideas You Can Start Testing NOW (Ft. Mirella Crespi) |
| 2025-02-04 | EVERGREEN | Motion (Creative Analytics) | main | zDHkSSsjFDw | Motion's 2025 Facebook Ad Creative Trends⚡️DTC Expert Lightning Round |
| 2025-02-03 | EVERGREEN | Motion (Creative Analytics) | main | SU5Tv9cRONg | How To Make Video Ads (Fast & Easy) |
| 2025-02-03 | EVERGREEN | Motion (Creative Analytics) | main | q-_wSPr4md8 | The BEST Performing 24 Ad Hooks for Meta in 2025 |
| 2025-01-28 | EVERGREEN | Fraser Cottrell | main | W1PADr1kjGk | These Are THE BEST ADS Of The YEAR (Copy Them) |
| 2025-01-27 | EVERGREEN | Dara Denney | main | wRA2VgYIDVs | Meta Ads Data Analysis in 2025: What Really Works with Barry Hott |
| 2025-01-23 | EVERGREEN | Dara Denney | main | _ZHS6tW3f_Q | 10 Meta Ads Creative Formats That Convert Like Crazy in 2025 |
| 2025-01-23 | EVERGREEN | Barry Hott | main | _lAjkqWSDsA | Creative Scaling in 2025: Avoiding Common Pitfalls for Agency and Brand Teams |
| 2025-01-16 | EVERGREEN | Alex Cooper | main | _9f0rTKKIOY | How to Make Facebook Ads Creative That Converts in 2025 (feat. Mirella Crespi) |
| 2025-01-16 | EVERGREEN | Dara Denney | main | CCsty8R0UaA | How to Analyze Facebook Ads Data the Right Way (The 2026 Guide) |
| 2025-01-10 | EVERGREEN | Sarah Levinger | main | kHUSl110eUM | Want to 3X Your CTR? Don’t Test Hooks…Just Do This |
| 2025-01-06 | EVERGREEN | Alex Cooper | main | Oj-KGCw7K1g | Facebook Ads Expert Reveals Advertising Secrets in 2025 (Q&A with Barry Hott) |
| 2024-12-10 | ALLTIME | Barry Hott | main | frk28Y6nOHg | How To Create Winning Ads in 2025? [LIVE WEBINAR] |
| 2024-12-06 | ALLTIME | Barry Hott | main | qoOBIPWH_qw | I spoke to 3 Founders about MAKING ADS (feat. Dara Denney) |
| 2024-12-06 | ALLTIME | Motion (Creative Analytics) | main | vEGa-38LVwg | How to Build the Ultimate Creative Flywheel to 10x Your Creative Ad Diversity |
| 2024-12-06 | ALLTIME | Fraser Cottrell | main | jv5ECAtsrHc | UGC Is Not Worth It For ECOM Brands In 2025 (As You Know It) |
| 2024-12-04 | ALLTIME | Fraser Cottrell | main | KH7FZfCUFn4 | Use These Tools To Create Endless Static Ads |
| 2024-11-28 | ALLTIME | Fraser Cottrell | main | VCnx3v_gZQI | 7 Facebook Ad Creative Tips to Try Today (Significant Results) |
| 2024-11-22 | ALLTIME | Motion (Creative Analytics) | main | DW6iH4tVFmA | The Secret to Writing B2B Ads that Sell (Inspired by DTC Advertising) |
| 2024-11-21 | ALLTIME | Alex Cooper | main | SmNpVtfIRHw | The ULTIMATE Guide to Facebook Image Ads |
| 2024-11-21 | ALLTIME | Dara Denney | main | lWpSmxuwSts | 10 Key Iterations I Make AFTER Finding a Winning Ad Creative on Meta |
| 2024-11-19 | ALLTIME | Fraser Cottrell | main | 0K7WXqYPFCE | 10 Best Hooks For Facebook Ad Creatives (For ECOM) |
| 2024-11-14 | ALLTIME | Dara Denney | main | U7T3_-NnHHg | Creative Diversity is the New Creative Strategy on Meta Ads |
| 2024-10-30 | ALLTIME | Dara Denney | main | hSy6X065x0g | How to Build Scalable Ad Creatives with Just 2 Tweaks |
| 2024-10-23 | ALLTIME | Dara Denney | main | R1HQW38EcRA | 10 Video Editing Tips for Meta Ads Creative That Converts |
| 2024-10-22 | ALLTIME | Ben Heath | main | z3LiJ0PbY-0 | The NEW Facebook Ad Creative Strategy that DOUBLES Results |
| 2024-10-17 | ALLTIME | Alex Cooper | main | MAwkpQWEQS8 | How to Use Psychology to Make WINNING Facebook Ads (with Sarah Levinger) |
| 2024-10-10 | ALLTIME | Dara Denney | main | Y2zEga0aptc | Meta Ad Creatives That Never Work |
| 2024-10-09 | ALLTIME | Motion (Creative Analytics) | main | jpzDn4mo3S0 | How to 7X Your Facebook Ad Creative Output (Step By Step) |
| 2024-09-20 | ALLTIME | Motion (Creative Analytics) | main | Be9YLcOory4 | 10x Your Creative Output with AI for Advertising [2024] |
| 2024-09-20 | ALLTIME | Motion (Creative Analytics) | main | yDaMOwADpNM | Secrets to Mastering Creative Strategy - The Knowledge Stacking Method |
| 2024-09-12 | ALLTIME | Alex Cooper | main | fawsUmNeCkg | Facebook Ads HOT TAKES 🌶 (with Barry Hott and Archit Batlaw) |
| 2024-08-29 | ALLTIME | Fraser Cottrell | main | svW3EyoYAiw | How To Create A Meta Creative Ad Strategy From Scratch |
| 2024-08-08 | ALLTIME | Colby Flood | main | R0k0rVzv_yQ | Optimizing Ad Success with Barry Hott |
| 2024-08-01 | ALLTIME | Motion (Creative Analytics) | main | fCZGNwESzjU | Study These 3 UGC Video Ad Examples [Content Break Down + Reviews] |
| 2024-07-15 | ALLTIME | Fraser Cottrell | main | a_hMenl-qes | Ads Tutorial: How To Create Winning Static Ad Creative in 2024 |
| 2024-06-19 | ALLTIME | Zing | Fueling Your Business Growth | main | kD_0ENSXdZw | Mastering Growth: Conversations with Marketing Consultant Barry Hott / Think Big with Dan and Qasim |
| 2024-06-19 | ALLTIME | Dara Denney | main | k533N5RxXPY | The 10 Best Hooks for Meta Ads Creative |
| 2024-06-13 | ALLTIME | Dara Denney | main | 8r1im4divXQ | The Best Creatives for Meta Ads 2024 |
| 2024-06-06 | ALLTIME | Motion (Creative Analytics) | main | hS47--F7290 | 12 Winning Ad Formats for TikTok and Meta (Budget Friendly) |
| 2024-05-25 | ALLTIME | Alex Cooper | main | 7htwuw0zO0Y | How to Use Midjourney to make Facebook Ads |
| 2024-05-23 | ALLTIME | Motion (Creative Analytics) | main | ZQAjWwxk2C0 | 2024 Ad Strategy for Pros – Make Ads That Convert |
| 2024-05-16 | ALLTIME | Alex Cooper | main | qhVdp32ebWM | How to Test Facebook Ads Creative (OCTOBER 2024) |
| 2024-05-08 | ALLTIME | Motion (Creative Analytics) | main | bUlwbCqw2og | The 10 Top-Performing Facebook Ad Hooks To Use in 2024 |
| 2024-04-29 | ALLTIME | BITESIZED | main | nAr5wmbnwP8 | Traditional Media Buying is Dead - The A-Z of growth marketing with Barry Hott |
| 2024-04-18 | ALLTIME | Fraser Cottrell | main | cUHJkQzisDQ | The Best Performance Creative Guide For 2024 (Facebook Ads, TikTok, & Instagram Ads) |
| 2024-04-11 | ALLTIME | Fraser Cottrell | main | rztrOsDpci0 | Top 8 Winning Ad Creative Templates For Meta Ads In 2024 |
| 2024-04-10 | ALLTIME | Motion (Creative Analytics) | main | TKv56GzwLLU | How To Create Video Ads With AI (Step by Step) |
| 2024-04-02 | ALLTIME | Motion (Creative Analytics) | main | ZwIkDPc1i0U | Static Ads Playbook: How To Create & Scale Static Ads in 2024 |
| 2024-03-29 | ALLTIME | Alex Cooper | main | 3wLk3D99JyA | Watch Me Write a Facebook Ads Creative Script |
| 2024-03-22 | ALLTIME | Barry Hott | main | FHVLQudikp8 | The DTC Shoooooow Ep 4 w/ Akvile DeFazio is LIVE! |
| 2024-03-15 | ALLTIME | Alex Cooper | main | gWNtOqesF4Q | How to Use AI to Make UGC for Facebook Ads |
| 2024-03-14 | ALLTIME | Motion (Creative Analytics) | main | KJ3Q5bha6WA | 🤩 Secrets of high-converting ads: Savannah Sanchez AMA |
| 2024-03-14 | ALLTIME | Fraser Cottrell | main | NNg9-TDiFDA | My Ultimate Meta Ad Creative Framework / Unlimted Creative Ideas |
| 2024-03-06 | ALLTIME | Alex Cooper | main | Z82ehPFBY54 | The BEST Facebook Ad Creative Style |
| 2024-03-05 | ALLTIME | The Andrew Faris Podcast | main | bd9MGQ0-Vqc | Ugly Ads Work. Trust Barry Hott (And Me). |
| 2024-02-23 | ALLTIME | Fraser Cottrell | main | qpJqASEvYuc | These Ad Creative Templates Made Millions For DTC Brands |
| 2024-02-21 | ALLTIME | Dara Denney | main | CmkWzdgl6iI | How to Test Facebook Ads Creative in 2024 |
| 2024-01-23 | ALLTIME | Dara Denney | main | 2jDQ3aPRX8U | These Facebook Ads Creatives Convert LIKE CRAZY in 2024 |
| 2023-12-19 | ALLTIME | Dara Denney | main | pMAxIOL8dtE | Meta Ads Creative Hack: Make Ugly Ads With Barry Hott |
| 2023-11-24 | ALLTIME | Alex Cooper | main | 9ikhnQi2ghE | How to Make Winning Facebook Ad Creatives (Step-by-Step Guide) |
| 2023-11-22 | ALLTIME | Fraser Cottrell | main | Ak6I-EIbBd4 | How to use Facebook Ad Library to Find Winning Ads |
| 2023-11-07 | ALLTIME | Ben Heath | main | Tkl3hhNu8_I | New AI Tools That Make Facebook Ads EASY! |
| 2023-10-05 | ALLTIME | Fraser Cottrell | main | 20xvM5AoJRg | Make Endless Ad Creative With AI |
| 2023-09-20 | ALLTIME | Ben Heath | main | KgO_J6pwv9I | The EASY Way To Create Facebook Ads That Convert (Full Tutorial) |
| 2023-08-24 | ALLTIME | Andrew Foxwell | main | cpnVXGQAWHg | Barry Hott's Monthly Ad Roast / Hott on Hott: Barry Roasts Himself |
| 2023-08-24 | ALLTIME | Andrew Foxwell | main | e54fR6s6WSw | Barry Hott's Monthly Ad Roast / Dynamite Starfish Gets Blown Up |
| 2023-08-24 | ALLTIME | Andrew Foxwell | main | HNnBBOYUlN0 | Barry Hott's Monthly Ad Roast / Roasting North County Smokehouse: Where's the Beef? |
| 2023-08-22 | ALLTIME | Colby Flood | main | XIn0vQdErsM | Ugly Ads: Barry Hott Sharing Why Brands Should Ditch Perfection and Embrace Authenticity |
| 2023-07-24 | ALLTIME | Northbeam | main | YuS18wnD_bc | Your Pretty Ads Suck. Why Ugly Ads Always Win, With Barry Hott / DTCx Media Buyer Summit |
| 2023-07-20 | ALLTIME | Northbeam | main | FjUkvTGkxWo | Top Media Buying & Creative Strategies for TikTok - Savannah Sanchez / DTCx Media Buyer Summit |
| 2023-06-28 | ALLTIME | The Social Savannah | main | pNECdkJjpCU | TikTok Top Media Buying & Ad Creative Strategies [JULY 2023] |
| 2023-06-26 | ALLTIME | Northbeam | main | MbqiexQiyGs | The Secrets to Making Ugly Ads with Barry Hott / The Media Buyer Webinar |
| 2023-06-12 | ALLTIME | Northbeam | main | wrbvSulohNI | TikTok Strategy with Savannah Sanchez / The Media Buyer Newsletter / June 12 2023 / Northbeam |
| 2023-05-04 | ALLTIME | Paolo Santanicchia • Meta Ads | main | nUVl_zpeipY | PodcAds #3 - Ugly Ads, Beautiful Accounts - with Barry Hott |
| 2023-03-31 | ALLTIME | Barry Hott | main | s1oyWDqCV9w | LIVE: Adtopsy Live! with Taylor Lagace |
| 2023-03-07 | ALLTIME | Dara Denney | main | MiurhGwirfY | The 10 Best Creatives to Test on All Facebook Ad Accounts |
| 2023-03-03 | ALLTIME | Barry Hott | main | P3IpafQunzU | LIVE: Adtopsy Live! with Ryan McKenzie |
| 2023-02-21 | ALLTIME | Ben Heath | main | N3X8CuD_VQk | The BEST Facebook Ad FORMAT (NEW DATA) |
| 2023-02-17 | ALLTIME | Barry Hott | main | ZyNdRSc9zQc | LIVE: Adtopsy Live! with Darien Payton |
| 2023-02-10 | ALLTIME | Barry Hott | main | 9YKsHMJXiIQ | LIVE: Adtopsy Live! with Anze Markovic |
| 2023-02-02 | ALLTIME | Motion (Creative Analytics) | main | 4g4WgCad_k4 | AMA: Ad Creation Strategy, Production, & Iteration With Mirella Crespi |
| 2023-01-27 | ALLTIME | Barry Hott | main | DsiASJulIhg | LIVE: Adtopsy Live! with TripleWhale CMO Rabah Rahil |
| 2023-01-20 | ALLTIME | Barry Hott | main | Fg3kHHRdhdk | LIVE: Adtopsy Live! with agency/brand owner Daniel Okon. Come hang with us! |
| 2023-01-13 | ALLTIME | Barry Hott | main | kYSxNySgmKc | LIVE: Adtopsy Live! with Ridge CMO Connor MacDonald. Come hang with us! |
| 2023-01-06 | ALLTIME | Barry Hott | main | vBTlKeyEpD8 | Tearing down ads LIVE - Adtopsy Live |
| 2022-12-16 | ALLTIME | Dara Denney | main | M2ObOuFQSv0 | LIVE: Let's analyze some ads with FireTeam and Barry Hott! |
| 2022-12-08 | ALLTIME | Modern Commerce | main | PSMit4vB8n8 | Internet Marketing Hot Takes for 2023 w/ Barry Hott / ModCom #61 |
| 2022-10-11 | ALLTIME | Dara Denney | main | Ss7bdFf0bsk | How to Brief UGC Creators (My Exact Template) |
| 2022-08-16 | ALLTIME | Dara Denney | main | ZrNh5MQuL3Y | How to Make Great UGC Content / 7 Expert Tips to Making More $$$ |
| 2022-08-08 | ALLTIME | Triple Whale | main | DGTwYyI-81s | This is Working RIGHT Now In Media Buying... - Adspend EP. 20 W/ Barry Hott |
| 2022-08-02 | ALLTIME | Dara Denney | main | Yi_1Vb4sfoQ | The Recipe for the Perfect UGC Ad (Facebook Ads & TikTok Ads) |
| 2022-07-12 | ALLTIME | Dara Denney | main | CdK0jdqxXOs | The 5 Best Hooks for Facebook Ads Creative |
| 2022-04-25 | ALLTIME | Dara Denney | main | rNsOaXtlmRM | How to Develop a Creative Strategy That Converts (Facebook Ads & TikTok Ads) |
| 2022-04-02 | ALLTIME | Social Snowball | main | xyvIAmfuZUo | Buying Ads For Toyota To Growing DTC Brands w/ Barry Hott / The Snowball Effect Ep. 12 |
| 2022-03-04 | ALLTIME | Barry Hott | main | hNs7mXEpOGU | Does Meta care about media buyers? |
| 2022-02-22 | ALLTIME | Ben Heath | main | 4mZ3F77dNdI | Copy This Facebook Ad To Guarantee Success |
| 2021-10-25 | ALLTIME | 2X eCommerce | main | l1_xSlj4Z50 | Savannah Sanchez: DON'T MAKE ADs, MAKE TIKTOKS - Social Creatives Prep for Q4 |
| 2021-09-30 | ALLTIME | Dara Denney | main | KFFcno59vQ8 | How to Test Facebook Ads Creative |
| 2021-03-30 | ALLTIME | Ben Heath | main | sxQwH4kjGW4 | Should You Use Dynamic Creative with Facebook Ads? |
| 2021-03-14 | ALLTIME | The Social Savannah | main | w1sz_OdVQiA | TikTok Advertising Influencer Strategies For eCommerce Brands |
| 2021-03-11 | ALLTIME | Ben Heath | main | dwUxmlgWfxQ | How To Test New Facebook Ad Creative The RIGHT Way! |
| 2021-01-21 | ALLTIME | Ben Heath | main | 1EQrp8MJRek | 7 Facebook Ad Copy Techniques That WORK |
| 2020-09-10 | ALLTIME | Dara Denney | main | RTUae3Tctgs | FACEBOOK AD CREATIVE THAT CONVERTS // Video Templates for Ads (How to Create Facebook Ads Creative) |
| 2020-07-28 | ALLTIME | Ben Heath | main | E0lbvr71wR8 | Facebook Advertising Psychology - How To Guarantee Success |
| 2020-07-21 | ALLTIME | The Social Savannah | main | Mwla1m64jSg | Dynamic Creative Testing for Facebook Ads: The Best Way Test Test Creatives in 2020 |
| 2020-07-06 | ALLTIME | Ben Heath | main | HzDJpKu7vew | Get 50% More Conversions With THIS Facebook Ad Creative Strategy |
| 2020-05-19 | ALLTIME | Affiliate World Conferences | main | 6OmF0BzBOHQ | Conversations With a Marketer: The Savannah Sanchez Tapes |
| 2020-04-24 | ALLTIME | The Social Savannah | main | PvjkCV9WelU | How To Make Great Video Ads for eCommerce Facebook Ads |
| 2019-07-09 | ALLTIME | Ben Heath | main | WeQrKeAwZDg | 6 SUCCESSFUL FACEBOOK ADS TO COPY |
