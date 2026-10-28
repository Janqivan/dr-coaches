---
name: fbc-teardown
description: "Meta ad teardown and pre-launch QA (image or video, own or competitor). Returns a scored 10-item checklist (first-second scroll-stop, relevance chain, message and persona, format fit, ad-signal check, body or hierarchy, proof and offer, CTA, sound and text, diversity vs the live ads) and a verdict; with metrics, a primary-vs-storytelling diagnosis (spend, results, CPA/CPL, then hook rate, hold rate, CTR) and one variable to test next. Built from the aggregate canon of seven practitioners (Denney, Hott, Cottrell, Levinger, Cooper, Savannah Sanchez, Heath) plus Motion guests: 297 videos, 141.6 h, 7,797 sourced items. ALWAYS activate for: /fbc-teardown, canon teardown, teardown with hook rate, pre-launch QA this Meta ad, QA before launch canon, scroll-stop check, relevance chain check, ad-signal check, is this ad too polished, primary vs storytelling metrics, hook rate hold rate diagnosis, good hook rate but no leads, competitor ad teardown canon, what variable to test next on this ad."
---

> **v2:** before writing, search the shared corpus: `python3 <plugin>/skills/facebook-creative-coach/scripts/search.py "<query>"` (items layer first; raw for worked examples). Grade the output against section T4 plus the universal checks of `<plugin>/skills/facebook-creative-coach/standards.md`. Follow the operating protocol in that skill's SKILL.md (retrieve → produce → grade, verify quotes, fix → deliver with inline sources, no scorecard).

# Meta Ad Teardown and Pre-launch QA (canon)

Produces a scored teardown of one Meta ad (static or video, Ivan's own draft or a competitor's live ad), a verdict, and, when numbers are supplied, a metrics diagnosis that names the failing link and the one change to test next. Methods are attributed to the named practitioner: Hott's relevance chain and so-what test, Levinger's 300 ms elements and ad-signal filter, Denney's primary vs storytelling metrics and diversity levels, Cottrell's metric read order, Cooper's middle ground, Heath's size-of-the-ask and lead-gen offer rules, Savannah's no-product openers and edit QC.

## RULES — read first

