# AI design tools (dated) and his process (Michal Malewicz)
> Sources: [YT:<id>] = YouTube video id; (YYYY-MM) = upload month (approximate); "mentions" = number of separate evidence items.

## PART 4. AI design tools (what they get right and wrong, dated) and his design process

### Rules (ranked by how often they say it)
- **Learn fundamentals first so you can judge AI output; slop comes from a human who cannot notice it** — Use AI as a teacher ("how does system architecture work", "what are the rules for good typography") to spot faults in AI-made work. Design done right is probably among the last things replaced, but only if you learn fundamentals, not AI tools or Figma speed. [YT:vUuOlCjP8VY, YT:iSC6JgFBZWg, YT:_PJLefMZwko, YT:GzDBkU0irpA] (2026-05, 2025-10, 2026-03, 2026-09) · mentions 10
- **AI-image-first heroes with filler copy are artwork, not design; design is what works** — Anime backgrounds, clouds, blobs, house photos with vague words only pass at thumbnail size; every visible line points away from the button. [YT:GzDBkU0irpA, YT:wrj4GDcLqJY, YT:nWbBZPjev_0, YT:ThmHV38Ecqk] (2026-09, 2025-10, 2025-10, 2025-10) · mentions 9
- **Slop is visibly low effort at every level, and AI inflates the 6/10 middle** — Copy and emails count, not just graphics; a site built in minutes is a "six out of 10 website". Money concentrates on the genuinely great, the rest race on price, customers drift to whoever shows effort. [YT:HQpQhmJi22s, YT:3BvDDjmzYY8, YT:vUuOlCjP8VY, YT:9nXMEqZH35A] (2026-06, 2026-07, 2026-05, 2026-08) · mentions 8
- **Consistency by copy-paste: apply every spacing or colour change to every element using that pattern, then re-audit** — Reuse existing elements, paste a nav tab at the exact same position on every screen, fix a wrong icon colour everywhere; edits shift things half a pixel, so select all and re-check. [YT:w2mNSOWiZbU, YT:Kqg3vN1ms2E, YT:FBDVzr0peO4, YT:ThmHV38Ecqk] (2026-09, 2026-08, 2025-10, 2025-10) · mentions 8
- **Use AI to make things better, not faster** — If AI saves 80% of the time, make the same number of things five times better; AI does code and components, he spends the effort on branding, copy and delight. [YT:vUuOlCjP8VY, YT:IkspcJdeP3U, YT:9nXMEqZH35A, YT:-xKgBgGOAqs] (2026-05, 2026-05, 2026-08, 2026-03) · mentions 7
- **Write copy, user story and spec by hand first; AI only reacts to them** — Never generate website copy; write it, then ask AI for angles, rephrasings, power words, emotional triggers. A user story started with AI is already lost. [YT:GzDBkU0irpA, YT:zatFKQqtmuw, YT:9nXMEqZH35A, YT:HnTv9J9RYrw] (2026-09, 2026-05, 2026-08, 2025-10) · mentions 7
- **Do not use ChatGPT for real UX research, unedited content, interface design, measuring success, niche or innovative products** — It averages the internet (knowledge only to 2021 then), cannot iterate, skips the unusual; a KPI set from an Uber case cannot fix a beach yoga app. Pasted survey or persona prompts are fine only in a portfolio piece you fully understand. [YT:VcM-6eT0WQ8] (2023-10) · mentions 7
- **Type frame first: real copy at real sizes and hierarchy in black and white, then a visual that comes from the text** — The visual must match and amplify the copy or it has no reason to exist; corporate teams reason from real-looking copy, not low-fi wireframes. [YT:GzDBkU0irpA, YT:nWbBZPjev_0, YT:aGTqFp7GAKE, YT:HnTv9J9RYrw] (2026-09, 2025-10, 2024-10, 2025-10) · mentions 6
- **"Good enough" is the trap: accepting AI's 80% erodes your eye** — Next time the tweaks seem unnecessary, 60% or 50% passes unnoticed; skill atrophies and you notice fewer issues. Designers lost by getting lazy, not because AI is better. [YT:O_9m_pcPSuU, YT:3BvDDjmzYY8, YT:HnTv9J9RYrw] (2024-10, 2026-07, 2025-10) · mentions 6
- **Keep manual control of what AI builds** — Understand most of the code, keep styles inline, expose sliders and tune by hand, give Claude exact CSS values, never ask it to move something 1px. [YT:-xKgBgGOAqs, YT:psyw2_j_5jk, YT:GzDBkU0irpA] (2026-03, 2026-06, 2026-09) · mentions 6
- **Use AI where it is strong: edge cases, forgotten questions, data processing, research parsing, flow skeletons** — Its images and text are only superficially good. [YT:GzDBkU0irpA, YT:zatFKQqtmuw, YT:3BvDDjmzYY8, YT:CEae73_HK9U] (2026-09, 2026-05, 2026-07, 2024-10) · mentions 6
- **Practise by recreating popular shots, add your own twist, never copy directly; practise without AI and without auto layout** — Daily at the start; skip 30-second animation tutorials. [YT:FBDVzr0peO4, YT:VUY8dOEJSaM, YT:HnTv9J9RYrw] (2025-10, 2023-10, 2025-10) · mentions 6
- **Do not invest in learning tokens, variants or design-system plumbing** — Design systems scale repetitive work, which AI now does; Figma's push that everyone needs a design system was "a marketing trick" for seats. One video only. [YT:6_t66Ef0Llk] (2025-12) · mentions 6
- **Keep know-how and client lists off frontier models; run narrow async jobs locally** — Uploads let a lab bake the best apps into its chatbot; local models need heavy guardrails (Python scripts around the model). [YT:HQpQhmJi22s, YT:4ilJC-kfqBs, YT:aLa-Anq4nuc] (2026-06, 2026-08, 2026-05) · mentions 5
- **No auto layout until you can lay out and align by hand** — Otherwise you miss proximity and cannot tell when it broke things; do the first couple dozen designs without it; groups still drift off-centre with it. [YT:w2mNSOWiZbU, YT:ThmHV38Ecqk, YT:Kqg3vN1ms2E, YT:ySbVqIMV5Ng] (2026-09, 2025-10, 2026-08, 2021-10) · mentions 5
- **Ask "How can I test it?"; deploy, test live, a page is never finished** — Bad design usually fails a well-run test; write a post-launch strategy doc before launch; A/B test or use Hotjar-type tools, change copy or button colour, measure clicks. [YT:Kqg3vN1ms2E, YT:Toonu-cTE60, YT:aGTqFp7GAKE, YT:nq07DZq3Og8] (2026-08, 2024-10, 2024-10, 2026-04) · mentions 5
- **Build things with intent: solve a problem you personally have, stay readable and functional** — His models are skilled people using AI; his breathing app's value comes from five years of daily practice, not the code. [YT:sYlBqbckWN0, YT:9nXMEqZH35A] (2026-08, 2026-08) · mentions 5
- **Reverse-engineered case studies are allowed: the project exists to show HOW you worked** — With only hi-fi, build wireframes, personas and flows afterwards; order is irrelevant, recruiters want an engaging story; run the real process from the start on real jobs. [YT:N-34Q9mhwvs, YT:_PJLefMZwko] (2025-11, 2026-03) · mentions 5
- **Do not vibe-code for the market; build for yourself only if you can maintain it** — Three fates: limbo, zero users, or built for yourself (single-digit to low-double-digit % life gain, breaks after weeks, leaks know-how); about 99.9% are existing products plus a quirk. [YT:kDZdbfXUndQ, YT:MpuMy5yipHM] (2026-07, 2026-04) · mentions 5
- **Client visuals: no single-prompt image; start from real photos and let AI only tweak** — Get branding, staff and people-at-work photos from the client; AI swaps backgrounds, raises colours, recolours. Never post a raw Midjourney image. [YT:GzDBkU0irpA, YT:iSC6JgFBZWg, YT:u01ZGoiLJ70] (2026-09, 2025-10, n.d.) · mentions 4
- **Test on real phones, not a shrunken desktop browser** — Night, sunlight, Android and iOS; export a PNG to the phone and check font sizes and tap targets; Apache preview serves every device. [YT:q8yUIbRiNRc, YT:FBDVzr0peO4, YT:-xKgBgGOAqs] (2025-10, 2025-10, 2026-03) · mentions 4
- **Designers and front-end developers converge** — Designers learn CSS/HTML, developers learn design; talk to developers as people, clarity first; be good across the whole spectrum. [YT:-xKgBgGOAqs, YT:u01ZGoiLJ70, YT:5G4mB9MQzlo, YT:f3qjhQG2prU] (2026-03, n.d., 2024-10, 2025-10) · mentions 4

