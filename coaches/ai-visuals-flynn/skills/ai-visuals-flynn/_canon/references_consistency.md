# References, style codes and consistency systems (Rory Flynn)
> Sources: [YT:<id>] = YouTube video id; (YYYY-MM) = upload month; (Fast Hours) = from the podcast with the speaker unclear (Rory or co-host Drew Brucker) — technique only, never quoted as Rory.

## PART 2. References, style codes and consistency systems

Speaker labels: unlabeled = Rory Flynn; "(Fast Hours)" = Rory or co-host Drew Brucker, speaker unclear; co-host Drew Brucker and "guest <name>" are not Rory's own views.

### Rules (ranked by how often they say it)
- **Hold the "brand of the image" fixed; swap only one to three blocks.** Split a reference into blocks (photo type, subject and action, environment, color scheme, lens, film, lighting, composition, details), keep the back half identical, change subject, environment or shot type only. [YT:aBgRhbYlF6Q, YT:dcrhhIKNaRQ, YT:34FQ8Ewa9ek, YT:MpcDWmhzNb0] (n.d., 2024-10, 2025-10) · mentions 16
- **Let references carry the look; prompt only the scene.** With a tight board, sref, profile or style card attached, the prompt shrinks to subject, action, maybe camera angle: board plus `cat`, board plus `Samurai in a bamboo forest`. [YT:jP9vWmf0TG4, YT:HSZoLRw4e74, YT:Rzr8TDN_0y8] (2025-10, 2026-06) · mentions 15
- **Image reference takes construction, style reference takes aesthetic; check image weight first.** Seal-and-flamingo demo: the image prompt blended the seal's pose and black feathers into the flamingo; sref kept the pink flamingo and took only the dark muted look. Image weight has far more firepower than the other controls. Image reference is "slept on". [YT:34FQ8Ewa9ek, YT:Fa79Iv3QFJk, YT:EBSPo2XCml8, YT:t0dgrFHEcwM] (2024-10, 2025-10) · mentions 15
- **One personalization profile per purpose; rank on purpose.** Whatever you rank carries heavy weight. His Global went gritty and contrasty because he skipped ~40 images to find one he liked, and later drifted into "a horror film"; so he trains separate profiles: soft (3D, minimalist), rank-everything, photoreal-only, one each for fine art, animation, Niji. Rank "Part utility, part preference". [YT:26bjN6CwwJs, YT:3lVfYTHknX4, YT:A4ZvuMXGQvY, YT:F6P2EAfAwjw] (2025-10) · mentions 13
- **Isolate variables: simple prompt, same seed, personalization off then on.** With five image prompts, three srefs and a P value stacked you cannot tell what drives the look; reset to subject-only plus P, then push stylize. Run weights as permutations, one change per run. [YT:EBSPo2XCml8, YT:t0dgrFHEcwM, YT:34FQ8Ewa9ek, YT:aBgRhbYlF6Q] (2024-10, 2025-10, n.d.) · mentions 12
- **Make it repeatable for a team: fix everything but the variable, trim the inputs.** A prompt that works only for you is pointless; give each part a value so teammates change only color or structure. A single-use tool beats a broad one. [YT:zPIBzQRJVT8, YT:N-tmQ_Can_o, YT:P3w112Qr-2s] (2024-10, 2026-09) · mentions 12
- **Build in layers: make each ingredient alone, then combine.** Be "the farmer of our own ingredients": generate gradient, texture, pattern, icons separately and image-prompt them together; prompting everything at once takes forever and Midjourney misses elements. Ingredient-style editing (character plus object plus environment) in Nano Banana: do it in steps. [YT:BwFzyeHozFk, YT:2vHM6owNx6c, YT:E41H2WIHMXg, YT:MzobW5KQEEI] (n.d., 2025-11) · mentions 12
- **Size a board by use: fewer images are tighter, more are freer.** 1-3 images act like an sref token; about 5 (storyboard-style set) is tight; 20-30 varied is the classic board; up to ~100 is the long game. One stylized image drags its construction in; ~30 varied images in one style give the look without the content. [YT:gdPY4W72-N0, YT:A4ZvuMXGQvY, YT:jP9vWmf0TG4] (2025-10) · mentions 12
- **Stack a personalization profile under every board, then compare with and without.** He leaves Global on and layers boards over it; the pair sometimes looks "radically different". V7 boards came out "jacked up" with personalization off; the profile code is "the bridge in the gap". [YT:26bjN6CwwJs, YT:vGy9dKPbtGc, YT:Siclp1Y75Mc] (2025-10) · mentions 11
- **Blend styles that balance each other, then weight them.** Juxtapose photoreal with doodles or sketch, photoreal with 3D, dark with bright; two super-photoreal styles clash. Three codes weighted 3x vs 1:1:1 vs 3:3:1 gave radically different, usable looks. Favorites: high-contrast black and white plus crazy neon; illustrative plus photoreal. [YT:34FQ8Ewa9ek, YT:Mw5iwBFp9EE, YT:Fa79Iv3QFJk, YT:J5U49z2_EKw] (2024-10, 2025-10) · mentions 10
- **Micro-boards: small single-purpose boards used as tokens and seasoning.** About five images (film negative, iPhone, sepia, motion blur) stacked on a bigger look: "you're creating your own tokens" instead of longer prompts. [YT:vGy9dKPbtGc, YT:26bjN6CwwJs, YT:gdPY4W72-N0] (2025-10) · mentions 10
- **Learn Midjourney's language by searching, not typing from scratch.** Search a strange token, drill into a style, a sub-style, then scene, expression, angle; click into any image for similar-results search; diagnose an unfamiliar look with "this is a style code right". Why: you have to know how to describe things, it's a different language. [YT:O9g2mwlwQcQ, YT:gdPY4W72-N0, YT:MzobW5KQEEI, YT:GzrYcMt62gA] (2025-10, 2025-11) · mentions 9
- **Style weight: stay under the default 100 to take only part; 400-800 look alike.** Same-seed ladder: sw 0 plain, 35-80 a little shading and eye detail, 100 somewhat transferred, 400-600 basically the whole style, 900-1000 finest detail; diminishing returns past ~600. Strongly coloured sref: try sw 40/50/70. A code that skews cartoon: sw 20-30, prompt things you like, board the results. [YT:34FQ8Ewa9ek, YT:6vMsfe-KgRI, YT:A4ZvuMXGQvY] (2024-10, 2025-10) · mentions 8
- **When a board misbehaves, remove images; diversify people; watch angle bleed.** Two or three added images wrecked one board, removing them made it ten times better; about ten photos of his own face among 20 other images made everyone look like him; four or five super-low-angle people images forced low angle on everything. [YT:gdPY4W72-N0, YT:A4ZvuMXGQvY] (2025-10) · mentions 7
- **Brand rules go in as a system prompt, not re-extracted from images each time.** A brand-guidelines doc becomes a Nano Banana system prompt (his "brand prompt engineer"); a strong style guide is dissected by local Claude Code into hard-coded rules; an optional "visual brand profile" variable keeps every generated prompt on brand. [YT:1V0xODN21tU, YT:zUe96tRUpDg, YT:PJ347ccVJBs] (2026-09, 2026-02, n.d.) · mentions 6
- **Reverse-engineer your own brands only; no artist or director names.** Ask ChatGPT which compositions, equipment and color schemes a director uses and build from those blocks. Never image-prompt with copyrighted images (generate your own first); reverse-image-search commercial outputs; tell clients you use AI. [YT:aBgRhbYlF6Q, YT:2vHM6owNx6c, YT:dcrhhIKNaRQ] (n.d.) · mentions 6
- **Midjourney for look and exploration; other tools for control and replication.** He leaves it for characters (Feb 2025: Krea-trained model, MiniMax subject reference, Pika ingredients, Kling Elements), uses its stills as reference for generators that handle text and real product, and says "when structure and process needs to be replicated, that's where nodes come in". [YT:26bjN6CwwJs, YT:0217lav5Dlo, YT:SQIGjY_Rs2s] (2025-10, n.d., 2025-12) · mentions 6
- **Exact things leave Midjourney: client details, logos, text.** Social: let drift go; client: fix it in Photoshop by hand. Products with text or logos will not work in omni reference. Editor is the Swiss Army knife, Photoshop the scalpel. [YT:oKQd-ZumqCA, YT:hAnYA2wJaZ4, YT:X-Nm3NGvrTE] (2026-08, 2025-10, 2025-10) · mentions 5
- **Remix first, then layer the sref, board or code on top.** Lock prompt and composition, hit Remix Strong, then add the sref, board or profile so it sits on the existing construction; these can "do too much" and morph the whole image. [YT:Siclp1Y75Mc, YT:J5U49z2_EKw] (2025-10) · mentions 5
- **Custom-trained brand models go stale; keep the style in a reference or system prompt.** "your stuff looks like the AI of two months ago, which everyone can tell"; Flux is probably the only one worth training for a brand look. After Nano Banana he thought LoRAs were done (Jan 2026), yet multi-image inputs and contact sheets still act like mini LoRAs. [YT:FGJCBhAiQJk, YT:MJZjmv6HMKA, YT:AOuXCRzjsS0, YT:Rzr8TDN_0y8] (2026-07, 2026-01, 2026-02, 2026-06) · mentions 5

