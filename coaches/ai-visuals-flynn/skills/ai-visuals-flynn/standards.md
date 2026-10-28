# Rory Flynn — Standards Bank

Corpus status: 120 transcripts (1591313 words) in the raw layer plus canon items. Checks re-sourced on 2026-10-20; tags without YT ids were not found in transcripts.

This file is the bar. Every piece of work the coach produces or judges is graded against the checks for its task type. A check is PASS only with evidence pointed at the work itself: a prompt line, a block, a setting, a frame of the output, a step in the plan. "Looks good" is not evidence. Each check states its evidence type (*Ev:*).

Each check carries its source. Pull the full context with `scripts/search.py "<check words>" --layer items` when a check is borderline or Ivan disputes it. Attribution rule: plain [YT:id] = Rory; "(Fast Hours)" = a show technique, may be Drew Brucker or a guest; "Jamey" = Jamey Gannon, second source, never voiced as Rory.

**Dating rule.** Any check marked **⏱ YYYY-MM** depends on a tool or model and is true only as of that date. Models change month to month. If the work is graded more than ~3 months after the stamp, run the check, but say in the result that it may be stale. "n.d." means the canon gives no date.

Scoring: count PASS / total for the task type. Deliver only at ≥ 85% with zero FAIL on checks marked ★. Otherwise fix and regrade (max 2 loops), then deliver with the remaining FAILs listed honestly.

---

## T1. Single-asset brief and prompt (site imagery, ad static image, product shot, hero)

- ★ **Job locked before the prompt.** The brief states the asset, its placement, the size it lives at, the aspect ratio and who finishes it. Lacking these = FAIL, however good the prompt is. "how are you going to use it" comes first. *Ev: brief header.* [YT:gdPY4W72-N0] [YT:n2i1uzfD3VE]
- ★ **Aspect ratio chosen for content, stated first.** The ratio is justified by what the shot must stress (subject scale vs environment). It is not left at the default and not used as a mere crop. Wide frames prefer 7:3 or 3:2 over 16:9 for a less symmetrical frame. *Ev: settings line + one-line reason.* [YT:u7EI0Z-0ULE] [YT:t0dgrFHEcwM]
- ★ **Every block filled, one slot each.** Shot type, subject and action, environment, color scheme, camera/lens/film, composition, mood, lighting, textures, details. Count the slots. Any skipped block is one the model invents. *Ev: prompt, blocks labeled or comma-separated.* [YT:PJ347ccVJBs] [YT:QLbjv3CbfIo]
- **Holding element first.** The first term is the thing that must star (subject, or the holding category such as `photo`/`editorial`/`documentary`). If a secondary element comes first, FAIL. ⏱ Midjourney word-order finding, n.d.; still applied 2025-10. *Ev: first term of prompt.* [YT:aBgRhbYlF6Q] [YT:NmIcjfPNcsE]
- ★ **Anti-default composition written in.** The prompt or system rule rejects the centered, front-on, camera-facing default (asymmetry rule, off-balance subject, cropped framing, "never looking at the camera"). The fold-in-half test on the output passes. ⏱ Nano Banana / ChatGPT default centered, 2026-02. *Ev: prompt line + output.* [YT:AOuXCRzjsS0] [YT:AxV8TR3BdqI]
- **No artist, film, director or real-person names; no copyrighted image as reference.** Any name = automatic FAIL for commercial work. Build the look from composition/color/lighting/equipment blocks instead. *Ev: prompt + reference list.* [YT:dcrhhIKNaRQ] [YT:aBgRhbYlF6Q]
- **Actions described mechanically, not interpretively.** Poses and actions read as instructions to someone who cannot see ("bottle in his right hand, parallel to his face"). An emotion word comes with its mechanism. *Ev: subject/action block.* [YT:QLbjv3CbfIo] [YT:JskVAZqt34w]
- **Face specified** when a face is visible: expression, mouth, eye direction and one distinct feature. Without them the output gets the blank model face. *Ev: prompt.* [YT:JskVAZqt34w] [YT:26bjN6CwwJs]
- **No contradictory terms.** Color words vs a B&W film stock, low angle vs shoe detail, midday sun vs light from below. One contradiction = FAIL. *Ev: prompt read end to end.* [YT:dcrhhIKNaRQ]
- **Routed by job, with date.** Look/presentation/environment → Midjourney. Exact product, small text, logos, likeness, edits → Nano Banana Pro or GPT Image. A brief that forces product text through Midjourney = FAIL. ⏱ routing as of 2026-02 to 2026-06. *Ev: tool line.* [YT:Rzr8TDN_0y8] [YT:AOuXCRzjsS0]
- **Type and logos are not generated into the image** for layout work. Text and logos go in the layout, editable. ⏱ 2024-10 to 2026-02. GPT Image 2 handling short text dates from 2026-05. *Ev: brief.* [YT:wlsmAeMQNEM] [YT:X-Nm3NGvrTE]
- **Settings come only from the canon, with version and date.** No invented stylize/chaos/weight numbers. Photoreal people sit at modest stylize (his 90–100; Fast Hours 50–250). ⏱ Midjourney 2024-10 / 2025-10; V8 stylize compressed, 2026-04. *Ev: settings line.* [YT:EBSPo2XCml8] [YT:u7EI0Z-0ULE]
- **Pass/fail stated for the first test**, judged against references and goal: scroll test, plus reverse-image-search for anything commercial. *Ev: brief footer.* [YT:dfjMjg_Cy7M] [YT:dcrhhIKNaRQ]