### Methods (named or ordered)
#### Red square method (web version, his name for it)
- When they use it: laying out any screen so spacing is a number, not a feeling; practise by hand before auto layout.
- Steps: 1. Frame at Dribbble-shot size. 2. 12-col grid, gutter 32, column 64, max width 1120, height ~750. 3. Make physical squares 8/16/24/32/40/48. 4. Block each screen as plain rectangles. 5. Drag squares between every element. 6. Between sections 24-32 (40 roomy), inside elements 8/16/24; smaller gap = same group. 7. Only then add content, icons, photos.
- Their example: a delivery dashboard built in a bit over an hour as a first-version template; the transferable part is the alignment and spacing concept.
- Sources: [YT:w2mNSOWiZbU, YT:ThmHV38Ecqk] (2026-09, 2025-10)
#### Type frames first (he says he invented it a couple of years ago with large corporate marketing teams)
- When they use it: starting any landing page, before any visual.
- Steps: 1. Write the problem and the solution the business solves. 2. Explain how it does it in the description. 3. Add a low-friction CTA. 4. Once it works in black and white, add colours, gradients, shadows and the visual, which must match and amplify the text.
- Their example: demo build for a fictional brand: logo, menu, kicker leading to the slogan "the best yellow hoodies ever", context line, button, right side reserved for the key visual; then a Midjourney visual, background removed in Pixelmator Pro, moved to the vector tool.
- Sources: [YT:GzDBkU0irpA, YT:nWbBZPjev_0, YT:aGTqFp7GAKE] (2026-09, 2025-10, 2024-10)
#### Planning phase before any design (writing only)
- When they use it: any product (web, mobile, watch); a logical structure needs back-and-forth that writing allows.
- Steps: 1. In a plain text tool (iA Writer, Docs, Notepad) say what the business is. 2. Invent about 5 sample products. 3. Write the structure as tabs (dashboard, orders, restaurants, drivers, settings). 4. List contents per tab. 5. Paste into Figma and go straight to hi-fi, no low-fi wireframes.
- Their example: delivery dashboard; blocks learned: dashboard, data table, map plus list, grid view, side overlay, forms, login, collapsed menu; homework: crypto exchange or online bookstore.
- Sources: [YT:w2mNSOWiZbU] (2026-09)
#### Figma-free web workflow (March 2026)
- When they use it: building his own and client sites; he says it is "a lot different than it was even a year ago". [quote src: YT:-xKgBgGOAqs]
- Steps: 0. Talk and brainstorm, often on walks. 1. Paper layout sketch, colours to map the vibe, logo sketches. 2. Obsidian: write copy structure (kicker, H1, description, CTA, notes, nav, top bar), export as MD for the AI's first build. 3. Sketch only for assets (SVG logo). 4. Build with Claude (Max/$100 plan) in the app's code tab, not the CLI, plus Sublime Text for manual edits with inline styles. 5. Git push to the Mac mini, which refreshes the Apache preview on every device. 6. Only when finished, have AI split JS and CSS and clean up.
- Their example: define the grid first ("64 by 32 by 12"), never let AI define mobile breakpoints; a landing page takes as long as before, the saved coding time goes into quality.
- Sources: [YT:-xKgBgGOAqs] (2026-03)
#### Paper to coded page in Framer (Nov 2025; sponsored by Framer)
- When they use it: apps and websites where delightful interactions matter; no handoff, no developer.
- Steps: 1. Rough paper notebook, on walks or in cafes. 2. Studio notebook, second coloured version: redraw in colour and write every idea in the margins (colouring switches the brain from linear to multimodal). 3. List core, delightful, optional elements. 4. Variants in Framer design pages. 5. AI generates structure and components. 6. Promote the winner to a live coded page. 7. Connect domain, publish.
- Their example: colouring the sky gave the idea that sky colour follows weather and time of day.
- Sources: [YT:YdgLBdbkR88] (2025-11)
#### AI flow-diagram skill (hand-written story, AI skeleton, manual rework)
- When they use it: early client collaboration, developer documentation, exporting to MD to seed wireframes.
- Steps: 1. Write the user story BY HAND from the user's view. 2. Annotate technically: back-end behaviour, data storage, private vs public data. 3. Load the MD skill plus the story. 4. AI returns an editable canvas (nodes he can move), much of it wrong; ask for all edge cases. 5. Edit every node: screen content, how it works, links, business logic and goals. 6. Convert to a type-frame prototype, then add visuals.
- Their example: a week of work becomes 1-2 days; the saving is mostly drawing boxes and arrows.
- Sources: [YT:zatFKQqtmuw, YT:GzDBkU0irpA] (2026-05, 2026-09)
#### Audit and repair a bad UI (stop designing, start auditing)
- When they use it: critiquing or fixing any UI, flow, resume or portfolio; he says tools change, human perception does not.
- Steps: fix one issue at a time: 1. alignment and margins (no font or colour changes yet) 2. fonts 3. hierarchy 4. icons 5. colour; keep coloured rectangles in a toggleable group named "helper lines"; re-audit after fixing; ask "How can I test it?".
- Sources: [YT:Kqg3vN1ms2E] (2026-08)
#### Redesign (client site, then your own work)
- Steps: 1. Run the old site through the studio's internal Web Review tool (problems top to bottom, colour, spacing, type, shorter or more convincing slogans). 2. Manual heuristic analysis with many annotations. 3. Ask the client where unsure, since a choice that looks bad may be right in their industry; track conversion at every step. Own work: find what worked via the client's user access and question database, keep the good, re-check market, devices, tools.
- Their example: a medical-startup audit; the "simplify" rule dropped when a high-stakes B2B buyer wants maximum information.
- Sources: [YT:Qb7FVefKH3I, YT:cS1J77CLqmA] (2025-10, 2025-11)
#### Practice drill and replication loop
- Steps: 1. Pick a popular Dribbble shot, recreate only background and card (rotate diagonal ones first). 2. Overlay a semi-transparent rectangle, match the shape, colour-pick where shadow meets background, raise Y then blur until similar; not 1:1. 3. In apps you like, find the twist and add something of your own. 4. Make many versions of the key screen: duplicate, vary background, overlay, shadow, framing, remove one thing.
- Sources: [YT:FBDVzr0peO4] (2025-10)
#### Test protocol for a new top model (he tested Fable, also called Mythos)
- When they use it: judging whether a model can replace designer work.
- Steps: 1. Give full context (all copy, all colours, real logo, site purpose) but NOT the original designs, or it recreates them. 2. Run three real agency projects: desktop landing page for a vet clinic, a tablet design for FX Pro, a complex web-app flow diagram prefilled as JSON for his internal diagramming tool. 3. Score each out of 10. Both UI baselines were 2+ years old, so a fair but soft benchmark.
- Sources: [YT:3BvDDjmzYY8] (2026-07)
#### Case-study build for recruiters (blueprint, not template)
- Steps: 1. UI-sandwich header, market block (category statistic plus problem line, chart 6 columns wide). 2. Competitors: 3 to 5 apps, one good and a couple bad per app. 3. Zero-user survey: ask on social media, 23 respondents looks fine. 4. Show ONE flow, say fail states exist; 3 to 5 wireframes. 5. Hi-fi: decisions, screen count, two tested variants. 6. Accessibility self-critique, before and after (FAIL red, PASS green).
- Their example: two personas as different as possible, never based on yourself; recruiters scan, so show informed decisions.
- Sources: [YT:N-34Q9mhwvs, YT:_PJLefMZwko] (2025-11, 2026-03)
#### Other process chains
- Startup from zero (Zeppelin sponsored): flow diagram, review with developers before any design (cross out what cannot be built), low-fi, hi-fi, handoff [YT:5G4mB9MQzlo] (2024-10). Animated site (Webflow sponsored): paper mind map, copy on paper with markers, higher-fidelity design, Webflow build, timeline animation [YT:DMUZEMEI_Xc] (2025-10)

