# franchise-mathews / _canon / routing index

Load the minimum file needed for the question. Do not load all three
unless the question spans the whole system.

---

## Quick router

| If the question is about...                                       | Load this file                                  |
|-------------------------------------------------------------------|-------------------------------------------------|
| Why are our franchisees failing?                                  | `franchise_lifecycle_5_phases.md`               |
| Franchisee retention / churn / closure                            | `franchise_lifecycle_5_phases.md`               |
| Field coaching / support programme design                         | `franchise_lifecycle_5_phases.md`               |
| Training / onboarding / Launch experience                         | `franchise_lifecycle_5_phases.md`               |
| Peer groups / advisory councils / brand culture                   | `franchise_lifecycle_5_phases.md`               |
| Why a franchisee is "stuck" or "burning out"                      | `franchise_lifecycle_5_phases.md`               |
| Exit / resale / alumni / failed-franchisee post-mortem            | `franchise_lifecycle_5_phases.md`               |
| Multi-unit / area developer pathing                               | `franchise_lifecycle_5_phases.md`               |
| Franchise lead generation strategy                                | `franchise_buyer_journey_recruitment.md`        |
| Recruitment process / sales process / FDC scorecard               | `franchise_buyer_journey_recruitment.md`        |
| Cost per signed franchisee / candidate-to-deal math               | `franchise_buyer_journey_recruitment.md`        |
| Validation calls / Item 19 / Item 20 / FDD                        | `franchise_buyer_journey_recruitment.md`        |
| Discovery Day design and execution                                | `franchise_buyer_journey_recruitment.md`        |
| Cultural fit criteria / 4 Ms scoring                              | `franchise_buyer_journey_recruitment.md`        |
| 10 buyer personas / persona-brand fit                             | `franchise_buyer_journey_recruitment.md`        |
| Franchise Sales Tipping Point / 10 keys                           | `franchise_buyer_journey_recruitment.md`        |
| Agency strategy for franchise development clients                 | `franchise_buyer_journey_recruitment.md`        |
| Resicert / Client B / AU-NZ franchise vertical brief              | `franchise_buyer_journey_recruitment.md` + corpus |
| Where did Mathews say X? / quote sourcing / citation              | `mathews_public_corpus.md`                      |
| What books should I buy? / what should Ivan read?                 | `mathews_public_corpus.md`                      |
| Podcast / video / article catalogue                               | `mathews_public_corpus.md`                      |
| Buyer Journey video URL / slide deck / FPG academy                | `mathews_public_corpus.md`                      |
| Mathews short quote with source URL for a deliverable             | `mathews_public_corpus.md`                      |

---

## Cross-file dependencies

- **Lifecycle and Buyer Journey are coupled.** The Lifecycle starts at
  the moment the Buyer Journey ends (signed franchise agreement →
  Phase 1 Launch). Questions about handoff load both files.

- **Validation call performance** is in `franchise_buyer_journey_recruitment.md`
  but is **caused by** Lifecycle support quality (Phase 2 Grind
  franchisees do bad validation calls). Diagnose with Buyer Journey,
  prescribe with Lifecycle.

- **Agency / DR / Resicert questions** typically load
  `franchise_buyer_journey_recruitment.md` first (because the agency
  conversation starts at the funnel), then `mathews_public_corpus.md`
  for citations in the deliverable.

---

## Default load order when in doubt

1. `franchise_buyer_journey_recruitment.md` (covers ~70% of franchise
   coaching questions — recruitment is where most operators are bleeding)
2. `franchise_lifecycle_5_phases.md` (covers the rest — operations,
   support, retention)
3. `mathews_public_corpus.md` (load only when citation / source URL /
   reading-list / book recommendation is needed)
