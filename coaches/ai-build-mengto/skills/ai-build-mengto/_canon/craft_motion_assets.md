# Premium craft — UI details, motion and 3D, images and video for sites (Meng To)
> Sources: [YT:<id>] = YouTube video id; (YYYY-MM) = upload month.

## PART B. Craft that separates premium from generic: UI details, motion and 3D, images and video for sites

### Rules (ranked by how often they say it)
- **One spacing system, held everywhere.** Tailwind 4-pt grid (1 = 4 px; 8, 12, 16 common), one gap repeated (30 title-to-text and text-to-button); iPhone: 16 margin, 24 between groups, 16 inside, 8 in tight cards; bigger text, bigger spacing; inner radius = outer radius minus padding; no decimals in sizes. [YT:9Ze0Lfx-8qY, YT:eQFAo9z24FM, YT:9nIwTjG2fdI] (2025-10, 2024-10) · mentions 14
- **Headings: replace AI's bold and loose tracking.** Semibold or medium (regular or light looks more refined); title tracking `tight` or `tighter` (he trained Aura to do tight); body stays normal. Text is about 80% of the work, so touch weight and tracking first. [YT:lgqnMzOu2Lw, YT:dXdxVi6Qz6k, YT:sFbCP27wFoY, YT:DsjEI6-5kgI] (2026-05, 2025-10, n.d.) · mentions 13
- **Do not ship the default font.** Unspecified, AI falls back to Inter; pick another free Google Font (Geist, Manrope, Space Grotesk, Instrument Serif, Newsreader), set title and body differently, try several until one feels right; a serif title over a sans UI font works, "not hard rules". [YT:M4DNgmI7MIM, YT:HO2a_BTx12k, YT:lgqnMzOu2Lw, YT:NhHfI47WQDM] (2026-06, 2026-01, 2025-10, n.d.) · mentions 13
- **Ask for depth styles by name; AI gives flat.** Glass = white fill about 10% + gradient border (white about 60%) + background blur 10 to 20; outline = very subtle borders on cards and dividers, straight to dark mode. He claims no other UI kit uses gradient borders. [YT:b-kTkak2FKs, YT:M-uUFLU9IFU, YT:9Ze0Lfx-8qY] (2025-12, 2025-10, 2024-10) · mentions 13
- **Kill the purple gradient.** AI goes purple by itself ("definitely not purple"); use amber/orange, emerald/green or blue and optionally tint the neutrals (stone is browner than gray); choose by vibe, which comes from looking at many apps. Premium direction: more monotone, fewer gradients. [YT:M4DNgmI7MIM, YT:lgqnMzOu2Lw, YT:dXdxVi6Qz6k] (2026-06, 2025-10) · mentions 12
- **Motion defaults.** Transitions for hover, keyframes for appear; `ease` or `ease out` for appear, spring only for drag or bounce (never with blur); delays step 0.1 s; appear plays on load so keep it above the fold, scroll-triggered below; CSS keyframes need `forwards`. [YT:M-uUFLU9IFU, YT:9nIwTjG2fdI, YT:_Lqa5o4gKJI] (2025-10, 2024-10) · mentions 12
- **Name the technology per element; never let the model default to HTML.** Procedural Three.js for 3D, `shader` plus `Three.js` for backgrounds (else AI says CSS, which is impossible), image generation for people, transparent PNG for ornaments, Iconify Solar for icons; name a library or paste its code. [YT:PA3f3MdRc08, YT:eQFAo9z24FM, YT:u5q8-fFmGtA] (2026-09, 2025-10, n.d.) · mentions 11
- **Performance is a design rule.** Procedural Three.js scenes weigh about an image (around 500 KB, under 1 MB total) against around 100 MB for video and heavy GLB; use 3D, Spline or Unicorn backgrounds only when optimized and never several heavy ones per page; video only if you can afford the bandwidth. [YT:PA3f3MdRc08, YT:G-F5Qvy-7KM, YT:9nIwTjG2fdI] (2026-09, 2024-10) · mentions 10
- **The background never fights the foreground.** Pick one with empty space under the heading; tune saturation (0 if overpowering), hue, brightness, blur and blend mode (soft light, screen); alpha-mask it so it fades on mobile; position absolute, not fixed, size 800 or 1,000, gray fallback, `pointer-events none` if it blocks; pause animated ones while editing. [YT:b-kTkak2FKs, YT:7MEsUtvEbyU, YT:lgqnMzOu2Lw, YT:dXdxVi6Qz6k] (2025-12, 2025-11, 2025-10) · mentions 10
- **Replace repeated stock faces and broken AI images with unique ones.** Unsplash shows the same faces everywhere and AI leaves broken or low-res images; swap them (Assets panel, Midjourney, GPT image 2, his Aura library). Custom images and video are the only way to elevate a site; in a first draft non-real faces are fine. [YT:T1WTGQesbrE, YT:lPtf_-J75Sk, YT:HO2a_BTx12k, YT:lgqnMzOu2Lw] (2026-08, 2026-06, 2026-01, 2025-10) · mentions 9
- **Slop is the baseline the model ships every time; delete it on sight.** His tells: uneven-border menu selected state, caps eyebrow with wide spacing, needless status chip, "random lights" (hates it most), grey that fights the purple, purple gradient ("very 2025"), default font. Value follows rarity. [YT:M4DNgmI7MIM, YT:Fs-nfTiWzvg, YT:UqKXQR5zcVo] (2026-09, 2026-07, 2026-06) · mentions 9
- **Prompt motion in exact words; AI is less mature at animation.** Name delay, duration, easing, iteration (loop, ping-pong), stagger, direction; use named effects (clip, beam, flashlight, marquee, scroll velocity); reference code snippets, or give a video and ask how to prompt it. [YT:PA3f3MdRc08, YT:jyfOAoMnxbY, YT:M-uUFLU9IFU, YT:u5q8-fFmGtA] (2026-09, 2025-12, 2025-10, n.d.) · mentions 9
- **Ask for separate transparent layers.** Transparent PNGs float over anything (giant type, video), enable parallax and orbit, and replace manual Figma layer work; avoid frame-baked images; do not let AI vectorize a screenshot. [YT:KOZjqVNHIo8, YT:G-F5Qvy-7KM, YT:lPtf_-J75Sk] (2026-09, 2026-08) · mentions 9
- **A generic page "lost its luster" once someone shares the same one.** Add a background and animation as special sauce; what only the 1% did with WebGL is commonplace, so stay a step ahead (next baseline: serif fonts and the same AI animations). [YT:G-F5Qvy-7KM, YT:DsjEI6-5kgI, YT:eQFAo9z24FM, YT:SznrOQYiahg] (2026-09, 2026-05, 2025-10, n.d.) · mentions 8
- **Use Tailwind's scale as the color system.** Steps 50 to 950: about 100 for light backgrounds and 900 for dark (reversed for text), middle shade for vibrant buttons; 80 to 90% neutral, about 10% color for CTAs and attention items; title primary, subtitle secondary. [YT:eQFAo9z24FM, YT:pZcwsjY81hA, YT:9Ze0Lfx-8qY] (2025-10, 2024-10) · mentions 8
- **Set responsive behavior per element; the check is no horizontal scroll.** Look at iPad and phone frames; set min and max on content (text min 280, max 600; iPad text under about 700); hide rather than delete at a breakpoint; wrap oversized decor in an absolute overflow-hidden frame. [YT:HO2a_BTx12k, YT:pZcwsjY81hA, YT:RJokEINz76o, YT:9nIwTjG2fdI] (2026-01, 2024-10) · mentions 8
- **Dark mode comes from semantic variables.** A tint hard-coded to black breaks in dark mode, so use the primary color or Tailwind 100/900 pairs; a white SVG icon gets `filter: invert(1)` in the dark media query; in dark UI prefer outline and glow over drop shadows. [YT:ebnUPRhfctc, YT:_Lqa5o4gKJI, YT:pZcwsjY81hA, YT:M-uUFLU9IFU] (2025-10, 2024-10) · mentions 8
- **Spend the last 10% by hand; details are the filter.** Only 10 to 20% of visitors notice them and they are the buyers; time is not quality; add hand-made flair (a plain background turned into a flag, `ornamental UI`) and avoid cramped sections. [YT:Fs-nfTiWzvg, YT:KOZjqVNHIo8, YT:SznrOQYiahg] (2026-09, 2026-07, n.d.) · mentions 7
- **Buttons get more emphasis than body text.** Medium weight; icon height equals line height (24), gap 8, paddings from spacing variables; tappable icons in 44 by 44 containers, buttons 44 high; normal, hover and active states; base variant has a 0% border so hover fades in. [YT:9nIwTjG2fdI, YT:jts39CN4fLk, YT:9Ze0Lfx-8qY] (2024-10) · mentions 7
- **Shadows: layered, colored, bigger on dark, softer on light.** White shadow with opacity reads as glow, dark as drop shadow; glass buttons stack several; use Tailwind terms (`shadow-2xl`); in dark UI use subtle outlines because shadows vanish. [YT:jyfOAoMnxbY, YT:M-uUFLU9IFU, YT:9nIwTjG2fdI] (2025-12, 2025-10, 2024-10) · mentions 7
- **Frame the UI.** A UI in a card or custom browser mockup with drop shadow "makes it look 10 times better"; turn flat screenshots into perspective or glass 3D mockups; add a background at the end. [YT:M-uUFLU9IFU, YT:HO2a_BTx12k, YT:WrlZlQVfL9Y] (2026-01, 2025-12, 2025-10) · mentions 6
- **Hero first, and most of the time.** About 50% of his time goes to the hero (the social cover); build only the hero first (30 to 60 s per generation vs 3 minutes per page), make several; hero = nav, title, text, CTA plus one animated focus. [YT:HO2a_BTx12k, YT:M-uUFLU9IFU, YT:9nIwTjG2fdI] (2026-01, 2025-10, 2024-10) · mentions 4