### Recipe library (exact, reusable)
- **AI help on copy without generating it** — Write the copy yourself, paste it into AI, ask for angles on how it solves your user group's problem, for paths that could be more beneficial to users, how to rephrase, which power words or emotional triggers fit; if you do not know what emotional triggers are, ask AI to explain them. [YT:GzDBkU0irpA] (2026-09)
- **Site from human-designed components (Relume MCP + Claude Code; Relume partner video)** — 1. Spec sheet `.md`: first draft by hand, AI merges its app analysis, edit by hand again. 2. Optional: ask Claude for a concise prompt, new Relume project, 5-10 pages, sitemap and wireframes, tweak style guide, export the naming-convention CSV. 3. Copy the MCP link from Relume, tell Claude Code to connect, exit and reopen, type `/mcp`, pick Relume, authenticate (one-time). 4. Tell Claude the content `.md` is the primary source of truth and the Relume CSV the secondary; it pulls components and builds the front end; run the dev server locally. [YT:9nXMEqZH35A] (2026-08)
- **Keep Fable from dropping to Opus on hardening work** — Leave "security", "hacking" and "vulnerability" out of the prompt; use synonyms for the same ideas and it mostly stays on Fable and fixes the issues. [YT:4ilJC-kfqBs] (2026-08)
- **Framer AI (sponsored)** — Wireframer: describe the content structure between header and footer. Workshop (Cmd+K): `a container of around 200 pixels in the middle of the screen` with a red square following the mouse (red placeholder is his trademark); a background component told which colour at which hours. [YT:YdgLBdbkR88] (2025-11)
- **AI-built interactive effect** — Have AI generate the component, expose sliders for every physics and lighting value, tune by hand until it behaves exactly as wanted. [YT:psyw2_j_5jk] (2026-06)
- **Branching-story character** — Generate the person (the client) with AI, then the same person on a transparent background in states (happy, angry, indifferent, sad); show the state that matches the user's chosen reply. [YT:DMUZEMEI_Xc] (2025-10)
- **Midjourney image he would publish** — Never post raw: cut parts out in Photoshop and mix with another image; prompt for a specific pose, swap in the real face, change lighting, replace background. Do not imitate artist styles, change eye colour or hair on people, skip images with a watermark or signature. [YT:u01ZGoiLJ70] (n.d.)
- **Custom UI-feedback GPT** — ChatGPT Plus ($20/month) and GPT-4: Explore, Create a GPT, Builder; tell it `my own GPT app that evaluates my user interface designs and I want to be able to upload a screenshot and get feedback`; specify colours, hierarchy, grid, spacing; answer the focus question (he chose hierarchy and spacing); test with a screenshot; Save, Confirm. Tailor it to one weak area. [YT:_4OBLx9_uLg] (2024-10)
- **Fake a long table** — About 8 rows suffice; duplicate in uneven chunks (copy 4, send back, copy all 8, or copy last 6); mask so one row is cut off at the card bottom to imply scrolling. [YT:w2mNSOWiZbU] (2026-09)
- **Manual pen-tool cutout (AI removal is weak on objects)** — Click around the edges (precision matters little on a large original), close on the first point, outline off and fill on, drag the vector under the photo, mask; trace each hole separately and Subtract. [YT:w2mNSOWiZbU, YT:FBDVzr0peO4] (2026-09, 2025-10)
- **Screen setup (iPhone 12)** — Red helper rectangles: status bar 44, navbar 60, tab bar 64, bottom safe area 22, grouped "OS helpers" and hidden; 100 between artboards; name every group and layer. [YT:ThmHV38Ecqk] (2025-10)
- **Post-launch strategy doc (written before launch)** — What happens one week after; how data is collected; what is tweaked first (A/B headline vs visuals); when to first email users about confusion; aim for 1-2% growth every week or two. [YT:nq07DZq3Og8] (2026-04)

