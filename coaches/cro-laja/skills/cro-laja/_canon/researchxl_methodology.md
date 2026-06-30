# ResearchXL — Peep Laja's Six-Stage Conversion Research Methodology

The framework Peep developed at ConversionXL (now CXL) and codified at
Speero. The job of ResearchXL is to find what is actually broken
before anyone touches anything. No test is run, no copy rewritten,
no design changed until the six stages have been executed and the
findings have been synthesized into testable hypotheses.

Peep's stance: "Stop guessing, start researching." The opposite of
ResearchXL is what most marketing teams do — open the page, squint
at it, change the headline, add a guarantee, swap the button color,
ship, declare a win on noise. ResearchXL refuses that loop.

The output of ResearchXL is not a redesigned page. It is a
**prioritized list of hypotheses**, each tied to a research finding,
each testable on a defined metric. Page changes follow. Tests
follow. Wins follow.

---

## STAGE 1 — HEURISTIC ANALYSIS

**Purpose:** Expert review of the page against the variables that
drive conversion. Done first because it requires no data infrastructure
— anyone with the framework can do it on day one.

**What you score (every page, every section):**

- **Relevance** — Does this page match the visitor's intent and the
  ad/source that delivered them? If the ad said "ROI calculator" and
  the page leads with company history, the relevance score is zero
  and no other fix matters.
- **Clarity** — Within 5 seconds, can a first-time visitor say what
  this is, who it's for, and what to do next? If not, clarity fails
  and the rest of the page is wasted.
- **Value** — Is the value proposition strong, specific, quantified,
  and unique? Generic claims ("the leading platform") score zero.
- **Friction** — Where does the visitor encounter resistance? Form
  fields, signup walls, unclear next steps, layout chaos, cognitive
  load. Each instance is a friction point.
- **Distraction** — What is on the page that is not driving the
  most-wanted action? Every non-converting element is competing for
  attention with the converting one. Peep's rule: every page should
  have one or maximum two most-wanted actions; everything else is
  noise.

**How to run it:**

1. Print the page. Or screenshot top to bottom, full length.
2. Annotate every section against the five variables.
3. Mark each section "drives," "neutral," or "blocks" conversion.
4. Note every assumption you can't verify — those become questions
   for later stages (analytics, qualitative, user testing).
5. Output a heuristic findings document with screenshots, scores,
   and 10–30 hypotheses.

**Common failure modes:**

- Reviewer is too familiar with the product — they "fill in" clarity
  the visitor doesn't have. Counter by recruiting a fresh-eyes
  reviewer who has never seen the product.
- Reviewer applies "best practices" instead of the framework. A best
  practice is what wins on average. The framework finds what wins on
  *this* page for *this* audience.
- Reviewer scores subjectively without anchoring to the visitor's
  job-to-be-done. Anchor every score to "would the target ICP, on
  first visit, with no prior context, understand and act on this?"

---

## STAGE 2 — TECHNICAL ANALYSIS

**Purpose:** Make sure the page works. Before you can optimize
conversion, the page has to load, render, and function on every
device and browser the audience uses. A page that converts at 5%
on desktop and breaks completely on mobile is a 50%+ leak.

**What you check:**

- **Cross-browser** — Chrome, Safari, Firefox, Edge. The page should
  render identically. Use BrowserStack or equivalent.
- **Cross-device** — Mobile (iOS Safari, Android Chrome), tablet,
  desktop. Mobile is usually >50% of traffic in B2C, 30–50% in B2B.
  A broken mobile experience is a broken business.
- **Page speed** — Largest Contentful Paint <2.5s, Time to Interactive
  <3.8s, First Input Delay <100ms. Every additional second of load
  time costs 4–7% of conversion.
- **Broken flows** — Click every CTA, fill every form, complete every
  funnel. Half the conversion problems in any audit are technical
  errors nobody knew about.
- **Tracking** — Are analytics, conversion pixels, and event tracking
  actually firing? If the data is wrong, every later stage produces
  wrong conclusions.
- **Accessibility** — Contrast, alt text, keyboard navigation. Not
  just compliance — accessibility issues are often conversion issues
  for users with imperfect vision, slow devices, or shaky connections.

**How to run it:**

1. PageSpeed Insights + GTmetrix + WebPageTest on every key page.
2. Manual click-through on at least 3 browsers, 3 devices.
3. Tag Assistant or equivalent for analytics validation.
4. Document every issue with severity (blocker / leak / cosmetic).
5. Hand blockers and leaks to engineering before any further work.

**Common failure modes:**

- Skipping mobile testing because the team is on laptops.
- Treating page speed as "good enough" because Lighthouse score is
  green. Real network conditions reveal what synthetic tests miss.
- Trusting analytics data before validating it fires correctly.

---

## STAGE 3 — WEB ANALYTICS

