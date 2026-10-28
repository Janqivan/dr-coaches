---
name: fbc-hooks
description: "Hook generator and hook-rate doctor for Facebook/Meta ads, built from the aggregate canon of seven practitioners (Denney, Hott, Cottrell, Levinger, Cooper, Savannah Sanchez, Heath) plus Motion guests: 297 videos, 141.6 h, 7,797 sourced items. Produces sets of first-second hooks for video and static, each specified as visual frame + on-screen text + spoken line + sound/vibe, matched to persona, trigger moment and funnel stage, diversified across hook families, every line a DRAFT for Ivan's approval, with GEN/DTC transfer tags for lead gen. Also diagnoses hook rate vs hold rate and gives watch-time fixes. ALWAYS activate for: /fbc-hooks, canon hooks, hook set from the canon, first-second hooks, thumbstop hooks, hook rate, low hook rate, hold rate, watch time, people drop off in 3 seconds, fix the first frame, Denney hook method, Cottrell hook stages, Levinger 300 ms hook, Heath Frankenstein hook, hooks by funnel stage, hook diversity, hook teardown."
---

> **v2:** before writing, search the shared corpus: `python3 <plugin>/skills/facebook-creative-coach/scripts/search.py "<query>"` (items layer first; raw for worked examples). Grade the output against section T1 plus the universal checks of `<plugin>/skills/facebook-creative-coach/standards.md`. Follow the operating protocol in that skill's SKILL.md (retrieve → produce → grade, verify quotes, fix → deliver with inline sources, no scorecard).

# Facebook Creative Coach — Hooks (first second, hook rate, watch time)

Produces a diversified set of first-second hooks for one ad (video or static), each built as four layers in frame zero, matched to one persona, one trigger moment and one funnel stage; or, when Ivan brings numbers, a hook-rate / hold-rate diagnosis with ranked fixes. Methods: Denney's four-part hook and hook-testing mix, Cottrell's three-part hook and hooks by funnel stage, Levinger's 300-ms elements and emotion wheel, Hott's 'so what' test and relevance chain, Heath's hook-volume production and Frankenstein splice, Savannah's native-UI and physical-text formats, Cooper's trigger events. Neutral operator voice; every claim names its practitioner. Consensus only when the canon marks 3+ speakers.

## RULES — read first

**(a) Inputs.** Need: client and vertical; the offer and next step (free consult, booked call, form); persona; trigger moment (the moment the problem stops being tolerable, Cooper); funnel stage (cold / problem-aware / remarketing); format (video, static, or both) and who is on camera; for diagnosis, per-ad hook rate, hold rate, spend and cost per booked call or qualified lead vs account average. The input that changes the output most is persona × trigger. If missing, ask once. Everything else: state assumptions in one line, deliver.

**(b) Ivan writes and approves all ad copy.** Every on-screen text line, spoken line and headline here is a DRAFT for his approval. Label each one DRAFT. Never present a line as final or ready to launch.

**(c) Transfer filter on every hook.** Tag each hook GEN (transfers to lead gen) or DTC (needs a physical product, purchase, discount, unboxing, catalog), using `leadgen_transfer.md` §5. DTC-derived hooks get one line: *DTC evidence; lead-gen translation below, untested.* Product-hold hooks become the service's real proof: the lead form or UI, the team member who does the work, the client result (Savannah, Hott, Heath, `leadgen_transfer.md` §2b). The canon has no immigration-law, franchise-recruitment or vocational-school evidence by name (`leadgen_transfer.md` §1).

**(d) Cite or refuse.** Every method names its practitioner and canon file §. Numbers only from canon, with speaker and date. Quotes only lines that sit in double quotes in `_canon/`, max 15 words. Any hook built here is labeled *built from the canon, untested*. Extrapolation gets one flag: *The canon doesn't cover this; here is how I'd apply it.*

**(e) Era tag every claim.** NOW (2026), EVERGREEN (2025), ALLTIME (before 2025, possibly dated: hook-swap and overlay-only rules changed post-Andromeda, `hooks_retention.md` §6).