### Fix library (problem → fix → why)
- **Problem:** AI output looks the same every time (pill kicker, same headline-to-description ratio, same button shadows) → **Fix:** feed human-designed components through an MCP library and add hand-made delight → **Why:** without the library the control run was "as generic as AI can go". [YT:9nXMEqZH35A] (2026-08)
- **Problem:** AI layout breaks on edge cases (a long German word at 375px gives horizontal scroll) → **Fix:** test long words at 375px and use tested components → **Why:** AI output is an average of the internet, not planned for edge cases. [YT:9nXMEqZH35A] (2026-08)
- **Problem:** AI hero template tells (invented pill kicker, pills competing with the CTA, thick multi-line headline, CTA colour copying the nav buttons, tinted icon in a rounded square, mismatched SVG sets) → **Fix:** contrasting CTA colour, thinner headline weight, emotion-adapted photo, hand-composited cards, structure from the audience's main questions → **Why:** the difference is intention. [YT:3BvDDjmzYY8] (2026-07)
- **Problem:** AI flow diagram adds far too many pages and steps (about 20-30% right) → **Fix:** start from a hand-written story and rework every node → **Why:** it pattern-matches junior portfolio flows, the most abundant flow material online. [YT:3BvDDjmzYY8] (2026-07)
- **Problem:** AI image hero pulls the eye away from the CTA → **Fix:** shorten text lines toward the button, make the button the only colourful element, aim gaze and perspective at it, blur-test → **Why:** a ragged right edge tires the brain and people look at the brightest point. [YT:wrj4GDcLqJY] (2025-10)
- **Problem:** photo clashes with the CTA (brown eyes, beige jacket, blue CTA) → **Fix:** recolour the eyes blue and shift the beige cooler; AI now does such swaps, so tweak an existing photo and let the visual come second → **Why:** photo and CTA colours must agree. [YT:GzDBkU0irpA] (2026-09)
- **Problem:** AI component search rarely returns the exact outcome → **Fix:** find the open-source solution by hand, tweak values in browser Inspect, hand Claude the exact CSS values → **Why:** saves time. [YT:-xKgBgGOAqs] (2026-03)
- **Problem:** generic bot feedback is vague (says alignment is wrong, never how to fix it) → **Fix:** train a bot only on your own work, pair it with human feedback, or aim a GPT at one weak area → **Why:** his own bot is about 30% off and 70% good; humans catch nuance. [YT:_4OBLx9_uLg, YT:u01ZGoiLJ70] (2024-10, n.d.)
- **Problem:** AI social content reads like old SEO articles (keywords, no resonance) → **Fix:** generate a post blueprint, add the human touch at every step, train on your own photos, rewrite text how you would talk to a friend → **Why:** a personal brand is where AI meets your humanity. [YT:lx2H_ROKgZs] (2025-10)
- **Problem:** angled 3D mockups hide uneven margins → **Fix:** one mockup in the case-study header, other screens flat in a grid or linked by flow lines → **Why:** an angle makes unequal distances look equal. [YT:Kqg3vN1ms2E] (2026-08)

