# Meng To — Standards Bank

This file is the bar. Every piece of work the coach produces or judges is graded against the checks for its task type. A check is PASS only with evidence pointed at the work itself (a line in the brief, a backticked prompt, a score, a screenshot at a named width, a file attached). "Looks premium" is not evidence.

Corpus status: 138 transcripts (660400 words) in the raw layer plus canon items. Checks re-sourced on 2026-10-20; tags without YT ids were not found in transcripts. Sergei Chyrkov transcripts are tagged SERGEI in the raw layer and cited as Sergei.

Each check carries its source. Pull the context with `scripts/search.py "<check words>"` when a check is borderline or Ivan disputes it. Checks tied to a tool, model, effort setting or price carry a year in brackets, e.g. **[2026]**: they age month to month, and a newer source beats them.

Scoring: count PASS / total for the task type. Deliver only at ≥ 85% with zero FAIL on checks marked ★. Otherwise fix and regrade (max 2 fix loops), then deliver with the remaining FAILs listed honestly.

---

## T1. Build brief (new page, new section, or upgrade of a live page)

The package Ivan pastes into Claude Code, Codex or Claude Design. Graded on the brief text and its attachments list.

- ★ **A reference rides with every ask; no blank prompt.** Each section ask names its input (URL, screen recording, screenshot, HTML or component code). A bare "build me a landing page for X" anywhere in the brief = FAIL. Evidence: the attachment line per section. [YT:7MEsUtvEbyU] [YT:M4DNgmI7MIM] [YT:G-F5Qvy-7KM]
- ★ **Every reference is labelled reference vs asset, with what to take and what to drop.** e.g. `make sure that you're not using it as an asset right now. It's used as a reference.` plus `adapt`. Evidence: label text next to each reference. [YT:T1WTGQesbrE] [YT:PA3f3MdRc08]
- ★ **Hero first, one section per thread.** The brief is split into numbered threads; thread 1 is the hero alone; no whole-page screenshot used as the build reference. Evidence: thread list. [YT:lgqnMzOu2Lw] [YT:HO2a_BTx12k]
- ★ **Upgrade jobs carry a frozen block, top and bottom.** Explicit list of what stays (sections, copy, colours, fonts, CTAs) plus `keep everything` / `keep the hero` / `don't change anything else`. Missing on an upgrade = FAIL; skip on a new build. Evidence: frozen block text. [YT:HO2a_BTx12k] [YT:jyfOAoMnxbY]
- **Reference ladder respected.** The strongest available input is used: URL with repo > URL > screen recording > screenshot > hand-written prompt. A hand-typed description where a URL exists = FAIL. [YT:lPtf_-J75Sk] [YT:G-F5Qvy-7KM]
- **Technology named per element.** Each non-trivial element names its technology (Three.js, shader, transparent PNG, image generation, Iconify Solar). Any "draw/illustrate X" left to HTML/CSS = FAIL. "HTML is just the wrong technology to draw a house." [YT:PA3f3MdRc08]
- **Design-system files attached.** design.md (foundations) plus the HTML (prescriptive, animations included), or a stated reason none exists yet and the step that makes one. [YT:M4DNgmI7MIM] [YT:LfgMBy0auL8]
- **Effects named, not adjectives.** Every motion/effect ask names the effect and at least one of delay, duration, easing, order. "Make it pop / modern / premium" alone = FAIL. [YT:M-uUFLU9IFU] [YT:jyfOAoMnxbY]
- **Verify clause present.** `self-verify until it's perfect` plus "score each element out of 10, push to 8 or 9" plus iPad and phone width checks. [YT:PA3f3MdRc08] [YT:G-F5Qvy-7KM] [YT:u5q8-fFmGtA] [YT:HO2a_BTx12k]
- **[2026] Effort set to `extra` (Claude Code) / extra high (Codex); `single HTML file` stated for prototypes.** Low/medium effort or no file format stated = FAIL. Date the line. [YT:G-F5Qvy-7KM] [YT:PA3f3MdRc08] [YT:lPtf_-J75Sk]
- **Feel and look stated before layout.** The brief opens with what the visitor should feel and what they should look at first. [canon: craft_motion_assets.md] (not found in transcripts)
- **Every field and limit spelled out; hard constraints stated twice** (Sergei). [canon: Sergei notes] (not found in transcripts)

