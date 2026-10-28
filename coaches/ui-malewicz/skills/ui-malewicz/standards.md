# Michal Malewicz — Standards Bank

Corpus status: 324 transcripts (839933 words) in the raw layer plus canon items. Checks re-sourced on 2026-10-20; tags without YT ids were not found in transcripts.

This file is the bar. Every piece of work the coach produces or judges is graded against the checks for its task type. A check is PASS only with evidence pointed at the work itself: a measured px value, a count, a ratio, a hex pair, a line of copy, a position on the page. "Looks cleaner" is not evidence. Malewicz measures before he judges taste; so does this bank.

Each check carries the source it comes from. Pull the context with `scripts/search.py "<check words>" --layer items` when a check is borderline or Ivan disputes it.

How to measure: on a live page, read computed styles (DevTools or a script) at 1120-wide desktop content and 390-wide phone; on a screenshot, draw guides and state the px you read. Every PASS/FAIL line states the measured number next to the threshold.

Where his tellings conflict, the check gives both values, newest first, and either one passes. A threshold marked *(operational)* is the coach's line for turning his "about" into a binary; the canon value it rests on is given next to it.

Scoring: count PASS / total for the task type. Deliver only at ≥ 85% with zero FAIL on checks marked ★. Otherwise fix and regrade (max 2 loops), then deliver with the remaining FAILs listed honestly.

---

## T1. Page critique (DR pages, client landing pages for franchisors, immigration firms, trade schools; screenshot or URL)

Graded on the critique Claude writes, and on the page measurements it contains.

- ★ **Bar set before verdict.** First lines name the page's one job, the visitor who must act, and the metric "better" is tested on. Judging against what looks good on design blogs = FAIL. [YT:u01ZGoiLJ70] [YT:1sC_KA3kTTo]
- ★ **Measured, not opined.** The critique reports, as numbers: left vs right margin (px each), count of distinct spacing values, count of typefaces, count of text sizes per section, count of weights, count of icon sets, count of effects. Any of the seven missing = FAIL. [YT:Kqg3vN1ms2E] [canon: web_pages.md, UI audit order]
- **Margins symmetric.** Left margin − right margin = 0 px (≤ 1 px rounding) on the content container. [YT:Kqg3vN1ms2E]
- **About four spacing values on an 8 base.** Distinct vertical gaps per page counted; every value is in 4/8/16/24/32/40/48/64; > 5 distinct values = FAIL *(operational; canon: "about four")*. [YT:ThmHV38Ecqk] [YT:w2mNSOWiZbU]
- **Group gap > inside gap.** In every section, the smallest gap between groups is larger than the largest gap inside a group (e.g. label→field 8 vs field group→field group 24–32). State both numbers. [YT:ThmHV38Ecqk] [YT:w2mNSOWiZbU]
- **Hero eye path traced.** Rendered line widths stated in px: headline line > description line > button row. Description wider than the headline = FAIL ("lets the eye run away"). [YT:wrj4GDcLqJY]
- **CTA is the only colourful thing in the hero.** Count elements in the hero using the CTA hue (or any saturated hue) other than the CTA: 0 = PASS. Run and report the blur test. [YT:wrj4GDcLqJY] [YT:Toonu-cTE60]
- **CTA label passes his ban list.** Primary label is not "Get started", "Next", "Okay", "Sign up", "get in touch", "get a quote" or bare "Search"; it names the benefit or exact action. [YT:Ni34Y2uSIF4] [YT:QaJyYl0SvyY]
- **AA on every text and control pair.** Contrast ratio listed per pair (text/bg, button label/button, field border/bg); each functional pair ≥ WCAG AA (4.5:1 body, 3:1 large text). Decoration may fail only if the switch-off test is stated. [YT:FBDVzr0peO4] [YT:ThmHV38Ecqk]
- **Strip-to-text verdict given.** The critique says whether the type frame (copy alone, black on white) sells, before any visual comment. [YT:nq07DZq3Og8]
- ★ **≤ 7 fixes, ranked, each Problem → Fix → Why.** Problem = what was measured; Fix = exact values (px, weight, hex or HSB, count); Why = the rule. An adjective-only fix ("cleaner", "more modern", "make it pop") anywhere = FAIL. [canon: SKILL.md, Mode 1] [YT:Kqg3vN1ms2E]
- **Fix order respected.** Fixes ranked conversion first, then consistency in his order: alignment → fonts → hierarchy → icons → colour. [YT:Kqg3vN1ms2E]
- **Self-reported results not promised.** If his 3x / 40% / +400% numbers appear, they are labelled as his own reported results, never a forecast for DR. [canon: SKILL.md, Behavior rules] (not found in transcripts)

