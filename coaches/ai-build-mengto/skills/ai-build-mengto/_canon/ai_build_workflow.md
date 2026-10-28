# Briefing and steering AI to build — how Meng To does it
> Sources: [YT:<id>] = YouTube video id; (YYYY-MM) = upload month; "mentions" = number of separate evidence items. Tool and model facts age fast: always say the date.

## PART A. Briefing and steering AI to build: prompts, references, design systems, workflow

### Rules (ranked by how often they say it)
- **Give the model a reference or real code, never a blank prompt** — "Build me a website" is hit or miss; a screenshot, URL, template HTML or component code carries more than words (best: image plus its HTML plus prompt-builder terms). Paste working source from anywhere, even another language; snippets with step 1-2-3 comments keep animation consistent. [YT:7MEsUtvEbyU, YT:dXdxVi6Qz6k, YT:M4DNgmI7MIM, YT:ebnUPRhfctc] (2025-10, 2025-11, 2026-06) · mentions 17
- **Start from something that exists** — Remix a template, copy a component's code or reuse your own past work; a remix starts from real code, a design system and Tailwind colours, so edits are more precise. [YT:eQFAo9z24FM, YT:NhHfI47WQDM, YT:Fs-nfTiWzvg] (2025-10, 2026-07, n.d.) · mentions 15
- **Name the technology, the effect and the part** — "HTML is just the wrong technology to draw a house." Say Three.js, shaders, transparent PNG, parallax, border beam, mask reveal, delay steps, slide from/to; vague words return the baseline. [YT:PA3f3MdRc08, YT:Fs-nfTiWzvg, YT:YhL3BHS5sGU] (2025-10, 2026-07, 2026-09) · mentions 15
- **A reference is a starting point to push past** — Change names, numbers and brand; swap technology or theme (cartoon to 3D, HTML to Three.js); credit the source. His Japanese page began as a replica and ended 0–10% similar. [YT:G-F5Qvy-7KM, YT:HO2a_BTx12k, YT:ItsKfNAoqTU] (2025-10, 2026-01, 2026-09) · mentions 15
- **Build it adaptive from the start: auto layout and stacks, fill or hug, min and max** — Frames not groups; fill all the way up to the outermost parent, the only fixed one; text that may wrap must fill; prefer fill/fit with min and max over breakpoint overrides; fix one container at a time from the smallest up. [YT:pZcwsjY81hA, YT:9nIwTjG2fdI, YT:AtoweRknIKA, YT:_Lqa5o4gKJI] (2024-10) · mentions 15
- **Colours and spacing live in tokens, in three layers** — Primitives (colour ramps 50–900, 4/8-point spacing) set once and unticked from the pickers; semantic tokens (foreground, background, container, border, divider, button states; brand primary only for selected state or call to action) carry light and dark values; components use only semantic. Variables flip with mode, colour styles hold gradients. [YT:pZcwsjY81hA, YT:AtoweRknIKA, YT:jts39CN4fLk, YT:9Ze0Lfx-8qY] (2024-10) · mentions 15
- **Direct the agent like a senior designer; taste is the input** — "You're relying on your taste more than on your execution ability": generate many, pick by taste, expect early mistakes, keep steering with references to verify against. [YT:WrlZlQVfL9Y, YT:HO2a_BTx12k, YT:PA3f3MdRc08] (2025-12, 2026-01, 2026-09) · mentions 14
- **AI builds the boring ~90%; you spend the last ~10% by hand** — Fonts, weights, colours, backgrounds, images, avatars, library buttons. [YT:lgqnMzOu2Lw, YT:jyfOAoMnxbY, YT:dXdxVi6Qz6k] (2025-10, 2025-12) · mentions 13
- **Hand the agent a design system; use design.md and HTML together** — design.md is foundations only (colours, type); HTML is prescriptive (animations included). design.md alone can leave a bare hero or pricing weak, and it needs a strong model. A blueprint prompt (markdown, "HTML but in a form of a prompt") gives a different result, so try both. [YT:M4DNgmI7MIM, YT:LfgMBy0auL8, YT:OZaE5ZezjYs, YT:SznrOQYiahg] (2026-05, 2026-06, 2026-07, n.d.) · mentions 13
- **One change per prompt; fix two-second things by hand** — "too much information is too much information"; for dark mode say only dark mode; select the element and prompt there for more control and less creativity; rename, delete or set a Tailwind height yourself. [YT:M-uUFLU9IFU, YT:jyfOAoMnxbY, YT:eQFAo9z24FM] (2025-10, 2025-12) · mentions 12
- **Say what to keep and what to take** — `adapt`, `it's used as a reference`, `keep the hero`, `don't change anything else`, `keep everything`; else a referenced style overwrites your content or font. [YT:T1WTGQesbrE, YT:HO2a_BTx12k, YT:jyfOAoMnxbY] (2025-12, 2026-01, 2026-06) · mentions 10
- **One section at a time, hero first** — Polish the hero; its language carries to later sections via `adapt`. Whole-page screenshots were his old mistake (the AI cannot tell what to take); whole page at once only for a holistic feel. [YT:lgqnMzOu2Lw, YT:b-kTkak2FKs, YT:u5q8-fFmGtA] (2025-10, 2025-12, n.d.) · mentions 10
- **Make the agent verify and score itself; testing is tasting** — Append `self-verify until it's perfect`; have it score each element out of 10 (it starts at 4–5), push to 8 or 9; you taste and report. [YT:PA3f3MdRc08, YT:u5q8-fFmGtA, YT:KOZjqVNHIo8] (2026-09, n.d.) · mentions 10
- **Slop is vague or rushed input** — "the less time that you spend on something, the more it becomes AI slop"; low and medium effort mean less research, so "Extra is my bare minimum". [YT:G-F5Qvy-7KM, YT:M4DNgmI7MIM] (2026-06, 2026-09) · mentions 9
- **No perfect prompt, no one-shot** — "there's no such thing as a perfect prompt"; each launched project took at least 10,000 prompts (his figure), a Three.js run 1–2 hours. [YT:hSSxuO6GdcE, YT:SznrOQYiahg, YT:PA3f3MdRc08] (2025-10, 2026-09, n.d.) · mentions 9
- **Screenshot first (~90% of prompts), annotate, dictate** — Cmd+Shift+4 into the thread, 5–10% annotation, the rest voice (Whisper Flow), 3–5x faster than typing. [YT:u5q8-fFmGtA, YT:SznrOQYiahg, YT:PA3f3MdRc08] (2026-09, n.d.) · mentions 9
- **One thread per task; lean context; save points** — New chat per task, shared rules in a Project or agents.md, commit before experiments; every request re-reads the chat or codebase. [YT:YhL3BHS5sGU, YT:hSSxuO6GdcE, YT:AQrnwXd1l0o] (2025-10) · mentions 9
- **Start tiny and decompose; function first for products** — List ingredients instead of `build a video editor`; one capability per prompt, aesthetics last. [YT:6t0_KEchMUk, YT:SznrOQYiahg] (n.d.) · mentions 9
- **Parallel threads, one project = one folder, single HTML file** — An HTML folder of experiments lets the agent see past work; without `single HTML file` Claude defaults to React. [YT:PA3f3MdRc08, YT:G-F5Qvy-7KM, YT:KOZjqVNHIo8] (2026-09) · mentions 8
- **Learn some code and the vocabulary** — "maybe you should learn code, right? It's not that big of a deal." Know hero, div, footer, Tailwind and part names. [YT:7MEsUtvEbyU, YT:HO2a_BTx12k, YT:YhL3BHS5sGU] (2025-10, 2025-11, 2026-01) · mentions 8