### Methods (named or ordered)
#### Asset hacking ("one image into a thousand")
- When they use it: rebuild a brand's visual signature in new subjects (Red Bull, Apple, Nike); own brands only; needs an existing consistent aesthetic.
- Steps: 1. Collect brand assets. 2. Run `/describe` (four prompts per image; alone they read like video games). 3. Give the image to ChatGPT with the extraction prompt (Recipe library). 4. Image-prompt Midjourney with the original plus that prompt (higher image weight for realism). 5. Keep color scheme, lens, film, lighting, composition, details; change only photo type, subject, environment.
- Their example: Red Bull F1 car to skier, motorcycle, mountain biker, dune buggy; the slow part is judging "is it there yet". Oct 2024 variant: image as sref, change only photo type, subject, action.
- Sources: [YT:aBgRhbYlF6Q, YT:dcrhhIKNaRQ, YT:34FQ8Ewa9ek, YT:k8rciHNdlvs] (n.d., 2024-10)

#### One story across many images (Tulum hotel series)
- When they use it: a storyboard or campaign where every frame must read as one place (entrance, desk, welcome drink, pool, bar, room, dinner).
- Steps: 1. Spend most time on the first look-and-feel formula. 2. Hold mood, lighting, color scheme, architecture style, camera and film stock constant; change only subject and environment. 3. Ask ChatGPT for "five prompts" (lobby, pool, suite, penthouse, bar) with the two-part prompt in the Recipe library.
- Their example: built at V5, redone in V6 ("the breakthrough"); each image took about a week before the editor and generative fill existed.
- Sources: [YT:Mg9oeq5T5Lg, YT:MpcDWmhzNb0, YT:gdPY4W72-N0] (n.d., 2025-10)

