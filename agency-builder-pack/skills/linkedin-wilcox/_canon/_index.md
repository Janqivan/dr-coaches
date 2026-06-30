# linkedin-wilcox — Canon Index / Routing Map

Route based on the user's question type. Don't load all files at once.

---

## File Inventory

| File | Size | When to load |
|---|---|---|
| `amo_framework_full.md` | ~10KB | Audience/targeting questions, copy/creative questions, offer design, funnel architecture, "why isn't my campaign working" diagnostics. |
| `linkedin_ad_formats_and_tactics.md` | ~12KB | Ad format selection, bidding/pacing/dayparting questions, lead gen forms vs landing pages, LAN setup, Insight Tag, matched audiences, full-funnel architecture. |
| `wilcox_public_corpus.md` | ~8KB | When user asks for source/citation, wants to go deeper, needs episode references, evaluating paid products, benchmarking agency pricing. |

---

## Routing Rules

### Route to `amo_framework_full.md` for:
- "Who should I target on LinkedIn?"
- "What audience size is right?"
- "Account list vs contact list?"
- "How do I write LinkedIn ad copy?"
- "What offer works on LinkedIn?"
- "Lead magnet vs demo offer?"
- "My CTR is low" / "My conversion is low" — diagnostic table.
- "How do I build a LinkedIn funnel?"
- Any question containing "AMO", "audience", "message", "offer".

### Route to `linkedin_ad_formats_and_tactics.md` for:
- "Sponsored content vs message ads?"
- "What ad format should I use for X?"
- "How do I bid on LinkedIn?"
- "Manual CPC vs auto?"
- "How do I stop overspending?"
- "Should I use lead gen forms?"
- "What's the LinkedIn Audience Network and should I use it?"
- "How do I set up retargeting?"
- "What's the Insight Tag?"
- "Dayparting on LinkedIn?"
- Any question containing "format", "bid", "pace", "LAN", "lead gen form",
  "landing page", "Insight Tag", "matched audiences", "retargeting".

### Route to `wilcox_public_corpus.md` for:
- "Where can I learn more?"
- "What episode covers X?"
- "How much does B2Linked charge?"
- "Should I buy AJ's course?"
- "Cite the source for that claim."
- Any question about Wilcox's paid offerings, agency pricing, course
  pricing, or where to listen/read.

### Multi-file load (diagnostic + tactical):
- "My LinkedIn Ads aren't working." → Both AMO + Formats.
- "How do I launch a LinkedIn campaign from scratch?" → Both.
- "Should DR add LinkedIn as a service line?" → All three (AMO for
  capability, Formats for delivery rigor, Corpus for pricing benchmark).

---

## Diagnostic Default

If unclear, run the AMO diagnostic first (load `amo_framework_full.md`):
1. Is it an Audience problem? (sizing, targeting layer wrong)
2. Is it a Message problem? (format, copy, visual)
3. Is it an Offer problem? (friction mismatched to temperature)

Then layer in tactical (load `linkedin_ad_formats_and_tactics.md`) if
the answer is "the campaign mechanics are wrong" (bidding, pacing, LAN).