### Methods (named or ordered)
#### Reference ladder (what to feed the agent, best first)
- When they use it: choosing the input for any build.
- Steps: 1. S tier: a URL carrying a GitHub repo with prompt, demo, technologies, references. 2. A plain URL. 3. A screen-recording video. 4. A screenshot. 5. Last, a hand-written prompt ("who does that nowadays").
- Sources: [YT:lPtf_-J75Sk, YT:G-F5Qvy-7KM] (2026-08, 2026-09)

#### Plan-first reference mixing (Mobbin connector)
- When they use it: new site, strongest agent, no design yet.
- Steps: 1. Install the Mobbin connector (needs Mobbin Pro). 2. `give me the top five websites from Mobbin for a solar panel website`, and demand screenshots or you get only links. 3. Name one base site (`use the inspiration from Daylight`) and mix sections from others. 4. Ask for 5–10 sections and `let's plan that first`. 5. The agent returns sections, build order and questions (brand, map region, photo type). 6. Steer, then self-verify.
- Sources: [YT:PA3f3MdRc08, YT:u5q8-fFmGtA] (2026-09, n.d.)

#### Screenshot skeleton (hero first)
- When they use it: starting from a favourite site or Dribbble shot.
- Steps: 1. Screenshot the hero only. 2. `change the text, the names and the numbers`. 3. `use exactly the UI structure`. 4. `animate the details`, naming each effect (mesh gradient, beam animation, mask reveal, blur in, fade in). 5. Mark images as reference, not asset; say `adapt`. 6. Set icons and logos: `use Iconify Solar and use the SVG logo monotone` (Iconify Simple Icons for named logos). 7. Mold: colours, light mode, serif, new concept.
- Their example: `create a hero section, change text names and numbers. use Iconify Solar and use the SVG logo monotone`; 2025-10 version: after the screenshot he always added `add details`, `change the names`, `use Lucide icons`, `make responsive`.
- Sources: [YT:DsjEI6-5kgI, YT:T1WTGQesbrE, YT:HO2a_BTx12k, YT:ItsKfNAoqTU] (2025-10, 2026-01, 2026-05, 2026-06)