#### Character sheet as a mini LoRA (cref era, Oct 2024)
- When they use it: only one character-reference slot, so one image must carry the person.
- Steps: 1. Prompt `character sheet` + person + clothing + studio setting + flat background (keeps data on the person) + `image split into four different pictures shot from multiple angles`. 2. More sheets via Vary (Subtle) or the same seed. 3. Best sheet becomes the CF image; describe the character the same way in the new prompt.
- Their example: five pictures in one reference worked; face, brows, hair color, ponytail carried; the simplest sheet (eyes in several directions, head from different angles) translated best. Nov 2023 version: `split this into four images`, Vary Subtle, multi-image prompts, repeat 2-3 times to a 16-20 image grid.
- Sources: [YT:_nT6fav4qFA, YT:Mg9oeq5T5Lg, YT:AOuXCRzjsS0] (2024-10, n.d., 2026-02)

#### Omni-reference face method (V7, Oct 2025)
- When they use it: placing a person or character in new scenes (same logic as old cref).
- Steps: 1. Reference = one face portrait, plain white or studio background, minimal detail, no other people, like you're training a LoRA. 2. Raw, un-upscaled, default `--ow 100`. 3. Change only pose and expression. 4. Himself in scenes: `--ow 400` with `--exp 30` to `40`. 5. Remove `--ow` before editing (no editing with omni ref active).
- Their example: `side profile screaming, head tilted back, eyes closed`, `winking`, then body poses; a wrinkle and crooked nose carried, freckles never one-to-one; "It can translate a face". Hands worsen the further the figure is from the frame.
- Sources: [YT:Ye6DOhTgsDc, YT:hAnYA2wJaZ4] (2025-10)

#### Reference pillars, then fan out (plus the nine-angle sheet)
- When they use it: a car, product or person that must match from every side; Nano Banana has only Midjourney's front three-quarter view, so every rear angle differs.
- Steps: 1. Turn the one image into rear, side and rear three-quarter views (the pillars). 2. Fan out many angles from each pillar (his Weavy car workflow does this with no manual prompting). Product version: the nine-angle system prompt in the Recipe library.
- Sources: [YT:2sY91XsiRuw, YT:AxV8TR3BdqI, YT:N-tmQ_Can_o] (2025-10, n.d., 2026-09)

