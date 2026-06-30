# Google Ads — Framework Map

**Author:** Perry Marshall (with Bryan Todd and Mike Rhodes)
**Source treatment:** Framework structures from *Ultimate Guide to Google Ads* (Entrepreneur Press, 6th ed., the most recent at time of writing — earlier editions titled *Ultimate Guide to Google AdWords*, spanning roughly 2003-2024 across six revisions). Framework structures described in own words for synthetic-coach use. Book text is NOT reproduced. Each framework is named, mapped, and described mechanically so the AIMarshall skill can apply it. To read Marshall's own prose, the SWISS army-knife screenshots, and the case studies, get the book. URL: `https://www.perrymarshall.com/google/`.

---

## Operator's view of the Google Ads corpus

Marshall co-authored the first widely-read trade book on Google AdWords in the mid-2000s and has revised it across six editions as the platform shifted from a keyword-bid auction to a partially automated, Smart-Bidding-driven system. The frameworks below survive across editions because they describe **the auction's underlying physics**, not the UI of any given year.

The core thesis across every edition: Google's auction rewards relevance, not budget. The operator's job is to engineer the highest possible alignment between query, ad, and landing page so the auction prices clicks cheaply. Without that alignment, the budget gets spent on impressions that don't convert and bids that get inflated beyond economic recovery.

Six editions, one operating premise: get the relevance right, the economics follow.

---

## Framework 1 — Keyword Themes (the SKAG-adjacent doctrine)

**What it is:** the principle that each ad group should contain a single, tight theme of related keywords — not a dump of every related term. The widely-discussed "SKAG" (Single Keyword Ad Group) practice is a degenerate case of this principle; Marshall's actual recommendation across editions is theme-tight rather than literally single-keyword.

**The mechanism:**
- Each ad group becomes the unit of relevance. Google scores the ad group as a whole.
- Keywords inside the group should share a single search intent (e.g. "EB-5 attorney" + "EB-5 lawyer" + "EB-5 immigration lawyer" — same intent, three phrasings).
- The ad copy can then mention the exact term the prospect typed, because every term in that group maps to the same headline.
- The landing page can then mirror the headline, because there's only one promise to make.

**The 80/20 inside the structure:** ~20% of ad groups will produce ~80% of conversions. Theme-tight structure makes the 80/20 cut surgical — you cut whole ad groups, not individual keywords. Cutting groups is faster, less error-prone, and lets you redeploy the budget cleanly into the winners.

**Failure mode:** the "shotgun ad group" — 40 keywords across 5 intents stuffed into one group. The CTR averages out to mediocre, Quality Score collapses, CPCs go up, and the operator blames Google.

**Operator's discipline:** before launching, ask "if a prospect typed any of these keywords, would the same headline make sense?" If no — split the ad group.

---

## Framework 2 — Quality Score Mechanics (the CPC-divisor model)

**What it is:** Quality Score is Google's 1-10 rating of how well an ad+landing-page combination serves a query. It's not vanity — it directly divides the effective CPC.

