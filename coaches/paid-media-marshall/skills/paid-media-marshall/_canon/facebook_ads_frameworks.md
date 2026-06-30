# Facebook / Meta Ads — Framework Map

**Author:** Perry Marshall (with Bob Regnerus and Thomas Meloche)
**Source treatment:** Framework structures from *Ultimate Guide to Facebook Advertising* (Entrepreneur Press, 4th ed., the most recent at time of writing — earlier editions spanning roughly 2011-2022). Framework structures described in own words for synthetic-coach use. Book text is NOT reproduced. Each framework is named, mapped, and described mechanically so the AIMarshall skill can apply it. To read Marshall's own prose, get the book. URL: `https://www.perrymarshall.com/facebook/`.

---

## Operator's view of the Meta corpus

Marshall's Facebook book was first published in 2011 — before retargeting was widely available, before the Pixel existed, before Conversions API, before Special Ad Categories, before the iOS 14.5 attribution collapse. The 4th edition rewrote large portions of the book to address signal-loss, algorithmic targeting, and the special-ad-category regime that applies to housing, employment, credit, and (in many implementations) immigration-related ads.

The thesis that survives across all editions: **Meta is a demand-generation platform, not a demand-fulfillment platform.** The prospect on Meta is not searching for your category. The operator's job is to interrupt attention with creative that compresses the demand-creation arc into a single scroll.

Where Google rewards relevance (Framework 2 in `google_ads_frameworks.md`), Meta rewards **creative-driven signal quality**. The audience-targeting controls are increasingly secondary — the algorithm finds the audience faster than humans can target it, IF the creative gives it clean signal to optimize against.

---

## Framework 1 — The Audience-Targeting Hierarchy

**What it is:** Meta's targeting options collapse into a stack, ordered by signal density. The operator's job is to know which layer applies, given the account's data state.

**The stack (highest signal at top):**

| Layer | Signal source | When to use |
|---|---|---|
| 1. Custom Audience — Customer List | Your own CRM/buyer list | Always. Foundational. |
| 2. Custom Audience — On-Site Events | Pixel + Conversions API | Once you have 100+ events/week. |
| 3. Custom Audience — Engagement | Page, video, lead-form, IG profile | When site traffic is thin. |
| 4. Lookalike — from Layer 1 or 2 | Meta finds users similar to your seed | When you need to scale beyond Layer 1-3. |
| 5. Interest + Behavior Targeting | Meta's declared / inferred attributes | When you have no first-party data yet. |
| 6. Broad / Open Targeting | No targeting except age/geo | When creative is strong and budget is large. |

**The operating rule:** start at the highest layer your data state supports. Move down the stack only as you exhaust the audience or hit Meta's frequency cap.