### Methods (named or ordered)
#### Level scale for web output
- When they use it: to judge how far a prompt result is from premium.
- Steps: 1. Level 0-1 is a one-line prompt result; level 10 is a landing page like Dia (browser) or Perplexity Comet. 2. To climb, know your prompt, the vocabulary and how the product works as a user (he studies products he personally uses). 3. Look for distinctive fonts, interactions, animation, beautiful buttons and backgrounds, AI images or video backgrounds, sound effects.
- Their example: unattainable without a design team and time, but AI can do some components.
- Sources: [YT:NhHfI47WQDM] (n.d.)

#### Technology per element (3D asset decision)
- When they use it: any hero, scene or ornament plain HTML would draw badly.
- Steps: 1. Split the scene into elements. 2. Procedural Three.js (all in code, part of the HTML, light) for buildings, phones, landscapes. 3. Image generation for people. 4. Transparent PNG layers for ornaments, Iconify Solar for icons, shaders for effects. 5. Characters (a human holding bamboo) cannot be procedural: feed a generated image to Tripo 3D, Meshy or Hyper 3D and name the tool from the start. 6. Blender only for promo videos, Pixar-like characters or 4K textures.
- Their example: a Three.js footer as a sunset water landscape with ripples on mouse-over.
- Sources: [YT:PA3f3MdRc08, YT:u5q8-fFmGtA, YT:KOZjqVNHIo8] (2026-09, n.d.)

