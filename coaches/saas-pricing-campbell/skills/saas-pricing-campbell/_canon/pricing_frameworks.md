# Patrick Campbell — Pricing Framework Map

**Author of record:** Patrick Campbell (Price Intelligently 2012 →
ProfitWell → Paddle CSO, 2022 acquisition for $200M).
**Corpus:** No single canonical book. Body of work = ProfitWell/Paddle
blog, Pricing Page Teardown YouTube series (7+ seasons), Protect the
Hustle podcast, ProfitWell Report, First Round Review essays, SaaStr /
BoS keynotes, @Patticus Twitter/X, guest appearances on Lenny's / Indie
Hackers / Acquired.

**Source treatment:** Frameworks named, mapped to source-genre,
described in own words. Campbell's prose is NOT reproduced. Short
fair-use quotes with URL live in `public_corpus_excerpts.md`.

---

## Theme map

| # | Theme | Source-genre |
|---|-------|------|
| 1 | Willingness-to-Pay research | First Round Review; ProfitWell blog; Lenny's |
| 2 | Van Westendorp's Price Sensitivity Meter | Acquired.fm; ProfitWell blog |
| 3 | Conjoint analysis | ProfitWell blog; Business of Software talk |
| 4 | Quantified buyer personas | First Round Review; Paddle docs; SaaStr |
| 5 | Value metrics | ProfitWell blog; PPT episodes; Reforge |
| 6 | Pricing Page Teardown methodology | YouTube series 7+ seasons; LinkedIn |
| 7 | Annual vs Monthly + discount math | Hidden Costs of Discounting |
| 8 | Freemium math & PLG conversion | Mastering Freemium benchmarks |
| 9 | Price localization | ProfitWell blog; Intercom |
| 10 | Cohort retention + expansion revenue | ProfitWell Report; Largest Study on Churn |

---

## Framework 1 — Willingness-to-Pay Research (master frame)

Treating pricing as a research problem, not a guess. WTP = the specific
number a defined persona will trade for a defined feature bundle.
Measurable.

**Campbell's headline:** Across the ProfitWell dataset (30,000+
companies), the vast majority are materially under-priced. Often-cited
figure: ~98% of SaaS under-price relative to the WTP their buyers
report. "Value-based pricing" has become a slogan with no operating
definition — replace with willingness-to-pay research.

**Research stack:**
1. Define 3-5 quantified buyer personas
2. Feature-preference survey, relative-preference methodology (forced
   ranking, NOT Likert — Likert creates ceiling effects)
3. Price-sensitivity via Van Westendorp's four questions
4. Conjoint for high-stakes decisions
5. Re-run every 6 months

**Failure modes:** "how much would you pay?" open-ended (noise);
surveying only current customers (selection bias); collapsing 3-5
persona WTPs into one market-wide point estimate.

---

## Framework 2 — Van Westendorp's Price Sensitivity Meter

**The four questions:**
1. At what price would this be **so expensive you wouldn't consider it**?
2. At what price would it be **getting expensive but you'd still consider**?
3. At what price would it be **a good deal**?
4. At what price would it be **so cheap you'd question the quality**?

Plot four cumulative curves. Crossing points produce: **PMC** (floor),
**PME** (ceiling), **IPP** (indifference), **OPP** (optimal — minimizes
total rejection).

**Sample-size bar:** 30/persona = directional for $100-$1000 products;
100-300 = quantitative for $1K-$10K decisions; <30 = don't anchor.

---

## Framework 3 — Conjoint Analysis (the higher-stakes layer)

Van Westendorp tells you what someone pays for the whole product.
Conjoint tells you what they pay for each feature inside it.

**When Campbell uses it:** decision >$1M impact; designing good-better-
best; choosing between value-metric options; new functionality with no
historical signal.

**Mechanic:** respondents see 8-15 forced-choice screens with 2-3
configurations at different prices. Choice pattern → utility coefficients
per feature and price level. Small decision → Van Westendorp enough. Big
→ conjoint. Don't run conjoint on 30-person sample.

---

## Framework 4 — Quantified Buyer Personas

Data-driven profiles — demographic + psychographic + buying-trigger
attributes, each with its own WTP distribution.

**Campbell's naming pattern** — first-name + segment: "Startup Susan",
"Mid-market Malik", "Enterprise Ernesto". DR services context:
"Solo-Practitioner Sofia", "Multi-Office Maria", "National-Franchise
Frank".

**Discipline:** target 3-5 (fewer = under-, more = fragmentation). Each
has different buying trigger, feature ranking, WTP range. Same curve +
ranking = same persona, collapse.

**Where it goes:** persona structure → tier structure. Pricing page is
a persona-routing UI.

---

## Framework 5 — Value Metrics (the pricing axis)

**Campbell's claim, backed by ProfitWell data:** some sort of value
metric beats tier-based pricing on every measure. Multiple metrics →
~30% higher growth; ~75% better retention vs feature-tier-only.