**The reverse direction (most agencies' mistake):** starting at Layer 5 (interest targeting) because it feels precise. In modern Meta, interest stacks are often less effective than broad-with-strong-creative because the algorithm's audience model is now more accurate than the interest taxonomy.

**Failure mode:** assuming "more targeting" = "better targeting". Layer 5 with 20 interests stacked together is worse than Layer 6 (broad) with the same creative, because the stack constrains the algorithm.

---

## Framework 2 — The FB vs Google Buyer-Intent Asymmetry

**What it is:** the single most important conceptual distinction in paid media — these two platforms are not interchangeable. The buyer state is different. The creative logic is different. The economics are different.

**The asymmetry:**

| Dimension | Google Search | Meta (Facebook + Instagram) |
|---|---|---|
| Buyer state | Actively searching | Passively scrolling |
| Demand model | Fulfilment | Generation |
| Creative job | Match the query, close the search | Interrupt attention, create demand |
| Targeting unit | The keyword | The audience + creative |
| Optimization rewards | Relevance | Engagement |
| First-touch attribution | Cleanest | Murky (especially post-iOS 14.5) |
| Conversion lag | Shorter (intent already exists) | Longer (intent has to be built) |
| Cost per click | Higher (intent priced in) | Lower (interruption taxed lightly) |
| Cost per qualified lead | Often lower | Often higher per lead, sometimes lower per signed client |

**The operator's implication:** the prospect on Meta is not the prospect on Google, even when it's the same human. Their state of mind is different. The creative that converts on Google ("EB-5 Immigration Attorney — Free Consult") will FAIL on Meta. The creative that converts on Meta (story-driven, problem-aware, scroll-stopping) will FAIL in a Google search ad.

**Failure mode:** copy-pasting Google ad copy into Meta or vice versa. They are different mediums with different physics. They require different creative entirely.

---

## Framework 3 — The Creative-Testing Protocol

**What it is:** in modern Meta, creative is the lever. Audience is secondary (Framework 1). Bid strategy is tertiary. The 80/20 of optimization sits in creative.

**The four-axis test matrix (test ONE axis at a time):**

| Axis | Variants to test | Sample size per variant |
|---|---|---|
| Hook (first 3 seconds) | 3-5 hooks | $50-100 spend each |
| Angle (the problem framing) | 2-4 angles | $100-200 each |
| Format | Static / Carousel / Video / UGC | $100-200 each |
| Call-to-action | Direct / Soft / Curiosity | $50-100 each |

**The cadence:** weekly test cycle. Kill losers fast (statistical significance is achievable with $50-150 spend at typical CPMs for high-volume objectives). Promote winners to the main set. Refresh the test slate every Monday.

**The 80/20 inside Meta creative:**
- 80/20¹: ~20% of creatives produce ~80% of conversions.
- 80/20²: ~4% drive ~64%. Often a single hook × format combination.
- 80/20³: ~0.8% drive ~51%. The "hero creative" — protect, defend, only retire when fatigue is measurable.

**Creative fatigue (Marshall's metric):** when CPM rises >40% or CTR drops >30% on a previously-stable creative, fatigue has set in. Refresh, don't push harder.

**Failure mode:** the "many creatives" trap — running 30 creatives in one ad set. Meta's algorithm cannot reach statistical significance per creative, so it picks a winner randomly. Run 3-6 per ad set, kill losers fast, replace.

---

## Framework 4 — Lookalike Audience Strategy

**What it is:** Lookalike Audiences (LAL) ask Meta to find users similar to a seed audience. The seed is the leverage point — feed Meta a high-quality seed and the LAL is strong; feed it a weak seed and the LAL is noise.

**The seed hierarchy (best seed → worst seed):**

| Seed | Quality | Notes |
|---|---|---|
| Highest-LTV customers (e.g. top 4% by revenue) | Best | The Star Principle applied to seeds. |
| All customers (paid clients) | Strong | Default starting point. |
| Lead-form submitters | OK | Many will never buy. |
| Purchase-event users | Strong (if Pixel is clean) | Equivalent to "all customers" via pixel. |
| Website visitors (any page) | Weak | Mostly tire-kickers. |
| Page-likers | Weakest | Liked your page for unrelated reasons. |

**The percentage knob:** 1% LAL = closest match, smallest audience. 10% LAL = loosest match, largest audience. For most accounts, 1-3% is the sweet spot. Stack multiple LALs (1%, 1-3%, 3-5%) into a single ad set to give Meta range without diluting too far.

**The minimum-seed-size constraint:** LAL needs ~100 minimum seeds in the target country to compute; 1,000+ is meaningfully better; 10,000+ gives the algorithm room.

**Special-ad-category exception (immigration, housing, employment, credit):** lookalikes are restricted or disabled entirely in special-ad-category accounts in many markets. The audience tools collapse to a constrained subset of broad + age + geo. The creative becomes even more important because targeting is artificially capped.

**Failure mode:** building LALs from a noisy seed (page-likers, video viewers, junk Pixel data). The LAL inherits the seed's noise and underperforms.

---

## Framework 5 — Retargeting Funnels (the warmth ladder)

**What it is:** Meta's most leverage-dense use case isn't prospecting — it's retargeting. A prospect who has already seen your brand once converts at 5-15× the rate of a cold prospect. The funnel is built by segmenting that traffic into warmth bands.

**The four-band retargeting funnel:**

| Band | Seed | Creative job |
|---|---|---|
| Hot (last 7 days) | Lead-started, cart-added, demo-booked-no-show | Direct close — "complete your application" |
| Warm (last 30 days) | Page-viewed, video-watched-75% | Re-introduce — "did you see this case study?" |
| Cool (last 90 days) | Any pixel event | Re-engage — broader story |
| Lapsed (90-365 days) | Old buyers, old leads | Win-back — new angle, new offer |

**The frequency cap (Marshall's discipline):** retargeting only works up to ~3-4 impressions per prospect per week. Beyond that, ad fatigue + brand resentment outweighs the conversion lift. Cap frequency explicitly at the campaign level.

**Special-ad-category exception:** even within special ad categories, retargeting based on website visits is usually still allowed (though the lookback windows and audience-creation tools are constrained). Retargeting becomes one of the few advantages available to special-category advertisers.

**The 80/20 inside retargeting:**
- Most of the spend should go on cold prospecting (Layer 5-6 in Framework 1), because the prospect pool there is far larger.
- But the **ROAS** is usually highest in the Hot and Warm bands. The conversion math says: cold to warm = high-volume, lower-ROAS. Warm to closed = low-volume, very-high-ROAS.

**The compounding move:** every dollar of cold prospecting refills the retargeting pool. So under-investing in cold = retargeting pool drains = retargeting ROAS collapses six weeks later. The system has to be balanced.

**Failure mode:** running retargeting in isolation, watching the ROAS look great, scaling retargeting budget, watching ROAS collapse as the warm pool shrinks. Cold and warm budgets are coupled.

---

## Framework 6 — Special-Ad-Category Constraints (immigration-specific)

**What it is:** Meta's special-ad-category regime — applied to housing, employment, credit, and in many jurisdictions to immigration adjacent advertising — strips out a large fraction of the targeting and lookalike toolkit on those campaigns.

**What's restricted (in special-ad-category):**
- Custom Audiences from customer lists — restricted in some implementations.
- Lookalike Audiences — replaced with "Special Ad Audience" (a weaker, less-similar version) or disabled.
- Detailed targeting — many demographic, behavioral, and interest filters are unavailable.
- Age ranges narrower than 18-65 — disabled.
- Geo targeting at zip-code level — disabled (city-level or larger only in most cases).

**What's still available:**
- Broad targeting + creative.
- Retargeting based on Pixel events (with restrictions).
- Engagement custom audiences (with restrictions).
- Geo at city/region/country level.

**The implication for DR's immigration vertical:** the audience-targeting toolkit collapses from Layers 1-6 in Framework 1 down to roughly Layers 2, 3, and 6. The creative carries even more weight because the algorithm has less to work with on the targeting side.

**The operator's adjustment:**
- Invest more per creative concept (Framework 3).
- Run more creative tests, not fewer.
- Lean into video and UGC formats (which give the algorithm more signal per impression than static).
- Use Conversions API aggressively (Pixel alone is too lossy post-iOS 14.5).
- Accept higher CPM than non-special-category accounts — it's a structural cost of the regime.

**Failure mode:** treating a special-ad-category account like a normal account, blaming the algorithm when it underperforms. The constraints are structural. The playbook has to change.

---

## How to use this file inside the /marshall skill

1. When Ivan describes a Meta diagnostic problem, identify which framework names the bottleneck (audience saturated → Framework 1 + 4; creative fatigued → Framework 3; ROAS collapsing → Framework 5; immigration-account constraints → Framework 6).
2. Pull the framework's mechanism and discipline from this file.
3. Cross-reference `eighty_twenty_frameworks.md` Framework 8 for the broader Meta Audience-Stack Model.
4. Reference the book for Marshall + Regnerus + Meloche's own prose: *Ultimate Guide to Facebook Advertising*, 4th ed., Entrepreneur Press.
5. Never substitute these summaries for the book.

---

*Source documents: Ultimate Guide to Facebook Advertising (Marshall + Regnerus + Meloche, Entrepreneur Press, 4th ed.); supporting context from the Marketing Letter at perrymarshall.com. For Marshall's own prose, screenshots, and case studies, buy the book.*
