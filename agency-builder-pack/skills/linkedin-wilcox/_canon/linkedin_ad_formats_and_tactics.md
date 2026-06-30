# LinkedIn Ad Formats + Tactics — Operator's Reference

This is the format-by-format matrix Wilcox uses on live $150M+ accounts,
plus the tactical layer: LAN, bidding, pacing, lead gen forms, Insight Tag,
matched audiences, dayparting.

---

## PART 1 — FORMAT MATRIX

### Sponsored Content — Single Image
The workhorse. Default format for most campaigns.

- **Typical CPC**: $8-11 (normal audiences). $15-20 on small/competitive.
- **Avg CTR**: ~0.44%.
- **When to use**: Cold prospecting with lead magnet. Retargeting. Top-
  and mid-funnel lead generation.
- **When NOT to use**: Pure brand awareness (use Video for reach), tiny
  audiences <10K (use Message Ads), pure ABM under 500 accounts (use
  Conversation Ads or Message Ads with named-list targeting).
- **Common mistakes**:
  - Importing Meta creative (busy, multi-element collages) — LinkedIn
    rewards clean, single-focal-point images.
  - Stock photography — kills CTR.
  - Promotional company logos in image — looks like an ad, gets scrolled.

### Sponsored Content — Video
Top-performing format when set up correctly.

- **Typical CPC / CPV**: $8-12 CPC; $0.05-0.15 CPV depending on objective.
- **Best aspect ratio**: 16:9 horizontal. Beats vertical 9:16 and square
  1:1 by 2-4x on view rate and completion rate on LinkedIn (opposite of
  TikTok/Reels — Wilcox finding from his accounts).
- **Length**: 15-90 seconds for prospecting. 30-180s for retargeting.
- **Best practice**: Talking-head, authentic > polished produced. Caption
  burned in (LinkedIn auto-play is muted). Hook in first 3 seconds.
- **When to use**: Trust-build, brand intro, complex value prop that
  needs explanation, retargeting nurture.
- **Anti-use**: Direct response with form fill (use single-image + lead
  gen form combo instead).
- **Video Objective trick** (Ep 101): Use "Video Views" objective for
  cheap impressions, but use "Website Visits" or "Lead Generation"
  objective if you actually want clicks/leads. Optimizing for views =
  optimizing for views, not anything else.

### Document Ads
Underrated. Use these over Carousel.

- **Typical CPC**: $8-13.
- **Engagement**: High. LinkedIn users will swipe through 5-10-page PDFs.
- **When to use**: Multi-step value delivery (report previews, framework
  walk-throughs, case study summaries). Top-of-funnel value-led ads.
- **Mechanic**: Show 3-5 pages, gate the rest behind a lead form.
- **Anti-use**: Single-message offers (just use Sponsored Content single
  image).

### Thought Leader Ads (TLA)
Promote an individual's organic post (the founder, the executive, the
SME) rather than the company page.

- **Engagement**: Materially higher than company-page boosted posts.
  Users trust people, not pages.
- **When to use**: Founder-led content motion, SME-driven authority
  plays, retargeting nurture that needs to feel non-promotional.
- **Setup gotcha**: The individual must approve each ad. Get this baked
  into your process or you'll stall.
- **Source**: https://b2linked.com/blog/ep128

### Message Ads (formerly InMail Ads)
LinkedIn-native message arriving in the prospect's inbox.

- **Typical cost**: $0.50-$1.00 per send. Effective CPC: $25-60.
- **Avg open rate**: ~55%. Avg CTR (open-to-click): ~3.2%.
- **When to use**: High-value ABM, event invitations, exec-to-exec outreach,
  hot retargeting.
- **When NOT to use**: Cold prospecting at scale (cost per outcome is
  punishing), low-ASP products.
- **Common mistakes**:
  - Sender is the company brand, not a human. Use a human "From" or it
    feels like spam.
  - Long-form sales pitch. Treat like cold email — 3 short paragraphs.
  - Always-on. LinkedIn rate-limits sends; can only message each prospect
    every 60 days. Plan accordingly.

### Conversation Ads
Branching message format with up to 5 CTA buttons per node.

- **Cost**: Similar economics to Message Ads.
- **When to use**: Self-segmenting offers (route by role, by interest, by
  funnel stage), event/webinar registrations with multiple sessions,
  nurture sequences that need to qualify.