#### Anti-slop pass (his checklist order)
- When they use it: after a one-shot baseline build.
- Steps: 1. Title weight, then tracking (text is about 80% of the work). 2. Different title and body fonts. 3. Accent off purple, neutrals tinted. 4. A distinct background and unique images; hand-fix hairline mismatches. 5. Animation last. 6. Save a version.
- Their example: Aura design mode does font pairing, spacing, primary colors, replace-a-color-everywhere, image and icon-set swaps in one click each.
- Sources: [YT:DsjEI6-5kgI, YT:dXdxVi6Qz6k, YT:eQFAo9z24FM, YT:9Ze0Lfx-8qY] (2026-05, 2025-10, 2024-10)

#### Image first, then video
- When they use it: hero backgrounds and scroll transitions.
- Steps: 1. Be sure of the art direction and start with a still (he asked 1080p, painting style, brighter). 2. Approve the stills. 3. Draft the video at 480p (about 10, 20 or 50 cents max) and approve. 4. Upscale to 1080p. 5. Pick loop (heroes usually take a 4-second loop), play once on load, play on hover, or scrub the video with scroll for a transition.
- Sources: [YT:lPtf_-J75Sk, YT:T1WTGQesbrE] (2026-08, 2026-06)

#### Score-and-iterate for a 3D hero
- When they use it: Three.js scenes built by an agent.
- Steps: 1. Put the quality block in the brief (see Recipe library). 2. Ask the AI to score every element out of 10; it starts at 4-5. 3. Keep it working to 8 or 9 as the token budget allows, with concrete asks (resolution, textures, lighting, contrast). 4. Have it self-verify against reference screenshots. 5. Spare threads can make the logo, brand guide and ads.
- Sources: [YT:PA3f3MdRc08, YT:u5q8-fFmGtA] (2026-09, n.d.)

