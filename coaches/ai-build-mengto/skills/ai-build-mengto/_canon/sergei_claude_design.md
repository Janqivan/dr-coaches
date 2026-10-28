# Second source — Sergei Chyrkov (Claude Design and Claude Code workflows)
> Sources: [YT:<id>] = YouTube video id; (YYYY-MM) = upload month.

Second source: Sergei Chyrkov. Cite as Sergei, not as Meng.

## PART S. Sergei Chyrkov: Claude Design and Claude Code workflows that avoid AI slop

### Rules (ranked by how often they say it)
- **Supply the system before the screen; keep it in a design-system .md; reuse it for every output** — Tokens first (Figma variables exported to one design-system.json, or a design MD file), agent told to use only them; keep a changelog .md and update the system file after any UI change. One system drove his website, hotel app and Instagram carousel. [YT:ScsjVpmhpyc, YT:0ajxdUNacQE, YT:1MdwweKCNwg] (2026-09, 2026-07) · mentions 19
- **Match model and tool to the step; spend no AI tokens on mechanical work** — Sonnet 5 for analysis ("we don't actually need Opus for this"), Opus 5 at high effort for screens, Composer 2.5 or a plain exporter for mechanical steps, hand edits for small fixes, a fresh chat per task. Claude Design burns limits fast: hand a good layout to Claude Code. [YT:ScsjVpmhpyc, YT:T96O8dTzi2Q, YT:UiOKZG2XeJY] (2026-09, 2026-08, 2026-07) · mentions 18
- **Never ask the model to design from nothing; supply the input** — Agents reuse one library (mostly shadcn), so `build me a SaaS landing page` with no style details guarantees generic output; with no system to follow, the model falls back on the UI kit built into the code. [YT:BtXCTWXr9mA, YT:8wsjt6IlxBw, YT:tty90cDna3A] (2026-09, 2026-01) · mentions 16
- **Edit by pointing, then finish by hand; do not prompt-loop small changes** — Select the element (canvas, edit mode, Cursor's browser panel) and change colour, type or copy directly. AI gives structure, wireframes and styles; the finish is manual so it reads as human. [YT:6tvOaRsKShQ, YT:26QlssTGjU8, YT:eT0fZ8XsAaY] (2026-09, 2026-07, 2026-06) · mentions 14
- **Design for the developer and the exporter** — "web design becomes more about engineering": auto layout, variables, 8-point grid, Fill or relative widths and Fit-content heights, never fixed widths; run a responsive pass after a pixel-perfect export. [YT:UiOKZG2XeJY, YT:PPqt_xLg_5c, YT:NUtB0Ri4f_w] (2026-07, 2025-10, 2024-10) · mentions 14
- **Work in small units: one component, one section, one reference per fresh chat** — Prompt a component alone with explicit fields and limits, then the screen that @-mentions it; chain your hand-refined screen, not the original reference, into the next prompt. "The more detailed prompt you give, the better the results you'll get." [YT:irQsPKXtsrY, YT:V2Bjb6VtHeA, YT:OuyGHRwgN_0, YT:SwaxTlY_rZw] (2026-04, 2026-02, 2025-10) · mentions 13
- **Correct by naming the broken part plainly with an exact number; verify by testing** — `problem in the buttons design`, then the inner part 80 by 80 pixels. Click every control, then batch the feature and all bugs in one follow-up; fix a defect that came from your own source frame at the source. [YT:PPqt_xLg_5c, YT:yNXbWGcQXs4, YT:V7ZpJLWY-CY] (2025-11, 2025-10) · mentions 13
- **Copy patterns, never pixels** — "We're not stealing anyone's design." Analyze references for patterns and build a unique interface; a reference's feel can transfer while the subject changes (spiral gallery to fashion photographer); an unrelated industry's look is fair game. [YT:BtXCTWXr9mA, YT:8wsjt6IlxBw, YT:BWQ542fvrXo] (2026-09, 2026-07) · mentions 10
- **One prompt never gives the best result; the loop is prompt, review, critique, iterate** — 15 to 20 minutes, an hour or a few hours ("nobody is doing it for you"). The prompt is the client briefing and mood-board work he did before AI. [YT:BtXCTWXr9mA, YT:V2Bjb6VtHeA] (2026-09, 2026-04) · mentions 8
- **Prepare the Figma file before any AI hand-off** — a variable for every number and colour ("Anywhere where I have a number I will use variable"), auto layout everywhere (it acts like flexbox), components for buttons, fixed elements set to fill. Quick test for an AI-made file: messy variables, odd numbers, inconsistent auto layout. [YT:1MdwweKCNwg, YT:H6FL3LU-cck, YT:PPqt_xLg_5c] (2026-07, 2025-12, 2025-10) · mentions 8
- **Taste, creativity and decisions stay yours; AI is a tool, not a replacement** — AI takes the jobs of lazy people building a career on one prompt; he works more now, building things he could only dream of; AI raised the importance of taste instead of lowering the bar. [YT:BtXCTWXr9mA, YT:0ajxdUNacQE, YT:BWQ542fvrXo] (2026-09, 2026-07) · mentions 8
- **Spell out every field and limit, then check each; the model drops asks and adds extras** — handle skipped (never asked); country dropped though asked; price "$2.99" instead of "starting from 99"; state hard constraints twice (HTML, CSS, JS only, no backend). [YT:ScsjVpmhpyc, YT:H6FL3LU-cck, YT:irQsPKXtsrY] (2026-09, 2025-12, 2025-10) · mentions 7
- **Unknown flow? Hand the model real-product flows, never guesses** — study working apps in Mobbin (not Pinterest-style concepts) for login, profile, settings, hotel booking; tell it `Keep their best practices.` [YT:ScsjVpmhpyc, YT:0ajxdUNacQE, YT:8wsjt6IlxBw] (2026-09) · mentions 6
- **Show the client something before they sign** — a reference-styled mock from a famous site, three style-guide concepts, three AI variants instead of a day of unpaid design, a Pinterest mood board first on every project. [YT:YdS4igzQ7AM, YT:ip7W-OMaz-c, YT:tty90cDna3A, YT:l68HFQV5RJU] (2026-05, 2026-01, 2025-10) · mentions 6

### Methods (named or ordered)
#### "No more slop" process (Claude Design to Claude Code)
- When they use it: a generic AI-built site that must look designed.
- Steps: 1. Claude chat turns a few words into a detailed prompt as an MD file. 2. Claude Design baseline, no template, no design system: type `implement`, attach the MD (Opus 5); the pizza site works but looks generic. 3. Pick a reference site image (Pinterest `fun website design`, Mobbin). 4. Design-system dropdown > create design system; drop in the image. 5. Re-run the layout update with that system. 6. Add real images (ChatGPT people photos, a real pizza photo). 7. Share > Claude Code (local agent), new folder, handoff prompt, cheaper model, polish the hero in code. 8. Reuse the system for a menu template and Instagram layouts.
- Sources: [YT:T96O8dTzi2Q] (2026-08)

#### Controlled A/B with Mobbin MCP (V1 no references, V2 with)
- When they use it: proving or fixing generic UI; building app screens from real patterns.
- Steps: 1. V1 in Claude Code (Fable 5, low effort): analytics SaaS "Pulse", direction left to the model (modern, professional, sophisticated, highly usable), built in a "version one" folder. 2. Connect Mobbin MCP. 3. V2, same agent, six steps: research named topics (SaaS analytics dashboards, business intelligence dashboards); extract patterns, copy no product; design direction; redesign with the same requirements, inventing nothing, fixing V1's generic areas; apply to every page; final pass hunting generic patterns and unnecessary elements. 4. Walk V1 against V2 screen by screen (V2 gained date-preset chips up front, a collapsible sidebar, row bars for relative size).
- Sources: [YT:8wsjt6IlxBw, YT:0ajxdUNacQE] (2026-09)

#### Token system to Claude Design (three Figma variable collections)
- When they use it: before any AI hand-off, so Claude Design output uses your exact tokens; about 95% of projects reuse the same numbers.
- Steps: 1. Base: colour steps 100 to 900 (500 main, 350 between); number scale 0, 1, 2, 4, 8, 12, 16, 20, 24, 28, 32, 40, 64, 80, 120, 160, 200. 2. Aliases linked to Base: text (link 500, hover 600, visited 400), surface, icons, borders, SP4 to SP40, RD4 to RD40 plus RD200, BR1, BR2. 3. Typography: body 12/16/20; H1 64, H2 48, H3 40, H4 32, H5 24, H6 20. 4. Scope each variable to its job; bind text styles to variables. 5. Variables > collection > export modes (zip each), unzip to three JSONs. 6. Claude or ChatGPT: `analyze these files and combine them into one design-system.json file`. 7. Claude Design: new project, high fidelity, drop the JSON in; the agent must use only its tokens, sizes and colors; verify in edit mode (gap 8, padding 16/32, H1 64, radius 16 matched; DM Sans for Inter fixed by one follow-up).
- Their trick: brand colour as the 500 swatch, overlaid on black (80/60/40/30%) and white (80/60/40/20%), eyedroppered into flat swatches, no opacity tokens.
- Sources: [YT:tvObuIcAooE, YT:1MdwweKCNwg, YT:BSRM5QSYq5k, YT:pH3JkLPwHL8] (2026-07, 2026-01, 2025-10, 2024-10)

#### Design-system-first generation (Claude Code + Figma)
- When they use it: Figma screens built from real library components, not drawn shapes.
- Steps: 1. Duplicate a simple design-system UI kit from Figma Community; Assets > libraries > publish (components and variables everywhere). 2. New file > Assets > browse team libraries > add. 3. Claude Code in an empty folder; /plugin shows Figma remote MCP authorized; `Check if Figma is connected` (always allow). 4. Paste the library link and have it analyze the system. 5. Slash figma generate design: `create login screen using our design system` plus the blank file link (about 10 minutes; typography tokens unused, no input-label token). 6. Change the library, publish, pull the update in the file.
- Sources: [YT:Xcgr-7LpzDM, YT:V2Bjb6VtHeA] (2026-04)

#### One design system, many outputs (Claude's design skill)
- When they use it: Claude Code mode with a working folder connected; slash design (not Design mode).
- Steps: 1. `Use design skill, analyze my website and create design system from it.` (Sonnet 5, high effort). 2. Real-flow screens (Opus 5, high effort): booking.com flow link from Mobbin; design home, hotel search and hotel results screens; use my design system from the first example; use Mobbin MCP to analyze this reference link; `Keep their best practices.` 3. Instagram carousel on the same system: cover, five slides, CTA to follow, `give me three variations`. 4. Edit on the canvas; export PNG (Instagram) or HTML (Claude Code builds from it).
- Sources: [YT:ScsjVpmhpyc] (2026-09)

#### AI SaaS pipeline (10 steps)
- When they use it: several SaaS products in one week.
- Steps: 1. Validate the idea in Claude chat; export a master prompt file. 2. Project folder in Claude Code or Cursor, plan mode, then agent mode; the agent builds the first concept. 3. Screenshots into Figma; iterate away from generic. 4. Flows via Mobbin MCP in Ask mode. 5. Supabase: Connect > pick the client, add the config as an MCP server. 6. Loops (or Resend) for magic-link email, keys in an env file. 7. Lemon Squeezy (easier, works where Stripe does not), Stripe or Polar; monthly and yearly products; test mode, then off; link to the hosted payment page, store no financial data. 8. Changelog and design-system .md files. 9. GitHub on each major update. 10. Vercel: paste every env secret into Environment Variables, redeploy (the step people forget), connect a domain.
- Sources: [YT:0ajxdUNacQE] (2026-09)

#### Premium site pipeline (Claude Code to Cursor to Framer)
- When they use it: a signature effect plus editable CMS and one-click publish.
- Steps: 1. Claude Code with Fable 5 prototypes one effect from a short prompt plus a visual reference. 2. Cursor with the Framer skill (install prompt at framer.com/agents/external): `fully migrate recreate the sample one` plus the empty project link. 3. Rebuild the gallery on Framer's Ticker idea so images link natively. 4. Agent builds other pages and effects as code components. 5. Link CMS meta title and description; publish.
- Why he left Claude Code: React he cannot easily modify, no CMS collection pages. Limit: migration yields a custom code component, not a native editable site.
- Sources: [YT:hNvIan93aPY, YT:BWQ542fvrXo, YT:eT0fZ8XsAaY] (2026-08, 2026-07)

#### Code, canvas, code round trips
- When they use it: edit visually, then sync back to code.
- MagicPath: install the MagicPath skill in Cursor; `transfer landing page layout to magic path project` plus `pixel perfect` (under a minute, zero MagicPath credits; animations came, fonts did not); edit visually; new Cursor agent on a new git branch: `use the selected MagicPath design ... and update the existing components in the repository.`; merge to main so Vercel redeploys. Claude Code and Figma: `put the designs in Figma file` plus the link; edit; copy link to selection; `update the design from the Figma file`.
- Sources: [YT:1d8vM0TXcTo, YT:FqQMIQRcdj8] (2026-08, 2026-03)

### Recipe library (exact, reusable)
- **Apply a design system to an existing Claude Design file** — open the file, plus icon, pick the system, then `Update the website design layout using design system. Hero screen should be full viewport. Add some parallax on scroll animations with pizzas and ingredients.` Gave a full-screen hero, custom cursor, parallax with a tweaks panel. [YT:T96O8dTzi2Q] (2026-08)
- **Claude Design dashboard from a design MD** — claude.ai/design, Prototype tab, high fidelity, no design system, design MD (grids, scales, colors, basic system) in the project folder so we're not going to get the generic Claude style interface; prompt `design a home screen dashboard for a Neo Bank web app. It should include balances, fiat and crypto transactions, currency converter, stocks, ETFs, and anything that you think is relevant. Use UX/UI best practices. Use design MD file for style reference.` [YT:0dj3_i849a4] (2026-06)
- **Claude Design to Figma** — `bring this design to Figma file` plus the share link plus `using html.to.design connector`; options: auto layouts, create styles and variables, hyperlinks and HTML layer names; hover effect off. [YT:0dj3_i849a4] (2026-06)
- **Awwwards-style site (Claude Code, Fable 5)** — short prompt naming business, hero effect and tech, plus a visual reference: `create an awwwards winner top level landing page website for a fashion photographer. Hero screen should include a spiral effect image gallery similar to the one used here on this website. Use three.js and GSAP.` [YT:hNvIan93aPY, YT:BWQ542fvrXo] (2026-08, 2026-07)
- **Figma frame to HTML** — `get the design layout from Figma and convert it into HTML and inline CSS` plus the frame link (copy link to selection, Cmd+L); or `create a design layout from my Figma file using HTML and CSS. Use exact variables, colors, dimensions from the file.` [YT:UiOKZG2XeJY, YT:Xcgr-7LpzDM, YT:V7ZpJLWY-CY] (2026-07, 2026-04, 2025-11)
- **Figma MCP in Cursor to React plus design-system JSON** — select the frame, paste Figma's example prompt, append `implement this design using ReactJS, pay attention to details and variables used in the file, and create a design system file in JSON format to keep future designs consistent` (Sonnet 4.5); then `create a send money screen using design system of the project`. [YT:H6FL3LU-cck] (2025-12)
- **Reference prompts** — screen: `deeply analyze the design layout shown in the attached screenshot. Pay close attention to spacing, fonts, colors, design style, and design principles. Use it as a style reference to create a design layout for a fitness tracker iOS app. Currently, I need the dashboard screen of the app.` Section: `use this reference to update the design of the hero section. Pay attention to details, colors, typography, and styles. make it as close as possible to the reference.` Copy too literal: `update the hero text to the provided text in the structure file.` [YT:SwaxTlY_rZw, YT:OuyGHRwgN_0] (2026-02)
- **Design system from a screenshot (Figma Make)** — `deeply analyze the design of the attached screenshot to create a design system layout of every UI component needed in a design system for SaaS product service. Pay close attention to spacing, fonts, colors, design styles, and design principles.` Order: ChatGPT plans 7 to 8 MVP screens, Pinterest mood board, system, key screen first, refine by hand, then send the refined screen to a new Make chat as the next reference. [YT:tty90cDna3A, YT:OuyGHRwgN_0] (2026-02, 2026-01)
- **Real-flow research (Mobbin MCP, Ask mode)** — `use Mobbin MCP to analyze best practices of logging in flows in, for example, lifestyle apps and profile settings. I need some easy and simple flow using email magic link. Create step-by-step full description to use in my app.` [YT:0ajxdUNacQE] (2026-09)
- **Landing-page chain (ChatGPT 5.2 deep search, then Cursor)** — `create and make a deep research on web design and vibe coding services in New York City. Analyze market demand and offers. Provide me a full deep report in PDF.` Same chat with the PDF: role `You're a marketing and website expert`, CTA `book a free discovery call`; Cursor plan mode: React, Next.js, Tailwind, responsive, `light theme with bright accent colors`. [YT:SwaxTlY_rZw] (2026-02)
- **MagicPath prompts** — wire pages (duplicate first): `when I click projects in the top navigation open the projects page` [YT:1nbkLB_8ZM8]; `add reveal animations to H1 heading on the home screen.` via the animations skill [YT:1d8vM0TXcTo]; components combined via `[@search widget]` and `[@hotel card]` [YT:irQsPKXtsrY] (2026-08, 2026-03, 2025-10)

### Fix library (problem → fix → why)
- **Problem:** generic output → **Fix:** name the style (brutalist, huge icons, huge typography), the typeface (Comic Sans, Poppins, Helvetica), spacing, card corners and the pixel radius → **Why:** agents default to one shared system, mostly shadcn. [YT:BtXCTWXr9mA] (2026-09)
- **Problem:** external agents gave generic (Claude) or glassmorphism (Cursor) screens → **Fix:** attach the Design.md and `update the UI of the screen using the provided design file` → **Why:** MagicPath's own agent matched the system; the others had none. [YT:26QlssTGjU8] (2026-06)
- **Problem:** messy Claude Design to Figma export (tons of tokens, random radii) → **Fix:** supply the tokens file first, then the screen → **Why:** he had asked AI to create the system while designing a screen. [YT:1MdwweKCNwg] (2026-07)
- **Problem:** the agent made a component per menu item → **Fix:** build one menu-link component yourself, have the agent link every item to it → **Why:** links and titles stay editable. [YT:hNvIan93aPY] (2026-08)
- **Problem:** HTML images point to Figma-hosted URLs and break → **Fix:** Figma.To.Code bundles images locally, or keep an assets folder and tell Cursor to use it → **Why:** Figma MCP sometimes links instead of saving. [YT:UiOKZG2XeJY, YT:ip7W-OMaz-c] (2026-07, 2026-05)
- **Problem:** pixel-perfect export locks to the frame width → **Fix:** responsive pass, check each section, `fix it` for what broke. [YT:UiOKZG2XeJY] (2026-07)
- **Problem:** a green override came out black → **Fix:** change the token in the library, publish, pull the update → **Why:** Claude treated the override as a mistake against the token. [YT:Xcgr-7LpzDM] (2026-04)
- **Problem:** generated page did not bind the file's variables → **Fix:** `apply all the variables to this design`, or by hand in about 5 minutes. [YT:YdS4igzQ7AM] (2026-05)
- **Problem:** thin sitemap (home, about, classes) → **Fix:** regenerate asking for 10 to 15 pages (it overwrites), then edit by hand → **Why:** page and section counts size the project. [YT:ip7W-OMaz-c] (2026-05)

### Tool and model notes (dated, newest first; these age fast)
- **Model picks (2026-09)** — Fable 5.1 (2026-09-25) built a working SaaS MVP from one prompt, impressive but generic; Sonnet 5 for analysis, Opus 5 high effort for screens; in Cursor the newest Grok or Composer 2.5 ("really cheap", mostly like Opus, very fast). [YT:8wsjt6IlxBw, YT:ScsjVpmhpyc, YT:0ajxdUNacQE] (2026-09)
- **Relume 2.0 (sponsor, 2026-09)** — human-made component library plus AI; sitemap overview first; Publish replaces export; launch-fix agent gave Lighthouse 93 performance, 100 best practices, 92 SEO. [YT:6tvOaRsKShQ] (2026-09)
- **Claude design skill (2026-09-05)** — Code mode with a folder connected, slash design; real UI and design systems on a Figma-like canvas (type, composition, spacing editable); artboards export PNG or HTML. [YT:ScsjVpmhpyc] (2026-09)
- **Mobbin MCP (sponsor)** — 600,000+ screens, 1,500 apps, 300,000+ flows. Claude app: Settings > Connectors > Mobbin > authorize; Claude Code: paste the command from Mobbin profile > MCP; Cursor: marketplace plugin. [YT:8wsjt6IlxBw, YT:ScsjVpmhpyc, YT:0ajxdUNacQE] (2026-09)
- **Claude Design (desktop app, 2026-08)** — templates exist, but his baseline used none; its design-system creator is "perfect and the best ones"; he hit his limit mid-session and spends about 80% of his time in Cursor. [YT:T96O8dTzi2Q] (2026-08)
- **Fable 5 (week of 2026-07-05)** — fashion-photographer site from one prompt in about 30 minutes, zero fixes; effect-heavy prompts burn usage limits; a developer needs a day or more for the GSAP parts. [YT:BWQ542fvrXo, YT:hNvIan93aPY] (2026-08, 2026-07)
- **MagicPath 2.0 (2026-06)** — humans and agents on one canvas; external agents burn no MagicPath tokens; visual edits (select all H1s: size 52, letter spacing minus 4); he calls it the best AI tool for web design. [YT:26QlssTGjU8, YT:1d8vM0TXcTo] (2026-08, 2026-06)
- **Figma.To.Code and html.to.design MCP (Div Riots, sponsor)** — Figma.To.Code has its own engine, no AI, zero tokens, HTML with inline styles or Tailwind; html.to.design MCP imports in seconds with variables and auto layouts; Figma MCP in his experience was slow, with variables and auto layout not set up properly. [YT:UiOKZG2XeJY, YT:0dj3_i849a4] (2026-07, 2026-06)
- **Framer 3.0 (sponsored, 2026-07)** — agents mode, branches on Pro, external agents spend your Cursor tokens; Framer's free AEO checker scores four areas and gives no fixes. [YT:eT0fZ8XsAaY, YT:YOzZYjpRSbM] (2026-07, 2026-06)
- **Claude Code for designers (2026-03, 2026-04)** — terminal, Cursor extension or the app's Code tab (his pick for visuals), paid plan; he hates the terminal but says designers must know it. [YT:FqQMIQRcdj8, YT:V2Bjb6VtHeA] (2026-04, 2026-03)

### Coaching and critique moves
- **Cost-to-the-user walk-through** — compare versions screen by screen, naming what each costs the user (extra clicks, information not needed, covered content, missing customization) before judging looks. [YT:8wsjt6IlxBw] (2026-09)
- **Name the AI tells, then ask what drives the decisions** — gray 1px strokes on every border, the same corner rounding everywhere, beige palettes (Claude especially), standard tab and button styling; nothing drives the decisions, so the model falls back on a generic UI kit. On a serious site: borders off, radius zero. [YT:8wsjt6IlxBw, YT:6tvOaRsKShQ] (2026-09)
- **Compare three variations on the canvas** — his verdict on A: "too clean," too much white; he preferred the black one and liked its green last slide even more. [YT:ScsjVpmhpyc] (2026-09)
- **Read the generated prompt before running it** — he added the missing remove-expense-row ability and deleted a currency note. [YT:UIPudlTEgQg] (2025-12)
- **Teaching moves** — open with the problem ("AI generated websites still look AI generated"), change one variable, show before and after, narrate "this is what I like"; explain each generated file in one line (HTML skeleton, CSS styling, JS functionality) and tell non-coders to agree to the agent's steps and wait; explain settings by photographer analogy (dispersion as cheap-lens chromatic aberration). [YT:8wsjt6IlxBw, YT:yNXbWGcQXs4, YT:2P-ls1jVIJ4] (2026-09, 2025-10)

### Numbers they have stated
- Fable 5 sites took about 30 minutes each; the NYC-studio site needed about 32 more for one fix round; his intro claims under 20 minutes per site. [YT:BWQ542fvrXo] (2026-07)
- Claude Code (Sonnet 4.6) on a Figma link: about 3 minutes, roughly 3,000 tokens by 1:25, 3% of session usage; Figma.To.Code: seconds, zero tokens. [YT:UiOKZG2XeJY] (2026-07)
- One Claude Code Figma prompt used 30% of a Pro session (similar tasks 12 to 15%); by hand it takes him 20 to 25 minutes; he suggests Max for whole pages. [YT:V2Bjb6VtHeA] (2026-04)
- Claude Design ate his daily and weekly limits in about 10 minutes; the same UI kit cost Nodey about 20 credits, which he guesses is 20 to 30% of a daily limit. [YT:YdS4igzQ7AM] (2026-05)
- The loop takes 15 to 20 minutes, an hour, or a few hours; the pizza example saved about one to two days of prep and design. [YT:BtXCTWXr9mA] (2026-09)
- Hourly rate: $7,500 a month over 160 hours is about $46 an hour; margin 50% + buffer 10% + tax 16% = 76% uplift, about $82.50 (margin usually 20 to 50%, buffer 10 to 30%). [YT:6JGAxnko89w] (2025-12)
- More than 10 years as a professional photographer. [YT:OuyGHRwgN_0] (2026-02)

### References they cite
- Mobbin, Pinterest, Dribbble — inspiration: Mobbin for real flows, Pinterest for mood boards; borrowing an unrelated industry's look (an electricity company's for a bank) is fine. [YT:BtXCTWXr9mA, YT:ScsjVpmhpyc] (2026-09)
- Dieter Rams' radio, the iPod, Renaissance painters sharing techniques — his case that copying working patterns is normal and copying pixels is plagiarism. [YT:BtXCTWXr9mA] (2026-09)
- shadcn — the default look every agent falls back on. [YT:BtXCTWXr9mA] (2026-09)
- Atomic design — capture small parts (a song card, a header strip) and recompose. [YT:6FtDQQMEtpQ] (2025-11)
- Tailwind-style 100 to 900 colour names; the Type Scale web tool (base 16, major third, weight 500, line height 1.6, pixels), rounding 61 to 64, 39 to 40, 31 to 32. [YT:tvObuIcAooE] (2025-10)