**Properties:** easy to understand (5-second test); aligned with value;
grows with usage (auto-expansion).

**Bad:** per-feature ("Pro unlocks 14 more"); per-developer-hour
(cost-plus disguised); per-arbitrary-tier with no scaling logic.

**DR services:** per signed case (immigration), per managed spend
(franchise), per office/location, per qualified appointment. Flat
retainers fail the value-metric test.

---

## Framework 6 — Pricing Page Teardown Methodology

The diagnostic protocol from tearing down 744+ pages. 8 dimensions:
1. **Value-metric clarity** — stranger gets it in <5 seconds?
2. **Persona signaling** — does each tier map to a buyer?
3. **Anchor structure** — high tier doing decoy work?
4. **Feature density** — sweet spot 5-7 bullets per tier
5. **Annual vs monthly default** — which is visual default?
6. **Decoy pricing** — middle ~2x cheap (Economist trick)
7. **Friction to convert** — self-serve / sales-call / hybrid (ACV-dep)
8. **Localization signal** — currency toggle? country detection?

**Use:** Ivan pastes a page → run all 8, surface 3 highest-impact changes.

---

## Framework 7 — Annual-vs-Monthly + Discount Math

Annual contracts increase LTV materially. Discount level and discount
communication independently drive conversion.

**Hard rules (Campbell's data):**
- **Humans can't do percentages.** "18% off" performs worse than "two
  months free" — even when math is identical. Translate to whole-number
  months/units.
- **30% is the cliff.** Discounts >30% at original purchase create WTP
  collapse at annual renewal.
- **Scalpel, not chainsaw.** Discount lowers activation energy.
- **Don't discount month 1.** Offer annual switch at month 2-3.

**Recipe:** anchor monthly first; offer annual as "save two months";
cap discount at 15-20% of annual list; renewal at full list.

---

## Framework 8 — Freemium Math (the 90% failure cliff)

**Campbell's positioning:** Freemium is an acquisition strategy, not a
pricing strategy. Mishandled, fails ~90% of attempts.

**The math:**
- Free-to-paid conversion: 1-2% pure / 3-5% PLG with strong funnel
- CAC for freemium-converters: ~50% of standard
- Retention uplift: ~20% better than cold-acquired paid
- B2B SaaS free-trial (comparison): 15-20%

**Break-even test:** (conversion × ARPU × retention-uplift) vs (cost of
serving free + free-product surface + support cost). Left must exceed
right by meaningful margin. If not, convert to free trial or remove.

---

## Framework 9 — Price Localization (the 25-40% revenue most SaaS leaves on the table)

**Rule:** >15% of base outside your home region → localize.

**Two definitions (don't confuse):**
- **Cosmetic:** display local currency, same ratio ($100 USD = €100 EUR).
  Conversion, not localization.
- **True:** different price points per region based on regional WTP.

**ProfitWell-cited results:**
- True localization: ~11% MoM growth (vs ~9% cosmetic only)
- Multi-region true-localized: nearly 2x growth vs no-localization
- Emerging-market conversion lift: up to ~30% without cannibalizing
  established markets

**Recipe:** segment by macro + competitive WTP → Van Westendorp per
region for top-3 personas → region-specific list price → detect region
at page load, serve right price by default → allow override.

**DR:** US, AU, NZ, UK are different agency-fee markets. Same offer,
three+ different price points minimum.

---

## Framework 10 — Cohort Retention + Expansion Revenue

Highest-leverage pricing improvement is usually retention, not list
price. 1% absolute reduction in monthly churn often beats 10% price increase.

**Headline benchmarks (ProfitWell dataset):**
- Most successful subscription companies see expansion revenue **outpace
  churned revenue within 12 months** of acquisition
- Top-quartile B2B SaaS historically posted NRR >120%
- NRR <100% = shrinking before new sales

**Discipline:** monthly cohorts; gross retention (cancellation) separate
from net (cancel + downgrade + expansion); annual cohorts mask quarterly.

**Expansion (DR/services):** scope (channel/vertical), seat (partner/
paralegal), outcome (per-signed-case scales as firm closes more),
geographic. Retainer must allow expansion *automatically* through the
value metric, not require renegotiation.

---

## How AICampbell uses this file

1. Ivan describes a pricing question → use SKILL.md diagnostic (A-G).
2. Pull mechanism, hard rules, benchmarks from this file.
3. Cite source-genre so Ivan knows where to read Campbell's own words.
4. For voice and verified wording, see `public_corpus_excerpts.md`.

---

*Source: Campbell's free public corpus — ProfitWell/Paddle blog, Pricing
Page Teardown, Protect the Hustle, ProfitWell Report, First Round
Review, SaaStr/BoS keynotes, @Patticus, guest appearances on Lenny's /
Indie Hackers / Acquired. URL catalogue in `free_authored_articles.md`.*
