# Canon Routing — Which File To Load For Which Question

This file is the routing brain. Default rule: load AT MOST one framework
canon file per response. Load `two_bobs_public_corpus.md` only when citations
or research depth are explicitly needed.

---

## Route by Question Pattern

### Positioning, identity, niche, expertise
Load: `business_of_expertise_frameworks.md`

Triggers:
- "Should I narrow my niche / pick a vertical / drop a vertical?"
- "We're a full-service agency for ambitious brands…" (kill this framing)
- "Horizontal vs vertical vs demographic vs psychographic"
- "What's the waterfall of differentiation?"
- "We have three verticals — is that too many?" (Ivan classic)
- "How do I demonstrate expertise without sounding like everyone else?"
- "Should I start a newsletter / podcast / book?"
- "Pattern matching" / "T-shaped expert" / "saying no"
- Anything about repositioning or rebranding the firm
- Paid diagnostic as front door (positioning-driven sales motion)

### Money, ops, portfolio, sellability
Load: `secret_tradecraft_frameworks.md`

Triggers:
- "What should my AGI per FTE / EHR / utilization be?"
- "How do I get off hourly billing?"
- "Should I do retainers?"
- "How do I fire a client?" / "Which clients should I fire?"
- "My biggest client is 40% of revenue" (concentration)
- "Innoficiency" / "innovation vs efficiency"
- "What are the seven traits of an expert?"
- "Should account managers close new business?"
- "How do I make the firm sellable?" / "Owner dependence"
- "Earnouts" / "valuation" / "multiple on EBITDA"
- "What's my new business hit rate supposed to be?"
- Any financial dashboard or benchmark question
- Pre-exit preparation, 18–36 months out from a sale

### Citation, research, "where did Baker say X"
Load: `two_bobs_public_corpus.md`

Triggers:
- "Send me the link to that 2Bobs episode"
- "Where did Baker write about X?"
- "Find me Baker's actual quote on Y"
- "Which book covers Z?"
- Writing a deck, memo, or article where Baker is cited
- Recommending Baker's paid services for Ivan's specific problem
- Verifying that a Baker claim is real

### Multi-file question
If the question genuinely spans positioning AND finance/ops (e.g., "I want to
reposition vertical AND raise EHR — how do I sequence?"), load both
framework files. Do NOT load the public corpus unless citing.

### Mindset / "I'm stuck" / "should I keep going"
Do not load anything. Use the SKILL.md behavior rules — redirect to a
measurable avoided behavior (firing a client, raising a price, killing a
service line, having a hard conversation with a senior employee). Numbers
and specificity, not empathy.

---

## Don't-Load Rules

- Don't load all three files "just in case." Context bloat reduces sharpness.
- Don't load the public corpus for normal coaching answers — the framework
  files already contain the URL references inline at each major framework.
- Don't load any canon file when the user is asking a meta-skill question
  ("what is this skill", "what frameworks do you know") — answer from
  SKILL.md.

---

## Order of Operations Inside a Response

1. Read SKILL.md (always, on activation).
2. Run the Diagnostic Protocol — identify which question pattern this is.
3. Decide whether to load 0, 1, or 2 canon files. Default: 1.
4. Diagnose first, prescribe second, math it, end with the next single
   action.
5. If the user asks "where did Baker say this?" — only then load
   `two_bobs_public_corpus.md` and cite the URL.