**(a) Inputs.** Needed: the ad (file, frames, script or Ad Library link), placement, vertical and offer, funnel stage (cold or remarketing), the next step after the click (form, call, landing page), and what is already live in the account. Optional: metrics (spend, results, CPL or cost per booked call, hook rate, hold rate, CTR, frequency, days live). The input that changes the output most is the ad itself: if missing, ask once. Everything else: state assumptions in one line and deliver.
**(b) Ivan writes and approves all ad copy.** Any rewritten hook, headline, overlay or script line in the output is a DRAFT for his approval, marked DRAFT. A competitor's copy is quoted as theirs, never offered as his.
**(c) Transfer filter.** Tag every finding and fix GEN or DTC using `leadgen_transfer.md` §5. The corpus is DTC-heavy: 3,425 DTC items vs 272 LEADGEN and 102 APP of 7,797 (GEN 3,998). A DTC-only element (discount static, product demo, unboxing, catalog, ROAS judging) gets one line: *DTC evidence; transfer to lead gen untested.*
**(d) Cite or refuse.** Every check names its practitioner and canon file §. Numbers only from canon, with speaker and date. The scoring scale and verdict rule are *built from the canon, untested*. Teardown of a competitor ad describes what is on screen; it does not claim its results unless the Ad Library run time is given.
**(e) Era tags.** NOW (2026), EVERGREEN (2025), ALLTIME (before 2025, flag as possibly dated). Platform behavior (Andromeda, hook swaps, attribution) is dated by video month.
**(f) Literal visuals.** Ivan's rule outranks the canon: visuals come from the buyer's world, literal and instantly understood; no symbolic or metaphor imagery. Flag any metaphor visual as a fail on item 3 even when a canon example used one (e.g. Cooper's pain-as-fire renders, `statics.md` §2).

## PROCEDURE

1. **Identify the job.** Funnel stage, persona, size of the ask (Heath's ladder: small ask → image, big ask such as an in-person consult or done-for-you service → longer video with proof, `formats.md` §2.5). Note Levinger's TEAP phase if it helps (`formats.md` §2.3). Format-to-stage mapping is contested: Cottrell maps it, Denney says messaging sets the stage (`formats.md` §2.2, §6).
2. **Item 1 — First second.** Frame zero and the top of frame (Hott: Mistake #1, first frame, top of frame, front-loaded words, `hooks_retention.md` §1). Levinger's 300 ms elements: face mid-emotion, motion against the scroll, format-breaking visual, familiar sound (`hooks_retention.md` §2). Statics have hooks too (Cooper, `statics.md` §2). Blurry or mid-transition first frames fail (Cottrell).
3. **Item 2 — Relevance chain.** Who stops, and for the right reason? The hook is targeting (Cottrell 2026-03); Hott's spectrum of relevance from words, setting, casting, accent; run Hott's so-what test on the first pixels, sound and words (`hooks_retention.md` §1, §2; `video_ugc.md` §1). Curiosity without relevance = high hook, poor hold (guest Anze Mikac). Lead gen: life-moment, location and persona call-outs (Heath, Cooper, `leadgen_transfer.md` §2a, §2b).
4. **Item 3 — Message and persona.** One goal, one persona per ad (Denney, `statics.md` §2); a stranger gets the point in one second (Denney's 1-second test); clear over clever, headlines 4–7 words (Levinger, `statics.md` §1); image and message agree (Cooper's congruency). Big life decisions need emotion over directness (Denney ISSA, `leadgen_transfer.md` §2b).
5. **Item 4 — Format fit.** Does the format carry this message to this persona at this ask? Founder content is the only format top-tier on all three tier lists (`formats.md` §2.1); podcast is the agreed bottom. Service ads with no humans are the biggest no-product mistake (Savannah, `formats.md` §3).
6. **Item 5 — Ad-signal check.** Levinger's tells: clean cuts, suspiciously good lighting, read-script voice; Hott's polish tells: logo open, perfect fades, sweeping zooms, shallow depth of field; Cooper's realism test (tripod in the kitchen vs phone on the counter) and middle-ground rule (`video_ugc.md` §1; `formats.md` §2.6). Logo or brand name up front for cold traffic fails (Hott, `hooks_retention.md` §1).
7. **Item 6 — Body (video) or hierarchy (static).** Video: hook sets up the body, not glued on (Cottrell 2026-09); hold 3–15 s (guest Josh Lavin); product enters at the emotional shift, ~40–50% through (Levinger); pacing and show-don't-tell (`hooks_retention.md` §3; `video_ugc.md` §1, §2). Static: headline → key visual → support, one heavy headline in the top third, at most ~3 callouts (`statics.md` §2).
8. **Item 7 — Proof and offer.** Lead gen: the offer is named (free consultation for what?), guarantees, scarcity of slots (Heath, `leadgen_transfer.md` §2a); proof filmed, specific, not vague (Heath, guest Alexandra). DTC discount stacks are DTC-tagged.
9. **Item 8 — CTA.** States what to do and matches the real next step (Heath's book-a-call CTAs, `leadgen_transfer.md` §2a); Feel / Believe / Do (guest Josh Lavin, `leadgen_transfer.md` §2c); yappers close soft (`video_ugc.md` §2).
10. **Item 9 — Sound and text.** Denney's four-part hook (text, sound, visual, vibe); hook text about two lines; check sound on and off (Levinger, Savannah); native caption boxes, no brand fonts (`hooks_retention.md` §2, §3; `video_ugc.md` §3).
11. **Item 10 — Diversity vs live ads.** Would Meta merge it with what is live? Same image with a new headline or overlay-only hook swaps collapse into one entity; Savannah: visual must differ in the first 3–5 seconds; Cottrell: format + messaging + persona; Denney's squint test (`testing_diversity.md` §1, §2, §6).
12. **Metrics diagnosis (only if numbers given).** Primary first: spend, results, cost per result decide; hook, hold, CTR only explain (Denney's columns, `testing_diversity.md` §2). Read order CPA → CTR → hook → hold (Cottrell), then the combinations below. Check sample before judging and the breakdown effect before killing a top spender (`testing_diversity.md` §1, §5).
13. **One variable next.** Name the failing link and one change that fixes it. Make it a real swing, not a one-word tweak: Heath's order is offer, angle, creative style, hooks; overlay-only hook swaps no longer count as a new test (Cottrell 2026-02, `testing_diversity.md` §1, §6). On a weak hook with a proven body, Heath's Frankenstein splice (`leadgen_transfer.md` §2a).

Metric combinations (`testing_diversity.md` §2): low hook + strong hold/CTR → new hook (Cottrell). Good hook + poor CPA → body fails (Heath). High hook and hold, low CTR → wrong audience (Denney) or educating, not selling → stronger CTA (Cottrell). Good CTR and hold, no results → Levinger: "you're not asking for a sale"; strong hook and CTR, no conversions → look past the ad: landing page, form, offer (Savannah). UGC drop at ~50% → Levinger: "you told people about the video way too soon". Statics have no hook rate; read CTR (Denney 2022).

## OUTPUT FORMAT

```
TEARDOWN — [ad name] · [static/video] · [own draft / competitor] · [vertical] · [stage] · assumptions: [one line]

| # | Check | Score 0–2 | What I see (on screen / in copy) | Canon basis (who, file §, era) | GEN/DTC | Fix (DRAFT if copy) |
|---|---|---|---|---|---|---|
| 1 | First-second scroll-stop | | | | | |
| 2 | Relevance chain | | | | | |
| 3 | Message, persona, literal visual | | | | | |
| 4 | Format fit (size of ask) | | | | | |
| 5 | Ad-signal check | | | | | |
| 6 | Body/retention or hierarchy | | | | | |
| 7 | Proof and offer | | | | | |
| 8 | CTA | | | | | |
| 9 | Sound and text | | | | | |
| 10 | Diversity vs live ads | | | | | |
TOTAL: __/20 (scale built from the canon, untested)

VERDICT: SHIP / FIX THEN SHIP / REWORK / KILL (or, competitor: STEAL / ADAPT / IGNORE) — one line why.
Rule: a 0 on item 1, 2 or 3 blocks SHIP whatever the total.

METRICS (if given):
Primary: spend · results · CPL or cost per booked call · days live · read: winning / not yet readable / losing
Storytelling: hook rate · hold rate · CTR · frequency → failing link: [hook / body / CTA / audience / post-click]
Account-relative: vs account average, not a universal benchmark.

NEXT TEST: one variable · why (canon §) · control · what changes · read on [primary metric] after [canon minimum] · GEN/DTC
Ivan to approve: [list of DRAFT lines]
```

## QUALITY CHECK — run before returning

1. Item 1 judged on frame zero and the top of frame, not on the script's first line (Hott, Levinger).
2. Relevance scored separately from attention: a high hook rate never passes item 2 on its own (Cottrell, Hott).
3. Verdict on metrics rests on spend and cost per result; hook, hold and CTR appear only as the why (Denney, Hott, Cooper consensus).
4. No call on thin data: sample and days live stated against a canon minimum; the top spender is not killed on CPA alone (breakdown effect).
5. Item 10 states whether the ad is a new entity or a variant Meta would merge (Savannah, Cottrell, Heath).
6. The next test is one change, big enough to register post-Andromeda, with a control and a read rule.
7. Every finding carries practitioner, file §, era and GEN/DTC; DTC-only fixes carry the one-line flag.
8. All new copy is marked DRAFT; no metaphor visuals recommended; minimal text.
9. Disagreements shown with dates where they decide a score (statics funnel role, format vs stage, hook rate's weight).

## BENCHMARKS AND NUMBERS

Creator-reported, from their own or client accounts, not audited. Benchmark against the account, not a universal number.
- Hook rate = 3-sec plays ÷ impressions; hold = ThruPlays ÷ impressions, later the share watching the first 15 s — Denney (2022, 2025) · ALLTIME/EVERGREEN
- Thesis average hook ~24%, best 40–50% — Denney (2022) · ALLTIME. Targets the 30s, 35–40%; hold now ~10% — Denney (2025-01) · EVERGREEN
- Profitable clients range ~12% to ~70% hook rate by niche — Cottrell (2026-07) · NOW. Skincare exploding-melon ad: ~70% hook rate, one of the brand's worst ads, wrong customer — Cottrell (2025-10)
- Lead gen: 26.80% hook at ~£30 per schedule vs 25.62% at ~£86 — good hook, weak body — Heath (2026-03) · NOW · LEADGEN. Frankenstein: 15.55% hook body at £11.02 per booked call got a ~26% hook spliced on — Heath (2026-03)
- False winner: 39.5% hook, only 14% reached 25%, 3.5% completed — guest Eric Zorsky (2026-06). Java Sock: 22% thumb-stop, 49% hold, 6.2% CTR, 0.3% CVR — hold-rate clickbait (guest Jess Bachmann, 2022-12) · ALLTIME
- Test reads: Denney waits ≥3 days, kills an ad at ~2x account average CPA, ad set off after 5–7 days with no winner; guest Mirella Crespi 3–5x CPA over 5–7 days; guest Josh Lavin (LEADGEN) ≥14 days — `testing_diversity.md` §2, §5
- Pause a format only if 40–50% worse on cost per conversion; within ~10–20% keep it — Heath (2025-05)
- Fatigue: ads burn audiences in ~2–3 weeks — Levinger (2026-07); frequency above 5 over 7 days worries Denney
- Meta's 7-day attribution undercounts long-consideration services — Heath (2025-05) · LEADGEN

## CONTEXT: IVAN

Ivan Janku, founder and CEO of Digital Rocket Ads (DR), a ~40-person performance agency selling lead gen to US/UK/AU/CA clients in immigration law, franchise recruitment (FranchiseFlow) and vocational training: high-consideration, form or call-booking funnels, not purchases. His rules outrank the canon: all ad copy comes from him and he approves it; short direct-response copy, minimal text; literal visuals from the buyer's world, no symbolic or metaphor imagery; proof and guarantees in remarketing, belief-shift in prospecting; new visuals shown to him first. Spend data lives in DR's Mirror app; images via Nano Banana, video via Higgsfield skills.
Transfers to his teardowns: relevance chain, so-what test, ad-signal check, persona and life-moment call-outs, named offer, size-of-the-ask format fit, humans on camera for services, founder ads, hold over hook, Frankenstein splice (`leadgen_transfer.md` §2, §4). Does not transfer without a stated translation: ROAS-based verdicts (use CPL, cost per booked call, lead quality downstream), discount and bundle statics, product demos, unboxing, catalog. No canon item covers immigration law, franchise recruitment or vocational schools by name (`leadgen_transfer.md` §1).

## REFERENCE FILES

| Question | Load (in `_canon/`) |
|---|---|
| First second, hook types, retention past 3 s, hook-rate numbers | `hooks_retention.md` |
| Metrics, primary vs storytelling, test reads, diversity, Andromeda | `testing_diversity.md` |
| Format fit, tier lists, size of the ask, ugly vs polished | `formats.md` |
| Static hierarchy, headline, Post-it, native statics | `statics.md` |
| Scripts, body, pacing, casting, ad signals in video | `video_ugc.md` |
| Lead-gen evidence and DTC → lead-gen transfer table | `leadgen_transfer.md` |
| Corpus counts, eras, accuracy notes | `sources.md` |

## HAND-OFF

- Rewrite the failing hook → /fbc-hooks · rebuild the script → /fbc-video-script · rebuild the static → /fbc-static-brief · plan the next test batch → /fbc-test-plan
- Consensus or disagreement across all seven → /facebook-creative-coach; one creator's lens → /creative-hott (relevance, ugly), /creative-levinger (psychology), /creative-heath (lead gen), /creative-denney, /creative-cottrell, /creative-cooper, /creative-savannah
- DR's play library → /fb-creative-director · AI image/video craft → /ai-visuals-flynn · media buying beyond creative → /paid-media-marshall · landing page and copy polish → /copy-wiebe · franchise → /franchise-mathews · immigration → /immigration-berry
- If a named skill isn't installed, say so in one line and give the canon's take.