#### Style card in an image (video to Codex, Jun 2026)
- When they use it: a look he saw (a flashy color grade) must transfer with only the subject typed afterwards.
- Steps: 1. In Codex download the video, pull ~50 frames (video plus frames beats one image: "it's all context"). 2. Have it build a standalone card: style locks, exposure curve (midtones, shadows), core tokens, source frames, camera logic, color-grade rules, "prompt nucleus"; if only this image arrived it must hold everything to replicate the style. 3. Attach it in Nano Banana and type only the scene; character consistency comes from a separate character sheet.
- Their example: `generate six successive images for a scene in brand content outdoor lifestyle fly fishing` held the grade; one frame got the jacket color wrong.
- Sources: [YT:Rzr8TDN_0y8] (2026-06)

#### Design system with a formula, then cascade (Sep-Oct 2026)
- When they use it: one strong output must seed every later asset.
- Steps: 1. One reference image, one explainer-style render (30-second target), then the one-by-one version; tweak composition; ask what it cost in tokens. 2. `document everything in this folder` so it becomes a general animation pipeline with skills and learnings. 3. Replicate the Negroni video for four other classic cocktails, same colors, design system, animation style, one-by-one ratio.
- Their example: four sub-agents built four videos in a few minutes. Cascade: a no-direction promo video, then `use the design system and whatever you did on this promo video` for podcast B-roll, then the whole system into a website.
- Sources: [YT:tlqnW1sp5X4, YT:nROQ4LJ4GcQ] (2026-09, 2026-10)

#### Style-code mining and judging
- When they use it: new srefs needed, or a fast verdict on a code.
- Steps: 1. One fixed test prompt: `street style photo` with `--sref random` and `--r 4` (hunting photoreal codes), or `samurai` (always returns detail, shows minimal vs maximalist); `--r 40` when time allows. 2. Check no mood board is toggled on. 3. Run randoms inside one folder. 4. Strongly colored code: test low sw. 5. On a keeper run `--weird` 0/50/100/500/1000. 6. Judge what pops, then keep or board it.
- Their example: a weekend of ~60 V7 randoms gave ~20 keepers vs the usual ~5 (speaker inferred). Co-host Drew Brucker's variant: skull emoji only, 4:5, `--sw 250`, personalization on, then `dribbble.com`, album cover, movie poster.
- Sources: [YT:gdPY4W72-N0, YT:6vMsfe-KgRI, YT:Mw5iwBFp9EE, YT:O9g2mwlwQcQ] (2025-10)

#### Board build-up and test loop
- When they use it: a board must hold across subjects and ratios.
- Steps: 1. Define the end goal; pick the size. 2. Tight look: start from one image, use sref plus prompting to generate the rest of the set (cowboy with a hat, man with a horse head, coffee kettle), board those. 3. (Fast Hours) test people, product, car; add images where one fails; retest; then test ratios.
- Their example: typing `1980s Miami` into Midjourney search and saving the first four images as a board gave a vintage look at once.
- Sources: [YT:jP9vWmf0TG4, YT:A4ZvuMXGQvY, YT:vGy9dKPbtGc, YT:gdPY4W72-N0] (2025-10)