#### Prompt builder vocabulary (Aura)
- When they use it: starting a page or section without the words for it.
- Steps: 1. Layout type (hero, feature section, mobile or web). 2. Layout configuration (table, sidebar, bento, feature focus, split). 3. Framing (card, frame, browser). 4. Styling (flat or outline, glass, light or dark, colours, border, shadow), then typeface. 5. One custom line, e.g. `create a nice landing page for a design studio called relay`. Skip colours, shadows and borders if unsure.
- Their example: feature section, bento, card, glass, light mode, large shadows, Instrument Serif, on Claude 4.
- Sources: [YT:M-uUFLU9IFU, YT:lgqnMzOu2Lw, YT:NhHfI47WQDM] (2025-10, n.d.)

#### Scoring loop plus self-verify (from his game development)
- When they use it: 3D or effect-heavy builds; the first output is always basic.
- Steps: 1. Starter prompt at extra effort. 2. Ask the AI to score every element (each 3D scene, background, object) out of 10. 3. Keep it working to 8 or 9, with before/after screenshots. 4. Steer with concrete asks: `increase the resolution, textures and lighting`, not pixelated for Retina; footer taller, show the sun, more contrast. 5. Then animate element by element when scrolled into view. 6. Spare threads: logo, brand guide, ads.
- Sources: [YT:PA3f3MdRc08, YT:u5q8-fFmGtA] (2026-09, n.d.)

#### Single-prompt template (from his tweet; use if results are weak)
- Steps (blocks in order): 1. the 3D scene. 2. theming and visual style. 3. specifics, decorations, ornaments. 4. requirements (game: no text in the scene; website: typography, visual hierarchy, colours). 5. details. 6. quality (performance, Retina, smooth interactions). 7. `use the most appropriate skills and tools and libraries and techniques`, without naming them. 8. browser testing in a loop, verify against references, brief reply.
- Sources: [YT:PA3f3MdRc08] (2026-09)

#### Choose the look first, then build (Diff UI to Codex)
- When they use it: a strong but slow model (GPT-6 Astra) builds the site.
- Steps: 1. Brainstorm many image versions in a fast tool (hero, sections, logo, cards, buttons, footer). 2. Pick a direction. 3. "copy for agent" per section. 4. New Codex thread in the HTML folder; paste (it starts `create a web page implementation from the following instructions`); add steering on technology. 5. `self-verify until it's perfect`.
- Sources: [YT:KOZjqVNHIo8] (2026-09)

#### Five-part anti-slop method
- When they use it: any first generation.
- Steps: 1. Know each model's strengths and weaknesses. 2. Always give an image or URL. 3. Never prompt without a skill or design system. 4. Standing rules in agents.md (minimal: browser, style). 5. Keep names of the problems (menu, selected state, lights, dark/light mode) to prompt them away. Tells (bundle highlight): uneven selected borders, caps eyebrows, status chips, random lights, purple gradient, default font.
- Their example: baseline to avoid: `Create a beautiful landing page in dark mode.`
- Sources: [YT:M4DNgmI7MIM] (2026-06)

