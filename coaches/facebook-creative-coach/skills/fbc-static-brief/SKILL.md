---
name: fbc-static-brief
description: "Static (single-image) Meta ad brief generator. Picks the static format for the message (native IG-story, Post-it/ugly, us-vs-them, testimonial, headline-led, persona call-out, offer, native storytelling), then writes a designer-ready brief per variant: hierarchy, literal image direction, text overlay as a DRAFT for Ivan, aspect ratios, a diversity matrix, and an optional image prompt handoff to /ai-visuals-flynn. Built from the Facebook Creative Coach aggregate canon (7 practitioners plus Motion guests; 297 transcribed videos, 141.6 h, 7,797 sourced items, 900 visual reads). ALWAYS activate for: /fbc-static-brief, static brief, static ad brief, designer brief for a static, brief statics from the canon, which static format for this message, Post-it ad brief, us vs them static brief, IG story static brief, headline static brief, static variants for Andromeda, Denney two-layer static."
---

> **v2:** before writing, search the shared corpus: `python3 <plugin>/skills/facebook-creative-coach/scripts/search.py "<query>"` (items layer first; raw for worked examples). Grade the output against section T3 plus the universal checks of `<plugin>/skills/facebook-creative-coach/standards.md`. Follow the operating protocol in that skill's SKILL.md (retrieve → produce → grade, verify quotes, fix → deliver with inline sources, no scorecard).

# Static Ad Brief — format pick, then a designer-ready brief per variant

Produces one brief per static variant that a designer (or Figma/Canva plus an AI image tool) can build without a call: which format and why, what the eye hits first, what the image shows, what the text says (draft), sizes, and how the variants differ. Methods: Denney (two-layer framework, tier list), Cooper (rules, 12 formats), Cottrell (static system, AI production), Hott (Post-it method), Levinger (hierarchy, cognitive load), Heath (lead-gen offer, size of ask).

## RULES — read first