### Recipe library (exact, reusable)
- **ChatGPT extraction prompt (asset hacking)** — `analyze the image, create a prompt for an AI image generator, describe it like an award-winning professional photographer in extreme technical detail, use your prompt formula, include camera, lens and settings, short powerful keywords, no fluff`; optionally blend in the best /describe prompts, then image-prompt with the original. [YT:aBgRhbYlF6Q] (n.d.)
- **Two-part formula prompt (Tulum)** — first give the Midjourney formula (photo type, subject and action, environment, color scheme, lens, film, lighting, composition, details, parameters) and say respond yes if you understand; then `create three prompts for a five-star luxury hotel in Tulum inspired by treehouses; use concise, visceral, powerful language; only use keywords; no filler words`; change only the shot (pool, lobby, bar, suite). [YT:MpcDWmhzNb0] (2025-10)
- **Fixed aesthetic block** — surfer in Antarctica: the background block (black mountains, rolling ocean landscape, dark atmosphere, muted colors, sharp resolution, color contrast) is identical in every prompt; only shot type, subject, details change: `closeup of a surfer with frost on his face` vs `closeup of a penguin on the beach`. [YT:aBgRhbYlF6Q] (n.d.)
- **Exact brand color** — Midjourney has no Pantone or hex association (at recording): stack a swatch or gradient as an sref inside a multi-panel mood board. [YT:_nT6fav4qFA] (2024-10)
- **Preview a style code in one job** — prompt a multi-panel mood board split into multiple images, with lifestyle shots and color swatches, and put the `--sref` code in it: one job shows the code on a person, a flower and objects instead of 9-10 prompts. [YT:34FQ8Ewa9ek, YT:_nT6fav4qFA] (2024-10)
- **Two characters in one image** — generate each alone, reference both, write `man on left: <description>`, `woman on right: <description>`; faces often still blend. His own post took ~20 steps, about two days of pain, then ~20 hours in Photoshop. [YT:QLbjv3CbfIo, YT:LvmCVPAD5G8] (2024-10, 2025-10)
- **Avatar of yourself** — self as image reference first (iw 0.5-0.8 keeps construction), then sref at sw 50-90 for a hint or 500-700 for heavy; his face now translates only at about iw 0.5-0.6. [YT:34FQ8Ewa9ek, YT:EBSPo2XCml8] (2024-10)
- **His "wacky" recipe** — one extreme, maximalist, photoreal-side style code at sw 20-50, chaos ~10, stylize 200-400. [YT:Fa79Iv3QFJk] (2024-10)
- **"Power three" order** — image reference alone, weighted; if the character stops looking like itself stack character reference; then higher image weight or add style reference; use the editor to change the character and keep the environment. [YT:Fa79Iv3QFJk] (2024-10)
- **Pattern and element layering** — make the pattern alone (`intricate '90s ugly pattern, symmetrical composition`; `intricate texture petrified wood pattern`), then image-prompt or sref it into the real shot; low image weight (iw 0.5) for clothes. Small editor edits: same reference as both image and style reference on a tight selection. [YT:JskVAZqt34w, YT:Fa79Iv3QFJk, YT:kR05Q2WxhCA] (2025-10, 2024-10)
- **Omni clothes and products** — low `--ow` ~50-150 changes clothes and keeps the rest; above ~400 adds nothing; low `--ow` of 10-25 puts a product on a person; paste several items into one image for a single object reference; couch or car work, text or logo products do not. [YT:hAnYA2wJaZ4, YT:Ye6DOhTgsDc] (2025-10)
- **Same car across key frames** — remove the background in the editor and regenerate it per location; any difference between two key frames morphs in; chain each end frame into the next start frame; keep subjects off-center, alternating sides. [YT:J5U49z2_EKw] (2025-10)
- **Nine-angle turnaround** — "lead CGI technical director" system prompt: ingest and analyze, rotate through a fixed list (full body front, side, rear, 3/4 views, full rear 3/4, low-angle hero) with fidelity lock (material, stitching), proportional lock, environment anchor, identical lighting direction; the proportion guide stays outside the automation. [YT:AxV8TR3BdqI, YT:N-tmQ_Can_o] (n.d., 2026-09)
- **System-prompt skeleton** — role, fixed inputs, tasks, identity lock, environment, format and look, lens, assembly order, output-only line. Style lock in Nano Banana as JSON-like code saying do this every time (his Polaroid and Kodak-car workflows). [YT:N-tmQ_Can_o, YT:AOuXCRzjsS0] (2026-09, 2026-02)
- **Image-stack analysis** — download 200-300 source images; an agent breaks each into ~65 points; a second agent clusters them into ~10-12 recipes; build system prompts from the recipes. An 800-image run used ~60 points and stripped brand-specific items. [YT:AxV8TR3BdqI, YT:92I8aNhyxwM] (n.d., 2026-04)
- **Token hunts** — feed unfamiliar named processes as style words and save what works: electrophotography, thermal imaging, exploded view, microfiche, CRT faux phosphor burn, photocopier art (found "encaustic waxing"). Style Explorer: search single tokens such as `precision photography`, `precision Polaroid`, `3D clay`. [YT:xLLtYn932qY, YT:MzobW5KQEEI] (2026-08, 2025-11)

