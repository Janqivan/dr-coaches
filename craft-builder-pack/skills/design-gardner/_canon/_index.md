# _canon — Routing Index

Reference loader for the design-gardner skill. Read this first when
you're unsure which canon file the task needs. Load the minimum.
Do not load all three unless the task is a full audit.

---

## What is in this folder

- **`conversion_centered_design_frameworks.md`**
  The 7 CCD principles, deep. Attention, Context, Clarity, Congruence,
  Credibility, Closing, Continuance. Each with definition,
  application, mistake, audit question, example. Plus the
  10-step CCD audit sequence.

- **`attention_ratio_and_message_match.md`**
  The math of paid-traffic landing pages. Attention Ratio (counting
  leaks), Message Match (ad↔page alignment), Conversion Coupling
  (form↔offer alignment). Includes fix sequences for each.

- **`gardner_public_corpus.md`**
  URL catalogue. Unbounce blog, CCD ebook, Attention-Driven Design
  ebook, CTAConf talks, YouTube, SlideShare, interviews. Plus
  recommended purchases and adjacent reading. Citation protocol at
  the bottom.

---

## Routing table

| If the task is… | Load this |
|---|---|
| Design a new landing page from scratch | conversion_centered_design_frameworks.md |
| Audit an existing landing page (full critique) | conversion_centered_design_frameworks.md + attention_ratio_and_message_match.md |
| Diagnose why paid traffic isn't converting | attention_ratio_and_message_match.md |
| Decide what to strip from a page (nav, footer, CTAs) | attention_ratio_and_message_match.md (Attention Ratio section) |
| Decide form length / form fields | attention_ratio_and_message_match.md (Conversion Coupling) |
| Match ad copy to page headline | attention_ratio_and_message_match.md (Message Match) |
| Write or fix CTA button copy | conversion_centered_design_frameworks.md (Closing principle) |
| Five-second test / headline/subhead flip | conversion_centered_design_frameworks.md (Clarity) |
| Trust / proof / testimonial placement | conversion_centered_design_frameworks.md (Credibility) |
| Thank-you page / post-conversion design | conversion_centered_design_frameworks.md (Continuance) |
| Cite Oli or send a client to source material | gardner_public_corpus.md |
| Decide whether to buy Unbounce / a course / a conference | gardner_public_corpus.md (Recommended Purchases) |
| Verify a framework attribution before quoting | gardner_public_corpus.md (Citation Protocol) |

---

## Load order for a full audit

If the user asks for a full Oli-style audit of a page (the most common
heavy task), load in this order:

1. `attention_ratio_and_message_match.md` — diagnose first.
2. `conversion_centered_design_frameworks.md` — prescribe second.
3. `gardner_public_corpus.md` — only if the user wants citations or
   to go deeper than the synthetic coach.

The audit itself runs in the order set out at the bottom of
`conversion_centered_design_frameworks.md` (the 10-step CCD audit
sequence). Steps 1–3 of that sequence are diagnostic — if they fail,
do not waste time on steps 4–10. The page needs to be rebuilt, not
optimised.

---

## Default behaviour

If the user invokes `/design-gardner` with no specific task — just
"audit this" or "look at this page" — default to:

1. Load `attention_ratio_and_message_match.md`.
2. Run the five-question diagnostic from the SKILL.md.
3. If diagnostic flags structural problems (page is a homepage,
   message match broken, AR > 10:1), report those and stop. Do not
   walk the seven principles on a page that fails the first three
   diagnostic questions.
4. If the page passes diagnostic, then load
   `conversion_centered_design_frameworks.md` and run the full
   seven-principle critique.