## T2. Upgrade plan for a live page (digitalrocketads.com and client sites: upgrade, not redesign)

- ★ **Do-not-change list first.** Locked items listed before any fix: brand hex values, Besley + Schibsted Grotesk, every content block. A fix that changes a locked hex or face = FAIL. [canon: SKILL.md, Mode 2] [YT:Qb7FVefKH3I]
- ★ **Content inventory whole.** Count content blocks (copy blocks, proof items, logos, case studies, FAQ entries) before and after: counts equal. Any block dropped or merged without Ivan's OK = FAIL. Decoration may be listed as a removal *candidate* only. [canon: SKILL.md, Behavior rules] (not found in transcripts)
- ★ **Baseline measured per section.** Header, hero, proof, doubts, offer, final CTA, footer, mobile: each has measured margins, spacing values, sizes and weights before any change. [YT:Kqg3vN1ms2E]
- **Sequenced alignment → fonts → hierarchy → icons → colour.** Batch 1 is site-wide cheap measurable fixes (grid, spacing values, type scale); colour use comes last. His own example improved from unified fonts and spacing, not colour. [YT:Kqg3vN1ms2E]
- **Each section: Keep / Change (exact values) / Do not touch / Test.** All four fields present for every section. [canon: SKILL.md, Mode 2] (not found in transcripts)
- **Change applied to every element using the pattern, then re-audit.** Each batch states which selectors/components it touches and includes a re-measure step. [YT:w2mNSOWiZbU] [YT:Kqg3vN1ms2E]
- **What worked is found before changing it.** Plan asks for or reads recordings/analytics and what past clients said convinced them; 20–30 recordings before tweaking (3–5 is first-option bias). [YT:Kqg3vN1ms2E] [YT:QaJyYl0SvyY] [YT:cS1J77CLqmA]
- **Header passes framing + selling point + what you do.** In plain words; zero of "seamless", "empowering", "leverage", "streamline". [YT:QaJyYl0SvyY] [YT:HnTv9J9RYrw]
- **Simplify is not assumed for franchisors.** Plan states whether the buyer is high-stakes B2B (he dropped "simplify" for a hospital director) and turns the choice into a test. [YT:Qb7FVefKH3I] [YT:Toonu-cTE60]
- **Each batch ends on a real phone check and a named test.** [YT:q8yUIbRiNRc] [YT:-xKgBgGOAqs]

## T3. Hero and above-the-fold build (new landing pages, client LPs, SaaS homepage)

- ★ **Type frame first.** The hero is delivered (or judged) as text in black and white at real sizes before any visual; the visual is added last and named as amplifying a specific headline claim. [YT:GzDBkU0irpA] [YT:nWbBZPjev_0] [YT:lpqTva43Bxo]
- ★ **Build order present:** kicker → headline → one-line description → 1–2 buttons → checks/validation → key visual (optional). Missing element or wrong order = FAIL. [YT:nWbBZPjev_0] [YT:9JnNtm4imqA]
- **Kicker is proof, not a pre-headline.** Contains a non-round, real number (not ending in 000) supplied by Ivan, or a rating. Invented number = automatic FAIL. [YT:lpqTva43Bxo] [YT:Hzr3Q1CJPbI]
- **Headline about the visitor.** Starts from "you, your problems, your money"; fails the swap test if it "can fit any product". [YT:Ni34Y2uSIF4] [YT:HnTv9J9RYrw]
- **Description is one line and shorter than the headline** in rendered width (px stated). [YT:wrj4GDcLqJY] [YT:nWbBZPjev_0]
- **Subhead kills the category objection.** Name the objection it answers. [YT:Ni34Y2uSIF4]
- ★ **One main button.** Hero primary buttons = 1; a second only for a high-stakes buy (case studies + demo), and then with unequal weight (different fill, not two identical buttons). [YT:nWbBZPjev_0] [YT:nq07DZq3Og8] [YT:FBDVzr0peO4]
- **CTA colour used nowhere else.** Count of non-button elements in the CTA hex = 0; a repeated header CTA does not copy the main CTA's colour or style. [YT:Toonu-cTE60] [YT:9JnNtm4imqA]
- **Key visual relevant.** Placed on his abstract↔literal × irrelevant↔relevant plot and sits in the relevant half; no dashboard/app screenshot as hero, no blobs, clouds, space imagery or single-prompt AI image. [YT:lpqTva43Bxo] [YT:GzDBkU0irpA]
- **A person, if used, gazes at the CTA or key copy.** Gaze direction stated. [YT:nWbBZPjev_0] [YT:1sC_KA3kTTo]
- **Zero hero motion.** Count of parallax, pre-loader, scroll hijack, header animation = 0. [YT:Toonu-cTE60] [YT:tP5KHuevhSI] [YT:aGTqFp7GAKE]
- **Grid stated.** 12 columns, gutter 32, column 64, 1120 content width; hero sits in the ~750 px fold (derived: his fold number applied to the hero). [YT:w2mNSOWiZbU] [YT:-xKgBgGOAqs]
- **Headline weight not AI-thick.** Weight stated; extra bold at 40 is his "too thick" case (bold 32 was his fix); very thick multi-line headline is a slop tell. [YT:ThmHV38Ecqk] [YT:3BvDDjmzYY8]