#### AI as a camera: mood-board, then mold
- When they use it: turning a replica into something original.
- Steps: 1. Replicate the reference. 2. Grow vocabulary and taste; test where the AI struggles. 3. Never be happy with the reference: ask for prototypes of typography, layout, colours, text, styling, borders; pick one; `make these changes permanent`; then images, light/dark, textures. 4. Swap technology or theme under one unifying theme. 5. Let the agent act as art director; approve by taste.
- Sources: [YT:G-F5Qvy-7KM, YT:PA3f3MdRc08] (2026-09)

#### First-principles decomposition (new product)
- When they use it: a complex product (video editor) from nothing.
- Steps: 1. List the ingredients as keywords (timeline, player, drag and drop, screen recording, inspector). 2. First 10 prompts, one capability each: player, timeline with clip, upload, multiple videos, drag and drop, audio timeline, text timeline, background frame, gradient, custom colours, video background, zoom. 3. Atomic flow per feature: modal records, file saves to cloud, saves into state, state feeds player, wire into master file, sync, export includes it. 4. Correct what comes back.
- Their example: endorses Ridd's point that this atomic breakdown is how engineers think and designers can too.
- Sources: [YT:6t0_KEchMUk] (n.d.)

#### Adapting a design into a design system (Figma tokens, 2024-era)
- When they use it: bringing an existing design under tokens.
- Steps: 1. Drag the design into the system file. 2. Typography first. 3. Colours as light/dark variables. 4. Later gradients, shadows. 5. Auto layout. 6. Extract components once the vibe is settled. Token layers: see the tokens rule.
- Sources: [YT:pZcwsjY81hA, YT:AtoweRknIKA] (2024-10)

### Recipe library (exact, reusable)
- **Starter for any URL** — `recreate this in a single HTML file. Self-verify until it's perfect.` Run at extra effort; one file is manageable and drags into any project; `self-verify until it's perfect` alone makes the agent work as hard as possible. Variant: `Recreate this entire thing in HTML in one single file.` [YT:G-F5Qvy-7KM, YT:lPtf_-J75Sk, YT:PA3f3MdRc08] (2026-08, 2026-09)
- **Constraint block (what the AI may use)** — 3D (Three.js) for buildings, phones, landscapes, backgrounds, no human characters; real people via an image-generation MCP or Higgsfield; logos and ornaments as transparent PNG layers; icons from Iconify "Solar Duotone", not drawn from scratch. [YT:PA3f3MdRc08] (2026-09)
- **3D landing-page briefs** — Solar (spoken): hero without giant text but a floating menu; lines and grids express the solar panels; whole home in 3D in Three.js; charts in 3D; Japanese style, brand Sunset; falling sakura, light god rays; beige light background alternating with dark sections. Card game (typed in Codex): single HTML file; Three.js 3D cards; every layer separate (cards, backgrounds as transparent PNGs, landscape, columns); depth, normal and roughness maps; end with self-verify. Keep/drop: `make the cards float`, drop the platforms, keep columns and landscape. [YT:PA3f3MdRc08, YT:KOZjqVNHIo8] (2026-09)
- **Reference prompts** — `Use the inspiration from Daylight and create a landing page that mix between sections ... Give me five to 10 section for the landing page and let's plan that and give me the screenshots`. Dragged screenshots: `make sure that you're not using it as an asset right now. It's used as a reference.` then `add these two sections and I want you to adapt to the content of the website.` [YT:u5q8-fFmGtA, YT:T1WTGQesbrE] (2026-06, n.d.)
- **Detail prompts and one-liner remixes** — `add vertical container size lines`, 01/02/03 step numbers, `add a one pixel beam animation that continuously goes around the button shape and the button is a pill shape`, `add noodles to connect with the circle`, `animate fade in blur in`. Remixes: `blue colors`, `light mode`, `purple and blue`, `add dividers`, `add frame layout corners`, `add social proof`, `add beam animations vertical`. [YT:HO2a_BTx12k, YT:LfgMBy0auL8] (2026-01, 2026-05)
- **Aura one-prompt checklist** — design system (fonts, spacing, motion, light/dark); sections (hero, features, testimonials, pricing, trusted-by logos, contact form, story, footer); animation (rich interactions, smooth scroll); polish (responsive; SVG logo only for the brand logo; an awards-site reference; images instead of plain colours or gradients; beautiful shadows); icons other than generic Lucide; then the product; paste design.md plus HTML. [YT:M4DNgmI7MIM] (2026-06)
- **Style-transfer JSON** — copy a template's HTML into Gemini AI Studio: `give me the JSON format of the styles of this design. So think design system`, listing fonts, colours, spacing, shadows, animation, layout, button styles, keyframes, icons; paste back with `adapt to this style`. Third attempt (caught the button too) looked best. [YT:jyfOAoMnxbY] (2025-12)
- **design.md from your own design** — export HTML, give to ChatGPT: `turn this into a design.md. A design system which includes the typography, the colors, and all the design system that you can think of`. Spec sections: overview, colours, typography, buttons, icons, spacing, elevation and depth, shapes, do's and don'ts, tokens. With both files, HTML is the reference and design.md the foundation. [YT:M4DNgmI7MIM, YT:LfgMBy0auL8] (2026-05, 2026-06)
- **Section swap and library variants** — `I want to replace this section of a screenshot into the design of this HTML`, then `adapt the content to fit it`; for a hover effect name the variants: `I want mono, and I want pulse outside`. After a swap add per-section text, left/right navigation, blur, scene transitions, hover. [YT:Fs-nfTiWzvg] (2026-07)
- **Brand guide thread** — `Build a beautiful brand guide for the <project> website. One page that collects every brand asset, documents the design system and same standard as a site: premium award level Japanese craft details`; show the process to the client, it is what makes a $10,000 site sellable. [YT:u5q8-fFmGtA] (n.d.)
- **Framer layout numbers** — Breakpoints 1200 desktop / 810 tablet / 390 phone (desktop changes cascade down, phone never up). Hero as a stack: padding 100 (top/bottom 140), gap 40, side padding 40 tablet and 20 phone, text stack fill plus max width 510 px (type px, not %). Bento: grid max 1000, section padding 40 / 30 / 20, gap 30 / 20, phone a vertical stack, cards fill. [YT:9nIwTjG2fdI] (2024-10)

