---
name: fbc-test-plan
description: "Meta creative test planner for the post-Andromeda account: dated test plan table from a diversity audit of live ads (format x message x persona), net-new vs iteration split, testing setup by budget (whose model named), monthly volume, naming convention, kill/scale rules on primary metrics, reading results, iterating winners. Built from the aggregate canon of seven practitioners (Denney, Hott, Cottrell, Levinger, Cooper, Savannah Sanchez, Heath) plus Motion guests: 297 videos, 141.6 h, 7,797 sourced items (272 lead-gen). Lead-gen transfer filter on every rule. ALWAYS activate for: /fbc-test-plan, creative test plan, canon test plan, creative diversity audit, Andromeda diversity audit, net-new vs iteration split, how many ads per month, creative volume by spend, Cottrell volume ladder, Denney testing setup, Hott test campaign, when to kill an ad, kill or scale rules, ad naming convention, read creative test results, squeeze a winner, Frankenstein ad."
---

> **v2:** before writing, search the shared corpus: `python3 <plugin>/skills/facebook-creative-coach/scripts/search.py "<query>"` (items layer first; raw for worked examples). Grade the output against section T5 plus the universal checks of `<plugin>/skills/facebook-creative-coach/standards.md`. Follow the operating protocol in that skill's SKILL.md (retrieve → produce → grade, verify quotes, fix → deliver with inline sources, no scorecard).

# FBC Test Plan — dated creative testing plan from the aggregate canon

Produces a dated creative test plan for one Meta ad account: diversity audit of what is live, net-new vs iteration split, setup for the spend level, concepts per month, names, kill/scale rules, read schedule, winner iteration. Methods from Denney (setups, diversity levels, iterations), Hott (test campaign, breakdown effect), Cottrell (volume ladder), Cooper (persona spend vs voice, naming), Levinger (efficiency audit, TEAP), Heath (lead gen, Frankenstein) and Savannah Sanchez (split).

## RULES — read first

**(a) Inputs.** Needed: monthly Meta spend for this account; vertical and offer (what the lead does next: form, booked call, consult); conversion event optimized and its weekly volume; target cost per lead or booked call; the live ads with spend, results and cost per result for the last 30–90 days; production capacity per week (founder, creators, editor, Nano Banana/Higgsfield). Spend is the input that changes the plan most: if missing, ask once. Anything else missing: state assumptions in one line and deliver.
**(b) Ivan writes and approves all ad copy.** Any hook text, headline or message line in the plan is a placeholder marked DRAFT — for Ivan's approval.
**(c) Transfer filter.** Tag every rule and row GEN or DTC using `leadgen_transfer.md` §5. Most budget/volume numbers are DTC. DTC-only elements get one line: *DTC evidence; lead-gen transfer untested.* Heath/Lavin/Zorsky lead-gen evidence = LEADGEN.
**(d) Cite or refuse.** Every method names its practitioner and canon file §. Numbers only from canon, with speaker and date. The plan itself is labeled *built from the canon, untested*. Disagreements side by side with dates.
**(e) Era tags.** NOW = 2026, EVERGREEN = 2025, ALLTIME = before 2025 (flag as possibly dated; platform rules changed with Andromeda).
**(f) Literal visuals.** Concept rows describe visuals from the buyer's world, never symbolic or metaphor imagery. New visuals go to Ivan before launch.

## PROCEDURE