**Purpose:** Find where the leaks are. The analytics stage answers
"which pages, which steps, which segments are losing the most
people?" It doesn't tell you why — that's later stages — but it
tells you where to look.

**What you investigate:**

- **Funnel diagnostics** — From entry to conversion, where do people
  drop off? Which step has the worst step-to-step rate? That is the
  highest-leverage step.
- **Page-level performance** — Bounce rate, scroll depth, time on
  page, exit rate. A page with high traffic and high exit rate is
  a target. A page with high traffic and low scroll depth means
  people aren't getting past the hero.
- **Segmentation** — Conversion rate by source (paid vs organic vs
  direct), device, browser, country, returning vs new, day of week,
  hour of day. Segments often reveal that the "site converts at 2%"
  number hides "paid mobile converts at 0.4% and organic desktop
  converts at 6.2%."
- **Content engagement** — Which blog posts, videos, or pages drive
  the most-converting traffic? These are the demand signal.
- **Search behavior** — On-site search queries. The most direct
  voice-of-customer data available. What people type into your
  search box is what they came for and couldn't find.
- **Form abandonment** — Which field is abandoned most? That field
  is the bottleneck.

**How to run it:**

1. Identify the conversion funnel from entry to goal.
2. Build segments before pulling reports. "Mobile / paid / new
  visitor" is one segment. Don't average across all traffic.
3. Pull at least 8 weeks of data — fewer than that and you're
  looking at noise.
4. Flag any segment converting at <0.5x or >2x the overall rate.
   These are the segments where the page works or doesn't work.
5. Output: ranked list of leak points by traffic-weighted impact.

**Common failure modes:**

- Looking at site-wide averages instead of segments.
- Mistaking correlation for causation ("people who view the pricing
  page convert more" — well yes, because they're further down the
  funnel).
- Not validating that goals and events are tracking correctly
  before pulling reports.

---

## STAGE 4 — MOUSE TRACKING

**Purpose:** Watch what visitors actually do on the page. Analytics
tells you they left; mouse tracking tells you what they did before
they left. Heatmaps, scroll maps, click maps, and session
recordings.

**What you investigate:**

- **Scroll maps** — How far down the page do people get? If 70%
  drop off before the value proposition appears, the page is too
  long above the fold or too boring through the middle.
- **Click maps** — What do people click? Especially: what non-link
  elements do they click? Those are signals that an element looks
  like it should be interactive but isn't — a UX failure.
- **Attention maps / mouse movement** — Where do people hover? What
  do they read? What do they skip?
- **Session recordings** — Watch 20–50 individual sessions. You will
  see things no aggregate report captures: people zooming in on
  pricing because the text is small, rage-clicking a broken button,
  filling a form and abandoning at field 4 because they don't have
  the data, scrolling past a section they should have stopped on.
- **Form analytics** — Time per field, abandonment per field,
  re-entry per field. The field with the highest abandonment is the
  bottleneck.

**How to run it:**

1. Install Hotjar, Microsoft Clarity, or equivalent on key pages.
2. Wait for at least 1,000 sessions before drawing conclusions.
3. Segment recordings by behavior — show me sessions that didn't
   convert, sessions that converted, sessions on mobile, sessions
   from paid.
4. Watch at least 30 recordings, taking notes on every friction
   point or surprising behavior.
5. Combine with analytics findings to confirm the "what" with the
   "why behavior."

**Common failure modes:**

- Drawing conclusions from 10 sessions.
- Cherry-picking recordings that confirm the team's hypothesis.
- Ignoring mobile recordings because the team is on desktop.

---

## STAGE 5 — QUALITATIVE ON-SITE

**Purpose:** Voice of customer, in their own words, while they are
on the page. Quantitative tells you what; qualitative tells you why.

**What you run:**

- **On-page polls** — Single question, contextual. Examples:
  - On the homepage: "What brought you here today?"
  - On the pricing page: "Is there anything preventing you from
    starting today?"
  - On the exit overlay: "What were you hoping to find on this page?"
  - On the post-purchase thank-you: "What almost stopped you from
    completing this?"
- **Email surveys** — To recent converters and recent visitors.
  Open-ended questions that surface the language they actually use.
  Peep's go-to questions:
  - "What were you doing before you signed up?"
  - "What was the moment you decided to try us?"
  - "What almost made you not sign up?"
  - "If we disappeared tomorrow, what would you use instead?"
- **Live chat logs** — Read 100 of them. Every objection, every
  confusion, every question that comes up repeatedly is a gap on
  the page that the page should have closed.
- **Sales call recordings** — If the company has a sales team, the
  first 30 seconds of every disco call is voice of customer.
  Especially the "what made you book this call" question.
- **Support tickets** — Cluster by topic. The top three topics are
  the top three things the product or page failed to clarify.

**How to use the findings:**

The output of qualitative is a **language inventory**. Words and
phrases customers actually used to describe their problem, your
solution, and the alternative they considered. This language goes
directly into copy. Stop writing in your branded voice — write in
their voice.

