# Founder-Robinson — _canon routing index

Routing layer for the founder-robinson skill. SKILL.md is the operating
identity; the files in this directory are the deep canon to load
proactively when a user's question maps to a domain below.

Load one file per question by default. Load two only if the question
genuinely spans both (e.g., "how do I bootstrap AND post daily" spans
flywheel + capital efficiency). Never load all three at once — context
budget matters.

---

## Files in this directory

### `founder_led_content_flywheel.md`
**Load when the question is about:**
- LinkedIn posting cadence, voice, what to post, how often
- Build-in-public — what to share publicly, transparency cap
- Founder voice vs corporate voice vs ghostwritten voice
- The P&L-snapshot tactic, screenshot posts, public numbers
- The 10:1 ratio (stories to hard CTA)
- How content routes to product / freemium / pipeline
- 90-day on-ramp for a founder starting from zero LinkedIn presence
- Why ghostwriting / branded company-page posts don't work
- "I'm scared to post the numbers" coaching moments
- The flywheel mechanics end-to-end

**Triggers (verbatim or close):** post on LinkedIn, founder voice,
build in public, share the P&L, what should I post, how often should
I post, daily posting, content cadence, transparency, P&L screenshot,
public dashboard, ghostwriter, branded content, my marketing team
posts, founder-led content, vulnerable post, mistake post, churn post.

---

### `capital_efficient_b2b_growth.md`
**Load when the question is about:**
- Bootstrap vs raise / venture vs bootstrap
- ARR per employee, revenue per head, gross margin math
- Freemium-as-distribution mechanics, the free tier as a channel
- Person-level vs company-level visitor / intent signal
- The 0 → $5M ARR RB2B playbook in detail
- RB2B vs Retention.com lessons crossover
- Pricing experiments, public pricing changes
- The traps to avoid (hiring ahead of revenue, raising because
  peers raised, multi-channel before single-channel works)
- DR / services-firm translation of the SaaS playbook
- Capital posture / when to take outside money / when not to

**Triggers (verbatim or close):** bootstrap, raise capital, venture
capital, VC, capital efficient, ARR per head, ARR per employee, gross
margin, freemium, free tier, person-level, company-level, intent
signal, visitor ID, pricing experiment, raise prices, RB2B playbook,
Retention.com, headcount, burn, dilution, services firm economics.

---

### `robinson_public_corpus.md`
**Load when the question is about:**
- Finding a specific Adam Robinson quote or post to cite
- Sourcing a podcast appearance for further listening
- Verifying a claim about RB2B's metrics / history
- Extending or refreshing the skill with new references
- "Where can I learn more from Robinson directly?"
- Recommending what to buy / subscribe to / listen to
- Confirming a URL before quoting

**Triggers (verbatim or close):** source for this, where did Robinson
say, can I see the post, link to the podcast, what should I read,
what should I buy, recommended purchases, his book, his course, his
LinkedIn, his Twitter, his YouTube, the RB2B newsletter.

---

## Default load behavior

- If the question is voice / content / posting — load `founder_led_content_flywheel.md`.
- If the question is bootstrap / pricing / freemium / capital — load `capital_efficient_b2b_growth.md`.
- If the question is sourcing / quoting / recommending — load `robinson_public_corpus.md`.
- If unclear — ask ONE clarifying question before loading anything.