1. **Pull the account read.** Sort live ads by spend, not hook rate or lowest CPA: spend is the winner signal (consensus) → `testing_diversity.md` §1. Levinger's audit adds a second list: top 10 by efficiency over 12 months, "about four ads that all do the same psychological thing" is the usual finding → `testing_diversity.md` §2.
2. **Diversity audit (format x message x persona).** Tag each ad by format, message/angle, persona, TEAP state (Levinger), net-new vs iteration, source (Cooper's 90-day chart) → `testing_diversity.md` §2. Score Denney's level (L0 statics vs video ... L5 true diversity; `formats.md` §2.7) and run her squint test on the top 10–20. Cottrell's definition: diversity = format + messaging + persona; UGC after UGC is not diversity. Post-Andromeda, near-identical ads collapse into one entity; Savannah's threshold is a different visual in the first 3–5 seconds (consensus, NOW) → `testing_diversity.md` §1.
3. **Find the gaps.** Cooper's persona spend vs voice: each persona's share of spend vs share of customer voice → `testing_diversity.md` §2. Denney's persona gap (who buys vs who the ads target) and diagnosis → `strategy_research.md` §2. DR customer voice = call recordings, intake notes, CRM objections (transfer, untested). Gaps become the net-new rows.
4. **Set the net-new vs iteration split.** Denney ~90% net-new / ~10% iterations, iterate only bangers; Savannah ~80/20; Levinger dissents: scale budget on a winner, build a new concept instead → `testing_diversity.md` §2, §6. Default ~90/10; show the dissent.
5. **Pick the setup by budget** → `testing_diversity.md` §2 (see SETUPS below). Separate testing + scaling campaigns is consensus → `testing_diversity.md` §1. Lead gen: optimize to the hardest downstream action with usable volume (Hott: booked call or hand-raiser, or an earlier tracked action on long cycles) → `leadgen_transfer.md` §2b.
6. **Set volume per month** from spend AND conversion volume AND capacity → `testing_diversity.md` §1, §5. Quality-first is the 2026 turn: Hott, "Blind volume is useless. You need guided volume." Cottrell's ladder is DTC; say so.
7. **Write the rows.** One concept per ad set; 3–6 ads per ad set (Denney), 4–6 (Hott), max ~5 (Heath) → `testing_diversity.md` §5. Each concept differs in persona, message or format, never a hook swap alone (big swings, consensus, NOW) → `testing_diversity.md` §1. Port proven messages across formats (Levinger's hero video + two statics + GIF + carousel) → `testing_diversity.md` §1. Format size matches the ask (Heath: free call → image; in-person or done-for-you → longer proof video) → `formats.md` §2.5.
8. **Name everything** with the convention below → `testing_diversity.md` §3, `strategy_research.md` §2.
9. **Set kill/scale and read dates** (rules below). Define each row's success metric before launch: Levinger, "a test you can't read is always going to tell you nothing" → `testing_diversity.md` §2.
10. **Plan winner iteration** (below), then run the QUALITY CHECK.

**SETUPS by budget (cite whose):**
- Denney, three setups (2025-03, EVERGREEN, DTC: built on Advantage+ Shopping): Lean ≤~$5–15K/mo, one ASC all testing, ~10 creatives, add 1–2/week. Growth ~$30–50K/mo: ASC becomes scaling + manual testing campaign, one concept per ad set, 3–6 creatives, $100–200/ad set/day. Scale >$1M/mo: 10–20+ tests/week, ABO, ~7 days or ~$1,000 spent. Lead-gen transfer: swap ASC for the scaling campaign on the lead/booked-call event (untested).
- Hott's test campaign (2023–2025, GEN): one testing campaign, each batch its own ad set, 4–6 ads, exclude customers/recent visitors/1- or 7-day engagers so creative learns cold, launch best-known ads first as the cost to beat, optional cost cap ~2x expected CPA.
- Heath (2026-07, NOW): $30/day, 5 days, broad, 5 ads; pick the best after 5–7 days.
- Cooper budget formula (2024-02 DTC): ad set daily budget = 50 x target CPA / 7; launch Monday/Tuesday; check every 3–4 days. Lead-gen use: target CPA = target cost per lead or booked call (transfer, untested).
- Testing share of budget: 15–65% across Thesis clients, start ~20% (Denney, 2021-09, ALLTIME); guest Zorsky 15–25% (LEADGEN/APP, 2026-07).

**VOLUME per month:** Cottrell (2026-08, DTC net-new/month): $10–20k → 3–4; $20–50k → 5–6; $50–70k → 10–15 + iterations; $70–100k → up to 20; $100–250k → ~30; $250–500k+ → 50+. Denney (2025-03): every $25K/month = one creative test/week. Savannah: $10–50K/month → at least two new ads/week. Hott: one conversion a day, you can't run 50 ads. Levinger: don't split avatars under $30k/month. Heath: four very different creatives plus a few variations is enough. Cap by conversion volume or capacity, whichever is lower.

**NAMING CONVENTION** (built from Cooper's formula naming and ad-set codes, guests Alicia and Spencer → `strategy_research.md` §2, `testing_diversity.md` §3; untested): ad set = SOURCE+NN_CONCEPT (e.g. INTERNAL01_<concept code>). Ad = YYMMDD_CONCEPT_PERSONA_MESSAGE_FORMAT_HOOKTYPE_SOURCE_V#. One row per concept; hook variants are V1/V2 on the same row. Not UGC Vid125A (guest Alicia).

**KILL / SCALE RULES (primary metrics only):**
- Judge on spend, results, cost per result. Hook, hold, CTR, CPM are storytelling metrics that explain why (consensus: Denney, Cottrell, Hott, Cooper, Heath) → `testing_diversity.md` §1. Lead gen: cost per qualified lead or booked call, not raw CPL (Hott → `leadgen_transfer.md` §2b).
- Denney's loop: wait ≥3 days; kill an ad at ~2x account average CPA; no winner after 5–7 days, turn the ad set off; winner → scale the test ad set ~20% every three days, 2–3 times, then duplicate into scaling; never turn the test ad set off after duplicating.
- Minimum before judging: guest Bachmann 2–3x CPA; guest Crespi 3–5x CPA over 5–7 days; guest Lavin (LEADGEN) ≥14 days. Heath: "It's not time, it's conversion volume". Cottrell: "One bad week does not mean a bad ad".
- Never turn off the top spender for CPA alone (breakdown effect; Hott, Denney, Cooper, Cottrell). Exceptions: a 2-day-old ad that sucks (Hott); a test that has only spent ~$1,000 (Denney); if a top ad suddenly doubles CPA, check its comments and the landing page first (Hott).
- Heath on formats: pause only if 40–50% worse on cost per conversion; within ~10–20%, keep.

**READ RESULTS:** two questions only, what is working (spend + results) and why (Denney) → `testing_diversity.md` §2. Locate the failure with metric combos: good hook + poor CPA = body fails; low hook + great CPA = strong body (Heath); high hook/hold, low CTR = wrong audience (Denney); strong hook and CTR, no leads = look past the ad: landing page, form, offer (Savannah). The why is in the creative, not the data (Cottrell, Denney, Levinger, Hott). Lead gen: Meta's 7-day window undercounts long-cycle service revenue; triangulate with CRM (Heath; Hott's triangulation) → `leadgen_transfer.md` §2a.

**ITERATE WINNERS:** in order of 2026 evidence: (1) port the message to new formats (consensus); (2) reshoot the same script with new talent/persona/setting (Cooper, Savannah, Hott); (3) run it as a partnership ad (Denney, Cottrell); (4) Heath's Frankenstein: best-converting body + best hook (LEADGEN, 2026-03) → `leadgen_transfer.md` §2a; (5) footage refresh, same script new B-roll (guest Beauvoir, 2026-06). Hook-only swaps register as the same ad post-Andromeda → `testing_diversity.md` §6. 9 of 10 times don't iterate losers (Denney).

## OUTPUT FORMAT

Return exactly these blocks:

**1. Assumptions** (one line) + label: *Built from the canon, untested. All copy lines DRAFT — for Ivan's approval.*
**2. Diversity audit**

| Ad (name) | Spend 30d | Cost/result | Format | Message | Persona | TEAP state | Net-new/iter |
|---|---|---|---|---|---|---|---|

Then: Denney level (L0–L5) · squint-test result · persona spend vs voice gaps · missing formats/messages · one-line diagnosis.
**3. Setup and volume:** setup chosen (whose model, era, GEN/DTC) · optimization event · testing share of budget · concepts/month · ads per ad set · net-new/iteration split (Denney vs Levinger shown).
**4. Dated test plan**

| Launch (YYYY-MM-DD) | Ad set name | Concept: persona x message x format | Net-new / iteration | Hypothesis (if X, metric Y improves because insight) | Budget/day | Ads (V#) | Kill rule | Scale rule | Read date | Tag GEN/DTC · era | Source (file §) |
|---|---|---|---|---|---|---|---|---|---|---|---|

Launch on the same weekday every week (guest Lavin; Cooper Monday/Tuesday). Read date = launch + 7 days (Denney, Heath) or + 14 days for lead gen (guest Lavin).
**5. Winner iteration queue:** for each current winner, the next move from ITERATE WINNERS with its row date.
**6. The move:** one test to run first, the control, kill/scale rule.

## QUALITY CHECK — run before returning

1. Pass/fail: winners called on spend + cost per result, never on hook rate or CTR alone.
2. Pass/fail: no two concepts Meta would read as the same ad (different persona, message or format; visual differs in the first 3–5 seconds).
3. Pass/fail: at least 3 formats and at least 2 personas or messages across the month's rows.
4. Pass/fail: concepts/month fits spend AND weekly conversion volume AND production capacity.
5. Pass/fail: testing campaign separate from scaling; test ads learn cold (exclusions per Hott).
6. Pass/fail: every row has a success metric, a kill rule, a scale rule and a read date before launch.
7. Pass/fail: no rule turns off the top spender on CPA alone.
8. Pass/fail: every DTC-sourced number or play carries the transfer flag; lead-gen rows optimize to the hardest usable event.
9. Pass/fail: every copy line marked DRAFT; every visual literal, from the buyer's world.
10. Pass/fail: methods cite practitioner + file §.

## BENCHMARKS AND NUMBERS (creator-reported, not audited)

- Hit rates: Motion data (speaker unclear, 2026-03, NOW): ~5–8% of ads become winners; more launches at the same budget tier ≈ 2x winners. Cooper: great strategists go ~7% → 8%. Savannah: ~1 winner in 8. Levinger: expect ~80% not to work. → `testing_diversity.md` §5
- Learning: 50 optimization events/week per ad set (Denney, 2021-09, ALLTIME); minimum $50–100/day per ad set (Denney, 2024-02, ALLTIME).
- Fatigue: ads burn audiences in ~2–3 weeks; up to 29% higher CPMs at 3–4 weeks (Levinger, 2026-07, NOW, DTC).
- Lead gen: expect ~3 months of unprofitable testing (Heath, LEADGEN); a webinar front end gave ~4x sales vs a lead magnet (Heath, 2020-07, ALLTIME).

## CONTEXT: IVAN

Ivan Janku, founder and CEO of Digital Rocket Ads (DR), ~40-person agency selling lead gen to US/UK/AU/CA clients in immigration law, franchise recruitment (FranchiseFlow) and vocational training. All ad copy comes from him and he approves it; short DR copy, minimal text; literal visuals from the buyer's world; proof and guarantees in remarketing, belief-shift in prospecting; new visuals shown to him first. Spend data: DR's Mirror app outranks this canon. Images via Nano Banana, video via Higgsfield skills; DR's play library lives in `/fb-creative-director`.
Transfers for this task: spend-as-winner, breakdown effect, separate test/scale campaigns, diversity audit, big swings over hook swaps, Frankenstein iteration, named-offer tests (Heath), harder downstream event (Hott), 14-day lead-gen reads (Lavin). Does not transfer without translation: Cottrell's volume ladder and Denney's ASC setups (DTC spend and purchase volume); purchase-based ROAS rules. Lead-gen evidence is thin (272 of 7,797 items) and names none of DR's verticals → `leadgen_transfer.md` §1.

## REFERENCE FILES

| Need | Load (in `_canon/`) |
|---|---|
| Setups, volume, kill/scale, metrics, iteration, naming | `testing_diversity.md` |
| Lead-gen offers, events, attribution, transfer table | `leadgen_transfer.md` |
| Persona gap, diagnosis, roadmap, creative ops naming | `strategy_research.md` |
| Format tiers, diversity levels, size of the ask | `formats.md` |
| What's working now, job → play map | `playbook.md` |
| Corpus numbers, eras, accuracy notes | `sources.md` |

## HAND-OFF

- Concept rows need hooks → /fbc-hooks; scripts → /fbc-video-script; statics → /fbc-static-brief; why a test won/lost → /fbc-teardown; strategy questions across all seven → /facebook-creative-coach.
- Creator coaches: /creative-hott (testing philosophy, hit rate), /creative-heath (lead gen, service offers), /creative-denney (setups, diversity), /creative-cottrell (volume ladder), /creative-cooper (personas, creative ops), /creative-levinger (TEAP, research), /creative-savannah (UGC cadence).
- DR skills: /fb-creative-director (DR play library, batch picks), /ai-visuals-flynn (AI image/video production), /paid-media-marshall (account structure beyond creative), /franchise-mathews, /immigration-berry (vertical specifics).
- If a named skill isn't installed, say so in one line and give your own take from the canon.