### Fix library (problem → fix → why)
- **Problem:** model draws a house in HTML/CSS → **Fix:** name the technology per element (Three.js houses and phones, image generation photos, transparent PNG ornaments, shaders effects) → **Why:** unsteered it defaults to HTML. [YT:PA3f3MdRc08] (2026-09)
- **Problem:** GPT image 2.5 clones the screenshot → **Fix:** say up front no same model or colours and the logo must differ: `recreate it as a neo classical landing page inspired by Shopify winter edition landing page` → **Why:** otherwise a clone. [YT:KOZjqVNHIo8] (2026-09)
- **Problem:** illustration where a photo belongs → **Fix:** `I don't want any illustration. I want to use images instead for the hero and for the third section.` → **Why:** else letters, plain colours or gradients stand in; for a text-heavy first pass ask `I want more images in the layout`. [YT:M4DNgmI7MIM, YT:T1WTGQesbrE] (2026-06)
- **Problem:** pricing section does not match the page → **Fix:** a Mobbin pattern as reference: `adapt this design into my design. Replace the pricing section and turn this into dark mode for this section.` → **Why:** a screenshot alone is not enough; prompt away or edit the stray gradient. [YT:M4DNgmI7MIM] (2026-06)
- **Problem:** hero title overlaps the image; background video not interactive → **Fix:** `In the hero section, I want the title to not be overlapping with the image. And the same with the description. Also, I want the image to be interactive.` (hover plays the video) → **Why:** a background video is not interactive by default; he used Gemini 3.5 Flash or GPT 5.5 (not guaranteed) and prefers 3.1 Pro over the faster 3.5 Flash for builds. [YT:T1WTGQesbrE] (2026-06)
- **Problem:** AI changes more than asked or skips text edits in a multi-task prompt → **Fix:** `don't change anything else`, `keep the hero`, `keep the navbar the way it was`; for one small region `don't change too much. Just correct the design and make sure that it's more together.`; Edits mode for small tasks, default mode to regenerate and clean the code → **Why:** negative instructions bound the change. [YT:HO2a_BTx12k, YT:KOZjqVNHIo8, YT:7MEsUtvEbyU] (2025-11, 2026-01, 2026-09)
- **Problem:** referenced style overwrites your content → **Fix:** `keep everything`, `keep all the style, shadows, layout, animations`; take only the content from the previous HTML; say you want only the technique, colour or shadow → **Why:** the model follows the reference. [YT:jyfOAoMnxbY] (2025-12)
- **Problem:** reference button or font collides; Lovable drops your font → **Fix:** `I want this button to replace this blue button here`, `I want all the font to be the same one as the hero`, `update the entire landing page to the font in my HTML that I shared here` → **Why:** tools adapt to their own style by default. [YT:WrlZlQVfL9Y, YT:NhHfI47WQDM] (2025-12, n.d.)
- **Problem:** inconsistent animation after adding sections → **Fix:** regenerate the whole page to clean the HTML, test iPad and mobile widths, reference "animate on scroll" and "animate key frame", hand-fix leftovers → **Why:** AI animates differently each time. [YT:b-kTkak2FKs] (2025-12)
- **Problem:** default AI tells (bold titles, loose tracking, Inter, purple) → **Fix (bundle highlight):** semibold, medium or regular weights, tight titles, a different title/body font pair, a non-purple accent, tinted neutrals; replace the single shadow with the layered beautiful shadow (medium, transparent border) → **Why:** Cursor amplifies foundation flaws, so polish the concept first. [YT:dXdxVi6Qz6k, YT:M-uUFLU9IFU] (2025-10)
- **Problem:** the generated file becomes one huge spaghetti file → **Fix:** before it grows, tell the model to turn this animation into a component, this function into a hook, this style into a reusable style, and pass props for customization → **Why:** artifact output defaults to one huge file. [YT:6t0_KEchMUk] (n.d.)
- **Problem:** a screenshot sent with no prompt, Claude only describes it and waits, and may invent names that clash with your code → **Fix:** send it with a written prompt: the task first, then project context, then complex features in smaller steps → **Why:** a bare image gets described, not built. [YT:hSSxuO6GdcE] (2025-10)
- **Problem:** a Figma layout pasted into Framer or Codux looks wrong (lost gradient stroke, broken icons, wrong font, extra spacing) → **Fix:** set a fallback stroke (white at 7% opacity) before copying; copy icons as SVG; compare with Dev Mode CSS and paste it over the plugin CSS; delete `font-family` to inherit the global font; look for max-width 90% on a parent → **Why:** not every Figma option exists in the target. [YT:9nIwTjG2fdI, YT:_Lqa5o4gKJI] (2024-10)