#### Custom shader, or a canvasui.dev effect
- When they use it: an effect that exists nowhere, or one from a shader library.
- Steps: 1. Custom: give a screenshot of the final look (HTML optional for precision). 2. The agent asks which variables to make customisable. 3. Animate with auto-animate. Library: copy canvasui.dev's prompt into the agent, then save each effect as a skill to skip the verify-and-fix loop next time.
- Their example: his Matrix shader; the Blaze effect on cards.
- Sources: [YT:KOZjqVNHIo8, YT:G-F5Qvy-7KM, YT:TGaCyIak-Ak] (2026-09, 2026-07)

#### 3D parallax portal card (Spline)
- When they use it: a 3D card with depth that reacts to the cursor.
- Steps: 1. Background wallpaper or blob. 2. Glass card base rectangle with extrusion and a glass layer. 3. Optional front glass face with a matcap mirror. 4. A cube in the scene background color with a glass layer BELOW its color layer, which hides everything but the card. 5. A 3D icon placed slightly in front.
- Sources: [YT:ixSDNrOM3-I] (2024-10)

### Recipe library (exact, reusable)
- **Starter for a 3D or reference-led site** — paste a reference URL, then `recreate this in a single HTML file. Self-verify until it's perfect`; run at extra effort (his bare minimum; low and medium make slop) and expect 1 to 2 hour runs while you work in parallel threads. [YT:G-F5Qvy-7KM, YT:PA3f3MdRc08] (2026-09)
- **3D quality block (Three.js)** — `amazing textures and high resolution`, `wood has to look like wood`, `Retina-display ready`, `lighting like a AAA game`, `god rays from the background`, `score at least 8/10`; he stacks "a ton of these words" on purpose. Add `orbit on hover` (small rotation, not a full 360) and `rotate on drag`. [YT:PA3f3MdRc08] (2026-09)
- **Layered parallax** — `I want layers that are transparent. I want them in front. I want them to orbit. I want them to have a parallax.` Then background and subject as separate layers (image-gen MCP or Higgsfield) and `I want a parallax effect as I scroll`. [YT:G-F5Qvy-7KM, YT:PA3f3MdRc08] (2026-09)
- **Pokemon-card lighting, no real 3D** — ask for depth, normal and roughness maps on the card layers so rotating moves light across the art; saved as a skill ("sky rays depth map"). Pick the look first as images in Diff UI, then "copy for agent" into Codex. [YT:KOZjqVNHIo8] (2026-09)
- **Aura batch images, then video** — one click generates every image from the site's text (5 to 7 per page) for one prompt; to tweak (make it greener, or ask for beige or sepia to match the palette), edit that image's title (it is the prompt) and redo only it. Video: loop, play once on load or on hover; hero as a 4-second loop, only after the still is right. [YT:T1WTGQesbrE] (2026-06)
- **Nano Banana Pro** — in Aura 2x resolution (2K plenty, 3:4 for Instagram) with `make the bottom half use progressive blur and work as a light background with a dark text possible on top`; batch API at 50% off: `I need to use the batch API and I don't mind waiting longer`, then `please remember the workflow`. [YT:ohgPI0NgvwQ, YT:jyfOAoMnxbY] (2026-03, 2025-12)
- **Unicorn Studio background** — remix a shared project, embed, copy the project ID, paste it over the existing ID in the page code; blend `screen` so grid lines survive; position absolute. [YT:b-kTkak2FKs, YT:lgqnMzOu2Lw] (2025-12, 2025-10)
- **Logo that is not AI-default** — remove AI's icon-plus-text, size 120 by 36 px with Tailwind, pick a library logo for style, make variants in Ideogram (best type) with `change to Aura`, remove the background for a sticky header. [YT:7MEsUtvEbyU] (2025-11)
- **Texture and video backgrounds** — texture image (16:9) with soft light, lower opacity, optional invert; video: Midjourney with the image as start and end frame (loop) and a `slow` motion prompt, paste the URL, soft light, less brightness. [YT:7MEsUtvEbyU] (2025-11)
- **Shader background from React Bits** — copy one (Silk: speed, scale, noise), prompt `create background shader background using Three.js` (say both words; include every file), then `in the hero section, use this shader background`; retry other backgrounds. Name a popular library (`add a Cobe JS globe`) or paste its code. [YT:eQFAo9z24FM, YT:M-uUFLU9IFU] (2025-10)
- **Animation vocabulary** — Gemini 3 list: clip, beam (border beam on a button), intro, flashlight (light follows the cursor on cards), mouse-following border gradient (testimonials), marquee with alpha mask, scroll velocity, preloader. Aura: fade, slide, scale, blur, 3D, pulse, shake, bounce, morph; stagger all-at-once or sequence (about 0.1 s per item). [YT:jyfOAoMnxbY, YT:M-uUFLU9IFU] (2025-12, 2025-10)
- **Scroll animation from snippets** — reference the animation-on-scroll and animation-keyframe snippets, not words; one-shot: paste the landing page image, `create the landing page`, Solar icons, the snippets. Word-by-word blur is one CSS keyframe (blur up/down) as inline style with per-element index and delay. [YT:jyfOAoMnxbY, YT:6t0_KEchMUk] (2025-12, n.d.)
- **Make a copied layout yours** — `I want this to be in green earth tones. I want to change the fonts to be serif. The brand should be Aura.` plus bigger headings and fresh AI images; polish with `add vertical lines container size` and `apply the same drop shadows as the first card`. [YT:M4DNgmI7MIM, YT:jyfOAoMnxbY] (2026-06, 2025-12)
- **Glass numbers (dark UI)** — card: white fill 10%, stroke gradient white (top 0%, bottom 100%), background blur 20; pill nav: black 18%, white border 10%, corner 40; secondary text white 60%. [YT:9Ze0Lfx-8qY, YT:RJokEINz76o, YT:A7qI3HAEu18] (2024-10)
- **CSS appear and hover** — `@keyframes fadeIn` from opacity 0 + translateY(-20px) to opacity 1, with `forwards`; delays 0.1 title, 0.2 subtitle, 0.3 text; hover: 0.8 s `cubic-bezier(0.2, 0.8, 0.2, 1)`. [YT:_Lqa5o4gKJI] (2024-10)
- **Framer motion numbers** — appear: Y 20, opacity 0, ease, delays 0.1/0.2/0.3; hero text: fade 1.5 s at 0, 0.5, 1 s; card hover: scale 1.02, Y -10, bezier 0.2/0.8/0.2/1, 0.8 s; press 0.9; parallax speeds 110 background, 115 card, 120 rings. [YT:9nIwTjG2fdI, YT:RJokEINz76o] (2024-10)
- **Spline settings** — glass cloud: glass (blur 150, thickness 250, refraction 1.08), fresnel dark gray bias 0.14 overlay, matcap screen; particles: sharp emitter (size 224, birth 2000, lifetime 6 s, `dot sharp`, gravity 0.20, curl noise scale 6) plus soft one (size 4, birth 200, `dot blur`); export check: Performance panel (red critical, yellow important, gray housekeeping), under 3 lights, under 3 subdivision levels, no hidden objects or image textures, few material layers, compression with the `performance` preset. [YT:ixSDNrOM3-I, YT:cgovoHOqS3s] (2024-10)
- **Font pairing menu** — Inter (AI default), Geist, Manrope, Playfair (skincare, serif looks), Instrument (Serif), Plus Jakarta, rounded Nunito or Quicksand (kids apps), Space Grotesk or Geist Mono (code, data); set title and body differently. [YT:dXdxVi6Qz6k, YT:sFbCP27wFoY] (2025-10, n.d.)