## T4. Below the hero: proof, doubts, pricing, final CTA (client LPs, DR service pages)

- ★ **Two jobs only: show value, then clear doubts.** Every section below the hero is labelled with the doubt it clears; a section with no named doubt or value job = FAIL ("Why are these shoes here?"). [YT:cS1J77CLqmA] [YT:9JnNtm4imqA] [YT:Kqg3vN1ms2E]
- ★ **Doubts come from real buyer questions.** The section order cites where each question came from (client calls, sales calls, recordings); a borrowed blueprint order = FAIL. [YT:QaJyYl0SvyY] [YT:nq07DZq3Og8] [YT:9JnNtm4imqA]
- **Proof is checkable.** Every logo maps to a named project or blurb (count logos vs count backed: equal); testimonials are verifiable people, text plus rough vertical video where available; no stock faces. [YT:DEs40FcLWUI] [YT:QaJyYl0SvyY]
- **FAQ only from asked questions.** Each FAQ entry traceable to a real question; zero invented FAQs. [YT:DEs40FcLWUI]
- **Stats realistic and real.** No 10x claims; every number from Ivan's data. [YT:DEs40FcLWUI] [YT:Kqg3vN1ms2E]
- **Pricing is not three identical cards.** Tiers differ in weight (the plan you want chosen is darker/higher contrast); action in the title; buttons name the exact purchase. [YT:9JnNtm4imqA] [YT:QaJyYl0SvyY]
- **Final CTA ≠ top headline.** String comparison: final CTA headline is not the hero headline; it goes deeper, tests another headline, or is a low-friction breather (call or email). [YT:9JnNtm4imqA] [YT:QaJyYl0SvyY]
- **Section rhythm on the grid.** One consistent between-section value (e.g. 32 or 40) stated and used everywhere; inside-section 8/16/24. [YT:Kqg3vN1ms2E] [YT:w2mNSOWiZbU]
- **Proof sits where doubt appears.** If case studies are the strongest proof, the plan answers "why not at the top?" explicitly. [YT:9JnNtm4imqA]

## T5. System spec for the builder (values sheet for Claude Code / Claude Design / the dr-pages plugin)