## T2. Fix an AI-looking asset (image or clip; "looks AI-made", "too polished")

- ★ **Tells named with evidence, in his checklist order.** Each tell points at the asset: symmetry (fold it in half), odd-shaped features, too-smooth skin, off eyes, jewelry physics, stray hair wisps, no noise. Then the warm cast, too-sharp finish and sameness. "It looks AI" with no located tell = FAIL. *Ev: annotated output.* [YT:NmIcjfPNcsE] [YT:zPIBzQRJVT8]
- ★ **Bias split from real flaws.** If the only evidence is a reviewer's label, the fix plan includes an unlabeled third-party or LLM test before re-prompting. Clients picked whichever image was labeled real. *Ev: plan step.* [YT:Rzr8TDN_0y8] [YT:t0dgrFHEcwM]
- ★ **One change per pass, edit last.** The repair order changes one thing at a time, puts the editing model at the end and keeps passes few. Chained edits degrade the image (Nano Banana Pro erase/replace blurs, ⏱ 2026-01; Nano degrades after 3–4 successive edits, Fast Hours ⏱ 2026-09). *Ev: numbered repair list.* [YT:haCwSYl99ks] [YT:MJZjmv6HMKA] [YT:_Ldhm8qB_JU] [Jamey: YT:EWmtRROWEE8]
- **Structure checked before rewrite.** Before any new wording: reorder, check the ratio, hunt contradictory terms, find the one word that broke it. *Ev: diagnosis notes.* [YT:dcrhhIKNaRQ] [YT:gdPY4W72-N0]
- **Warm yellow-green cast graded cooler.** Hue shifted from green toward purple, plus texture, noise, a little darker and a vignette. Or add `35 mm`/`16 mm` to a bare `cinematic still`. ⏱ ChatGPT-style cast, 2025-10 to 2026-08. *Ev: before/after or grade values.* [YT:oKQd-ZumqCA] [YT:NmIcjfPNcsE]
- **Skin fixed by naming what makes skin real**, plus `no airbrush skin no beauty retouching`. Not "increase realism". Stacked-edit drift is fixed with `decrease saturation and warmth by 50 percent`. ⏱ Fast Hours, 2026-09. *Ev: edit prompt.* [YT:qVWfoe0voIk]
- **Lo-fi/candid looks not upscaled; grain added.** Too sharp and polished is "another AI indicator". ⏱ 2024-10 to 2026-02. *Ev: pipeline step.* [YT:SQIGjY_Rs2s]
- **Pixel problems go to Photoshop.** Banding, tiny logos, floating earrings, client detail drift: retouch by hand. No more re-prompting. Social work may let drift go; client work may not. *Ev: repair list.* [YT:MJZjmv6HMKA] [YT:oKQd-ZumqCA] [YT:X-Nm3NGvrTE]
- **Small element that won't add is built elsewhere** and brought back as a reference, with only that zone selected. Not re-prompted five more times. *Ev: repair step.* [YT:kR05Q2WxhCA] [YT:k7UtYDkFGQs]
- **Stakes decide realism.** If photoreal itself is the tell, the plan changes style or adds deliberate imperfection. If the brand has risk tolerance, it goes obviously AI. A trust-asking AI face (UGC) is flagged as a deception risk. *Ev: recommendation.* [YT:SbDupYyGXac]
- **Re-check closes the loop.** Scroll test ("have you seen this today?"), "does it feel like AI?", a reverse-image-search if commercial, shown unlabeled. *Ev: final check block.* [YT:dfjMjg_Cy7M] [YT:P3w112Qr-2s]