### Fix library (problem → fix → why)
- **Problem:** AI-generated people look like slop → **Fix:** regenerate the same pictures in Midjourney (fine for a first draft), switch to a drawing or illustration style, or have it collect Midjourney references → **Why:** some image models are worse at people. [YT:PA3f3MdRc08] (2026-09)
- **Problem:** broken, low-res or hidden images and avatars → **Fix:** open the Assets panel and swap one by one from Unsplash (`face`; `headshot` for business-neutral portraits) or Aura's library, or generate in Midjourney and upload → **Why:** AI is poor at images. [YT:HO2a_BTx12k, YT:sFbCP27wFoY] (2026-01, n.d.)
- **Problem:** buttons came out as plain gradients → **Fix:** ask for shaders (a liquid-ish button that turns into a landscape on mouse-over) → **Why:** shaders mean effects like liquid glass and particles, not necessarily 3D. [YT:PA3f3MdRc08] (2026-09)
- **Problem:** 3D looks pixelated on retina screens → **Fix:** add `retina` and high-resolution text to the brief (he made them skills) → **Why:** without it the AI sometimes picks non-retina resolution. [YT:KOZjqVNHIo8] (2026-09)
- **Problem:** `animate letter by letter` ran in reverse with a blending-mode glitch → **Fix:** specify the order (logo first, then text) and fade in plus slide in → **Why:** he could have been more specific about order. [YT:TGaCyIak-Ak] (2026-07)
- **Problem:** static hero photo or boring gradient animation → **Fix:** a Three.js scene (animated, orbiting, interactive); for a 2D-illustration look, the couple as a separate layer above the background → **Why:** photo about 500 KB, scene the same or smaller, video 50 to 100 MB; AI is better at 3D than illustration. [YT:u5q8-fFmGtA] (n.d.)
- **Problem:** flat design screenshot reads as AI slop → **Fix:** run a preset prompt that turns it into a perspective mock-up; give GPT image the flat logo and ask `can you turn that into glass? can you turn that into 3D perspective?` → **Why:** "suddenly it looks so much better". [YT:SznrOQYiahg] (n.d.)
- **Problem:** the result looks like another design → **Fix:** flip a section to light or dark, change the font, use a known palette (earth tone, pastel, off-white). [YT:M4DNgmI7MIM] (2026-06)