### Tool and model notes (dated, newest first; these age fast)
- **Opus 5 / 5.5 in Claude Code** — runs for hours (still working at 12, 33, 40–44 minutes and 1 hour; pulled 100+ MB of textures itself); inferred stamps and a Japanese mark from his logo with little steering. [YT:PA3f3MdRc08, YT:G-F5Qvy-7KM] (2026-09)
- **GPT-6 Astra, GPT image 2.5 in Codex** — Astra is very smart but slow, error-prone and needs heavy steering, so settle the design in a fast, cheap image tool first; GPT image 2.5 makes the layer images. [YT:KOZjqVNHIo8] (2026-09)
- **Harnesses** — Codex has a GPT image tool; Claude Code or Cursor need an external image tool. A harness has "hands and legs": it dissects a video or drives Playwright on a URL, for more tokens. Permission mode went manual, bypass once, now `auto`. [YT:lPtf_-J75Sk, YT:G-F5Qvy-7KM] (2026-08, 2026-09)
- **Skills** — build your own, do not install downloads (security); "impeccable" is really good and the taste skill is what most people use (2026-06); in `skills.sh` "grill me" is good, "front-end design" used to be amazing but his technique is now more efficient (2026-09). [YT:M4DNgmI7MIM, YT:G-F5Qvy-7KM, YT:ohgPI0NgvwQ] (2026-03, 2026-06, 2026-09)
- **Gemini 3 and GPT 5.1** — Gemini 3 detects fonts from a screenshot and needs Tailwind class and font names; GPT 5.1 is second-best and struggles with floating elements, grids and animations; Gemini took about 3 minutes per generation, Aura about 30 seconds. [YT:b-kTkak2FKs, YT:HO2a_BTx12k] (2025-12, 2026-01)
- **Aura context and modes** — each prompt reads the whole codebase, hence the price and the reference caps (see Numbers); Edits is cheap and changes only what you ask, default regenerates and cleans; Lovable refused over 50,000 characters, v0 and Cursor did not. [YT:WrlZlQVfL9Y, YT:7MEsUtvEbyU, YT:lgqnMzOu2Lw] (2025-10, 2025-11, 2025-12)
- **o3, Claude 3.7 and 4, Cursor agent** — o3 from a screenshot for style and layout, then Claude 4 to complete and fix; each model is trained differently, so switching changes style. Cursor agent mode (Claude only then) found three files itself; 3.7 can run 25 or 50 steps, so keep asks simple; 21st.dev React components hide shadcn imports, single-file HTML translates easily. [YT:dXdxVi6Qz6k, YT:3LFGrI8m3Z8, YT:AQrnwXd1l0o, YT:M-uUFLU9IFU] (2025-10)