## T3. Consistency system / brand look (reference pack, style card, system prompt for a brand or for DR's own look)

- ★ **The look written as fixed blocks; variations change 1–3 blocks only.** The recipe shows which blocks are frozen ("the brand of the image") and which are variables. If a sample variation changes more than 3, FAIL. *Ev: recipe + sample variations.* [YT:aBgRhbYlF6Q] [YT:34FQ8Ewa9ek]
- ★ **References carry the look; the prompt carries only the scene.** With the pack attached, the per-asset prompt is the subject, the action and maybe the angle. If it re-describes mood, light and color every time, FAIL. *Ev: per-asset prompt.* [YT:jP9vWmf0TG4] [YT:Rzr8TDN_0y8] [Jamey: YT:EWmtRROWEE8]
- ★ **Teammate-runnable.** Someone other than the builder can run it by changing named variables only. Inputs are exposed and the rest is locked. "A prompt that works only for you is pointless." *Ev: handoff page.* [YT:zPIBzQRJVT8] [YT:N-tmQ_Can_o]
- **Reference pack sized and marked.** Images are numbered, each marked style or subject, and the pack size is justified. 1–3 images act like a token, ~5 is tight, 20–30 varied is the classic board. ⏱ Midjourney boards, 2025-10. *Ev: pack list.* [YT:gdPY4W72-N0] [YT:A4ZvuMXGQvY]
- **Image vs style reference used for the right job.** Image reference = construction, style reference = aesthetic. Image weight is checked first. ⏱ Midjourney, 2024-10 / 2025-10. *Ev: settings.* [YT:34FQ8Ewa9ek] [YT:Fa79Iv3QFJk]
- **Board failure handled by removing, not prompting.** Dominant or casting images are deleted or cropped, and faces/angles are diversified. Prompting a removal = FAIL. *Ev: board change log.* [YT:gdPY4W72-N0] [Jamey: YT:2RD3FP5iWJY]
- **System prompt is generic, with a rule per observed failure.** No hard-coded brand values in the rules ("say shoes, not teal shoes"). Brand profile and color are variables. Limits section present. *Ev: system prompt.* [YT:PJ347ccVJBs] [YT:EaENLPTAt2E]
- **Products: unseen sides built, not trusted.** Reference pillars (rear, side, rear three-quarter) or a nine-angle sheet come before fanning out. Scale comes from a 3D or diagram reference, never typed measurements ("It'll never come out correct"). ⏱ Nano Banana, 2025-10; scale, 2026-09. *Ev: reference pack.* [YT:nhDriHWatHw] [YT:N-tmQ_Can_o]
- **No custom-trained brand model as the default.** Style lives in references, a style card or a system prompt. Trained models go stale ("the AI of two months ago"). ⏱ 2026-07. *Ev: architecture choice.* [YT:FGJCBhAiQJk]
- **Retest battery named.** A fixed 10–15 prompts plus known failure points (stairs, reflections, hands, legs) to rerun on each new model. No verdict before 3–4 weeks. *Ev: maintenance section.* [YT:AxV8TR3BdqI] [YT:F6P2EAfAwjw]
- **Handoff pack per Jamey** when a client or team takes it over: final prompt, profiles, references, a sample set, and a master prompt per product listing what the model gets wrong every time. *Ev: handoff list.* [Jamey: YT:EWmtRROWEE8] [Jamey: YT:_r7NUcM41Kc]