- **Better than Message Ads when**: You need the prospect to self-identify
  before you route the conversation.
- **Common mistake**: Building too many branches. Cap at 3-4 nodes deep
  or drop-off compounds.

### Text Ads
The right-rail desktop unit. Old school, still useful.

- **Typical CPC**: $3-6. Cheapest CPCs on the platform.
- **CTR**: extremely low (~0.025%) — but it's cheap because it's low.
- **When to use**: Always-on retargeting at low spend, awareness
  reinforcement, brand presence on a small budget.
- **Anti-use**: Lead generation as primary mechanism (CTR too low).
- **Pairing tactic**: Run Text Ads as a always-on "ambient" layer
  alongside Sponsored Content prospecting. Pennies-on-the-dollar reach.

### Dynamic Ads
Personalized ads with the user's name/photo pulled from their profile.

- **When to use**: Follower growth campaigns, light awareness.
- **When NOT to use**: Lead generation (weak performer here).
- **Don't over-index on these.** Wilcox's accounts rarely run them for
  performance objectives.

### Lead Gen Forms (cross-format add-on)
Native LinkedIn form, pre-fills from profile, fires inside the ad.

- **Conversion lift**: 10-50% over equivalent landing page (Wilcox data).
- **Lead quality**: Lower than landing page. Prospects often "forget"
  they filled it out — follow up within 24h or burn the lead.
- **Tracking gap**: No third-party retargeting fires. Lead never visits
  your site, so no Insight Tag fire, no GA capture.
- **When to use**: Top-funnel low-friction lead magnets, volume goals,
  mobile-heavy audiences.
- **When NOT to use**: Bottom-funnel where lead quality matters more
  than volume, where you need the prospect on your site for retargeting,
  where attribution to revenue is critical.
- **Source**: https://www.linkedin.com/pulse/linkedin-lead-gen-form-ads-leading-landing-page-which-aj-wilcox

---

## PART 2 — TACTICAL LAYER

### LinkedIn Audience Network (LAN) — Allow-Lists

LAN is LinkedIn's off-platform inventory — third-party publisher sites
and apps. Default-on. Default-junk.

- Pre-allow-list: per Wilcox's case study, **63% of LAN traffic was
  identified as bot/problematic** before allow-listing.
- Post-allow-list: traffic quality improved dramatically — flipped to
  positive good-to-bad ratio.
- **Wilcox's rule**: Allow-list > Block-list. Block-lists are reactive
  (you only block what you already saw bad). Allow-lists are proactive
  (only premium publishers like Forbes, WSJ, NYT, Business Insider).
- B2Linked publishes a free curated allow-list. Use it.
- Alternative: turn LAN off entirely. Cleaner but you lose ~25% of reach.
- Source: https://b2linked.com/blog/ep150

### Bidding — Manual CPC at the Floor

LinkedIn's bidding defaults are designed to extract maximum spend from
unsophisticated advertisers. Wilcox's discipline:

1. **Always use Manual CPC.** Not "Max Delivery." Not "Target Cost."
2. **Bid the actual floor** — typically $2-3 *below* LinkedIn's
   "suggested minimum." LinkedIn lies about the floor.
3. **Only raise bids if volume is too low**, never to "win the auction."
4. **Kill "enable bid adjustment for high-value clicks"** — this setting
   is on by default and lets LinkedIn bid up to 45% above your bid,
   routinely overspending daily budgets by ~40%.
5. **Watch the spend curve daily** in the last week of every month.
   LinkedIn pacing models are unreliable. Expect overshoots.
- Source: https://b2linked.com/blog/ep89

### Pacing — The Discipline LinkedIn Punishes You For Missing

- LinkedIn doesn't have native dayparting. You can't schedule ads on/off
  by hour or day in the native interface.
- Workaround: third-party tools (e.g. AdStage / Marin) to dayparting +
  budget cap automation.
- **Wilcox's preferred safety mechanism**: automation that auto-pauses
  the account on hitting monthly cap, auto-unpauses on day 1 of the next
  month. Without this, your last-week overspend can be 20-40% over budget.
- Manual pacing rule: target 1/30th of monthly budget per day. If you're
  on day 20 and 80% spent, lower bids immediately to slow the burn.
- Sources: https://b2linked.com/blog/ep63 (Dayparting), https://b2linked.com/blog/ep164 (Pacing)