### Tool and model notes (dated, newest first; these age fast)
- **Claude Design + Relume MCP test (Relume partner video)** — Claude Design on a medical and a trading site gave "eerily similar" results; Relume MCP access is in the paid Pro plan (7-day trial). [YT:9nXMEqZH35A] (2026-08)
- **Fable (also called Mythos)** — Top model leaves $20/$100/$200 plans for pay-per-usage at about 2x Opus (his date: July 7); nerfed since the June release and July re-release; he predicts users drift to Opus, then usage billing; he uses it daily. [YT:4ilJC-kfqBs] (2026-08)
- **Local models** — 18 hours for 4,500 websites every 1-2 weeks; good only at narrow async jobs with guardrails; doubts Fable-level models will run locally within 2 years. [YT:4ilJC-kfqBs] (2026-08)
- **Fable on three agency projects** — Landing page 6/10, tablet 4/10, flow diagram failed spectacularly yet was the most sensible use of AI in design; he expects subscription tiers to be nerfed to push paid tokens. [YT:3BvDDjmzYY8] (2026-07)
- **AI-built interactive UI effects** — Designers can prototype bendy buttons, realistic shadows and lighting fast; use sliders and tune by hand; such details lift products out of the slop. [YT:psyw2_j_5jk] (2026-06)
- **GPT Image 2** — Designs better than about 80% of pixel pushers: banking and pregnancy-app UIs scored 7-8/10, Dribbble-inspired, small mistakes; moving boxes in Figma is the easiest part to replace. [YT:zatFKQqtmuw] (2026-05)
- **Claude Design (Anthropic)** — Opus plus MD spec files around Claude Code, outputs React, inspector layer; he reads it as a Canva replacement, not a Figma killer. The same demo prompt in plain Claude Code needed 3 clarifications and gave the better exploration start; both slop. [YT:IkspcJdeP3U] (2026-05)
- **Gemma 4 (Google)** — Not yet workable on their Radeon-based rig and super slow, but output quality "amazing"; he expects local models to win and Apple (sells the hardware) to be well placed. [YT:twmPjqYedaw] (2026-05)
- **Google Stitch** — Generated design system "looks like a copy of a copy of a copy of some Material Design clone"; text wraps inconsistently; a prefilled UI kit; his Longevity Deck one-shot looked nothing like the real app. [YT:qEwzCPGt9BQ] (2026-04)
- **His build stack** — MacBook Air M4 (32 GB); M1 Mac mini (32 GB) as Apache and Git server, 14B local model, agent server; Framework desktop running a 32B model over Ethernet; Claude Max ($100) in the code tab. [YT:-xKgBgGOAqs] (2026-03)
- **Framer (sponsored)** — He says he pays for a license; design pages let you draw without thinking of breakpoints or auto layout, duplicate artboards into variants, promote the winner to the coded site. [YT:YdgLBdbkR88] (2025-11)
- **AI photos and UI** — Photos about 95% there, Square Block wants 99% and will tell clients when AI photos reach 99-100%; AI UI is pretty good but not perfect and just gets cheaper. [YT:iSC6JgFBZWg] (2025-10)
- **Hype4 Academy AI reviewer** — Built on his books and courses; "cannot replace human feedback"; the hardest part was a training PDF both precise and concise. [YT:5G4mB9MQzlo] (2024-10)
- **His own ChatGPT feedback bot** — Polite and vague, could not explain his red square method to an 8-year-old, needed several asks to credit him with glassmorphism; not worth $20 a month. [YT:_4OBLx9_uLg] (2024-10)
- **Older tools** — Midjourney: nice images, replaces a designer no more than a stock site (2024); Gemini demo impressive but aimed at search, not designers (2024); ChatGPT knowledge ended in 2021 (2023); Figma trains on users' work, opt-out until August 15th (2024). [YT:KS7l6AzFUUI, YT:CEae73_HK9U, YT:VcM-6eT0WQ8, YT:O_9m_pcPSuU] (2024-10, 2024-10, 2023-10, 2024-10)

