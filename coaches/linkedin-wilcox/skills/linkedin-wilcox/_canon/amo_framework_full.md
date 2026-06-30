# AMO Framework — Full Deep Dive

The AMO Framework is the operating skeleton of every LinkedIn Ads campaign
Wilcox has ever shipped. Three things, all three, in this order:

1. **A**udience — who you reach
2. **M**essage — what they see (format + copy + visual)
3. **O**ffer — what they get when they click

You cannot fix a broken campaign without knowing which leg is broken.
You cannot build a campaign without locking all three first.

Public quote (Wilcox, b2linked.com Ep 112):
> "Audience, message, and offer — you need all three."
> Source: https://b2linked.com/blog/ep112

---

## A — AUDIENCE: The LinkedIn Moat

LinkedIn's targeting is the only reason the platform's $8-15 CPC math works.
You're paying that premium because every user is self-attesting to their
job title, employer, function, seniority, and skills. That's worth the
markup — IF you use it.

### Targeting Layers (Wilcox's Operating Order)

**Layer 1 — Account Targeting (highest leverage when applicable)**
- Upload a list of target company names (or use account list match).
- LinkedIn now shows match rate (it didn't pre-2024).
- Combine with role/seniority for ABM precision.
- Best for: closed-list ABM, named-account selling, post-trade-show retarget.

**Layer 2 — Job Function + Seniority**
- More forgiving than job title (LinkedIn only "understands" ~55% of job
  titles, per Wilcox's analysis).
- Function = "Engineering" / "Marketing" / "Finance"
- Seniority = Manager / Director / VP / CXO
- Run as a parallel campaign to job-title-based targeting and compare.

**Layer 3 — Job Title (high precision, lower volume)**
- Direct match, but coverage gap on the 45% of titles LinkedIn doesn't
  understand cleanly.
- Layer with seniority to disambiguate ("Director of Marketing" not
  "Marketing Director" at a 5-person agency).

**Layer 4 — Skills + Groups**
- Skills: self-attested, surprisingly clean for technical roles.
- Groups: declining quality post-2020, still useful for narrow technical
  niches (e.g. "PostgreSQL DBA").

**Layer 5 — Company Size + Industry**
- Always layer with role. Company-size-only is too broad and burns budget.
- Example: $1,200/mo SaaS targeting CFOs → company size 200+ AND CFO role.

### Audience Sizing — The Operating Zone

- **<20K** — Expensive, will see CPCs $15-20+. Only worth it for ABM.
- **20K-300K** — Sweet spot. Best CPC, enough volume to learn.
- **300K-1M** — Acceptable for top-funnel awareness only.
- **>1M** — Too broad for LinkedIn economics. You're paying sniper-rifle
  prices for shotgun targeting. Either narrow it or move to Meta.

### Matched Audiences (LinkedIn's Second-Best Feature)

Released 2017. Four flavors:
- **Contact lists** — email-based, lower match rate (~50-70%).
- **Account lists** — company-name-based, higher match rate (~80%+).
  Wilcox preference: account lists over contact lists, almost always.
  One contact list reaches one person. An account list with role/seniority
  layered reaches that person AND their coworkers AND their manager.
- **Website retargeting** — requires Insight Tag (see formats doc).
- **Engagement retargeting** — built from video views, single-image ad
  clicks, lead gen form opens, event attendees, etc.

### Lookalikes Are Dead

LinkedIn sunsetted Lookalike Audiences end of February 2024. Replaced
by **Predictive Audiences**, which are continuously updated rather than
static snapshots. If anyone tells you to "build a lookalike on LinkedIn",
they're working from outdated playbooks.

### Audience Anti-Patterns (kill on sight)

- Open targeting / "LinkedIn algorithm will find them" — no it won't,
  not at $9 CPC.
- Targeting "Decision Makers" as a seniority alone — too broad.
- Geographic-only — you'll bleed money on people who'll never buy.
- One mega-campaign covering all personas — split by persona, you can't
  optimize a campaign with three audiences in it.

---

## M — MESSAGE: Format + Copy + Visual

Message is the second leg, and the one most operators get wrong because
they import Meta creative patterns. LinkedIn users behave differently:
they're in work-mode, in lower volumes, with longer attention spans on
business content. The creative job is to interrupt the work-mode scroll
with a specific business problem statement, not entertain.

### Copy Frameworks That Work on LinkedIn

**Framework 1 — Pattern Interrupt + Specific Pain**
- Line 1: A specific number or claim ("63% of our LAN traffic was bots")
- Line 2: Why it matters to a specific role ("If you run LinkedIn Ads,
  this is silently killing your CPL")
- Line 3: What we do about it ("We built an allow-list publishers can't
  bypass — link below")
- CTA: low-friction (download, watch, read)

**Framework 2 — Industry Insight Hook**
- Open with a contrarian or specific data point about the prospect's
  industry. Not platitudes. Not "Did you know B2B is hard?"
- Anchor it to a named role or segment.
- Deliver the value in the post itself, asset is the upgrade.

**Framework 3 — Direct Problem Statement**
- "If you're a [role] running [thing], you've probably hit [specific
  problem]. Here's the math on why it happens, and the fix."
- Works best in document ads and longer Sponsored Content.

### Visual Rules

- **Video**: horizontal 16:9 beats vertical 9:16 and square 1:1 by
  2-4x on view rate, completion rate, and cost efficiency on LinkedIn.
  (Opposite of TikTok/Reels — this is the platform behaving like LinkedIn,
  not like social.)
- **Talking-head video** > polished produced video for LinkedIn audiences.
  Authenticity beats production value.
- **Single-image static**: bright color, contrast against LinkedIn's blue/
  white feed, faces > graphics, no stock photography.
- **Document ads** > carousel ads. Carousel has been deprioritized on
  LinkedIn. Document ads have higher engagement.

### Copy Length

- **Sponsored Content**: 150 chars before "see more" — front-load the hook.
  Full body up to ~600 chars, but bail at 300 unless the body earns it.
- **Message Ads**: Subject line + 1500 chars body. Treat like cold email.
- **Conversation Ads**: Each node 500 chars. Tree out the conversation.
- **Text Ads**: 25-char headline + 75-char body. Brutal economy.

---

## O — OFFER: The Thing They Get

Offer is where most LinkedIn campaigns die. Operators import a "Book a
Demo" CTA from their warm-audience funnel and run it cold on LinkedIn.
Cold demo asks at $9 CPC convert at 1-4%. That's $225-$900 CPL on top
of the click. Math doesn't work unless your deal size is enormous.

### The Offer-Friction Ladder

Match offer friction to audience temperature:

**Cold audiences (prospecting) — LOW FRICTION**
- Industry report / benchmark study
- Tool / template / calculator
- Webinar (recorded > live for cold)
- Cheat sheet, swipe file
- Conversion rate goal: 10-15% on low-friction lead magnets.

**Warm audiences (retargeting / engagement) — MEDIUM FRICTION**
- Live webinar
- Free assessment / audit
- Office hours / Q&A
- Case study download with form
- Conversion rate goal: 5-10%.

**Hot audiences (bottom-funnel, post-engagement) — HIGH FRICTION**
- Demo request
- Discovery call
- Pricing / quote
- Trial signup
- Conversion rate goal: 1.5-4% on cold (don't run these cold!),
  10-20% on properly warmed audiences.

### What Doesn't Work on LinkedIn

- **Free trials of low-ASP SaaS** — the platform's CPC math doesn't
  support sub-$5K ACV products via paid LinkedIn.
- **"Subscribe to our newsletter"** — too thin an offer to justify $9 CPC.
- **Generic "Learn More"** without a tangible asset behind it.
- **Long forms on landing pages** — strips conversion. Use lead gen forms
  for top-funnel, short landing pages for bottom-funnel.

### Offer Stacking (Wilcox Tactic)

A single offer in a single ad is fine. But the campaign should stack:
- Cold prospecting: low-friction lead magnet.
- Retargeting Layer 1 (LM downloaders): case study or related asset.
- Retargeting Layer 2 (case-study viewers): assessment or call.
- Retargeting Layer 3 (assessment takers): demo / sales call.

Each layer escalates friction as audience warms. This is what Wilcox
means by "full-funnel LinkedIn" — not one campaign, a sequence.

---

## DIAGNOSTIC RULES — Which Leg Is Broken?

Use these to pinpoint the failure when a campaign underperforms:

| Symptom | Likely Cause |
|---|---|
| CTR < 0.4% on Sponsored Content | Message (creative/copy) |
| CTR > 0.6% but conversion < 2% | Offer (audience clicked, didn't buy promise) |
| CPC > $15 on normal-sized audience | Audience (too small or too competitive) |
| CPC < $7 but no leads | Audience (too broad, wrong people) |
| Leads coming in but no pipeline | Offer (wrong intent, lead quality issue) |
| Pacing overspending daily | Bidding (high-value-clicks on, or auto-bid) |

Diagnose first. Don't blame creative when the audience is wrong.
Don't blame the audience when the offer is misaligned to temperature.

---

## SOURCES (Wilcox public)

- AMO Framework intro — https://b2linked.com/blog/ep112
- 3 Things You Need For Every Successful LinkedIn Ads Campaign —
  https://www.linkedin.com/pulse/3-things-you-need-every-successful-linkedin-ads-campaign-aj-wilcox
- LinkedIn Ads Targeting — https://www.linkedin.com/pulse/linkedin-ads-targeting-how-target-your-ideal-audience-aj-wilcox
- Match Rates for List Uploads — https://b2linked.com/blog/ep120
- Matched Audiences — https://www.linkedin.com/pulse/linkedin-ads-matched-audiences-best-feature-show-aj-wilcox
- Lookalikes sunset — https://www.linkedin.com/posts/wilcoxaj_become-a-linkedin-ads-fanatic-activity-7152741440777785344-viUO
- Retargeting Strategies — https://www.linkedin.com/pulse/linkedin-ads-retargeting-strategies-precision-nurturing-aj-wilcox
- Full-Funnel Retargeting Setup — https://b2linked.com/blog/ep154