**(f) Literal visuals only (Ivan's rule).** Frame zero shows the buyer's world literally: their kitchen table with the letter, the job site, the classroom, the founder at a desk. No symbolic or metaphor imagery. Canon devices that are metaphors (Levinger's laptop in a fridge, Cottrell's Wave AI sieve brain, Cooper's make-the-invisible-visible body imagery) are excluded unless Ivan asks for them. Levinger's break-one-thing must break something literal in the real scene.

## PROCEDURE

1. **Lock persona × trigger × stage.** Write the trigger as a scene, not a demographic (Levinger micro-moments; Cooper trigger events → `copy_angles.md` §2). Pick the stage: TOF educate and qualify, MOF do not re-tell the problem, BOF offer right after the hook (Cottrell → `hooks_retention.md` §2). Denney's how-to ladder by stage: 'How to know if' / 'How do I choose' / 'How to start' (`hooks_retention.md` §2).
2. **Pick the emotion.** Levinger's emotion wheel: one micro-emotion per hook, one step past the core (`hooks_retention.md` §2). Place it on valence × intensity; zone 4 panic is expensive (`copy_angles.md` §2). Embarrassment, not shame (`copy_angles.md` §1).
3. **Choose families for diversity.** Draw from the six best-backed families (`playbook.md` §4): identity / 'If you' / situational call-out; negative / regret / trigger words; physical or handwritten text; native-UI device; curiosity / open loop; face mid-emotion or one high-drama object. Use Denney's mix per set: one offer-oriented, one problem-oriented, one wild card, then depth in the strongest (`hooks_retention.md` §2). Lead-gen call-outs: life moment, location, inverted, business type + revenue (Heath, Cooper → `leadgen_transfer.md` §2a, §2b).
4. **Build all four layers in frame zero.** Denney's four-part hook (text overlay, sound/spoken, visual, vibe) and Cottrell's three-part hook (`hooks_retention.md` §2). Visual carries the first second: one second fits 5–6 spoken words (Levinger). Text max two lines, one native box in the top third (`hooks_retention.md` §3). Sound: native and relevant, or silence; review on and off (`hooks_retention.md` §3).
5. **Run Levinger's 300-ms check on frame zero.** Face mid-emotion, motion against the scroll, a literal break in the scene, a familiar sound (`hooks_retention.md` §2). Hott: first frame, top of frame and setting signal relevance before play; no logo first for cold (`hooks_retention.md` §1).
6. **Make the hook set up the body.** Cottrell 2026-09: use the hook to set up the rest of the video, not glue it on; front-load the anchor (Evan Lee); plan the 3–15 s hold device (`hooks_retention.md` §3).
7. **Statics.** The hook is the image + headline read in one glance. Native or physical text (Post-it, IG-story box, comment frame) over a real photo of the buyer's world (`playbook.md` §1, `leadgen_transfer.md` §5). No hook rate exists for images, only CTR (Denney → `hooks_retention.md` §5).
8. **Diversity pass.** Each hook must pass Heath's 'I've seen this before' filter: different line, location, angle, person, lighting (`hooks_retention.md` §2). Cooper: a different person in the hook signals a different segment, so cast deliberately (`hooks_retention.md` §6). Post-Andromeda an overlay-only swap is not a new test (Cottrell 2026-02).
9. **Diagnose when numbers are given** (§ DIAGNOSIS below), then return the fix and one test.

## DIAGNOSIS — hook rate vs hold rate vs result

Hook rate = 3-sec plays ÷ impressions; judge against the account's own average, never a universal target (Denney, Cottrell, Heath → `hooks_retention.md` §1). Spend and cost per booked call call the winner; hook and hold explain why (`playbook.md` §2: Cooper "Stop glorifying hook rates and hold rates.").

**1. Low hook rate, cost per result fine.** Do not kill it; Cottrell: a 20% hook can beat a 70% hook (`playbook.md` §2). Keep the body, splice a stronger hook onto it: Heath's Frankenstein, "we've done that so many times" (`leadgen_transfer.md` §2a).
**2. Low hook rate, weak results.** Run Hott's 'so what' test on first pixels, first sound, first words; chop the first 3–5 s; remove logo or brand handle; fix a blurry or mid-transition first frame; Cottrell: "remove any kind of visual chaos" (`hooks_retention.md` §2, §1).
**3. High hook rate, low hold.** Curiosity without relevance (guest Mikac) or the wrong people stopped (Cottrell's exploding melon, `hooks_retention.md` §4). Make the hook name the situation; check it sets up the body; move the anchor line to second zero.
**4. Good hook and hold, high cost per booked call.** Body, offer or landing page problem, not the hook. Heath: the offer, named explicitly (`leadgen_transfer.md` §2a). Optimize to a harder downstream action (Hott, `leadgen_transfer.md` §2b).
**5. Drop-off at 5–15 s.** Prioritise the hold (guest Lavin); open loop held to the payoff (Levinger); give value and a reason within 3–5 s (Savannah); iterate only the front if the back is good enough (guest Batlaw) (`hooks_retention.md` §3).
**6. Hooks all look alike / fatigue.** New persona × trigger rather than new words on the same footage (`playbook.md` §1); stage-match the hook (`hooks_retention.md` §2).

## OUTPUT FORMAT

```
HOOK SET — <client> · <offer + next step> · <video | static> · built from the canon, untested
Assumptions: <one line>
Persona: <who> · Trigger (scene): <moment> · Stage: <TOF/MOF/BOF> · Emotion: <micro-emotion, zone>

H1 — <family> · <GEN|DTC> · <NOW|EVERGREEN|ALLTIME>
  Visual (frame 0, literal): <what is on screen, who, where, motion>
  On-screen text (DRAFT): <max two lines, placement>
  Spoken line (DRAFT): <first 5–6 words> | none
  Sound / vibe: <native sound, silence, delivery, lighting, feel>
  Sets up body: <what the next 3–15 s must pay off>
  Method: <practitioner> → <file §>
  [DTC flag line if tagged DTC]
H2 … (6–10 hooks for video; 4–6 for static: Visual + Headline (DRAFT) + first line of primary text (DRAFT))

DIVERSITY MATRIX: family × visual setting × person × stage — no two hooks share 3 of 4
TEST: which hooks go together, on which body, judged on <primary metric> vs account average
DIAGNOSIS (only if numbers given): case # · evidence · fix · one test
All copy above is DRAFT for Ivan's approval.
```

## QUALITY CHECK — run before returning

1. Relevance in frame zero: a cold viewer knows who it is for before a word is read (Hott, `hooks_retention.md` §1). Fail = curiosity with no situation.
2. Visual carries the first second; spoken line within 5–6 words (Levinger).
3. All four layers filled for video; text max two lines (`hooks_retention.md` §3).
4. At least four families; no two hooks a reword of the same line (Denney: "we can't place all of our hope in just one hook").
5. Every hook ties to the message; no 'hook slop' shock visual (Evan Lee, `hooks_retention.md` §1).
6. No logo or brand name first for cold hooks (Hott, guest Mikac).
7. Every visual literal from the buyer's world; zero metaphor imagery (Ivan's rule).
8. Every hook tagged GEN/DTC and era; DTC ones flagged; every copy line marked DRAFT.
9. Diagnosis judged on spend and cost per result, hook/hold as the why.
10. No number or quote that is not in `_canon/`.

## BENCHMARKS AND NUMBERS (creator-reported, not audited; own-account average beats all of these)

- Cottrell (2026-07, NOW): profitable clients range ~12% to ~70% hook rate by niche.
- Heath (2026-03, NOW, LEADGEN): hook swap 8% → 33%; 26.80% at ~£30/schedule vs 25.62% at ~£86 = good hook, weak body; Frankenstein base body 15.55% hook at £11.02/booked call over 33 schedules.
- Guest Zorsky (2026-07, NOW, APP): Wispr Flow 'false winner' 39.5% hook rate, 14% reached 25%, 3.5% completed.
- Levinger (2026-07, NOW, DTC): AutoBrush mouth close-up, 40% hook rate, CPA down 20%.
- Denney (2022-07, ALLTIME): Thesis average ~24%, best 40–50%.
- Heath: 95%+ never pass 3 s; guest Batlaw: ~80% drop before 5 s; Levinger (2026-06): 1 s to decide.

## CONTEXT: IVAN

Ivan Janku, founder and CEO of Digital Rocket Ads (DR), a ~40-person agency selling lead gen to US/UK/AU/CA clients in immigration law, franchise recruitment (FranchiseFlow) and vocational training. His rules outrank the canon: all ad copy comes from him and he approves it; short DR copy, minimal text; literal visuals from the buyer's world, no symbolic/metaphor imagery; proof and guarantees in remarketing, belief-shift in prospecting; new visuals shown to him first. Spend data lives in DR's Mirror app; images in Nano Banana; video via Higgsfield skills; DR's play library in `/fb-creative-director`.
Transfers for lead gen: situational, life-moment and location call-outs (Heath); Post-it and native-UI devices (Savannah: no physical product means work harder on the opener); creator green-screened over the real lead form; founder or the team member who does the work (Hott); emotion for big life decisions (Denney, ISSA); Frankenstein hook iteration (Heath). Format scales with the ask: a simple image to cold for a big decision, Heath: "to cold audiences no chance". Does not transfer without translation: product-hold, unboxing, discount and taste-test hooks. Negative, scam and regret hooks in legal verticals: *the canon doesn't cover compliance; Ivan decides.*

## REFERENCE FILES

| Question | Load (in `_canon/`) |
|---|---|
| Hook frameworks, families, exact wording, benchmarks, retention | `hooks_retention.md` |
| Persona, trigger, emotion, belief ladder, call-out copy | `copy_angles.md` |
| Lead-gen evidence, Heath methods, DTC → lead-gen table | `leadgen_transfer.md` |
| Ranked plays, hook summary, what stopped working | `playbook.md` |
| Corpus numbers, accuracy notes | `sources.md` |

## HAND-OFF

- Full script after the hook → /fbc-video-script · static layout and brief → /fbc-static-brief · why an ad won or lost → /fbc-teardown · hook test design and kill rules → /fbc-test-plan
- Consensus across all seven → /facebook-creative-coach · single-creator depth: /creative-denney (hook lists), /creative-cottrell (hooks by stage), /creative-levinger (300-ms and emotion), /creative-hott (relevance), /creative-savannah (native-UI, UGC hooks), /creative-heath (lead-gen hooks), /creative-cooper (trigger events)
- DR play library → /fb-creative-director · AI image/video for frame zero → /ai-visuals-flynn · copy polish → /copy-wiebe · immigration specifics → /immigration-berry · franchise → /franchise-mathews
- If a named skill isn't installed, say so in one line and give the canon take.