### Tool and model notes (dated, newest first; these age fast)
- **Opus 5.5 and Fable** — by 2026-09 consistently best at front-end design and 3D (a cartoony animated scene in code, a custom text effect); weak on humans and animals, so use image generation there; preferred over costlier GPT-6 Astra; Codex has the best harness. Earlier, Gemini 3 was "the midjourney era for web design". [YT:PA3f3MdRc08, YT:b-kTkak2FKs] (2026-09, 2025-12)
- **Seedance 2.5** — a video model that can replace 3D, especially for the hero; video is cheap enough for hero use; many new image models now match GPT image 2. [YT:G-F5Qvy-7KM] (2026-09)
- **Higgsfield (CLI and MCP)** — aggregator that picks the model per task (video probably Seedance, images GPT image 2; models change), also makes 3D and promos; Claude Code has no built-in image generation (Codex does); install by giving the agent the URL; MCP spend is not hidden in the subscription. [YT:G-F5Qvy-7KM, YT:lPtf_-J75Sk] (2026-09, 2026-08)
- **canvasui.dev and shaders.com** — canvasui.dev puts shader effects (water droplets, cloth, flame, snow, glass, rays of light) on the HTML itself via a prompt you paste; shaders.com has an MCP; if MCP setup confuses: `install it for me, authenticate for me, and do everything for me`. [YT:KOZjqVNHIo8, YT:G-F5Qvy-7KM, YT:lPtf_-J75Sk] (2026-09, 2026-08)
- **Aura** — image block presets (article image, YouTube cover, slide deck, landing page) with a taste skill against generic blog art; one-click batch images and loop video for one prompt (he says it is the only AI builder with video); iterate, which stays close, is what he mostly uses. [YT:Fs-nfTiWzvg, YT:T1WTGQesbrE, YT:DsjEI6-5kgI] (2026-07, 2026-06, 2026-05)
- **GPT image 2** — contextual faces and places (a real-looking Montreal location); not perfect, but gives you and the client a direction before real photography. [YT:T1WTGQesbrE] (2026-06)
- **Nano Banana Pro** — reads typography and translucent UI, makes realistic people without finger errors, "way better than Midjourney"; used for site assets, slides, banners, covers and video stills; can place a design in a 3D mockup. [YT:ohgPI0NgvwQ, YT:HO2a_BTx12k] (2026-03, 2026-01)
- **Unicorn Studio** — WebGL, lightweight, interactive on mouse-over, 100+ components in Aura; free as-is, customising or removing the watermark needs Pro. [YT:jyfOAoMnxbY, YT:lgqnMzOu2Lw] (2025-12, 2025-10)
- **Spline** — a favorite (three Design+Code courses); remix a community scene, export a public URL and embed; Pro hides the logo; glTF export drops gradient and glass layers. [YT:9nIwTjG2fdI, YT:ixSDNrOM3-I, YT:RJokEINz76o] (2024-10)