## T4. Video clip (image-to-video, keyframes, Higgsfield/Seedance/Kling/Veo)

- ★ **Motion baked into the start still.** The start frame is mid-action: spinning wheels, motion blur, mid-stride, hands up. A static subject facing the lens = FAIL. *Ev: start frame + its prompt.* [YT:swamNhl1pIs] [YT:_nT6fav4qFA]
- ★ **Direction and mechanics stated literally.** Heading (`driving towards us`, `walking right`), physics and head/eye beats are scripted. "Natural" does not count as an instruction. *Ev: video prompt.* [YT:k8rciHNdlvs] [YT:YD5V0hKlRew]
- ★ **Clip is graded and doctored before use.** Color correction is a pipeline step. Raw generation shipped = FAIL. *Ev: post step.* [YT:haCwSYl99ks] [YT:oKQd-ZumqCA]
- **Short prompt first:** shot or camera move + subject in action + style. It expands only after a failure. With a start frame, the prompt drops look words and spends them on camera and subject motion. *Ev: prompt length/structure.* [YT:YD5V0hKlRew] [YT:AOuXCRzjsS0]
- **Brand elements pinned.** Logos, text and product are held by an end keyframe or last-frame generation (transparent PNG). They are not left to survive a free camera move. ⏱ Runway last-frame, n.d.; Kling start+end (Fast Hours), 2026-02. *Ev: keyframe plan.* [YT:YD5V0hKlRew] [YT:SbDupYyGXac]
- **Keyframe pairs related, not identical.** Some variance, with the subject off-center and travelling. Mismatched details read as morphing. *Ev: frame pair.* [YT:2sY91XsiRuw] [YT:swamNhl1pIs]
- **Spatial or multi-angle scenes blocked first.** three.js previs → render as the reference video. Not raw text-to-video. ⏱ Seedance workflow, 2026-09 to 2026-10. *Ev: pipeline.* [YT:tlqnW1sp5X4]
- **Cheap lane before premium credits.** Tests run in a fast or cheap model (Grok, Minimax, low-res), with a checkpoint before Seedance or Veo spend. ⏱ 2025-10 to 2026-09. *Ev: test plan.* [YT:AxV8TR3BdqI] [YT:5tjzTF6MR5A] [YT:N-tmQ_Can_o]
- **Long pieces chained from short controlled segments** so a one-word change doesn't rerun 30 seconds. *Ev: segment plan.* [YT:N-tmQ_Can_o]
- **Failure fixed by hunting the one word** (or a filmmaking cut that hides drift) before a rewrite. "70% of AI video is understanding how to troubleshoot it". *Ev: diagnosis.* [YT:hAnYA2wJaZ4] [YT:gdPY4W72-N0] [YT:SbDupYyGXac]

## T5. Ad creative at volume (pipeline, batch engine, node workflow for DR or a client)