- ★ **Exact values, one per role.** Every token is a number or hex; zero ranges ("16–24"), zero adjectives. [canon: SKILL.md, Mode 3] [YT:-xKgBgGOAqs]
- ★ **Breakpoints and line breaks set by a human, written into the spec.** Spec states the breakpoint px values and where line breaks fall; a spec that delegates breakpoints to the AI = FAIL. [YT:-xKgBgGOAqs] [YT:3BvDDjmzYY8]
- ★ **Nothing invented as his.** Values the canon lacks (desktop hero size, line length, phone heading sizes, hover/focus/pressed/disabled) are marked "outside canon, proposal" and put on a test. [canon: SKILL.md, Rule 4 and Mode 3] (not found in transcripts)
- **Grid and spacing:** 12 col / gutter 32 / column 64 / 1120; scale 8/16/24/32/40/48; inside group 8/16/24, between groups 24/32/40; label→field 8, form groups 32 (24 in 2025-10). [YT:w2mNSOWiZbU] [YT:ThmHV38Ecqk]
- **Type floors:** body 14–16, nothing under 12, line height 1.3–1.4 (×1.618 in another 2025-10 lesson), no thin weights, button label ≥ 16 and about 1/3 of button height. [YT:ThmHV38Ecqk] [YT:FBDVzr0peO4]
- **Colour roles:** page ~95% lightness with white cards (lighter is closer); text tinted dark gray, never #000 (2E2E2E his dashboard value); one CTA colour used nowhere else; secondary = accent at lightness ~80, no border. Any change to a locked brand hex flagged for Ivan's OK. [YT:Kqg3vN1ms2E] [YT:FBDVzr0peO4] [YT:w2mNSOWiZbU]
- **Buttons vs fields:** button ≥ 44 (50 sweet spot, desktop 48–52, phone CTA 52–64); field 40–44; button height > field height. [YT:FBDVzr0peO4] [YT:ThmHV38Ecqk] [YT:q8yUIbRiNRc]
- **Shadow math:** Y ≥ 0, blur ≥ 2 × Y, negative spread, opacity ≤ 50% (cards 30–40%), tinted from the surface hue; one big shadow per screen. [YT:FBDVzr0peO4]
- **Radius:** 8 default (his safe number); nested radii concentric, inner corner diagonal = side gap. [YT:ThmHV38Ecqk] [YT:w2mNSOWiZbU]
- **One page, machine-ready.** One paste-ready block (Rules, CSS custom properties, Components, Never, Check list) plus the do-not-change list; no token/variant plumbing (his 2025-12 view). [YT:6_t66Ef0Llk] [canon: SKILL.md, Mode 3]
- **No 1 px nudge requests.** Instructions to the builder are exact CSS values, never "move it 1px". [YT:-xKgBgGOAqs]

## T6. Mobile layout (390/375 wide; lead forms on phones)

- ★ **Own layout, not stacked desktop.** At least one of: rewritten copy, hero visual cut or shrunk, reordered blocks, enlarged targets, is stated per section; a straight stack of the desktop = FAIL ("irresponsible, not responsive"). [YT:q8yUIbRiNRc] [YT:cS1J77CLqmA]
- ★ **Long-word test at 375 px.** Longest real word/URL/firm name rendered at 375: document scrollWidth ≤ 375, zero horizontal scroll. [YT:9nXMEqZH35A]
- **Margins 32 at 390.** Side margin measured; card padding 24; 16 between tappable items. [YT:ThmHV38Ecqk] [YT:FBDVzr0peO4]
- **Tap targets ≥ 44 × 44.** Count of tappables under 44 in either dimension = 0; close X 48 × 48; icon ≤ half the target. [YT:ThmHV38Ecqk] [YT:N-34Q9mhwvs]
- **Phone CTA 52–64 high.** [YT:q8yUIbRiNRc]
- **Form ≤ 2 fields on mobile.** Count stated; more fields need a stated reason and a test. [YT:q8yUIbRiNRc]
- **Zero sticky bars, zero hero animation.** Counts stated. [YT:q8yUIbRiNRc]
- **Copy rewritten for the phone.** "tap" not "click"; CTA softened where the ask is big. [YT:q8yUIbRiNRc]
- **Checked on a real phone**, not a shrunk desktop browser: device and conditions named. [YT:q8yUIbRiNRc] [YT:-xKgBgGOAqs]
- **Text floors hold:** body ≥ 14 on phone (12 minimum anywhere). [YT:ThmHV38Ecqk]

## T7. Components, forms, states and SaaS UI (lead forms, Funnel Message Map app, dashboards)

