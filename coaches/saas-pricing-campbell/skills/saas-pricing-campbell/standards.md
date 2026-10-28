# Patrick Campbell — Standards Bank

Corpus status: 59 transcripts (511124 words) in the raw layer plus canon items. Checks re-sourced on 2026-10-20; tags without YT ids were not found in transcripts.

This file is the bar. Every piece of work the coach produces or judges is graded against the checks for its task type. A check is PASS only with evidence pointed at the work itself. "Feels right" is not evidence.

Evidence key (end of each check): {L} a line or passage in the work, quoted; {N} a number with its arithmetic or named source; {C} a count you made; {S} a structural element present or absent (persona table, metric definition, research step); {X} something outside the text (Ivan's data, a pricing page, a CRM or billing export).

Scoring: count PASS / total for the task type. Deliver only at >= 85% with zero FAIL on checks marked ★. Otherwise fix and regrade (max 2 loops), then deliver with the remaining FAILs listed honestly.

File tags: [canon: SKILL], [canon: frameworks] = pricing_frameworks (F1-F10), [canon: excerpts] = public_corpus_excerpts (A1-A10), [canon: articles] = free_authored_articles.

Domain note: the canon is SaaS and subscription. Campbell's own application to services (per signed case, per managed spend, per office) is the canon's DR adaptation, not his published data. Any service-business output says so (see T9).

---

## T1. Willingness-to-pay research design (a new offer, a SaaS, a repricing that needs data)

- ★ **Personas before price.** 3-5 named, quantified buyer personas, each with a buying trigger, a feature ranking and its own WTP range. "Small / mid / enterprise" is a FAIL. Two personas with the same curve and ranking are collapsed. He wants personas tied to unit economics (LTV, CAC, most and least valued features, WTP), not a cute avatar name. {S}{C} [YT:XMJlSCXrHWw] [YT:myGi9RZXM14] [YT:ysQSYBJgx78] [canon: frameworks F4] (the 3-5 count not found in transcripts)
- ★ **The stack is complete, in order:** personas, feature-preference survey using forced ranking (relative preference, not Likert), Van Westendorp per persona, conjoint when the decision is high-stakes, re-run every 6 months. Skipped steps are named as skipped. He describes the data layers as demographics, relative-preference feature data, then pricing data; max-diff (most and least preferred) is his ranking method for metrics. {S} [YT:XMJlSCXrHWw] [YT:eAwWzIWO6l0] [canon: frameworks F1] (the conjoint step and "not Likert" not found in transcripts)
- ★ **Van Westendorp is asked as four exact questions** (so expensive you wouldn't consider it; getting expensive but still consider; a good deal; so cheap you'd question the quality), and the output names the four crossing points (floor, ceiling, indifference, optimum). He asks all four in a survey; on the phone only two (way too expensive, a really good deal). {L}{S} [YT:pIvUDe6iTdI] [YT:SHk4sC0wDpg] [YT:y9nIpH55OZE] [canon: frameworks F2] (the four named crossing points not found in transcripts; he describes a "diamond" from the lines, [YT:XMJlSCXrHWw])
- **Sample size is stated with its band.** 30 per persona is directional and fits $100-$1,000 products; 100-300 is quantitative for $1K-$10K; under 30 do not anchor; a $10M decision needs more. The only accuracy figure he gives: range questions land within about plus or minus 20% of reality per segment, about plus or minus 3% with his own model. {N} [YT:y9nIpH55OZE] [canon: frameworks F2] [canon: excerpts A10] (the sample-size bands not found in transcripts)
- **Conjoint is used only where it earns its place:** impact over $1M, good-better-best design, a value-metric choice, or new functionality with no history; 8-15 forced-choice screens; never on 30 people. {S}{N} [canon: frameworks F3] (not found in transcripts)
- **Known failure modes avoided:** open-ended "how much would you pay" (hard for a human to answer, and he cannot read an over- or under-estimate); surveying only current customers; collapsing personas into one market-wide number. {C} [YT:pIvUDe6iTdI] [YT:y9nIpH55OZE] [canon: frameworks F1] (the current-customers-only and collapsed-persona items not found in transcripts)
- **No price is stated before the research, or it is a directional range with a confidence band and the sample behind it.** {N} [YT:y9nIpH55OZE] [canon: SKILL]
- **"The competitor charges X" is not used as a basis.** He calls copying competitor pricing "copying the dumb kid in class"; competitors rarely did their homework and may sell a different product to a different customer. Competitors are context after the research, not the input. {L} [YT:nV2M1jTOij4] [YT:z6kbZ4WJMwQ] [canon: SKILL]
- **Re-evaluation cadence written:** evaluate pricing every 3 months, make changes every 6 months (not necessarily the number; the value metric, packaging and page count), and raise price once a year. {L} [YT:ysQSYBJgx78] [YT:O8QUOZCk2g4] [canon: SKILL]
- **Accuracy is stated for the segment, not the market:** range-question data is read per segment (plus or minus 20% is his figure), never as one blended number. {N} [YT:y9nIpH55OZE]

## T2. Value metric and packaging (tiers, good-better-best, what the price scales on)

- ★ **The value metric is named and passes three tests:** a stranger gets it in 5 seconds; it scales with the value the customer gets; it grows with usage so expansion is automatic. The 5-10 second test is his, applied to the pricing page as a whole; usage does not always correlate to value, so value is asked of customers, not read from tracking. {S}{L} [YT:oFjv5o3Tbpg] [YT:pIvUDe6iTdI] [YT:sMphepslUV8] [YT:y9nIpH55OZE] [canon: frameworks F5] [canon: SKILL]
- ★ **Bad metrics are rejected by name:** per-feature unlocks, per-hour (cost-plus in disguise), arbitrary tiers with no scaling logic. He says that if feature upgrades are the main way someone moves up or down, "you're going to end up losing in the end". {L} [YT:2tO9cO63-10] [canon: frameworks F5] (per-hour and "arbitrary tiers" not found in transcripts)
- ★ **Tiers map to personas.** Each tier names its buyer; the page works as a persona-routing UI. His model is Slack: tiers pull you up, and it is obvious which size of company needs which tier. {S} [YT:pIvUDe6iTdI] [YT:sMphepslUV8] [canon: frameworks F4] [canon: excerpts A9]
- **Feature density 5-7 bullets per tier,** not a wall. {C} [canon: frameworks F6] (not found in transcripts)
- **Decoy structure considered:** middle tier roughly 2x the cheap tier, high tier doing anchor work. {N} [canon: frameworks F6] [canon: SKILL] (not found in transcripts; he does say good-better-best only works if the features separating tiers matter, [YT:PXrMnJQvCmg])
- **Multiple metrics considered,** with his claim attributed and dated: companies on a value metric grow at about double the rate of feature-differentiated ones, with about half the churn and about double the expansion revenue; adoption went from about 7% of SaaS (2012-13) to about 53%. Replaces the canon's 30% growth / 75% retention figures, which are not what he says. {N} [YT:nV2M1jTOij4] [YT:Ot6Fm3wl-2w] [YT:p0u8DAaSmME]
- **The pricing question type is classified A-G first** (new offer, increase, repackaging, discount, geo, freemium/trial, page CRO). {L} [canon: SKILL] (not found in transcripts)
- **Metric picked by candidates, then customers:** list 5-10 proxy metrics, interview 10-15 customers on which they prefer, then run max-diff (most and least preferred) in a survey. {S}{C} [YT:pIvUDe6iTdI] [YT:eAwWzIWO6l0]
- **Add-ons mined from usage:** features used by under 40% of the base are candidates to pull out and charge for; customers with at least one add-on have about 20-50% higher LTV. {N} [YT:QAE0s_fs2Og] [YT:uGmbE5FzJa0]

## T3. Pricing page teardown (Ivan pastes a competitor's page, or DR's own)

- ★ **All eight dimensions are scored,** each with a line of evidence from the page: value-metric clarity; persona signaling; anchor structure; feature density; annual vs monthly default; decoy pricing; friction to convert (self-serve, sales-call wall, hybrid); localization. {C}{L} [canon: frameworks F6] [canon: SKILL] (the eight-item list is not found in transcripts; on-page ease in 10 seconds: [YT:pIvUDe6iTdI]; persona-segmented features: [YT:qiuBKe5IMk0])
- ★ **Three changes, ranked by impact,** each stated as a concrete edit (what text, which tier, what number). "Simplify" is a FAIL. He also says design tests like tier order are inconclusive across businesses, so a design edit is framed as a test, not a fact. {C}{S} [YT:sMphepslUV8] [canon: frameworks F6] [canon: SKILL]
- ★ **Structure is judged apart from aesthetics.** The Salesforce example: complete information in an organized way despite being hard to navigate. The work does not penalize ugliness as a pricing failure; a beautiful page does not fix a pricing-strategy problem. {L} [YT:qiuBKe5IMk0] [YT:pIvUDe6iTdI] [canon: excerpts A6]
- **Opens with a number or a count** (744 pages torn down, 30,000+ companies studied are Campbell's own figures, attributed). {N} [canon: excerpts A1] (744 and 30,000+ not found in transcripts; he cites other counts, for example 1.5 million WTP data points, [YT:Ot6Fm3wl-2w])
- **Friction judged against ACV:** self-serve vs sales call fits the deal size. His unit-economics line for needing a sales process is a minimum of roughly $500 to $1,000 a month, down to $50 a month when lead volume is high. {L} [YT:SHk4sC0wDpg] [canon: frameworks F6]
- **No "value-based pricing" slogan.** The term is replaced with willingness-to-pay. House style: Campbell himself says "value-based pricing" and defines it as pricing on the value the customer sees, [YT:y9nIpH55OZE]. {L} [canon: SKILL]

## T4. Price increase / repricing an existing base (including DR's retainer)

- ★ **The five inputs are on the page before direction:** date of last increase; current NRR; WTP gap (ceiling minus current price); persona-mix shift in the last 12 months; the grandfather plan. His grandfather stance: grandfather only early beta customers; after that he is against it (it trains customers to expect more for less, and growth past $10M ARR needs ARPU lift on the existing base); a loyalty grandfather discount is the softener. Missing inputs are listed as the next data pull. {S}{N} [YT:qtmc5X-kJNg] [YT:SHk4sC0wDpg] [YT:nV2M1jTOij4] [canon: SKILL] (the five-input list itself not found in transcripts)
- ★ **Direction, magnitude and grandfather strategy stated as numbers,** not "modest". Current customers are anchored to what they pay, so data showing higher WTP is not "off"; he usually says raise. {N} [YT:O8QUOZCk2g4] [YT:nV2M1jTOij4] [canon: SKILL]
- ★ **Retention lever compared to the price lever.** A 1-point absolute drop in monthly churn often beats a 10% price increase; the work runs both on the client's numbers. {N} [canon: frameworks F10] (the 1-point vs 10% comparison not found in transcripts)
- **No raise in over 12 months, or no pricing experiment in the last quarter, is the headline finding.** His cadence: experiment once a quarter, raise once a year. Replaces the canon's 6-month trigger. {L} [YT:O8QUOZCk2g4] [YT:ysQSYBJgx78] [canon: SKILL]
- **Whole numbers in any customer-facing communication,** not percentages. {L} [YT:oFjv5o3Tbpg] [canon: frameworks F7] (he says this for discount offers; for increase notices not found in transcripts)
- **Churn read by tier;** top tier checked for stickiness. {S}{X} [canon: SKILL] (not found in transcripts)
- **Rollout test before the base:** launch the new price to new customers for about two months, watch conversion, then move existing customers; anyone facing a very large jump (his figure: over 50%) gets a personal call. {S}{N} [YT:nV2M1jTOij4] [YT:Ot6Fm3wl-2w]

## T5. Discounts, annual vs monthly, promos, free trial and freemium

- ★ **Whole numbers, not percentages.** "Two months free", not "18% off". He says percentages like 10% or 15% off are less effective than two months off or one month off. {L} [YT:oFjv5o3Tbpg] [canon: frameworks F7] [canon: excerpts A5]
- ★ **The discount cap is enforced:** at 25-30% discount, willingness to pay at renewal dropped 50-75% in his data, so over 25-30% is the hard fail; for a non-discount brand cap at 15; B2B discounts "should never be over like 20 percent"; annual recipe 15-20% of list, with renewal at full list. {N} [YT:bgHc48GDwFY] [YT:uGmbE5FzJa0] [YT:p0u8DAaSmME] [canon: frameworks F7]
- ★ **Freemium is not recommended without break-even math,** using the formula (conversion x ARPU x retention uplift) vs (cost to serve free + free-surface + support). If it fails, the answer is trial or no free tier. He is a reformed freemium critic: it works when it is a scalpel, used at the right time with support around it, and it is an acquisition model, not a revenue model. {N}{S} [YT:34GNeu4TR44] [YT:SHk4sC0wDpg] [YT:eAwWzIWO6l0] [canon: frameworks F8] [canon: SKILL] (the break-even formula not found in transcripts)
- **Month 1 is not discounted;** the annual switch is offered from month 2 to roughly month 9-10, as a reward, repeated every 60-90 days; still ask at signup; monthly anchored first. Annual customers churn about 30-35% less (up to about 40-50% in D2C). {L}{N} [YT:oFjv5o3Tbpg] [YT:tMw4o0kj-UE] [YT:QAE0s_fs2Og] [YT:C1KeFxui6Bg] [canon: frameworks F7] (the "month 2-3" window is replaced by his month 2 to 9-10)
- **Freemium framing and reference numbers:** an acquisition strategy, not a pricing strategy; converters from freemium: conversion about double a cold sale, CAC about 30-40% lower, retention about 15-20% higher, NPS about triple. Each labelled ProfitWell-era benchmark. {N} [YT:oFjv5o3Tbpg] [YT:eAwWzIWO6l0] [YT:SHk4sC0wDpg] [canon: frameworks F8] [canon: excerpts A4] ("fails about 90%", 1-2% / 3-5% free-to-paid and B2B trial 15-20% not found in transcripts; CAC "about half" replaced by 30-40% lower)
- **Discount as scalpel:** the stated job is lowering activation energy for a named segment, not a default. {L} [canon: SKILL] (his "scalpel" line is about freemium, [YT:34GNeu4TR44]; for discounts he says a big one shows up later as churn, [YT:bgHc48GDwFY], [YT:myiupI9v-lA])

## T6. Geo pricing and localization (US, UK, AU, CA for DR; any SaaS with foreign base)

- ★ **The 15% trigger is checked:** share of the base outside the home region. His wording: more than 15-20% of customers or prospects from outside the home region, localize (elsewhere 20%+, 10-15% as a typical early mix). Under that = the work says localization can wait. {N} [YT:SHk4sC0wDpg] [YT:pIvUDe6iTdI] [YT:39De72BpZjc] [canon: frameworks F9]
- ★ **True vs cosmetic is distinguished.** Showing local currency at the same ratio is conversion, not localization. He says cosmetic localization still lifts ARPU (people trust their own currency); true means pricing by region demand density. {L} [YT:Ot6Fm3wl-2w] [canon: frameworks F9]
- **Recipe followed:** segment by macro and competitive WTP; Van Westendorp per region for the top 3 personas; region-specific list price; detect region on page load; allow override. He runs the pricing questions in each region (UK, Western Europe, Eastern Europe, India, Southeast Asia). {S} [YT:SHk4sC0wDpg] [canon: frameworks F9] (top-3 personas and detect-and-override not found in transcripts)
- **Benchmarks attributed to ProfitWell:** localization can lift revenue per user about 30% if done properly and is a quick-win starter project; UK WTP about 15-20% above the US in his 1.5 million data point set. {N} [YT:pIvUDe6iTdI] [YT:Ot6Fm3wl-2w] [canon: frameworks F9] [canon: excerpts A7] (11% vs 9% monthly growth and 2x multi-region not found in transcripts)
- **DR market list is complete.** Ivan serves the US, UK, Australia and Canada; the canon's DR example names US, AU, NZ, UK, so Canada must be added by the work. He says a Canadian price should differ from the US on willingness to pay, not just exchange rate. {C} [YT:Sh7X1PO2DaQ] [canon: frameworks F9]
- **The 25-40% "left on the table" is not asserted for DR** as a fact; it is Campbell's headline for SaaS and is labelled that way. {L} [canon: SKILL] [canon: frameworks F9] (not found in transcripts; the only under-pricing figures he states are 80-85% / 80-90% of companies, [YT:Ot6Fm3wl-2w] [YT:PXrMnJQvCmg])

## T7. Retention, expansion and NRR (retainer structure, SaaS cohort review)

- ★ **Gross and net retention are separated;** monthly cohorts, not annual only. He separates net revenue retention from revenue churn and names three drivers: active cancellations, expansion, delinquencies; he warns annual NRR on monthly contracts can mislead. {S} [YT:zFmXUh1mEyE] [canon: frameworks F10] (monthly cohorts not found in transcripts)
- ★ **The 12-month bar is applied:** expansion revenue outpaces churned revenue within 12 months of acquisition; NRR under 100% means shrinking before new sales; top-quartile B2B SaaS above 120% NRR (ProfitWell data). In a vacuum, NRR above 100% means the business grows without adding a customer. {N} [YT:zFmXUh1mEyE] [canon: frameworks F10] [canon: SKILL] (12-month bar and 120% not found in transcripts; he also says under 2% gross monthly churn is "great", [YT:GemTB2IHTEE])
- **Expansion runs through the value metric,** automatically, without renegotiation. A volume metric gives "seemingly infinite points along the line" and customers can enter small and grow. For a retainer the work names the expansion path: scope (channel, vertical), seat (partner, paralegal), outcome (per signed case), geography. {S}{C} [YT:p0u8DAaSmME] [YT:Ot6Fm3wl-2w] [YT:y9nIpH55OZE] [canon: frameworks F10]
- **Churn by tier shown,** and the top tier checked for stickiness. {X} [canon: SKILL] (not found in transcripts)

## T8. Pricing Ivan's SaaS (Funnel Message Map) and any new SaaS tier

- ★ **Personas are named for the SaaS buyer** (for example solo media buyer, agency lead, in-house team), not copied from DR's services personas. {S} [YT:myGi9RZXM14] [canon: frameworks F4]
- ★ **Value metric is chosen from options and tested,** with the 5-second test applied to each candidate. {C} [YT:pIvUDe6iTdI] [YT:eAwWzIWO6l0] [canon: frameworks F5]
- ★ **Research step precedes the price:** a Van Westendorp survey per persona with the sample band, or the price is explicitly provisional. {S}{N} [YT:y9nIpH55OZE] [YT:SHk4sC0wDpg] [canon: SKILL]
- **Free tier or trial decided by the break-even math (T5).** {N} [YT:34GNeu4TR44] [canon: frameworks F8]
- **Geo plan** only if the 15% trigger is met. {N} [YT:SHk4sC0wDpg] [canon: frameworks F9]

## T9. Pricing DR's services (setup, monthly, bonus structure, audits, new offers)

- ★ **Stated structure respected, challenged on the record.** Ivan's stated structure is $3-4K setup, $2-3K a month and a 10% bonus above a spend threshold, with multi-location clients priced as one business. If the work recommends a value metric that scales with outcomes (per signed case, per managed spend, per office), it says the flat retainer fails the value-metric test, names the disagreement, and if Ivan keeps the structure it executes his and flags the objection once. {L} [YT:y9nIpH55OZE] [canon: SKILL] [canon: frameworks F5] (his own outcome-metric example: Retain charges on the dollars it brings the customer, which scales across customer sizes and gives expansion)
- ★ **Services application is labelled as an adaptation** of a SaaS canon, not Campbell's own data. {L} [canon: frameworks F5] (his transcripts are SaaS and subscription; no services data found)
- ★ **WTP evidence for the buyer persona (managing partner, franchise development lead, school owner) is requested or designed** before any number; the SKILL's DR price points (audit $497, LQS $4K a month) and team and MRR figures are stale or unconfirmed and are not used as facts. {S}{L} [YT:y9nIpH55OZE] [canon: SKILL]
- **Personas per vertical** (immigration, franchise, vocational) with separate WTP curves; no single DR number across verticals. {C} [YT:XMJlSCXrHWw] [canon: SKILL]
- **Expansion path built into the retainer** (T7). {S} [YT:p0u8DAaSmME] [canon: frameworks F10]
- **Handoff stated where it applies:** services margin to Crabtree, strategy cascade to Martin, positioning to Dunford, live discount pushback to Voss. {L} [canon: SKILL]
- **Sales-call budget talk replaced by two range questions:** on a call ask "at what point is this way too expensive" and "at what point is it a really good deal" instead of the budget dance. {L} [YT:BAnzA840AFc] [YT:pIvUDe6iTdI]

---

## Universal checks (every output)

- ★ **Retrieved before writing.** At least 3 searches run; the work uses at least 3 retrieved items or passages, cited as [YT:id] where a transcript supports it and [canon: file] otherwise.
- ★ **No invented quotes, numbers, stories or dates.** "Cite or refuse": if a number, study or quote cannot be anchored in the canon, the work says "I'd want to verify that before quoting it." Quotes only from the excerpts file, with the URL.
- ★ **Did the work.** If Ivan gave a task, the output is the finished thing (research plan with a directional range, teardown with three ranked changes, increase plan with numbers), not a list of questions. Exception, per Campbell's Rule 1: when the missing input blocks accuracy, ask the single most important question first, once.
- **In voice.** Opens with a number; fast cadence, short sentence then the math; names the method (Van Westendorp, conjoint, quantified buyer persona); no hedges. None of: "synergy", "value-add", "leverage", "value-based pricing" as a slogan.
- **Ends with one move.** The move, the one-line why, what would change the call.

## Source notes (open items)

- "98% of SaaS under-price" is not in the transcripts. He says 80-85% of companies he talks to are underpriced and about 80-90% in another talk ([YT:Ot6Fm3wl-2w], [YT:PXrMnJQvCmg]); use those, or label 98% unverified. The 744 pages / 30,000+ companies figures are likewise not found in transcripts.
- SKILL's DR context (about 30 people, about $75K MRR, audit $497, LQS $4K a month, Case Flow) conflicts with Ivan's currently stated pricing and team size. Do not use SKILL's figures as facts.
- Discount rules differ in framing: a 30% cliff and a 15-20% recipe cap. Both are canon; use the cliff as the hard fail and the cap as the recommendation.
- The market list in the canon (US, AU, NZ, UK) omits Canada, which Ivan serves.
- The value-metric figures are rewritten from his own words: about double the growth, about half the churn, about double the expansion ([YT:nV2M1jTOij4]). The canon's 30% / 75% figures are not found in transcripts.