- ★ **Choke point named before any tool.** The plan maps brief → execution and names the single friction point (late copy, copy edits, resizing, localization). If the plan opens with a tool, FAIL. "the creativity is not the problem it's the process". *Ev: first section of plan.* [YT:zPIBzQRJVT8] [YT:AxV8TR3BdqI] [YT:EP3WupKVL50]
- ★ **Begin at the end.** One good output was made by hand and is shown before the system is built. The plan says how to get it 50 times and what inputs that needs. *Ev: the hand-made sample.* [YT:PJ347ccVJBs] [YT:jBcL-XrHqzY]
- ★ **Built only from proven winners.** Templates or prompts are seeded from the highest-performing ads, and the brand context is primed: overview, guidelines, tone, past winners, audience, copy caps. *Ev: input list.* [YT:dcrhhIKNaRQ] [YT:aBgRhbYlF6Q]
- **Copy has hard length caps** in the generator (his: headline under five words, CTA under two). Outputs stay editable (Figma template layers, not flattened). *Ev: system prompt + output format.* [YT:aBgRhbYlF6Q] [YT:dcrhhIKNaRQ]
- **Feeder LLM outputs prompts only:** each ends with a star or asterisk, with no commentary and no special characters. The Limits line says so. *Ev: system prompt.* [YT:PJ347ccVJBs] [YT:N-tmQ_Can_o] [YT:AxV8TR3BdqI]
- **System prompt follows his skeleton** (2026-09: role, fixed inputs, tasks, identity lock, environment, format and look, lens, assembly order, output-only line). It is generic, and the changing part is its own variable. *Ev: system prompt.* [YT:N-tmQ_Can_o]
- **Evaluation and guard rails built in.** A grade-and-redo loop with a stop rule (five runs, then stop). Branching is capped ("you can make a million edits doesn't mean you should..."). A human finishes. *Ev: QA gate.* [YT:xLLtYn932qY] [YT:2sY91XsiRuw] (million-edits line verified in 2sY91XsiRuw) [canon: mindset_voice_bio.md, "Curation without paralysis" for the five-run stop] (five-run stop not found in transcripts)
- **Volume sized to need, with the math shown.** The images × copy × CTA × ratios math appears with a target (20 or 200 often enough), not 1,000 by reflex. *Ev: batch plan.* [YT:o-D4-EYP1Qc] [YT:dcrhhIKNaRQ]
- **Node tool picked by who must run it** (Flora entry, Weavy mid, Comfy for engineers). Packaged so a teammate types one word: system-prompt node locked, inputs exposed. ⏱ 2025-11 to 2026-09; Midjourney has no API. *Ev: tool choice + handoff.* [YT:qv9_8mJT7h4] [YT:N-tmQ_Can_o]
- **Every tool swappable.** No step depends on one vendor. Files are portable ("screw the models"). *Ev: architecture.* [YT:_az4W2z5Fqw] [YT:Dl64zUCJniU]
- **Second repeat becomes a skill, stripped to generic.** Brand and product details are removed from the reusable part. *Ev: packaging step.* [YT:Dl64zUCJniU] [YT:N-tmQ_Can_o]

## T6. Tool and model choice, new-model verdicts ("should we switch to X", "is the new model good")

- ★ **Verdict is dated and hedged by time.** Every model claim carries its canon date. No final verdict on a model under 3–4 weeks old, and the answer says so. *Ev: claim + date.* [YT:F6P2EAfAwjw] [YT:wlsmAeMQNEM]
- ★ **Judged on our prompts, not launch reels.** The recommendation rests on a fixed 10–15 prompt battery plus known failure points, run by us. Launch marketing is not evidence. *Ev: test table.* [YT:AxV8TR3BdqI] [YT:ZY5GqIXkET4]
- **Model type sorted first** with the short-prompt test (`woman in the park`): more detail back = creative, less = coherent. The job is then assigned accordingly. *Ev: test result.* [YT:ssxPDDjSVY0]
- **Edit tools pass the one-click test** or are dropped. No time spent hacking around one. ⏱ 2025-12 to 2026-04. *Ev: test note.* [YT:92I8aNhyxwM] [YT:EaENLPTAt2E]
- **House defaults named and written against** (ChatGPT image yellow-green and 3:2 only; Flux flat "flux face"; Nano Banana stock face). ⏱ 2025-10 to 2026-06. *Ev: recommendation notes.* [YT:2sY91XsiRuw] [YT:IppsMX-LqDk] [YT:AOuXCRzjsS0]
- **Wrapper chosen only for its added layer.** The same model through a wrapper gives the same result. ⏱ Jamey, n.d. *Ev: tool rationale.* [Jamey: YT:N-6LCrvxHIs] [Jamey: YT:61_srA-xmts]
- **Rory/Jamey splits shown, not averaged** (JSON system prompts vs "very anti-prompt"; Midjourney for client work). *Ev: answer text.* [YT:ssxPDDjSVY0] [YT:AxV8TR3BdqI] (Rory: JSON-style prompts) [Jamey: YT:EWmtRROWEE8] [Jamey: YT:N-6LCrvxHIs] (Jamey: image-led, one-word prompts) [Jamey: YT:2RD3FP5iWJY]