### Fix library (problem → fix → why)
- **Problem:** toy or product scale comes out wrong → **Fix:** a 3D or diagram scale reference (8x8 plush beside a Chihuahua, beagle, golden retriever), not typed measurements → **Why:** "type in measurements you want all day. It'll never come out correct" [YT:N-tmQ_Can_o] (2026-09)
- **Problem:** details drift across shots (table legs, hat emblem, a food-glass reflection) → **Fix:** social: let it go; client: retouch in Photoshop by hand → **Why:** the model could not generate the reflection; "drives me up the wall" [YT:oKQd-ZumqCA] (2026-08)
- **Problem:** green tuxedo would not leave a James Bond scene → **Fix:** add `--exp 10` → **Why:** his guess: exp offset his personalisation; it also fixed hands holding a glass, "don't ask me why" [YT:Ye6DOhTgsDc] (2025-10)
- **Problem:** adding people one at a time degrades them → **Fix:** compositor node puts all characters on one canvas, then edit with Gemini (better than Seedream for boots, knife, background removal) [YT:PJ347ccVJBs] (n.d.)
- **Problem:** board outputs go soft or model-looking; own face leaks into everyone → **Fix:** stack a profile code for texture; add an iPhone board of non-model friends; fill the board with random varied subjects [YT:gdPY4W72-N0, YT:A4ZvuMXGQvY] (2025-10)
- **Problem:** rough or flat look (claymation, flat 2D calligraphy) → **Fix:** drop style weight and set `--q` to 0.5 instead of text-prompting roughness → **Why:** quality pulls Midjourney's creativity back to reality [YT:jP9vWmf0TG4] (2025-10)
- **Problem:** an old sref code looks different → **Fix:** add `--sv 4` (his sref 323 764 5460 only reproduces that way on V7) → **Why:** default is now `--sv 6`, `--sv 5` does not exist, nothing marks a code as legacy [YT:J5U49z2_EKw, YT:6vMsfe-KgRI] (2025-10)
- **Problem:** sref photo leaks its subject → **Fix:** new sref has none (white sneaker plus jungle photo took only colour and mood at `--sw 900`); bring content in by image prompt or omni reference [YT:6vMsfe-KgRI] (2025-10)
- **Problem:** V8 outputs crappy on a combined V7/V8 profile → **Fix:** abandon it, start brand-new V8 profiles, use only those → **Why:** board stabilized, "less freakouts" [YT:Dl64zUCJniU] (2026-05)