## T2. Output critique and ranked fix prompts ("looks AI-made", "came out worse")

Graded on the critique itself, against the screenshots/URL it judged.

- ★ **Slop tells named by name, each located.** Uses his list (uneven selected-menu border, caps eyebrow with wide spacing, needless status chip, random lights, grey fighting the purple, purple gradient, default font, bold titles with loose tracking) and Sergei's (grey 1px strokes everywhere, same corner radius everywhere, beige palette, stock tabs/buttons, cited as Sergei). Each tell found points to where it is. Evidence: tell → location list. [YT:M4DNgmI7MIM] [YT:dXdxVi6Qz6k] [YT:8wsjt6IlxBw]
- ★ **Fix prompts: one change each, paste-ready, ending with a keep line.** Max seven, ranked. Each ends with `don't change anything else` (or a named keep). Any fix prompt bundling two changes = FAIL. "too much information is too much information" [YT:M-uUFLU9IFU] [YT:HO2a_BTx12k]
- ★ **Upgrade critique lists what dropped and what got added.** Item-by-item against the frozen list / previous version. Missing on an upgrade = FAIL. [YT:HO2a_BTx12k] [YT:8wsjt6IlxBw]
- **Anti-slop pass in his order.** Title weight → tracking → title/body font pair → accent off purple, tinted neutrals → distinct background and unique images → animation last. Animation fixes ranked above type fixes = FAIL. [YT:lgqnMzOu2Lw] [YT:dXdxVi6Qz6k] [YT:DsjEI6-5kgI]
- **Each section scored out of 10, page placed on his level scale** (0–1 one-line prompt result; 10 = Dia / Perplexity Comet class). Anything under 8 has a fix. [YT:NhHfI47WQDM]
- **Two-second fixes go to a by-hand list,** not into prompts (rename, delete, set a height). [YT:jyfOAoMnxbY] [YT:M-uUFLU9IFU]
- **Decision source asked.** Critique states where each weak decision came from: reference, system file, or nothing (Sergei: nothing → generic kit). [YT:8wsjt6IlxBw]
- **Checked at iPad and phone widths; no horizontal scroll.** Evidence: named widths in the critique. [YT:HO2a_BTx12k]
- **Images audited.** Repeated Unsplash faces, broken or low-res avatars, illustration where a photo belongs each flagged; "fix at least the broken images" is the floor. [YT:lgqnMzOu2Lw] [YT:HO2a_BTx12k] [YT:T1WTGQesbrE]
- **Spacing on the 4/8-pt scale (Sergei), no decimals in sizes (Meng).** Flags odd fixed values. [YT:3qAAfKcJK08] [YT:1MdwweKCNwg]
- **Redesign ask keeps the requirements and ends with a generic-pattern review pass** (Sergei): study references for patterns, don't copy; keep the same product requirements and functionality; final pass for generic UI patterns and unnecessary elements. [YT:8wsjt6IlxBw]
- **Locked items not re-litigated.** When Ivan has frozen colours/type (Besley + Schibsted Grotesk), the critique skips font/accent checks and says so. [canon: SKILL.md Ivan context] (not found in transcripts)

## T3. Design-system file (design.md + HTML pair, Sergei's JSON route)

Graded on the file(s) delivered.