### Coaching and critique moves
- Open a critique with his slop tells: uneven selected-menu border, caps eyebrow, status chip, random lights, mismatched grey, purple gradient. [YT:M4DNgmI7MIM]
- Before any layout ask "what do you want them to feel" and "what do you want them to look at" (the New York parking sign). [YT:AtoweRknIKA]
- Show baseline fade-in text and ask the room "How would you animate this?"; every answer is a prompt, so "please save them". [YT:u5q8-fFmGtA]
- Portfolio red flags: decimals in sizes (the biggest), hidden layers, claiming responsive without auto layout, odd fixed values (141, 29); unnamed layers are not one. [YT:pZcwsjY81hA]

### Numbers they have stated
- Aura image library: 8,000+ own Midjourney generations in 4K [YT:lgqnMzOu2Lw] (2025-10), then almost 22,000 [YT:7MEsUtvEbyU] (2025-11).
- Video about $1 to 2 each; draft at 480p, then 1080p [YT:lPtf_-J75Sk] (2026-08).
- One scene as video about 100 MB, high-res image 1 to 2 MB, procedural 3D about 500 KB; his scenes total under 1 MB [YT:PA3f3MdRc08, YT:G-F5Qvy-7KM] (2026-09); a Spline scene of 37 KB [YT:9nIwTjG2fdI] (2024-10).
- Details are noticed by 10 to 20% of visitors; about 10,000 prompts per big project [YT:Fs-nfTiWzvg] (2026-07).
- Hero title Inter medium 60, tracking -0.04; paragraph minimum 16; line height about 1.5x, 45 to 90 characters per line; page padding 64 desktop, 30 to 40 tablet, 20 mobile; titles 50, 40, 34 [YT:9nIwTjG2fdI, YT:RJokEINz76o, YT:9Ze0Lfx-8qY, YT:_Lqa5o4gKJI] (2024-10).