### Coaching and critique moves
- Make it score each element out of 10 and refuse a skipped weak one (battery section 3.8). [YT:u5q8-fFmGtA]
- Ask for suggestions, not prescriptions: `what is the best open-source library for video editing that you can start from`. [YT:Fs-nfTiWzvg]
- "how knowledgeable are you of your product?" [YT:SznrOQYiahg]
- "do we really need a new style" before adding any token. [YT:pZcwsjY81hA]
- Let the agent act as art director (`should we model it after this image? Yes or no`); answer by taste. [YT:G-F5Qvy-7KM]
- Find the spark in each reference (a map, networking lines), say what you drop, tie it with one theme. [YT:PA3f3MdRc08]
- Taste the output: `make sure every button works`, `make sure that the flow is not blocked by the UX`. [YT:u5q8-fFmGtA]

### Numbers they have stated
- Each launched project took at least 10,000 prompts [YT:SznrOQYiahg] (n.d.); runs take 1–2 hours, not 5–15 minutes [YT:PA3f3MdRc08] (2026-09).
- AI scores start at 4–5 out of 10; target 8 or 9 [YT:u5q8-fFmGtA] (n.d.).
- Screenshots about 90% of prompts, 5–10% annotation; voice 3–5x faster than typing [YT:u5q8-fFmGtA, YT:SznrOQYiahg] (n.d.).
- Aura reads 1,700 lines per prompt [YT:WrlZlQVfL9Y] (2025-12); $20/month, 100,000-character cap, 50,000 per template (about 1,000 lines), a 79,000-character prompt [YT:7MEsUtvEbyU] (2025-11).
- AI-written code in Dream Cut about 95% to 99% [YT:k2ZxYK2Mgb0] (2025-10); his own share 95% to 0%, about 12 months without touching code [YT:SznrOQYiahg, YT:u5q8-fFmGtA] (n.d.).
- A $10,000 website in about 2 hours of workshop; beginners charge about $500 [YT:u5q8-fFmGtA] (n.d.). Mac app rebuilt in about 24 hours [YT:Fs-nfTiWzvg] (2026-07).
- 90% of his time went into the design system, so the Framer build took minimal effort [YT:AtoweRknIKA] (2024-10).

### References they cite
- Linear, Apple, Stripe, Vercel — named in prompts for minimalism, type and spacing rules (`create a portfolio in the style of Linear`); they "care about the details". [YT:eQFAo9z24FM, YT:AtoweRknIKA]
- Mobbin (shipped designs; agent connector), Dribbble, Layers, Lapa Ninja, CodePen, UIverse, 21st.dev, React Bits, CTA.gallery, H1 Gallery — layouts and section patterns; Dribbble for concept and colour, Mobbin for structure. [YT:DsjEI6-5kgI, YT:HO2a_BTx12k, YT:ItsKfNAoqTU, YT:NhHfI47WQDM]
- getdesign.md (big brands, clean, not the most creative), Aura's design.md library, Google's DESIGN.md spec (one format that moves designs between platforms). [YT:DsjEI6-5kgI, YT:M4DNgmI7MIM, YT:LfgMBy0auL8]
- Design-system models: Figma's variables file, Uber's Base, Microsoft Fluent, Material, Apple Human Interface Guidelines; his own five-year-old course is outdated. [YT:AtoweRknIKA, YT:9nIwTjG2fdI]
- Daylight (map), Origin (charts), Daniel Snow's hero, Trevor Noah's site book section, canvasui.dev cloth effect, a border-beam library by Jacob. [YT:PA3f3MdRc08, YT:G-F5Qvy-7KM, YT:lPtf_-J75Sk, YT:Fs-nfTiWzvg]
- Dieter Rams ("whether I'm inspired by Apple or Apple is inspired by Dieter Rams": taste is choosing the inspiration) [YT:G-F5Qvy-7KM]; Elon Musk's first-principles battery example, and endorses Ridd's atomic-breakdown point [YT:6t0_KEchMUk].