- ★ **Never two identical buttons for one question.** Mutually exclusive actions (Save/Cancel, Book/Learn more) differ in fill or outline; separate processes may be equal, and the critique says which case applies. [YT:FBDVzr0peO4] [YT:Kqg3vN1ms2E]
- ★ **State never by colour alone.** Selected, error, closed, valid each add shape, icon, text or size change; list each state and its non-colour cue. [YT:w2mNSOWiZbU] [YT:ThmHV38Ecqk]
- **Button visibly taller than the field.** Heights stated (field 40–44 vs button 44–60). [YT:FBDVzr0peO4] [YT:w2mNSOWiZbU]
- **Button padding:** side padding > top/bottom padding (px stated); label ≥ 16. [YT:FBDVzr0peO4]
- **Fields:** white fill, inside stroke 1 pt (2 pt playful B2C), label 14 above; label→field gap < field-group gap. [YT:ThmHV38Ecqk] [YT:w2mNSOWiZbU]
- **Error copy says exactly what happened** ("Your passwords do not match"), and each error offers the next action. [YT:ThmHV38Ecqk]
- **Icons:** one set; stroke width matches the adjacent text stem; count of icon sets = 1. [YT:Kqg3vN1ms2E] [YT:ThmHV38Ecqk]
- **One effect in one place.** Count of stacked effects per element ≤ 2 (no gradient + shadow + inner shadow + glow); one big shadow per screen. [YT:FBDVzr0peO4] [YT:Kqg3vN1ms2E]
- **Tables:** text left, numbers right, never centered; 24 between columns; identical row baseline spacing. [YT:w2mNSOWiZbU] [YT:_PJLefMZwko]
- **Dashboards for intent:** a simple overview shows 5–6 numbers; the working tab is a searchable, sortable, filterable table. [YT:6_t66Ef0Llk] [YT:w2mNSOWiZbU]
- **Numbers add up** across steps (totals, counts, prices identical across screens); real varied sample content, zero Lorem Ipsum. [YT:Kqg3vN1ms2E] [YT:ThmHV38Ecqk]
- **Navigation: each destination once;** hamburger not chosen where 2–5 tabs fit. [YT:Kqg3vN1ms2E] [YT:FBDVzr0peO4]
- **Hover/focus/pressed/disabled values flagged as outside canon** (proposal, AA kept), not presented as his. [canon: SKILL.md, Mode 3] (not found in transcripts)

## T8. AI-built output review and AI tool reality check (Claude Design / Claude Code builds, generated LPs)

- ★ **Every tool or model claim dated**, with a one-line "tools change fast" warning; undated tool claim = FAIL. [canon: SKILL.md, Rule 4] [canon: sources.md] (not found in transcripts)
- ★ **Slop tells counted = 0.** Count each: pill kicker, very thick headline, CTA in the nav colour, tinted icon in a rounded square, mismatched SVG icon sets, pill shapes competing with the CTA, button shadows by default. Each one present is named with its location. [YT:3BvDDjmzYY8] [YT:6_t66Ef0Llk] [YT:9nXMEqZH35A]
- ★ **Content inventory preserved.** Blocks in the AI output vs the source copy: count equal (Ivan's past AI redesigns came out simpler and worse). [canon: SKILL.md, Context: Ivan] (not found in transcripts)
- **Copy was written by a human first;** the AI only reacted (angles, rephrasings). Generated copy = FAIL. [YT:GzDBkU0irpA] [YT:zatFKQqtmuw]
- **Breakpoints were not set by the AI.** [YT:-xKgBgGOAqs] [YT:3BvDDjmzYY8]
- **Long-word test at 375 px passes** (scrollWidth ≤ 375). [YT:9nXMEqZH35A]
- **Scored out of 10 with the gap to above 7 named.** Score stated; the specific changes that move it above 7/10 listed. A deliverable scoring ≤ 6 is not shipped (his "six out of 10 website"). [YT:3BvDDjmzYY8] [YT:HQpQhmJi22s]
- **Images start from real photos;** zero single-prompt AI images as client visuals. [YT:GzDBkU0irpA] [YT:iSC6JgFBZWg]
- **At least one hand-made detail** named (a hand-tuned value, custom component, or photo edit) that the generator did not produce. [YT:3BvDDjmzYY8] [YT:psyw2_j_5jk]
- **Someone understands most of the code;** fixes given to the builder as exact CSS values. [YT:3BvDDjmzYY8] [YT:-xKgBgGOAqs]
- **Sponsored/partner sources labelled** (Relume, Framer, Webflow, Zeppelin) and his own products labelled when cited. [YT:0X3qFzT_wik] [YT:9nXMEqZH35A] [canon: SKILL.md, Behavior rules]

---

## Universal checks (every output)

- ★ **Retrieved before writing.** At least 3 searches run; the work uses at least 3 retrieved items, cited as [YT:id].
- ★ **No invented quotes, numbers, stories or dates.** Every quoted line exists verbatim in a retrieved hit (15 words max); every value attributed to him is in the canon; anything else is labelled "outside canon, proposal".
- ★ **Did the work.** If Ivan gave a page or task, the output is the finished thing (critique with measured fixes, upgrade plan, spec block, scored review), not a list of questions. Questions only for inputs that block the work (the page, locked values, real proof numbers), one at a time, after doing everything possible without them.
- **In voice.** Verdict up front; one flaw at a time, each named with the number that proves it; blunt, no praise padding (what works goes on a keep list); "Don't go over the top" used where effects pile up. None of: "seamless", "empower", "leverage", "streamline", "elevate", "make it pop".
- **Ends with one move.** The one next change, why in one line, and how to test it.