### Coaching and critique moves
- Ask of any design or claim: "How can I test it?" [YT:Kqg3vN1ms2E]
- Interrogate every element, e.g. "Why are these shoes here?", and delete pretty elements with no job [YT:Kqg3vN1ms2E]
- Ask what the website is for; AI-image-first designers never do, and the visual must come from the copy [YT:HnTv9J9RYrw, YT:nWbBZPjev_0]
- Trace the eye path on AI heroes (text edge, gaze, lines) and blur-test it [YT:wrj4GDcLqJY]
- Ask the client where unsure; a choice that looks bad may be right in their industry [YT:Qb7FVefKH3I]
- Redesign review: what worked, what did not, what changed in the world versus what you got wrong [YT:cS1J77CLqmA]
- Demand process proof (sketches, annotations), because clients suspect you only typed a prompt [YT:_PJLefMZwko]

### Numbers they have stated
- Copilot multipliers on Anthropic models 3x to 27x; monthly messages Sonnet 4.6 300 to 33, Opus 4.6 100 to 11, Opus 4.7 40 to 11; some Claude Design users ran out of tokens in six prompts on Claude Pro [YT:aLa-Anq4nuc] (2026-05)
- Half-serious vibe coding costs about $100/month for about $4,000 of tokens; unsubsidised he estimates $4,000-8,000/month [YT:kDZdbfXUndQ] (2026-07)
- AI measured at about 25% more quality output at the same client price [YT:4ilJC-kfqBs] (2026-08)
- Flow diagram: about 20-30% of the structure right in 2 hours, saves about a day on a 2-3 day job; his skill: a week becomes 1-2 days [YT:3BvDDjmzYY8, YT:zatFKQqtmuw] (2026-07, 2026-05)
- Social-post tool: 60-90 minutes per post (7-10 hours a week) down to under 1 hour a week [YT:lx2H_ROKgZs] (2025-10)
- 200+ successful portfolios in 14 months; about one got a job with its first version [YT:Kqg3vN1ms2E] (2026-08)
- Dedicated mobile layout per breakpoint: results views +400%, registrations +270% [YT:cS1J77CLqmA] (2025-11)

