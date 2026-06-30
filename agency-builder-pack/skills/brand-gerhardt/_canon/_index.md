# Brand-Gerhardt Canon — Routing Index

Skill: `brand-gerhardt`
Coach: Dave Gerhardt (synthetic) — Founder Brand book, Conversational Marketing,
Drift category-creation era, Exit Five community + podcast + newsletter,
HubSpot author archive, Delphi persona.

This index tells the parent SKILL.md (and any orchestrating agent) which
canon file to load for a given prompt class. Load proactively. Don't load
all three by default — pull what the question needs.

---

## Routing Table

| If the prompt is about... | Load this file |
|---|---|
| Founder content, CEO LinkedIn, podcast launch, build-in-public, founder voice, "should the CEO post," delegation rules for founder content, founder-brand cadence, the 3 pillars (social + podcast + speaking) | `founder_brand_methodology.md` |
| B2B brand voice, sounding corporate, B2B-acts-like-B2C, B2B-is-P2P, community-led growth, voice/tone calibration, homepage rewrite, anti-corporate-jargon, brand vs demand, category creation, Drift playbook, Exit Five playbook, community-as-product | `b2b_acts_like_b2c_frameworks.md` |
| "Where can I read/listen to Dave on X," sourcing a quote, finding a specific episode, recommending books/community/event, recommending Delphi clone, citing a LinkedIn post, finding HubSpot articles | `gerhardt_public_corpus.md` |

---

## Default Load Behavior

- If the user asks a **diagnostic** question (e.g., "audit my B2B brand,"
  "should I do founder brand," "we sound generic, help") — load
  `b2b_acts_like_b2c_frameworks.md` first; layer in
  `founder_brand_methodology.md` if the founder is the blocker.

- If the user asks a **how-to** question on founder content specifically —
  load `founder_brand_methodology.md` first.

- If the user asks for **sources, episodes, books, quotes, or where to
  buy** — load `gerhardt_public_corpus.md`.

- If unsure — load `b2b_acts_like_b2c_frameworks.md`. It's the most
  general-purpose canonical layer.

---

## Cross-References (when to load two files)

- "Build a founder brand for a B2B SaaS that sounds generic today" →
  load BOTH `founder_brand_methodology.md` + `b2b_acts_like_b2c_frameworks.md`.

- "Sales pitch for an Exit Five-style community in our category" →
  load `b2b_acts_like_b2c_frameworks.md` + `gerhardt_public_corpus.md`
  (for the Exit Five model + specific pricing/structure reference).

- "Find me the Gerhardt episode about X" → load only
  `gerhardt_public_corpus.md`.

---

## File Inventory

- `_index.md` (this file) — routing
- `founder_brand_methodology.md` — Founder Brand framework, 3 pillars,
  voice rules, cadence, delegation rules, 90-day plan
- `b2b_acts_like_b2c_frameworks.md` — B2B-is-P2P thesis, voice
  calibration, Drift playbook, Exit Five playbook, brand vs demand,
  anti-generic filters, operational sequence
- `gerhardt_public_corpus.md` — owned platforms, podcast top 15
  episodes, Delphi clone, HubSpot archive, LinkedIn high-signal posts,
  recommended purchases (Founder Brand book, Conversational Marketing
  book, Exit Five membership, Drive conference, Delphi)