- **(a) Inputs.** Needed: the offer and the named service; the persona; the one message (or belief to shift); funnel temperature (cold prospecting vs remarketing); placements; any Ivan-approved copy; any proof he has (reviews, results, numbers); brand constraints. The input that changes the output most is **the message** (format follows message: Cooper, `statics.md` §1, image first / message first). If it is missing, ask once. Otherwise state assumptions in one line and deliver.
- **(b) Ivan writes and approves all ad copy.** Every headline, overlay line, callout, primary text and CTA in the brief is labeled **DRAFT — for Ivan's approval**. Where Ivan supplied copy, use it verbatim and say so. Never present draft copy as final.
- **(c) Transfer filter.** Tag every format and element GEN (transfers to lead gen) or DTC (needs a physical product, purchase, discount, catalog) using `leadgen_transfer.md` §5. DTC-only elements get one line: DTC play, no lead-gen translation stated in the canon, untested for DR. The corpus is DTC-heavy: 3,425 DTC vs 272 LEADGEN items (`sources.md`).
- **(d) Cite or refuse.** Every method names its practitioner and canon file §. Numbers only from the canon, with speaker and date. Results are creator-reported. Anything assembled here (format-to-message mapping, the brief itself) is labeled built from the canon, untested.
- **(e) Era tags.** NOW = 2026, EVERGREEN = 2025, ALLTIME = before 2025 (possibly dated). Denney's format verdicts moved between 2024 and 2026 (`statics.md` §6): use the 2026 tier.
- **(f) Literal visuals only (Ivan's rule).** The image shows the buyer's real world: real people, places, documents, screens, moments. No symbolic or metaphor imagery. This overrides Cooper's render-the-invisible move (pain as fire, thorns, X-ray; `statics.md` §2) and AI-billboard concepts (Denney D tier, NOW). Text-in-context on a real object (Post-it, sign, paper) is literal and allowed.

## PROCEDURE

1. **Strategy layer first (Denney two-layer framework, `statics.md` §2).** Write: one goal per static, Denney's rule "Don't try to do two jobs in one ad." (NOW); one persona (type, stage, objection); temperature; production level (graphic, hi-fi, lo-fi creator). One persona per ad, separate ads for other personas (Cooper, Denney, Levinger; `statics.md` §1).
2. **Size the ask (Heath, `formats.md` §2.5, `leadgen_transfer.md` §2a).** Small ask (free named consultation, Zoom call, webinar, lead magnet) suits an image. Big ask (in-person meeting, done-for-you service) to a cold audience: Heath says a simple image has no chance cold; brief the static for warm/remarketing and send the cold job to `/fbc-video-script`. Say which case applies.
3. **Pick the format from the message (built from the canon, untested).** Map message type to format using `statics.md` §3 templates and the 2026 tiers (`statics.md` §2, Denney tier list; `formats.md` §2.1):
   - Pain/problem line, cold, need it cheap and fast → Post-it / text-in-context (Hott method, `statics.md` §2; consensus, GEN; LEADGEN translation: Post-it on the website or a screenshot, `leadgen_transfer.md` §5).
   - First-person moment in the buyer's life → IG-story native static (Cottrell, `statics.md` §3; NOW). Product-in-hand is DTC; for lead gen swap in a phone photo of the buyer's real moment.
   - Named persona with a stated situation → persona call-out (Cooper, Hormozi text posts, LEADGEN, `statics.md` §3; Heath life-moment and location call-outs, `copy_angles.md` §2).
   - One sharp claim a stranger gets in a second → headline-led / headliner (Cooper, Denney, Cottrell; Denney B tier 2026 only if messaging is strong).
   - Old way vs this way, buyer already solution-aware → us-vs-them (Denney four steps, `statics.md` §2; consensus, DTC-tagged; Denney 2026 B tier, mid-funnel). Generic them, never a named competitor without Ivan's call (disagreement, `statics.md` §6).
   - A client's exact, specific words → golden-nugget testimonial or comment-frame (Denney, Cottrell, Hott; Denney rates generic testimonial statics E/F in 2026, nuggets only).
   - The offer itself → offer static with the service named (Heath: free consultation alone fails, name it; `leadgen_transfer.md` §2a) plus one trust device (Cottrell, `statics.md` §3).
   - A real story worth reading → native storytelling static: raw literal image plus long primary text (Cottrell, NOW, possibly a trend; `statics.md` §2).
   - Education before the ask → educational infographic (Denney, Levinger; supporting cast).
   - Founder voice / apology / letter → letters (Cottrell, Denney; strongest in sale periods).
   Skip Notes-app/iMessage/AirDrop UX statics (Denney F tier, Cooper skip; `statics.md` §6) and press screenshots (Denney F tier, permissions).
4. **Hierarchy and layout (consensus, `statics.md` §2 static anatomy).** Headline in the top third, never over the busiest part of the photo (Hott); headline does the targeting, then the key visual, then support (Denney); three sections, one element each, F/Z eye path, one font and never more than two (Levinger); at most ~3 small callouts or one oversized number as a second focal point; social proof device; small CTA. Headline 4–7 words, max 8 (Levinger). Denney: "clarity is always going to out-beat creativity".
5. **Headline and overlay draft (`copy_angles.md` §1, §3).** Source wording from client words (Cooper, Denney: customers are your copywriters). Test it on a stranger: Cooper, "Assume no one knows or cares." Specific beats vague (Levinger). Clear over clever (Levinger, Savannah, Hott, Heath). Lead gen: offer clear instantly plus one or two benefits (Heath, `copy_angles.md` §3). All of it marked DRAFT.
6. **Image direction (`statics.md` §1, §4).** Image and message must agree; incongruence is the biggest static failure (Levinger, Cooper). Native, phone-shot, believable setting beats ad-looking for most formats (consensus, NOW); Cooper: pick a clear end, ugly-organic or obviously-an-ad with great copy, never the middle (`formats.md` §2.6). Common or intangible offers need context or an end-result image (Hott, Savannah); portfolio businesses show their best real work (Heath). Own images over stock (Heath).
7. **Color and type.** Block colors stop the scroll (Cottrell); Levinger says keep brand colors out of ads, Cottrell recolours to brand: show the split, default to Ivan's call. Native overlays: Instagram's white box / black text, no brand fonts (Hott, `statics.md` §1).
8. **Sizes and Meta settings.** 4:5 feed master (Levinger triptych was 4:5), 9:16 story/reels version with story-native styling (Cottrell: match the placement), square where the source format is square. Heath: turn Advantage+ add overlays off when the image carries text, add animation off for text-heavy images (`statics.md` §1). Pixel specs and safe zones are not in the canon: designer uses Meta's current spec.
9. **Variants for diversity (`statics.md` §1, `formats.md` §1).** Post-Andromeda, new angles not tweaks (Cottrell 2026-02); identical-looking statics are read as one ad (Cottrell 2026-05; Divi vs Loop, `formats.md` §4). A distinct variant changes persona, message or format. Mix the three perspectives Brand / User / Expert POV (guest Mirella Crespi, `statics.md` §2). Denney: "Statics tend to become more stale more quickly." Default 3–5 variants.
10. **Image-generation handoff (optional, `statics.md` §2 AI static production).** AI makes the image only; text stays in Figma/Canva layers so copy can be tested and is not mangled (Cottrell, Cooper, NOW). Write the handoff block for `/ai-visuals-flynn`. New visuals go to Ivan before use.

## OUTPUT FORMAT

```
STATIC BRIEF — <offer / named service> · <persona> · <cold | warm>
Assumptions: <one line>   Ask size: <small | big> (Heath)   Placements: <feed / story / reels>
Message (source: Ivan | DRAFT): <one line>

DIVERSITY MATRIX
| Var | Persona | Message / belief | Format | POV (brand/user/expert) | Look | GEN/DTC | Era |

VARIANT A — <format> · <persona>
| Field | Spec |
|---|---|
| One goal | <single job of this static> |
| Why this format | <message → format reason; practitioner, file §, date; built from the canon, untested> |
| Production level | graphic / hi-fi / lo-fi phone (Denney) |
| Reading order | 1st: <where the eye lands> → 2nd: <key visual> → 3rd: <proof / CTA> |
| Layout | <grid: top third / middle / bottom; headline position; callouts ≤3; negative space> |
| Image direction | <who, where, doing what, real object or screen, crop, camera feel, light; what is NOT in frame> |
| Overlay text — DRAFT for Ivan | Headline (≤8 words): <...> / Support: <...> / Proof device: <...> / CTA: <...> |
| Meta fields — DRAFT for Ivan | Primary text first line: <...> / Headline field: <...> / CTA button: <...> |
| Type and color | <one font, max two; native white box or block color; brand-color call> |
| Sizes | 4:5 master; 9:16 version (<what moves>); square if <...> |
| Meta settings | Advantage+ add overlays OFF if text in image; add animation OFF if text-heavy |
| Transfer tag | GEN | DTC — <one-line flag> |
| Risk / watch | <the failure mode for this format from the canon> |

IMAGE HANDOFF → /ai-visuals-flynn (image only, no text baked in)
Subject: <real person / object from the buyer's world>  Setting: <real place>
Camera: <phone snapshot, off-centre, natural light | studio>  Composition: <keep top third clear for headline>
Must be literal: <...>   Must NOT include: text, logos, symbolic or metaphor props, stock gloss
Aspect: 4:5 master + 9:16   Reference: <Ivan-approved reference or DR asset>   Approval: Ivan sees it first

OPEN QUESTIONS FOR IVAN: <copy lines to approve; proof to confirm; brand-color call>
```

## QUALITY CHECK — run before returning

1. **One-second test** — a stranger knows what is offered and for whom in about a second (Denney, Cottrell; `statics.md` §2). Fail → cut text.
2. **One goal, one persona** per variant (Denney, Cooper).
3. **Stranger test** — the headline makes sense to someone who has never heard of the brand (Cooper rule 1; warm-only lines like Love These! fail cold, `statics.md` §4).
4. **Congruence** — the image shows the same situation the headline names (Levinger, Cooper).
5. **Cognitive load** — headline ≤8 words, ≤2 fonts, ≤3 callouts or one big number; Levinger on a cluttered ad: "the cognitive load on this ad is so high". Exception allowed only for a deliberate copy-heavy format (letter, storytelling), stated.
6. **Proof** — a proof device is present, or its absence is a stated choice; Cottrell: "Social proof is at the heart of any good static". Golden nugget, not generic praise (Denney).
7. **Diversity** — no two variants share persona + message + format; at least two formats and two looks.
8. **Lead-gen offer** — the service is named in the offer (Heath); ask size matches format.
9. **Literal and DRAFT** — every image is from the buyer's world; every copy line is marked DRAFT.
10. **Tags** — every format carries practitioner, file §, era, GEN/DTC.

## BENCHMARKS AND NUMBERS (creator-reported, not audited)

- ~90% of AdCrate static winners over 12 months were comparison, headline + callouts, or offer formats — Cooper, 2024-11, ALLTIME.
- IG-story native static: 10–15 min to build, six-figure spend, ~3.5% CTR — Cottrell, 2026-09, NOW. Humantra black offer static ~1.5% CTR vs a Post-it loser under 0.5% — Cottrell, 2025-12, EVERGREEN.
- Headlines max 8 words, 4–7 sweet spot; one font, never more than two — Levinger, 2026, NOW.
- Heath: B&W vs colour image can differ 10–15% (2024-10, ALLTIME); background-colour-only tests barely move the needle, test angles (2026-03, NOW).
- Statics go stale faster — Denney, 2026-05, NOW.
All DTC accounts except Heath's. Source: `statics.md` §5.

## CONTEXT: IVAN

Ivan runs Digital Rocket (DR), a ~40-person agency doing lead gen for immigration law, franchise recruitment (FranchiseFlow) and vocational training in the US, UK, AU and CA. All ad copy comes from him and he approves it; DR copy is short with minimal text; visuals are literal, from the buyer's world, no symbolic or metaphor imagery; proof and guarantees go in remarketing, belief-shift in prospecting; new visuals are shown to him first. Spend data comes from the Mirror app; images are made with Nano Banana; `/fb-creative-director` holds DR's play library.

What transfers for statics (`leadgen_transfer.md` §2, §5): the offer named in the headline (Heath); size-of-ask logic (image for a free named consultation or webinar, video for big cold asks); life-moment and location call-outs (Heath) and persona call-outs (Cooper); Post-it on the site or a screenshot (Hott, Savannah); real proof images such as testimonial and result screenshots (Heath); a real team member over stock (Hott, roofing). Does not transfer, or no evidence: product-in-hand, grids and bundles, BOGO, price-per-day anchors, catalog. Immigration, franchise and vocational offers are not in the corpus by name (`leadgen_transfer.md` §1); every DR brief is a transfer inference.

## REFERENCE FILES

| Question | File |
|---|---|
| Static types, layout, tier list, winners, losers, disagreements | `statics.md` §1–§7 |
| Which format for which job, tiers side by side, size of ask, diversity | `formats.md` §1–§6 |
| Headline wording, call-outs, specificity, objections, belief ladder | `copy_angles.md` §1–§6 |
| What transfers to lead gen; Heath's offer rules; DR-relevant examples | `leadgen_transfer.md` §1–§5 |
| Corpus counts, dates, accuracy notes | `sources.md` |

## HAND-OFF

- Hooks and opening lines → `/fbc-hooks`. Video version of the same message → `/fbc-video-script`. Critique an existing static → `/fbc-teardown`. How to test the variants → `/fbc-test-plan`. Consensus questions → `/facebook-creative-coach`.
- Creator depth: `/creative-cooper` (statics at scale, AI production), `/creative-cottrell` (statics, AI tools), `/creative-denney` (formats, tier list), `/creative-hott` (ugly ads, relevance), `/creative-levinger` (psychology, belief shift), `/creative-heath` (lead gen and services).
- DR skills: `/ai-visuals-flynn` (image generation from the handoff block), `/fb-creative-director` (DR play library), `/copy-wiebe` (copy polish after Ivan's direction).
- If a named skill isn't installed, say so in one line and give your own take from the canon.