### References they cite
- Valve and Half-Life 3 (slop is fine only with extreme demand); Uber and Netflix (subsidise, then raise price and drop quality) [YT:HQpQhmJi22s, YT:aLa-Anq4nuc]
- Chris, Daniel, Dmitry and a branding designer — his models of skilled people using AI with taste [YT:sYlBqbckWN0]
- Endorses a viewer comment's point that generative AI lifts the bell curve's middle, so average-plus widens and good enough stops standing out [YT:zatFKQqtmuw]
- Relume, Framer, Webflow, Zeppelin sponsored the videos behind several items above (Relume as a partner video) [YT:9nXMEqZH35A, YT:YdgLBdbkR88, YT:PFQsC-8z8X4, YT:5G4mB9MQzlo]

### Evolution and contradictions
- **AI versus designers** — 2022-10: six reasons AI will not replace UI/UX designers soon [YT:bx_6l4rAH7k]; 2023-10: five things not to do with ChatGPT [YT:VcM-6eT0WQ8]; 2025-10: juniors' jobs will be taken (not flagged as a change) [YT:iSC6JgFBZWg]; 2026-03: design done right is among the last things replaced [YT:_PJLefMZwko]; 2026-05: GPT Image 2 beats about 80% of pixel pushers [YT:zatFKQqtmuw].
- **ChatGPT then Claude** — n.d. and 2024-10: ChatGPT is "so bad", never found it useful, own bot not worth $20 [YT:u01ZGoiLJ70, YT:_4OBLx9_uLg]; 2026-03 and 2026-04: no Figma at all, the team designs quite a lot directly in Claude Code with manual edits [YT:-xKgBgGOAqs, YT:qEwzCPGt9BQ].
- **Vibe coding** — 2026-04: "vibe coding is over" (he got hate) [YT:MpuMy5yipHM]; 2026-07: the build window is closing, his apps now maintainable with local models or no AI [YT:kDZdbfXUndQ]; 2026-08: build complex things with AI coding tools now [YT:4ilJC-kfqBs].
- **Figma, components, speed** — 2023-10: 20-minute Figma redesign, "super fast and super imprecise" [YT:Ktrb44pzMjc]; 2025-12: learning tokens and variants "makes very little sense anymore" [YT:6_t66Ef0Llk]. Speed: 2026-03 landing page takes as long as before, 2026-05 flow diagram week to 1-2 days, 2026-07 saves about a day [YT:-xKgBgGOAqs, YT:zatFKQqtmuw, YT:3BvDDjmzYY8].
- **Photos** — 2025-10: real people because AI is about 95% and he wants 99%, will say so when AI reaches 99-100% [YT:iSC6JgFBZWg]; 2026-09: no usable client image from one prompt "no matter what you write" [YT:GzDBkU0irpA].

### Signature lines (verbatim, ≤15 words)
- "you're not going to get a skill by downloading a skill MD" [YT:sYlBqbckWN0] (2026-08)
- "Slop is visibly low effort, and it happens on every level" [YT:HQpQhmJi22s] (2026-06)
- "good enough is no longer going to be good enough" [YT:IkspcJdeP3U] (2026-05)
- "we're not getting design killers. We're getting tools and templates." [YT:IkspcJdeP3U] (2026-05)
- "The main mistake here is assuming design is assembly" [YT:zatFKQqtmuw] (2026-05)
- "if you start by generating something with AI at this stage, you already lost" [YT:zatFKQqtmuw] (2026-05)
- "UI is not art. So it's not about being creative." [YT:ThmHV38Ecqk] (2025-10)
- "Use AI as a helper but not as a replacement for your brain." [YT:HnTv9J9RYrw] (2025-10)
- "you have no idea how good the average designer on the internet really is" [YT:VcM-6eT0WQ8] (2023-10)