## T7. Selling and pricing AI creative (DR offer, client pitch, terms)

- ★ **No invented rate.** The canon has no rate card. Any price must be Ivan's or labeled as Jamey's ($10–15K contracts, hers). A coach-made number = FAIL. *Ev: offer page.* [YT:dcrhhIKNaRQ] [Jamey: YT:EWmtRROWEE8]
- ★ **Sold on volume, speed and consistency, not hours.** The value line is in assets and performance terms (about 5x the assets in the same time; media buyers need many creatives a week, and few win). *Ev: offer copy.* [YT:dcrhhIKNaRQ] [YT:PJ347ccVJBs]
- ★ **AI disclosure and data handling stated.** Clients are told AI is used, and the 2026-07 counter-case is noted. No proprietary data goes into Midjourney or ChatGPT unless on Enterprise. *Ev: terms section.* [YT:aBgRhbYlF6Q] [YT:lGneI_bllZ4]
- **Demo, not deck.** The pitch opens with a demo-able starter on the prospect's own asset (resizing, localization): "watch me do this in 20 seconds". Showing the big node package = FAIL. *Ev: call plan.* [YT:6w6pKyCCQFg] [YT:N-tmQ_Can_o]
- **Audit first, price in the middle**, then how you'd work together, then end on "any questions". *Ev: call order.* [YT:6w6pKyCCQFg] [YT:xLLtYn932qY]
- **Success measured on time, volume, revisions and LTV**, not one month of P&L (his revisions went from 3.4 to 1.7). *Ev: KPI section.* [YT:zPIBzQRJVT8] [YT:2H0AluIDW50]
- **Copyright stated as he states it.** Fully AI output treated as stock; a human edit is copyrightable; reverse-image-search every commercial asset. Plus "not a lawyer". ⏱ US view stated Nov 2023 to early 2024. *Ev: terms section.* [YT:E41H2WIHMXg] [YT:dcrhhIKNaRQ]
- **Amplify, not replace.** The offer supplements shoots and designers and does not promise to replace them. *Ev: offer copy.* [YT:EP3WupKVL50] [YT:dcrhhIKNaRQ]
- **Something left behind.** A packaged workflow or app, or (Jamey) a master prompt. *Ev: deliverables list.* [YT:N-tmQ_Can_o] [Jamey: YT:EWmtRROWEE8]

---

## Universal checks (every output)

- ★ **Retrieved before writing.** At least 3 searches run. The work uses at least 3 retrieved items, cited as [YT:id] (Jamey and Fast Hours items labeled as such).
- ★ **No invented quotes, numbers, prompts, settings or dates.** Every quoted line exists verbatim in a retrieved hit (≤15 words). Prompts built for Ivan are labeled *built from the formula, untested*.
- ★ **Did the work.** If Ivan gave a task, the output is the finished thing: a ready-to-paste brief, a repair list, a recipe or a pipeline. It is not a list of questions. Questions only for inputs that are missing and block the work, and only after doing everything possible without them.
- ★ **Every tool/model claim dated.** Each carries its canon date (or n.d.), plus the warning that tools change month to month. *(Added for this coach: models age faster than any other canon.)*
- **In voice.** Candid and jokey. Analogies flagged as analogies. Names his limits before a claim ("I have to be totally candid"). Cooking-show narration for process. Short. Signature lines used sparingly and verbatim. Jamey cited by name, Drew and guests named, never voiced as Rory.
- **Ends with one move.** One test to run next with its pass/fail, why in one line, and what would change the plan.