**The mechanism (operator's math):**
- Ad Rank ≈ Bid × Quality Score (simplified — actual formula includes expected impact of extensions, etc.).
- High Quality Score = high Ad Rank at lower bid.
- Low Quality Score = needing to bid 3-10× as much to get the same position.

**The three primary components of Quality Score:**
1. **Expected CTR** — historical click-through rate of the keyword × ad, normalized for ad position.
2. **Ad relevance** — semantic match between keyword and ad copy.
3. **Landing page experience** — relevance of LP to the keyword, plus speed and mobile usability.

**The leverage point:** of the three, expected CTR has the largest dynamic range. Move CTR from 1% to 5% on a high-volume keyword and the CPC can drop by half or more. This is why CTR-improvement tactics (Framework 3) sit at the top of Marshall's optimization stack.

**Failure mode:** treating Quality Score as a static metric. It's recomputed continuously per auction. A 7 yesterday can be a 4 tomorrow if the CTR drops.

**Operator's discipline:** track Quality Score weekly on the top-spending keywords. A drop precedes a CPC increase by days — fix the lagging ad before the budget bleeds.

---

## Framework 3 — Single-Keyword (or Tight-Theme) Ad Groups for CTR Lift

**What it is:** the structural enabler of Framework 2. The reason you tighten ad groups isn't aesthetic — it's because tight ad groups let you write ads that contain the exact phrase the prospect searched, which lifts CTR, which lifts Quality Score, which lowers CPC.

**The compounding loop:**
1. Tight ad group → ad headline can include exact-match query
2. Exact-match query in headline → CTR rises (often 2-3×)
3. CTR rises → Quality Score rises
4. Quality Score rises → CPC drops
5. CPC drops → same budget gets more clicks
6. More clicks → faster learning → more data to optimize

This is a positive-feedback loop. The operator who runs it pays less per click AND learns faster than the operator who runs broad ad groups.

**The diminishing-returns point:** below ~5 keywords per ad group, the operational overhead exceeds the lift. The sweet spot for most accounts is 3-15 close-variant keywords per ad group, sharing a single intent.

**Failure mode:** SKAG fundamentalism — splitting every singular/plural variant into its own group. Google's close-variant matching already handles this. Over-splitting creates a maintenance nightmare without an Quality Score gain.

---

## Framework 4 — CTR-Boosting Tactics (the ad-copy stack)

**What it is:** Marshall's catalog of ad-copy moves that reliably increase CTR — and therefore lower CPC via the Quality Score loop in Framework 3.

**The tactic stack, ordered by typical lift:**
1. **Echo the query in headline 1** — if they searched "EB-5 immigration attorney", H1 says "EB-5 Immigration Attorney". Typical lift: 30-80%.
2. **Quantify the offer** — "Free 30-Minute Consult" outpulls "Free Consult". "847 Cases Won" outpulls "Many Cases Won". Typical lift: 10-30%.
3. **Use a question** — "Need an EB-5 Attorney Today?" makes the reader auto-complete a yes/no, which is cognitively engaging. Typical lift: 5-15%.
4. **Specificity in numbers** — "$1.2M Investment Threshold" outpulls "Low Investment". Specificity reads as credibility. Typical lift: 5-15%.
5. **Negation hook** — "Don't Hire An Immigration Lawyer Until You Read This" pulls clicks from people in the comparison phase. Typical lift: variable, sometimes large.
6. **Call-to-action verb in description** — "Book", "Apply", "Schedule", "Calculate". Imperative verbs convert better than passive descriptions. Typical lift: 5-10%.

**The discipline:** test two ads per ad group at all times. Pause the loser at statistical significance (typically ~100 clicks per ad on high-volume keywords). Replace with a new challenger. Compound the lift across iterations.

**Failure mode:** "set and forget" ad copy. Marshall's claim: if you haven't refreshed your top ad groups in 90 days, you're paying ~30% more per conversion than necessary.

---

## Framework 5 — Search vs Display vs YouTube — Three Different Buyer Modes

**What it is:** the three primary Google ad networks address three structurally different buyer states. Treating them as interchangeable is the most common Google Ads mistake.

**The buyer-state map:**

| Network | Buyer state | Marshall's frame |
|---|---|---|
| Search | Active query, problem-named | Hottest. Demand fulfillment. |
| YouTube | Passive watching, interest-adjacent | Warm. Demand generation. |
| Display | Passive browsing, ad-blind | Coldest. Brand reinforcement at best. |

**The operating rule (Marshall's stance across editions):** start with Search exclusively. Master the relevance triangle there. Only then expand to YouTube if the niche has video-relevant content patterns. Treat Display as a remarketing channel only, not a prospecting channel.

**Why this ordering:** Search is the only network where the prospect has self-identified as desperate (Framework 2 in the 80/20 file — DRT). YouTube and Display ask you to interrupt attention. Interruption is harder, slower, and more expensive per converted prospect. Master fulfillment economics on Search first, then graduate.

**Failure mode:** enabling "Search Partners" or "Display Network" with default settings on a Search campaign. This silently dumps budget into low-intent placements that look fine in aggregate but tank ROI. Marshall's discipline: every new Search campaign starts with Display and Search Partners OFF.

---

## Framework 6 — Conversion Tracking Discipline

**What it is:** if conversion tracking is broken or imprecise, every downstream optimization is hallucination. Marshall treats tracking setup as the first deliverable, not an afterthought.

**The five tracking rules:**
1. **One macro-conversion per campaign** — book-a-call, submit-application, purchase. Optimize the campaign toward this single goal.
2. **Track micro-conversions for diagnosis, not optimization** — page-view, scroll-depth, form-start. Useful for funnel analysis, never the bid-optimization target.
3. **De-duplicate counting** — one prospect filling out the form three times is one conversion, not three.
4. **Attribute on the right time-horizon** — for high-consideration B2B (e.g. immigration retainer), the lookback window must be 30-90 days, not the default 30 days, because conversion lag is real.
5. **Validate weekly** — manually compare Google's conversion count to the CRM's lead count. If the variance exceeds 10%, the pixel is misfiring.

**80/20 inside tracking:** ~20% of conversion-tracking setups have errors that materially distort budget allocation. The audit is high-leverage; the fix is one-time.

**Failure mode:** optimizing to a vanity event (e.g. "page viewed for 30 seconds") instead of the macro-conversion. The algorithm faithfully optimizes for what you told it to value — if you valued the wrong thing, you got the wrong scaling.

---

## Framework 7 — Negative-Keyword Discipline

**What it is:** in any keyword auction, the queries that match your keywords but should NEVER click your ad are a tax on Quality Score and budget. Negative keywords cut the tax.

**The four categories of negatives every account needs:**
1. **Free/cheap/DIY** — "free immigration lawyer", "cheap EB-5", "do it yourself green card". Wrong economic profile.
2. **Wrong-job-titles or wrong-stage** — "immigration lawyer salary", "how to become an immigration lawyer". Job-seekers, not clients.
3. **Wrong geographies** — if you serve US clients, negative every non-US city/country term.
4. **Brand confusion** — competitor names, similar-sounding names that drag the wrong intent.

**The harvest cycle (Marshall's discipline):**
- Weekly: pull the Search Terms report.
- Sort by impressions descending.
- For every query in the top 100 that doesn't fit your buyer profile, add it as an exact-match or phrase-match negative.
- Within 4-6 weeks, the irrelevant impression volume should drop by 30-60%.

**Compounding effect:** removing irrelevant impressions doesn't just save budget — it lifts CTR (because the denominator shrinks), which lifts Quality Score, which lowers CPC. Negative keywords are leverage, not hygiene.

**Failure mode:** treating the Search Terms report as optional. Marshall's claim: an account that hasn't been negative-pruned in 30 days is paying for clicks it doesn't want.

---

## Framework 8 — The Account-Structure Pyramid

**What it is:** how to organize an account so that budget pacing, reporting, and optimization all become tractable.

**The four-level pyramid:**

```
        Account
       /       \
    Campaign   Campaign      ← one per BUDGET POOL or geo/match-type segment
    /     \     /    \
  AdGroup  AdGroup  AdGroup  ← one per KEYWORD THEME (Framework 1)
   /|\      /|\      /|\
  Ads Keywords      ← multiple ads per group; tight keyword set per group
```

**Rules at each level:**
- **Campaign** carries the budget, the bid strategy, the geo, the network setting, the schedule. Use campaigns to isolate spend you want to control independently.
- **Ad Group** carries the keyword theme and the ad copy variants. Use ad groups to isolate relevance.
- **Ad** carries the message. Always 2+ ads per group for testing.
- **Keyword** carries the query match. Tight cluster per ad group.

**The common-mistake account:** one campaign, one ad group, 200 keywords, two ads. Quality Score collapses, the operator can't see what's working, and budget bleeds into the worst-matched queries.

**The well-structured account:** 5-15 campaigns (one per major budget pool / strategic segment), 30-80 ad groups (one per keyword theme), 60-160 ads (2+ per group), 200-600 keywords (tight clusters).

**Failure mode:** mirroring the website's information architecture in the ad account. The website is organized for buyers; the ad account should be organized for the auction. Different organizing principles, different structures.

---

## Framework 9 — The Relevance Triangle (cross-reference)

**What it is:** this framework is covered in detail in `eighty_twenty_frameworks.md` as Framework 7. Mentioned here for completeness — it is the structural backbone of every other framework in this file.

Briefly: keyword → ad → landing page must align. High alignment = low CPC. Low alignment = bid prison.

**The 80/20 inside the triangle:**
- 80/20¹: ~20% of keyword/ad/LP triangles drive 80% of conversions.
- 80/20²: ~4% drive 64%. Build dedicated LPs for these.
- 80/20³: ~0.8% drive 51%. These are the business — protect, defend, never let them go down.

See `eighty_twenty_frameworks.md` Framework 7 for the full treatment.

---

## How to use this file inside the /marshall skill

1. When Ivan describes a Google Ads diagnostic problem, identify which framework names the bottleneck (CTR low → Framework 4; CPC high → Framework 2 + 7; conversions inconsistent → Framework 6; account messy → Framework 8).
2. Pull the framework's mechanism and discipline from this file.
3. Reference the book for Marshall's own prose, case studies, and screenshots: *Ultimate Guide to Google Ads*, latest edition, Marshall + Todd + Rhodes, Entrepreneur Press.
4. Never substitute these summaries for the book — these are operator-grade structures, not Marshall's voice.

---

*Source documents: Ultimate Guide to Google Ads (Marshall + Todd + Rhodes, Entrepreneur Press, 6th ed.); supporting context from the Marketing Letter at perrymarshall.com. For Marshall's own prose, buy the book.*