**Common failure modes:**

- Leading questions ("How awesome was your experience?"). Run
  open-ended only.
- Acting on a single response. Look for repeated language across
  many responses.
- Asking customers to design the solution. They are the source of
  problems; you design the solution.

---

## STAGE 6 — USER TESTING

**Purpose:** Watch ICP users perform real tasks on the page, aloud,
in real time. This is the highest-fidelity research method. It
reveals the gaps that analytics, recordings, and polls all miss
because the user is narrating their thought process as they hit them.

**What you run:**

- **Moderated user tests** — Recruit 5–8 users who match the ICP
  (job title, industry, company size). Give them a task: "You're
  looking for a tool that does X. Find one. Explain what you're
  thinking out loud as you go." Record. Observe.
- **Unmoderated user tests** — Use UserTesting.com, Maze, or
  equivalent for scale. Lower fidelity but faster and cheaper.
- **First-click tests** — Show a screenshot; ask "where would you
  click to do X?" Reveals navigation and information architecture
  failures.
- **5-second tests** — Show the page for 5 seconds, ask what they
  remembered. Reveals whether the hero communicated anything at all.
- **Comparative tests** — Show the user three competitor sites and
  yours, ask which they'd consider and why. Direct sameness audit.

**How to recruit:**

- Use Wynter for B2B audiences (verified job titles).
- Use UserTesting / Userlytics for B2C or broader audiences.
- Recruit from your own customer base if testing with current
  users.
- Never test with your team, your friends, or random panel users.
  Wrong audience produces wrong findings.

**What you look for:**

- Where do they hesitate? Hesitation = friction.
- Where do they say "I don't get this"? That's a clarity failure.
- What word do they use to describe the product? If it's not your
  word, your messaging hasn't landed.
- What competitor do they mention? That's your real reference point,
  not the one your team thinks.
- What do they do when they finish the task? Did they convert, or
  did they say "I'd want to think about it"? Both reveal a gap.

**Common failure modes:**

- Recruiting the wrong audience (the #1 failure).
- Asking leading questions ("Wasn't this easy?").
- Acting on a single user's preference. Look for patterns across
  5+ sessions.
- Stopping at the test. The synthesis is where the value is.

---

## SYNTHESIS — FROM FINDINGS TO HYPOTHESES

ResearchXL produces a lot of findings. The synthesis step turns
findings into testable hypotheses, ranked by priority.

**Hypothesis format (Peep's):**

> Because [observation from research], we believe that [proposed
> change] will result in [expected outcome], measured by [metric].

Examples:

- "Because 6 of 8 user tests showed people didn't understand 'AI-
  powered insights' on the hero, we believe rewriting the hero to
  'See which deals will close this month before your team does'
  will increase demo-request rate, measured by demo CVR."
- "Because session recordings show 73% of mobile users zoom in on
  the pricing table, we believe redesigning the pricing table for
  mobile-first will reduce pricing-page exit rate, measured by
  pricing → demo CVR."

**Prioritization — PXL:**

Speero's prioritization model. Each hypothesis scored on:

- **Potential** — How big could the impact be? (page traffic ×
  baseline rate × MDE)
- **Importance** — How load-bearing is this page in the funnel?
- **Ease** — How fast and cheap to build and test?

Score, rank, run top hypotheses first. Never start with the
easiest test — start with the highest expected value.

**Test design:**

Before running any test, calculate:

- Baseline conversion rate
- Traffic on the test page per week
- Minimum detectable effect (MDE) you care about (usually 5–20%
  relative lift)
- Required sample size for 95% confidence and 80% power
- Expected runtime

If the test can't reach significance in 4–6 weeks, it's not worth
running on this page. Either change the test, change the page, or
combine multiple low-traffic pages.

---

## WHY RESEARCHXL WORKS

- It separates research from opinion. Findings come from data,
  not the founder's gut.
- It catches sameness and technical issues before any test is run.
- It produces hypotheses that win at 2–3x the rate of random
  "let's test this" suggestions, because each is anchored to a
  research finding.
- It builds a research baseline that compounds. Every audit makes
  the next audit faster, because the team learns what to look for.
- It is a teachable, repeatable system. Not a personality.

## WHY MOST TEAMS DON'T USE IT

- It is slower than guessing on day one.
- It requires literacy across analytics, copy, UX, psychology, and
  experimentation. Most teams have one of those, not all six.
- It produces hard truths. ("Your hero is generic." "Your funnel
  leaks at step 3 because the form is broken on iOS.") Teams that
  have shipped the current page don't want to hear it.
- It cannot be sold as fast as "redesign the page." Agencies that
  redesign sell more than agencies that research.

Peep's frame: ResearchXL is the only honest way to do CRO. The
alternative is a slot machine where you pull the lever (ship a
test) and hope. Slot machines don't compound.