### References they cite
- Impeccable's AI-slop page — the catalog of clichés to avoid [YT:u5q8-fFmGtA]
- Apple (keynote slides, apple.com, WWDC mesh gradients), Linear, Framer, Stripe, Vercel — bento, outline style, hover curves, mesh gradients, Stripe-like Spline backgrounds [YT:9nIwTjG2fdI, YT:_lsnGyF2WZg, YT:M-uUFLU9IFU, YT:dXdxVi6Qz6k]
- UIverse (simple buttons only), React Bits, canvasui.dev, framer.supply — copy-in buttons, backgrounds and effects [YT:NhHfI47WQDM, YT:eQFAo9z24FM, YT:KOZjqVNHIo8, YT:9nIwTjG2fdI]
- Instagram designers for typography, color and heroes — follow them to upgrade your arsenal [YT:HO2a_BTx12k]

### Evolution and contradictions
- Images: Midjourney library and portraits (2025-10) → Nano Banana Pro "way better than Midjourney" (2026-03) → GPT image 2 for contextual faces (2026-06), yet Midjourney is still named as a fix for slop people (2026-09). [YT:lgqnMzOu2Lw, YT:ohgPI0NgvwQ, YT:T1WTGQesbrE, YT:PA3f3MdRc08]
- 3D: Spline embeds and a 37 KB scene (2024-10) → Unicorn Studio and Spline presets in Aura (2025-10) → procedural Three.js from agents (2026-09); by 2026-05 what only the 1% did with WebGL is commonplace. [YT:9nIwTjG2fdI, YT:lgqnMzOu2Lw, YT:PA3f3MdRc08, YT:DsjEI6-5kgI]
- Video weight: a Midjourney video background is lighter than WebGL or all-code (2025-11) vs video about 100 MB against 500 KB for procedural 3D (2026-09), though video is now cheap enough for the hero. [YT:7MEsUtvEbyU, YT:PA3f3MdRc08, YT:G-F5Qvy-7KM]
- Animation: AI is less mature at animation (2025-10) → Gemini 3 animates from a named vocabulary (2025-12) → `animate letter by letter` still ran in reverse (2026-07) → Opus did a custom text effect effortlessly (2026-09). [YT:M-uUFLU9IFU, YT:jyfOAoMnxbY, YT:TGaCyIak-Ak, YT:PA3f3MdRc08]
- Heading weight: titles medium, semibold or bold, iOS avoids light weights (2024-10) vs regular or even light looks more refined (2025-10). [YT:9nIwTjG2fdI, YT:9Ze0Lfx-8qY, YT:lgqnMzOu2Lw]
- Purple and Inter: a purple easing gradient and Inter titles (2024-10) vs "definitely not purple" and leave Inter (2025-10), purple gradient "very 2025" (2026-06). [YT:9nIwTjG2fdI, YT:lgqnMzOu2Lw, YT:M4DNgmI7MIM]
- Dark-mode shadows: none, because they vanish (2024-10) vs bigger on dark, softer on light (2025-12). [YT:pZcwsjY81hA, YT:jyfOAoMnxbY]
- Slips in the source: hover speed named 0.3 s while his hovers run 0.8 s (2024-10); padding 6 called 30 px though his 1 = 4 px rule gives 24 (2025-10); A7qI3HAEu18 and RJokEINz76o are narrator-unnamed in tops.md. [YT:9nIwTjG2fdI, YT:eQFAo9z24FM, YT:A7qI3HAEu18, YT:RJokEINz76o]

### Signature lines (verbatim, ≤15 words)
- "It feels almost like an insult nowadays." [YT:lgqnMzOu2Lw] (2025-10)
- "You're creating a vibe. You're creating a standard." [YT:lgqnMzOu2Lw] (2025-10)
- "The people who notice these details are the ones that will buy your product" [YT:Fs-nfTiWzvg] (2026-07)
- "HTML is just the wrong technology to draw a house" [YT:PA3f3MdRc08] (2026-09)
- "just enough code to be dangerous" [YT:_Lqa5o4gKJI] (2024-10)
- "Aesthetics is function" [YT:u5q8-fFmGtA] (n.d.)
- "definitely not purple" [YT:lgqnMzOu2Lw] (2025-10)
- "spend that last 10%" [YT:SznrOQYiahg] (n.d.)