### Tool and model notes (dated, newest first; these age fast)
- **Weave/Weavy node tools** — Comfy is too extreme for designers: connect output nodes, lock what must stay hidden, publish a tool so a teammate types one word. Midjourney has no API, so it stays manual. [YT:N-tmQ_Can_o, YT:PJ347ccVJBs] (2026-09, n.d.)
- **Codex and Claude Code** — Codex runs locally with no ChatGPT-style limits (20 style-card images fast); rebuilding Midjourney boards with Claude took "a lot of steps"; Claude Code dissects brand guides into rules. [YT:Rzr8TDN_0y8, YT:RNF9xZYHOiQ, YT:zUe96tRUpDg] (2026-06, 2026-03, 2026-02)
- **Midjourney V8.1 and V8** — V8.1: simple prompt plus board read "extremely well", board resolution unchanged; (Fast Hours) only `--sv 6` works. V8: two boards, or board plus style reference, failed with "generation failed" while V7 ran them; (Fast Hours) prompt text beats the board (a stray "blue" turned a green-and-black board blue). [YT:FlnyD8Eqabk, YT:92I8aNhyxwM] (2026-05, 2026-04)
- **Nano Banana** — daily tool; plain language handles change, add, subtract, so reference parameters matter less; ingredient-style edits slip. (Fast Hours: after a brand logo update it kept the old logo despite the new file and a don't-change rule.) [YT:MJZjmv6HMKA, YT:qFnBQBvzhc4, YT:MzobW5KQEEI] (2026-01, 2025-11)
- **Style Creator (Fast Hours, Dec 2025)** — Refine Style updates the style, hearting does nothing; End Session to reset. Rory: it still feels random; he wants search or drop-in control. [YT:cZ99diltT6w] (2025-12)

### Coaching and critique moves
- Trainer diagnostic before a training: do you know what sref is how comfortable are you with it and do you know how to weight it; super comfortable but cannot weight = does not really know it [YT:vGy9dKPbtGc]
- Unfamiliar look: first ask "this is a style code right", expecting a stack (two boards plus a profile) [YT:GzrYcMt62gA]
- Before any board: "how are you going to use it" [YT:gdPY4W72-N0]
- Consistency stuck: does it need image prompting, the text prompt or a seed? [YT:P3w112Qr-2s]

### Numbers they have stated
- Global profile ranked ~18,000 pairs, stopped long ago; V7 unlock needs 200 ranked images, he ranked ~1,000 in one sitting; profiles now need ~40 ranks each; photoreal-only profile ~20 minutes [YT:gdPY4W72-N0, YT:F6P2EAfAwjw, YT:26bjN6CwwJs] (2025-10)
- ~60 sref randoms over a weekend, ~20 liked vs usual ~5 (speaker inferred) [YT:Mw5iwBFp9EE] (2025-10)
- With his P code: stylize 100 feels like him, up to ~400-500 still does, past that Midjourney takes over; tipping point ~650 [YT:EBSPo2XCml8, YT:u7EI0Z-0ULE] (2024-10)
- About 90% of his favorite 2025 images came from his boards [YT:MJZjmv6HMKA] (2026-01)
- Photo shoot 2-3 months to about an hour; ~5 min extraction plus under 20 min loop (Superside project) [YT:E41H2WIHMXg, YT:dcrhhIKNaRQ] (n.d.)
- Claymation brief: ~5 hours to a tight look; one board would have taken 20 minutes [YT:jP9vWmf0TG4] (2025-10)

### References they cite
- Marco: recommends Cosmos (cosmos.so), "Pinterest for designers"; Rory admires his intentional Rome reimagined work [YT:2sY91XsiRuw] (2025-10)
- Guest Allar: transparent look = two boards plus a profile at stylize 700; Rory calls it "a new medium" [YT:GzrYcMt62gA] (2025-10)
- Guest Tyler: Seedance canvas 1080x1440, character sheet on top, two offset copies of the Midjourney image below, so no single frame to lock onto [YT:FAvFtbjM5DY] (2026-07)

### Evolution and contradictions
- **Characters:** Oct 2024 four-view sheets, multiple characters "a hackathon" [YT:_nT6fav4qFA] (2024-10) → Feb 2025 leaves Midjourney for characters [YT:26bjN6CwwJs] (2025-10) → Oct 2025 omni reference: first "This sucks", good after 2-3 days [YT:Ye6DOhTgsDc] → Jan 2026 LoRAs done [YT:MJZjmv6HMKA] → Jun 2026 style cards [YT:Rzr8TDN_0y8] → Jul 2026 trained brand models go stale [YT:FGJCBhAiQJk]
- **Boards:** his practice went tight, then broad, then tiny [YT:vGy9dKPbtGc] (2025-10) → Jan 2026 a "vibes" board replaces Global [YT:MJZjmv6HMKA] → Apr 2026 V8 breaks stacking [YT:92I8aNhyxwM]
- **Personalization:** early 2025 ranks almost nothing, the "antithesis" of David's rank-everything [YT:HaoNwhf_qE8]; then "you don't have to" [YT:gdPY4W72-N0]; yet on V7 he ranked ~1,000 in one sitting [YT:F6P2EAfAwjw]; Dec 2025 back on V6 codes inside V7, "I haven't looked back" [YT:EaENLPTAt2E]
- **Contradictions:** `--exp` fixed the tuxedo and hands [YT:Ye6DOhTgsDc] but the same month he no longer balances `--ow` against it [YT:hAnYA2wJaZ4]; board plus profile not that different (co-host Drew Brucker) vs "radically different" (Rory) [YT:26bjN6CwwJs]

### Signature lines (verbatim, ≤15 words)
- "I like to call it the brand of the image" [YT:34FQ8Ewa9ek] (2024-10)
- "Consistency at scale is the product. That's the thing that brands pay for." [YT:N-tmQ_Can_o] (2026-09)
- "Define your goddamn end goal" [YT:gdPY4W72-N0] (2025-10)
- "when you get into multiple characters it's a hackathon" [YT:_nT6fav4qFA] (2024-10)
- "turn one image into a thousand" [YT:E41H2WIHMXg] (n.d.)
- "the farmer of our own ingredients" [YT:BwFzyeHozFk] (n.d.)
- "a Midjourney mood board in an image" [YT:Rzr8TDN_0y8] (2026-06)
- "your stuff looks like the AI of two months ago, which everyone can tell" [YT:FGJCBhAiQJk] (2026-07)
- "I'm prompting but I'm looking for styles at the same time." [YT:MzobW5KQEEI] (2025-11)