- ★ **Two parts, two roles.** design.md holds foundations (colours, type, spacing, elevation, shapes, do's and don'ts, tokens); the HTML holds the prescriptive part including animations. A design.md with no HTML partner, or with no statement of which file is reference vs foundation = FAIL. [YT:M4DNgmI7MIM] [YT:LfgMBy0auL8] [YT:OZaE5ZezjYs]
- ★ **Built from real work, not invented.** Generated from exported HTML of an existing design (`turn this into a design.md...`) or a named source (getdesign.md, a template). Evidence: source named in the file header. [YT:M4DNgmI7MIM] [YT:DsjEI6-5kgI]
- **Every value is a number or a named token.** No "subtle shadow" without its values; spacing on a 4/8-pt scale; no decimals. [YT:3qAAfKcJK08] [YT:1MdwweKCNwg]
- **Brand colour reserved** for selected state and CTA; semantic tokens carry light and dark values. [YT:pZcwsjY81hA] [YT:AtoweRknIKA]
- **"Do we really need a new style" applied:** no near-duplicate tokens. [YT:pZcwsjY81hA]
- **Re-attach rule stated (rewritten from transcript).** design.md is strongest at the start; once iterating fast, the file says where the rules now live (agents.md, or "in the style of" a finished page) instead of re-attaching it every prompt. [YT:SznrOQYiahg] [YT:M4DNgmI7MIM]
- **Sergei route (if used, cited as Sergei):** agent uses only the tokens; a changelog .md updated after every UI change (changelog not found in transcripts). [YT:1MdwweKCNwg]
- **Design system is exported, not invented during screen design** (Sergei): AI asked to design screens and a system at once invents hundreds of tokens, odd spacing and random radii; export the real tokens first and have the agent use only those. [YT:1MdwweKCNwg]

## T4. Motion, 3D, shader and background recipe

Graded on the recipe text and the stated budget.

- ★ **Scene split into elements, technology per element.** Procedural Three.js for rigid shapes; image generation for people; transparent PNG layers for ornaments; shaders for effects; Iconify Solar for icons. [YT:PA3f3MdRc08] [YT:KOZjqVNHIo8]
- ★ **[2026] No humans or animals coded in Three.js.** Characters go to image generation, then Tripo 3D / Meshy / Hyper 3D, named up front (Opus 5.5 makes stick figures, 2026-09). [YT:PA3f3MdRc08]
- ★ **Weight budget stated.** Procedural scene ~500 KB, under 1 MB total; high-res image 1–2 MB; video ~100 MB; never several heavy backgrounds on one page. [YT:PA3f3MdRc08] [YT:G-F5Qvy-7KM] [YT:9nIwTjG2fdI]
- **Motion in exact words.** Delay, duration, easing, iteration, stagger, direction, order (logo first, then text). `ease` to appear, spring only for drag/bounce; 0.1 s delay steps; appear above the fold, scroll-triggered below. [YT:M-uUFLU9IFU] [YT:TGaCyIak-Ak] [YT:9nIwTjG2fdI]
- **Background never fights the heading.** Empty space under the heading, saturation/blend mode tuned (screen, soft light), alpha mask on mobile, `pointer-events none` if it blocks. [YT:b-kTkak2FKs] [YT:7MEsUtvEbyU]
- **One animated focus per hero.** [YT:HO2a_BTx12k] (rule not found in transcripts)
- **Quality block pasted unchanged** for 3D (`Retina-display ready`, `lighting like a AAA game`, `score at least 8/10`...); `retina` stated. [YT:PA3f3MdRc08] [YT:KOZjqVNHIo8]
- **Snippet or named library referenced, not described** (React Bits shader, Cobe globe, canvasui.dev prompt). Say both `shader` and `Three.js` for backgrounds. [YT:eQFAo9z24FM] [YT:jyfOAoMnxbY]
- **Layers requested as separate transparent PNGs** when parallax/orbit is wanted. [YT:G-F5Qvy-7KM] [YT:KOZjqVNHIo8]

## T5. Site images and video (hero stills, hero loops, people, mockups)

- ★ **Still first, video second.** Art direction approved on a still; video drafted at 480p, approved, then 1080p. [2026] costs: ~$1–2 a video, 480p 10–50 cents. [YT:lPtf_-J75Sk]
- ★ **No repeated stock faces, no broken or low-res images in the deliverable.** [YT:lgqnMzOu2Lw] [YT:T1WTGQesbrE] [YT:dXdxVi6Qz6k]
- **Playback mode chosen and stated:** loop (hero: 4 s), once on load, on hover, or scroll scrub. [YT:T1WTGQesbrE] [YT:lPtf_-J75Sk]
- **Images where a photo belongs, not illustration or gradients.** `I don't want any illustration. I want to use images instead...` [YT:M4DNgmI7MIM] [YT:T1WTGQesbrE]
- **[2026] Spend guardrail in the agent prompt:** under $1 no asking, over $1 ask. [YT:PA3f3MdRc08]
- **[2026] Model named and dated** (Nano Banana Pro 2026-03 for typography/translucent UI/people; GPT image 2 2026-06 for contextual faces). [YT:ohgPI0NgvwQ] [YT:T1WTGQesbrE]
- **Flat UI screenshots framed** (card, browser mockup, perspective/glass) before they go on the page. [YT:M-uUFLU9IFU] [YT:WrlZlQVfL9Y]

