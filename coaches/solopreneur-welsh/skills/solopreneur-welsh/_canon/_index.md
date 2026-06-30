# _canon/ — Routing Index

Three reference files live in this folder. Load them based on
question type. Do not load all three by default.

---

## ROUTING TABLE

| User's question is about... | Load this file |
|---|---|
| LinkedIn cadence, hooks, post structure | `content_os_methodology.md` |
| PAIPS formula, hook bank, first 2 lines | `content_os_methodology.md` |
| Hub-and-Spoke model, 1-3-5 method | `content_os_methodology.md` |
| Content matrix, scoring, 730-day library | `content_os_methodology.md` |
| Batching, 4-hour week, content calendar | `content_os_methodology.md` |
| Newsletter setup, repurposing flow | `content_os_methodology.md` |
| "What phase am I in?" / phase diagnosis | `solopreneur_5_phases_frameworks.md` |
| Survival → Growth → Expansion → Defense → Automation | `solopreneur_5_phases_frameworks.md` |
| First product launch, pricing ladder | `solopreneur_5_phases_frameworks.md` |
| When to hire, when to stay solo | `solopreneur_5_phases_frameworks.md` |
| The $10M journey / 23-step roadmap | `solopreneur_5_phases_frameworks.md` |
| Anti-VC, anti-team, anti-scale logic | `solopreneur_5_phases_frameworks.md` |
| "Where do I read Welsh's actual essay on X?" | `welsh_public_corpus.md` |
| "Which Welsh course should I buy?" | `welsh_public_corpus.md` |
| URLs for newsletter archive, LinkedIn posts, X | `welsh_public_corpus.md` |
| Pricing for LinkedIn OS / Content OS / Creator MBA | `welsh_public_corpus.md` |
| Podcast appearances, third-party case studies | `welsh_public_corpus.md` |

---

## LOAD-COMBINATION RULES

- **Diagnosis question** (where am I, what's broken, what's next):
  load `solopreneur_5_phases_frameworks.md` FIRST. Diagnose phase.
  THEN load `content_os_methodology.md` for the specific install.

- **"How do I post on LinkedIn?"-class question:**
  load `content_os_methodology.md` only. Don't over-route.

- **"Should I quit my job and go solo?"-class question:**
  load `solopreneur_5_phases_frameworks.md` only. Stay in the
  phase model. Don't dump content tactics on a pre-Phase-1 user.

- **"Where can I read more / buy more?"-class question:**
  load `welsh_public_corpus.md` only.

- **Never load all three at once unless the user explicitly asks
  for "the full Welsh playbook from scratch."**

---

## DEFAULT ROUTING WHEN AMBIGUOUS

If the question is ambiguous and you're not sure which file to load,
default to `content_os_methodology.md` — that's the operational core
and answers ~60% of incoming Welsh-coach questions. Diagnose first
inside SKILL.md, then load the canon file that matches the
diagnosis.

---

## FILES IN THIS FOLDER

- `content_os_methodology.md` — Content OS, PAIPS, 1-3-5,
  Hub-and-Spoke, Matrix, batching, 730-day library
- `solopreneur_5_phases_frameworks.md` — 5 phases, $10M roadmap,
  ladder of products, hiring philosophy, phase traps
- `welsh_public_corpus.md` — URL catalogue: newsletter archive,
  LinkedIn, X, podcasts, courses, recommended purchases
- `_index.md` — this file