### Dayparting — When You Should and Shouldn't

- LinkedIn audiences cluster Mon-Thu 9am-4pm in their local timezone.
- Friday afternoon and weekends: noise, lower-intent, often cheaper
  CPC but worse conversion.
- For lead-gen campaigns: schedule heavy Mon-Thu, throttle Fri-Sun.
- For brand/video views: 24/7 acceptable, the cheap weekend impressions
  are fine for view-rate optimization.
- Need a week of high-budget high-bid data to see your audience's actual
  pattern before locking a schedule.

### Insight Tag — The First Thing You Install

- LinkedIn's pixel equivalent. Required for: website retargeting,
  conversion tracking, matched audiences from web visits, attribution.
- Install via Google Tag Manager, native, or partner stack.
- Validates within 24h in Campaign Manager.
- **Test it before you spend a dollar.** If it isn't firing, you're
  wasting all your retargeting potential.

### Matched Audiences — The Second-Best Feature

(See full breakdown in amo_framework_full.md.)
- Account lists > Contact lists.
- Website retargeting requires Insight Tag.
- Engagement retargeting (video viewers, ad clickers, lead form openers)
  is the fastest way to build a warm audience without Insight Tag.
- Audiences need 300+ members to be usable.
- Matched audiences expire / archive after extended periods of non-use —
  watch your status dashboard.

### Lead Gen Forms vs Landing Pages — Decision Rule

| Factor | Lead Gen Form | Landing Page |
|---|---|---|
| Conversion rate | +10-50% higher | Baseline |
| Lead quality | Lower | Higher |
| Retargeting capture | None | Yes (Insight Tag fires) |
| Attribution to revenue | Hard | Clean |
| Mobile UX | Excellent | Variable |
| Use when... | Top-funnel volume | Bottom-funnel quality |

Default rule: **lead gen form for cold prospecting low-friction LMs,
landing page for warm/hot funnel stages where retargeting and revenue
attribution matter.**

### Funnel Stages — Wilcox's Standard Architecture

Per Ep 154 (Full-Funnel Retargeting Setup):

1. **Stage 1 — Cold Prospecting**: Sponsored Content + Lead Gen Form,
   low-friction asset. KPI: CPL.
2. **Stage 2 — Engagement Retargeting**: target lead-gen-form openers
   who didn't submit, video viewers >50%, single-image-ad clickers.
   Format: Document Ad or Video. Offer: case study, deeper asset.
3. **Stage 3 — Asset-Consumer Retargeting**: target Stage 2 converters.
   Format: Thought Leader Ad or Conversation Ad. Offer: assessment,
   webinar, office hours.
4. **Stage 4 — Bottom-Funnel**: target Stage 3 engagers + website
   visitors of pricing/demo pages. Format: Message Ad from a human
   sender. Offer: direct call/demo.

Each stage uses different formats and increases offer friction. This
is the architecture for predictable LinkedIn pipeline.

---

## SOURCES (Wilcox public)

- LinkedIn Ad Formats overview — https://www.linkedin.com/pulse/linkedin-ad-formats-units-which-should-you-use-what-performs-wilcox
- LinkedIn Ad Benchmarks — https://www.linkedin.com/pulse/linkedin-ad-benchmarks-aj-wilcox
- Video Objectives (Ep 101) — https://b2linked.com/blog/ep101
- Thought Leader Ads (Ep 128) — https://b2linked.com/blog/ep128
- Lead Gen Forms vs Landing Page (Ep 17) — https://b2linked.com/blog/ep17
- LAN Allow-Lists (Ep 150) — https://b2linked.com/blog/ep150
- LAN Interview w/ LinkedIn (Ep 85) — https://b2linked.com/blog/ep85
- Bidding (Ep 89) — https://b2linked.com/blog/ep89
- Dayparting (Ep 63) — https://b2linked.com/blog/ep63
- Pacing (Ep 164) — https://b2linked.com/blog/ep164
- Full-Funnel Retargeting (Ep 154) — https://b2linked.com/blog/ep154
- $10/day strategy for small budgets (Ep 125) — https://b2linked.com/blog/ep125
- 100% Match Rates (Ep 120) — https://b2linked.com/blog/ep120
- Hidden Setting That Burns Your Budget — https://b2linked.com/blog-page/the-hidden-linkedin-ads-setting-that-burns-your-budget