## T6. Tool, model and effort pick

- ★ **[2026] Every pick dated by the month of its source, with the warning** "tools change month to month; test on your own page." An undated model claim = FAIL. [canon: sources.md] [YT:SznrOQYiahg]
- ★ **Pick per job, not one tool for all.** Jobs separated (reference → first page, hero polish, 3D, images/video, mechanical edits, code hand-off) with a pick each. [YT:PA3f3MdRc08] [YT:lgqnMzOu2Lw]
- **[2026] Current picks match the canon:** Opus 5.5 / Fable in Claude Code at `extra` for front-end and 3D; Codex for harness and agentic work; Claude Design is not Meng's tool (Sergei's notes cited as Sergei). [YT:PA3f3MdRc08] [YT:G-F5Qvy-7KM] [YT:LfgMBy0auL8] [YT:u5q8-fFmGtA]
- **Input over model stated.** A top model on a naive prompt shows no gain; the pick comes with the input it needs. [YT:M4DNgmI7MIM] [YT:NhHfI47WQDM]
- **Test, don't trust:** same input through two models, each one's tell named. [YT:M4DNgmI7MIM]
- **Aura bias disclosed** whenever Aura is recommended (Meng builds Aura himself). [YT:KOZjqVNHIo8] [YT:LfgMBy0auL8] [YT:NhHfI47WQDM]
- **Model and effort matched to the task, not the top model by default** (Sergei): Sonnet for design-system extraction, Opus at high effort for Mobbin-referenced screens, Fable at low effort for a plain MVP pass. [2026] [YT:ScsjVpmhpyc] [YT:8wsjt6IlxBw]

## T7. App or SaaS build steering (Funnel Message Map, internal tools)

- ★ **Decomposed into ingredients; one capability per prompt.** The plan lists the feature keywords and the first ~10 prompts, one capability each; aesthetics last. A "build me a [whole app]" prompt = FAIL. (the ~10-prompt count not found in transcripts) [YT:6t0_KEchMUk]
- ★ **Save points and one thread per task.** Commit before experiments; new thread per task; shared rules in agents.md kept minimal (browser, style). [YT:YhL3BHS5sGU] [YT:hSSxuO6GdcE] [YT:M4DNgmI7MIM] (commit-before-experiments not found in transcripts)
- **Component/hook split asked before the file grows** (about a thousand lines, or 100 layers' worth). [YT:6t0_KEchMUk]
- **Screenshots carry a written prompt** (task, then context, then the complex feature in steps). [YT:hSSxuO6GdcE]
- **Real flows as reference** for login, settings, onboarding (Mobbin), not concept shots (Sergei). [YT:0ajxdUNacQE]
- **Taste pass:** `make sure every button works`, `make sure that the flow is not blocked by the UX`. [YT:u5q8-fFmGtA]
- **Idea validated into a master prompt file before the first build prompt** (Sergei). [YT:0ajxdUNacQE]

---

## Universal checks (every output)

- ★ **Retrieved before writing.** At least 3 searches run; the work uses at least 3 retrieved items or passages, cited as [YT:id].
- ★ **No invented quotes, prompts, numbers, stories or dates.** Every quoted line and every backticked prompt exists verbatim in a retrieved hit or the canon. Composed lines for Ivan are labelled composed.
- ★ **Did the work.** If Ivan gave a task, the output is the finished thing (brief, fix prompts, recipe, design.md), not a list of questions. Questions only for inputs that are missing and block the work, and only after doing everything possible without them.
- **In voice.** Short declaratives with "right?" / "okay?", "you know", numbers first, blunt verdicts, admits misses; Sergei always named as Sergei. No invented catchphrases, no praise opener.
- **Ends with one move.** The one prompt to run first, in which thread, and what to check when it returns.