### Evolution and contradictions
- **Figma to code** — 2025-11: Cursor with Figma MCP beats Figma Make because it reads the real file, yet Make did not lose on a big dashboard and on really complex designs "didn't work with them at all" [YT:V7ZpJLWY-CY]. 2026-03: MagicPath's Figma import matched about 98 to 99%, better than he got through MCP in Cursor [YT:1nbkLB_8ZM8]. 2026-06: Figma MCP is slow, variables and auto layout not set up properly; html.to.design MCP is far faster [YT:0dj3_i849a4]. 2026-07: LLMs were never designed to read designs through screenshots, URLs and Figma connections; for plain HTML an exporter beats an agent [YT:UiOKZG2XeJY].
- **Prompting** — 2025-10: designers should not spend hours texting prompts [YT:l68HFQV5RJU]; 2026-09: shipping a tiny prompt's first output is not professional and the real loop is prompt, review, critique, iterate [YT:BtXCTWXr9mA], while the Relume pitch promises no endless AI prompting [YT:6tvOaRsKShQ].
- **Prompt length** — detailed prompts win (2026-04 [YT:V2Bjb6VtHeA]), yet Fable 5 got a site from a very short prompt plus one reference (2026-08 [YT:hNvIan93aPY]) and Firefly a tiny prompt steered by chips (2023-10 [YT:2GhKWD_NzPQ]).
- **Claude Design** — 2026-05: ate his limits in about 10 minutes [YT:YdS4igzQ7AM]; 2026-08: its design-system creator is "perfect and the best ones", yet about 80% of his time is in Cursor [YT:T96O8dTzi2Q]; 2026-09: the design skill runs in Code mode [YT:ScsjVpmhpyc].
- **Labels that differ inside the input** — one video names Fable 5 (low effort) for V1 and Fable 5.1 (2026-09-25) for the one-prompt MVP [YT:8wsjt6IlxBw]; Fable 5 is the week of 2026-07-05 in one video, just out in 2026-08 in another [YT:BWQ542fvrXo, YT:hNvIan93aPY].
- **His role** — 2024-10: "web design becomes more about engineering" [YT:NUtB0Ri4f_w]; 2025-10: designers will be more like engineers and stop waiting for a front-end developer, while he does not code himself [YT:PPqt_xLg_5c]; 2026-07: he goes from Figma or straight to Cursor without asking a developer [YT:BWQ542fvrXo].

### Signature lines (verbatim, ≤15 words)
- "where are the design decisions coming from? Nowhere." [YT:8wsjt6IlxBw] (2026-09)
- "When AI doesn't have the system to follow, it invents one." [YT:1MdwweKCNwg] (2026-07)
- "The truth is the tool isn't the problem. The input is." [YT:tty90cDna3A] (2026-01)
- "We are asking you to research, learn, and then design." [YT:8wsjt6IlxBw] (2026-09)
- "AI doesn't have the taste that you have." [YT:BtXCTWXr9mA] (2026-09)
- "the difference wasn't just a better prompt. It was the design process." [YT:T96O8dTzi2Q] (2026-08)
- "designers will be more like engineers" [YT:PPqt_xLg_5c] (2025-10)