### Evolution and contradictions
- **Prompt length** — 2025-10 one change per prompt, "too much information is too much information" [YT:M-uUFLU9IFU]; 2025-11 used to like short prompts, now giant @-reference prompts [YT:7MEsUtvEbyU]; 2025-12 "the most power is when you give a ton of description in your prompt" [YT:b-kTkak2FKs]; 2026-09 no longer hand-types, dictates long prompts [YT:G-F5Qvy-7KM, YT:PA3f3MdRc08].
- **Reference input** — 2025-10 image plus HTML plus builder terms [YT:dXdxVi6Qz6k]; 2026-01 "A screenshot is worth everything with Gemini 3." [YT:HO2a_BTx12k]; 2026-08 URL with repo beats URL, video, screenshot [YT:lPtf_-J75Sk]; 2026-09 the super prompt is less needed as harnesses read sources [YT:G-F5Qvy-7KM].
- **Icons** — 2025-10 use Lucide in the concept phase [YT:dXdxVi6Qz6k]; 2026-01 Lucide is baseline slop, prefer Iconify Solar [YT:HO2a_BTx12k].
- **Design system** — 2024-10 Figma tokens in three layers with adaptive auto layout [YT:AtoweRknIKA]; 2026-05 design.md is the exact prompt that makes designs consistent [YT:DsjEI6-5kgI]; 2026-06 foundations only, HTML is prescriptive [YT:M4DNgmI7MIM]; 2026-07 a design system for AI is design.md plus the HTML [YT:OZaE5ZezjYs]; n.d. needs a strong model and fades after project start [YT:SznrOQYiahg].
- **Design first or function first** — 2025-12 design before engineering [YT:WrlZlQVfL9Y]; 2025-10 back to Figma because companies have design systems [YT:eQFAo9z24FM]; n.d. skipped Figma for the video editor, function first [YT:6t0_KEchMUk].
- **Scratch** — 2026-07 both "Nothing nowadays is started from scratch anymore." and "starting from scratch is the solution to all solutions."; reconciled: restart the code, seeded from a library or template [YT:Fs-nfTiWzvg].
- **Date tags** — 2024-10 tags the Figma, Framer, Wix and Spline courses (tools of 2023) [YT:9nIwTjG2fdI, YT:RJokEINz76o]; 2025-10 tags videos on o3 and Claude 3.7 and 4 [YT:dXdxVi6Qz6k, YT:AQrnwXd1l0o]; order by model names.

### Signature lines (verbatim, ≤15 words)
- "HTML is just the wrong technology to draw a house." [YT:PA3f3MdRc08] (2026-09)
- "These are your weapons. These are your prompts." [YT:UqKXQR5zcVo] (2026-09)
- "AI needs context. And the context is code." [YT:7MEsUtvEbyU] (2025-11)
- "It's like the midjourney era for web design." [YT:b-kTkak2FKs] (2025-12)
- "You can never do too much." [YT:jyfOAoMnxbY] (2025-12)
- "there's no such thing as a perfect prompt" [YT:hSSxuO6GdcE] (2025-10)
- "Nothing nowadays is started from scratch anymore." [YT:Fs-nfTiWzvg] (2026-07)
- "You are creating an interface for your AI to not create AI slop." [YT:G-F5Qvy-7KM] (2026-09)
- "the design system is what makes a coder" [YT:AtoweRknIKA] (2024-10)
- "Testing is tasting" [YT:u5q8-fFmGtA] (n.d.)
