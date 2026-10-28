# UI components and visual details (Michal Malewicz)
> Sources: [YT:<id>] = YouTube video id; (YYYY-MM) = upload month (approximate); "mentions" = number of separate evidence items.

## PART 2. UI components and visual details (buttons, cards, forms, icons, depth, states, spacing systems)

### Rules (ranked by how often they say it)
- **"Don't go over the top": subtle, one or two effects per screen** — Shadow opacity ≤50%, gradient hues 10–30 apart, one big shadow and one heavy object per screen; never stack gradient + shadow + inner shadow + glow, or border + inner + drop shadow on a card. Cut decoration with no job ("design is reduction"). [YT:FBDVzr0peO4, YT:Kqg3vN1ms2E] (2025-10, 2026-08) · mentions 16
- **Center and align optically with helper squares; no formula** — Fonts render differently: squares on all sides of a label or icon, nudge 1 pt (0.5 in portfolio work), redo after every font-size change; align text to a capital letter, not a lowercase k. [YT:ThmHV38Ecqk, YT:FBDVzr0peO4] (2025-10) · mentions 13
- **Never two identical buttons; derive weaker ones from the primary** — Mutually exclusive answers to one question get unequal weight; login stronger than register; one strong CTA per screen. Counter-case: Send / Receive / More in a finance app can be equal (separate questions): logic, not rule-following. [YT:FBDVzr0peO4, YT:Kqg3vN1ms2E] (2025-10, 2026-08) · mentions 13
- **Shadow math** — Y never negative (shadows point down), blur at least 2x Y, negative spread, opacity ≤50% (cards 30–40%). Bigger Y + blur = closer = attention: one big shadow per screen, small blur/Y for grids; an upper card's shadow never falls on a lower one. [YT:FBDVzr0peO4, YT:ThmHV38Ecqk] (2025-10) · mentions 13
- **Function stays accessible; decoration is where you experiment** — Text, buttons, fields, switches, nav pass AA contrast and size; decoration may be low contrast if removing it loses no function. "never sacrifice contrast for the sake of being original"; no experiments on login/checkout; no decoration on the product screen. [YT:FBDVzr0peO4] (2025-10) · mentions 12
- **Button size and label padding** — Height 44 min, 50 sweet spot, 54–60 his own, over 60 too much. Label ~1/3 of height, 16 pt minimum, bold; more padding left/right than top/bottom; small buttons two W's each side, one W top/bottom. [YT:FBDVzr0peO4, YT:ThmHV38Ecqk] (2025-10) · mentions 11
- **Mobile spacing set (8 base)** — 32 screen margin (16 for a card on a full-colour screen), 24 card/modal padding, 24–40 between stacked buttons and never less, back arrow and navbar icons 32 from the edge, floating tab bar 16 from edges. [YT:FBDVzr0peO4, YT:ThmHV38Ecqk] (2025-10) · mentions 10
- **Shadow colour from the surface or accent hue; one light source** — Pick the background/accent, brightness −10 to −20, desaturate; gray shadows for white-on-white; cutout shadow = darker shade of the object; one light direction, or it will "make our brain go crazy". [YT:FBDVzr0peO4, YT:ThmHV38Ecqk] (2025-10) · mentions 10
- **Nested corners: diagonal distance equals side distances** — Measure inner-to-outer corner on the diagonal and match the top/left/bottom gaps; lower the inner radius if uneven and break the grid when it looks right. Button radius concentric with card radius, not identical. [YT:w2mNSOWiZbU, YT:FBDVzr0peO4] (2026-09, 2025-10) · mentions 9
- **Radius: start low, 8 is the safe number** — Beginner: 0–8, first app 4 (a high radius forces pill fields, and the label above a pill field belongs to no edge). Hi-fi: start 16, 32 max when starting out; "fully sharp corners aren't really that user friendly". 2021: 4 or 2, 8 really good. [YT:ThmHV38Ecqk, YT:FBDVzr0peO4] (2025-10) · mentions 9
- **Touch targets: 44 minimum, icons at most half** — Every tappable 44x44 (invisible square, 0% opacity); menu rows 48; checkbox 40 is the exception. Mobile web CTA above 52 and under 64, at most two form fields; tiny targets add anxiety. [YT:ThmHV38Ecqk, YT:q8yUIbRiNRc] (2025-10) · mentions 9
- **Fields: outlined, white fill, shorter than buttons** — Stroke inside, 1 pt (dashboard) or 2 pt (playful B2C), hue of the secondary button, darker so it stays visible; text left-aligned. Field 40–44 vs button 50–60: "buttons should always be visibly taller than the form fields". [YT:FBDVzr0peO4, YT:w2mNSOWiZbU] (2025-10, 2026-09) · mentions 9
- **Charts, tables, sample data: build by hand, make it plausible** — Draw in the design tool (never PowerPoint, plugin or auto charts) with one spacing system (60 and 120). Round axis steps, "0" not "0K", sorted sample data, survey bars sum to 100%, no Lorem Ipsum ("lazy design"). [YT:w2mNSOWiZbU, YT:_PJLefMZwko, YT:N-34Q9mhwvs] (2026-09, 2026-03, 2025-11) · mentions 9
- **Tables: text left, numbers right, identical rows** — Text left-aligned to header, numbers and headers right-aligned, never centered; 24 between columns; capital-letter-to-line distance identical above and below each row ("crucial"); money bold, secondary names lighter gray. [YT:w2mNSOWiZbU, YT:_PJLefMZwko] (2026-09, 2026-03) · mentions 8
- **Navigation: never complicate it, tabs first** — Tab bar (2–5 tabs) is the preferred mobile pattern; hamburger is "likely one of the worst navigation styles you can ever choose"; animated concept navs lengthen the task; pill navs clash with rounded list items. [YT:FBDVzr0peO4, YT:ThmHV38Ecqk] (2025-10) · mentions 8
- **Know the conventions, then bend them; a button must look like a button** — Odd fonts and thumbnails add friction; a custom UI gets a custom toggle behaving like native; all-kit work looks generic; "We don't always have to follow the platform rules". [YT:ThmHV38Ecqk, YT:Kqg3vN1ms2E] (2025-10, 2026-08) · mentions 7
- **Tune the map** — Grayscale/monochrome or a light hue tweak, never generic full colour; the tuning is "what actually differentiates a great design from a mediocre one". Pins get white border + shadow; water blurs never over streets. [YT:FBDVzr0peO4, YT:w2mNSOWiZbU] (2025-10, 2026-09) · mentions 7
- **Icons: one set, one stroke, stroke matches text** — Same stroke width, about the weight of an adjacent letter stem; never mix filled colour, thin/thick outline, solid white; only variance: outline icons with the selected one filled. [YT:Kqg3vN1ms2E, YT:ThmHV38Ecqk] (2026-08, 2025-10) · mentions 6
- **Proximity: groups apart more than inside** — 32 divides groups, 24/16 inside; a separate element (button under text) gets 32; practically the most important rule. [YT:w2mNSOWiZbU, YT:ThmHV38Ecqk] (2026-09, 2025-10) · mentions 6
- **Gradients: same hue, close, both stops 100% alpha** — Brightness 10–20 apart, saturation ~10; subtle ±3–4 lightness; darker at the bottom ("that's just how our brain works"); a solid works if vibrant. [YT:FBDVzr0peO4, YT:ThmHV38Ecqk] (2025-10) · mentions 6
- **Cutout craft** — Clean mask artifacts zoomed in; match exposure, saturation, temperature across photos; shadow = blurred duplicate below plus small contact ellipses, never over the image. [YT:FBDVzr0peO4] (2025-10) · mentions 6
- **Overlap lifts fidelity** — Product over card instantly raises it; a cutout exceeds the card by 16 at most (even a couple of pixels); if one circle overlaps the card the next shouldn't. [YT:FBDVzr0peO4, YT:w2mNSOWiZbU] (2025-10, 2026-09) · mentions 5
- **Neumorphism: decoration only, never buttons** — Fine on a background or non-essential shape; his complaint is using it on every element; beautiful "if done right, and if not overdone" (2026-06). [YT:FBDVzr0peO4, YT:psyw2_j_5jk] (2025-10, 2026-06) · mentions 5
- **Don't coin new "morphisms"** — Glass is more than a material (translucency shows what is underneath); metal, mirror, leather are opaque skeuomorphism; "We don't really need another morphism". [YT:psyw2_j_5jk] (2026-06) · mentions 5
- **Text is tinted dark gray, not pure black** — Headline in the background hue at HSB brightness 8 (20 max); dashboard text 2E2E2E, only the logo pure black. [YT:FBDVzr0peO4, YT:w2mNSOWiZbU] (2025-10, 2026-09) · mentions 4
- **Plasticity: tangible, not loud** — Flat minimalism plus skeuomorphic touches, "it's about making it tangible even just a little bit"; real experimentation pushes materials and depth, not a radius moved by two points. [YT:w1kITFbUU1U] (2024-10) · mentions 4
- **Desktop admin is not stretched mobile** — Side menu 2 of 12 columns; collapse to icons or a top menu if tables scroll sideways; buttons 2 columns wide, right-aligned. [YT:w2mNSOWiZbU] (2026-09) · mentions 3
- **State never relies on colour alone** — Selected pin changes colour and grows (48 max); closed status gets a badge (see Fix library). [YT:w2mNSOWiZbU, YT:ThmHV38Ecqk] (2026-09, 2025-10) · mentions 2
- **Dial effects back for finance, banking and professional services** — they have their own rules. [YT:FBDVzr0peO4] (2025-10) · mentions 1

### Methods (named or ordered)
#### Red-square method (helper squares on an 8-pt grid)
- When they use it: every spacing, centering and width decision; layouts by hand before auto layout.
- Steps: 1. Drop red squares from the 4/8/16/24/32/48 scale between elements. 2. Gaps between groups bigger than inside (32 divides, 24/16 inside). 3. Squares on all sides of a label or icon, nudge 1 pt until centered. 4. Reusable button: stretch the label box to touch 16 squares at both ends, center-align, group. 5. Even spacing: squares at both ends, four copies between, distribute horizontally, align content to them. 6. Desktop grid: 12 columns, gutter 32, column 64, 1120 wide.
- Their example: 390 tab bar: 2 tabs = 195, 3 = 130, 5 = 78; 4 = 97.5 and no decimals, so 96 wide with three 2-pt gaps; one border line between tabs, not two.
- Sources: [YT:ThmHV38Ecqk, YT:w2mNSOWiZbU, YT:FBDVzr0peO4] (2025-10, 2026-09)

#### UI audit order (measure before judging taste)
- When they use it: reviewing any UI or portfolio screen.
- Steps: 1. Equal left and right margins. 2. About four spacing values on an 8 base (outer 20, inner 16, cards 24, bigger gaps between groups). 3. One typeface, 2–3 sizes (12/16/20). 4. One icon pack, stroke matched to text. 5. Lighter = closer (white cards on a ~95% lightness page). 6. One effect in one place. Fix in order: alignment, fonts, hierarchy, icons, colour.
- Sources: [YT:Kqg3vN1ms2E] (2026-08)

#### Primary → secondary → tertiary from one colour set
- When they use it: any screen with more than one action.
- Steps: 1. Primary = vibrant gradient or solid, optional shadow. 2. Secondary = duplicate 32 below, delete the shadow, solid fill colour-picked where the primary's shadow starts. 3. Secondary text = same hue, brightness down until contrast passes. 4. Tertiary = near-gray or plain text; ghost/outline is the alternative.
- Sources: [YT:FBDVzr0peO4, YT:ThmHV38Ecqk] (2025-10)

#### Shadow build: drop shadow, then blurred rectangle
- When they use it: the default shadow looks bad or you need edge control.
- Steps: 1. Effects "+", colour-pick the background, HSB brightness −10 (88 or 78). 2. `Y 16`, blur at least double, negative spread (Shift+arrows change by 10). 3. Still fuzzy: delete it, add a rectangle coloured from the first shadow, layer blur 40 (100 too much). 4. Slide it under the card's bottom edge so it shows only there; group as "card with shadow".
- Sources: [YT:FBDVzr0peO4] (2025-10)

#### Practice process for high-fidelity components
- Steps: 1. Recreate popular Dribbble shots (background + card). 2. Make many versions of the key screen (duplicate, then remove). 3. Experiment with backgrounds first, then icons. 4. Test on a real phone (min 14 pt text, 10 only for tab labels). 5. Run an AA contrast plugin.
- Sources: [YT:FBDVzr0peO4] (2025-10)

### Recipe library (exact, reusable)
- **Primary button, hi-fi** — Gradient: same colour on both handles, diagonal, lightness −3/−4 one side and +3/+4 the other, darker at the bottom. Shadow = darkest gradient shade, brightness −20 (95→75), `Y 12 / blur 24 / spread −8`, opacity ≤50% (also `8/16`, `16/32`); small `Y 4 / blur 8 / spread −2`; never X. [YT:FBDVzr0peO4, YT:ThmHV38Ecqk] (2025-10)
- **Button inner shadows and label shadow** — Inner: white `X 4 / Y 4 / blur 8` (≤50%, he used ~30%; more looks plastic) + darker `X −4 / Y −4 / blur 8` (brightness −10 to −20); no blend modes. White label on a bright button: text shadow in accent hue, lightness −10, alpha 50, `Y 2 / blur 4` (orange: `Y 1 / blur 2`), same on its arrow; none on light secondaries. [YT:FBDVzr0peO4, YT:ThmHV38Ecqk] (2025-10)
- **Secondary and combo buttons** — Pale fill = accent at lightness ~80, no gradient, no border (or ghost: border + accent text), dark label. Combo `Already have an account? Log in`: one label, description medium, action extra bold. [YT:ThmHV38Ecqk, YT:FBDVzr0peO4] (2025-10)
- **Form field** — White fill, stroke inside, colour = main colour eyedropped, saturation ~20 and lightness ~80 (60–70 for more contrast), radius 4, label 14 medium. Icons from one set in the text colour, 16 from the edge; placeholder italic, label size, lighter. [YT:ThmHV38Ecqk, YT:FBDVzr0peO4] (2025-10)
- **Dashboard form controls (2026)** — Label 14 bold, field 40 high, 1 pt gray stroke, 4–8 label gap, 32 margins; two columns (320−24)/2 = 148; `$` 16 from left; valid = green stroke. Submit full width, 2E fill, white text, radius 4, height 44. [YT:w2mNSOWiZbU] (2026-09)
- **Dropdown and toggle** — Dropdown = duplicated field, chevron-triangle from a helper square (fill 3 steps darker than the outline), selected value bold and darker than the label. Toggle: height 50, width at least 150%, 4 inset; off = hue darkened, on = CTA properties + dark bottom inner shadow `−4/−4 blur 8`, no outer shadow. [YT:FBDVzr0peO4] (2025-10)
- **Checkbox, radio, slider** — Checkbox 40x40, radius 4, 16 to label. Radio = checkbox with circle radius, inner dot inset 8 in CTA gradient, selected label gets tab weight. Slider track `320x8`, thumb 40x40 with shadow in track colour at 50% and a field-colour border. [YT:FBDVzr0peO4] (2025-10)
- **Tabs** — Segmented: two rects 50 high, radius 4, inner corners 0, 2.5 stroke, white fill. Underline: bar 60 high, shadow `blur 32 / Y 16` low opacity, 4-pt line exactly half the bar (150 of 300); glow = same-blue gradient rotated 180°, 15%→0%. [YT:FBDVzr0peO4] (2025-10)
- **Mobile tab bar** — White rect, top border only; labels medium 10, baseline 8 above the safe area, 16 icon-to-label; active = radius-8 accent rect behind icon + label (8 above label, 8 from bar top), inactive labels lightness +20; safe alternative: full-tab radius 0, white text. Floating bar 16 from edges, shadow blur 2x Y. [YT:ThmHV38Ecqk, YT:FBDVzr0peO4] (2025-10)
- **Hamburger drawer** — About 2/3 width, full height, accent fill, the other 1/3 a darker accent overlay; items 48 high stacked touching (24 apart is too far); icon box 24 (icon ~16), 16 to text, 32 left margin; depth = diagonal gradient + layer-blurred rectangle; selector = 4-pt left line + gradient 20%→0%. [YT:ThmHV38Ecqk, YT:FBDVzr0peO4] (2025-10)
- **Dashboard side nav (2026)** — Text 14 medium 2E2E2E, icons in 16x16 frames; selected = dark radius-8 rect, white icon/text, inset 24, 44 high (green stays for notifications); collapsed ~40 between icons, expands over the table on hover; count badge 18 high, radius 32. [YT:w2mNSOWiZbU] (2026-09)
- **Cards and lists** — Tile: white, border = field colour at saturation 10 / lightness +10, radius 8, 32 from sides, 16 padding. Category cell: title 16 semibold, count 12 desaturated, 44x44 photo radius 4. Product tile: photo 88 ("people buy with their eyes"), 24 between tiles. Card fidelity: photo rounds top corners only (8), inner elements 4, shadow tinted from the photo `Y 16 / blur 32`; dark cards: radial gradient ≤20 apart, no shadow. [YT:ThmHV38Ecqk, YT:FBDVzr0peO4] (2025-10)
- **Pop-up, bottom sheet, scrim** — Overlay black 70% (or accent 50–70%, lightness 20–30); scrim = desaturated very dark gradient, solid at bottom → transparent at top; modal padding 24, buttons 8 apart (16 stacked), top corners 32, a different width than the card behind (e.g. 16 from the edges); primary label confirms the action ("Sign out"). [YT:FBDVzr0peO4, YT:ThmHV38Ecqk] (2025-10)
- **3D inner-shadow card, neumorphic decoration** — Linear gradient both stops 100%, diagonal, darker bottom, radius 16→32; inner shadow 1 `X −8 / Y −8 / blur 16` from the darkest part, inner shadow 2 `+16 / +16 / blur 32` white; decorations get inner shadow only. Neumorphic circle: fill = background, dark `X 8 / Y 8 / blur 16` + white `X −8 / Y −8 / blur 16`. [YT:FBDVzr0peO4] (2025-10)
- **Glass** — Pass-through 100%, fill ~60%, background blur; shadow = background-colour oval, brightness −10, layer blur. Dark glass: near-black green-gray, gradient with one end almost 0 opacity, radius 24, white text, no shadows; border 1 pt inside, white→transparent. [YT:FBDVzr0peO4] (2025-10)
- **Maps** — Hi-fi: small main-green circle + thick white border + green-tinted shadow; route by pen along several streets, ≥3 pt (3→5), under markers. Dashboard: gradient `2E2E2E` → 0% behind white text; route solid traveled, dashed remaining; pins 48 px white circles with logo; FigMap 800x1200 "add 2x", dark style. [YT:FBDVzr0peO4, YT:w2mNSOWiZbU] (2025-10, 2026-09)
- **Dashboard table (2026)** — Header 12 px medium, +40–50 lightness, 12 above divider, first row 12 below, rows 24 baseline to baseline (or 16 above/below each divider); status dots 5–6 px (delivered dark green, in delivery lighter green, pending payment orange, ordered gray); sorted header = light radius-8 pill + up arrow. [YT:w2mNSOWiZbU] (2026-09)
- **Line chart** — App: sharp joins, 5 pt, area = duplicate closed, gradient to transparent. Case study (600 wide): 3 pt (2–5, never 1), round caps, 1 pt very light gridlines, labels ~7 pt (14 on web), tooltip white rounded box `Y 6 / blur 12 / 15%` + 45° square pointer. Dashboard: baseline 24 from left/bottom, gridlines 5 lightness lighter. [YT:FBDVzr0peO4, YT:N-34Q9mhwvs, YT:w2mNSOWiZbU] (2025-10, 2025-11, 2026-09)
- **Icons from primitives** — Bag = rectangle with rounded bottom corners + pen handle, subtract; pin = circle dragged to a point minus inner circle; search = circle 14 with 2 pt stroke + 2 pt line, rotate 45° (odd circle size for 1 pt lines, even for 2 pt). Repair: nearest outline icon, stroke 1.5 (or 1.2), delete shadows and tints. [YT:w2mNSOWiZbU, YT:Kqg3vN1ms2E] (2026-09, 2026-08)
- **Case-study frames and flows** — Rotate groups 13°; mockup shadow equal X/Y (24), blur at least double, tinted dark brand colour; white frame 16 pt padding (20–24 max), inner radius reduced to match; frameless `16/16/64`. Flow lines: plain → circle end, straight → diagonal bend → straight through box centers; detour lighter via the picker, not opacity. [YT:_PJLefMZwko, YT:N-34Q9mhwvs] (2026-03, 2025-11)

### Fix library (problem → fix → why)
- **Problem:** nested radii look uneven (avatar in a rounded container, 64-high map bar at radius 32, photo radius 4 in a white gap) → **Fix:** match diagonal to side distances: avatar gap 20→18 (avatar 32→36), bar radius 16, photo radius 2 → **Why:** a pill breaks the diagonal; breaking the grid "makes those elements look good". [YT:w2mNSOWiZbU, YT:ThmHV38Ecqk] (2026-09, 2025-10)
- **Problem:** closed status shown by colour alone → **Fix:** "Closed" badge (12 bold, white fill, 8 from corners, radius 2) plus grayed logo and lower opacity → **Why:** colour alone is not accessible to everyone. [YT:w2mNSOWiZbU] (2026-09)
- **Problem:** 24 between form groups, label crowds the field above → **Fix:** 32 between groups → **Why:** the label-to-field gap must read smaller than the group gap. [YT:w2mNSOWiZbU] (2026-09)
- **Problem:** Save/Cancel or primary/register look identical (very common) → **Fix:** Save solid, Cancel outlined with dark border and text; or secondary = ghost/outline or accent fill at lightness ~80, no border → **Why:** mutually exclusive answers need unequal weight. [YT:Kqg3vN1ms2E, YT:ThmHV38Ecqk] (2026-08, 2025-10)
- **Problem:** long labels, two buttons squeezed into a row → **Fix:** stack them vertically, do not shrink text → **Why:** safer for translations (German). [YT:FBDVzr0peO4] (2025-10)
- **Problem:** drop shadow left under an inner-shadow bar → **Fix:** make it dark and opaque, fill the bar white, or build a blurred rectangle instead → **Why:** it makes a fuzzy edge. [YT:FBDVzr0peO4] (2025-10)
- **Problem:** rounded top corners (32) on a tab bar end where content begins → **Fix:** let the curve end further from the content → **Why:** scrolling shows a rounded corner coming out of a rounded corner. [YT:FBDVzr0peO4] (2025-10)
- **Problem:** dark strong shadow under a map nav; pins vanishing on a colourful map → **Fix:** fading gradient mostly hidden under the navbar and pushed high (bottom card: rotated 180°, lower opacity); pin shadow `Y 4 / blur 4 / 25%`, bold pin text → **Why:** light shadow + light border = fuzzy line, so switch the card border off. [YT:ThmHV38Ecqk, YT:w2mNSOWiZbU] (2025-10, 2026-09)
- **Problem:** shadow-only floating fields → **Fix:** back to a stroke; if shadows, soft from the main colour, primary button only → **Why:** accessibility, and the thing you type into appears to float. [YT:FBDVzr0peO4] (2025-10)
- **Problem:** partial element poking out of a screen edge → **Fix:** cover with a background-colour shape or delete; check radii, overlaps, shadow colour and strength before export → **Why:** looks messy, a tiny miss matters. [YT:_PJLefMZwko] (2026-03)
- **Problem:** skills rated with ducks, stars, percentages → **Fix:** two plain lists, "tools you use daily" and "tools you're familiar with" → **Why:** scale undefined, a low score advertises weakness. [YT:Kqg3vN1ms2E] (2026-08)

### Tool and model notes (dated, newest first; these age fast)
- **AI-generated prototypes (2026-06)** — AI builds the interactive base, he tunes by hand with sliders wired to every value: "bendy buttons" (bend toward the tap, opposite side brightens, shadow shifts), used in Longevity Deck. Trend picks: camera-driven real lighting on skeuomorphic elements; hand-drawn elements against AI slop. [YT:psyw2_j_5jk] (2026-06)
- **AI-built systems (2025-12)** — Look alike (as if Shadcn and Tailwind had a baby), fine for non-consumer B2B. Tells: pill kickers, pill shapes competing with the CTA, buttons repeating the nav colour, "template card 101" (tinted icon in a rounded square), mismatched SVG icon sets. [YT:6_t66Ef0Llk, YT:3BvDDjmzYY8] (2025-12, n.d.)
- **Apple Liquid Glass (2025-10)** — "completely unreadable" and inconsistent on most backgrounds; readability is fixable, lost design sense is the real problem. His glassmorphism.com (also liquidglass.io) now builds the effect in CSS to copy. [YT:f3qjhQG2prU] (2025-10)
- **Figma (2025-10 to 2026-09)** — No iPhone 12 preset (type the size in); background blur needs layer opacity 100% with the fill lowered; FigMap for maps; charts drawn by hand, not plugins. [YT:FBDVzr0peO4, YT:w2mNSOWiZbU, YT:N-34Q9mhwvs, YT:_PJLefMZwko] (2025-10, 2026-09, 2025-11, 2026-03)

### Coaching and critique moves
- Measure before taste: run the audit order (margins, spacing values, typeface, icon pack, one effect) — [YT:Kqg3vN1ms2E]
- Adjacent buttons: one question (unequal weight) or separate processes (may be equal)? — [YT:Kqg3vN1ms2E, YT:FBDVzr0peO4]
- Sort each element into function or decoration; removing decoration must lose no function — [YT:FBDVzr0peO4]
- Build a detector for bad design and ask "How can I test it?" and, of each element, "Why are these shoes here?" — [YT:Kqg3vN1ms2E]
- Zoom out to judge consistency, zoom in to clean artifacts, check the data adds up — [YT:w2mNSOWiZbU, YT:FBDVzr0peO4, YT:N-34Q9mhwvs]
- Do not settle on the first take: rotate, resize, re-blur a cutout; duplicate the key screen, then remove — [YT:FBDVzr0peO4]
- All-white dashboard: add a few bigger, bolder, darker elements — [YT:w2mNSOWiZbU]

### Numbers they have stated
- Tap target 44; buttons 44–60 (50 sweet spot; 48 safe, 56 on the beginner course); mobile web CTA 52–64, desktop 48–52; fields 40–44; checkbox 40 (32 px mobile web) [YT:ThmHV38Ecqk, YT:FBDVzr0peO4, YT:q8yUIbRiNRc] (2025-10)
- Type: body 14–16, minimum 12, tab labels 10, badges ~10–11, button label 16+, line height 1.3–1.4 [YT:ThmHV38Ecqk, YT:FBDVzr0peO4] (2025-10)
- Radius: first app 4, safe 8, start 16, 32 max when starting out, pins 48 max; shadow opacity ≤50%, usual `Y 16 / blur 32`, spread −8; gradient 10–20 brightness apart [YT:ThmHV38Ecqk, YT:FBDVzr0peO4] (2025-10)
- Lines: chart 3 pt on a 600-wide page (2–5), 5–6+ in app/presentation; route ≥3 pt; selected-tab line 4 pt [YT:N-34Q9mhwvs, YT:FBDVzr0peO4, YT:_PJLefMZwko] (2025-11, 2025-10, 2026-03)
- Mockups: rotation 13° (12–15), shadow X=Y 24, frame padding 16 (20–24 max) [YT:_PJLefMZwko] (2026-03)
- Screen 390x844; desktop 12 columns, gutter 32, column 64, 1120 wide; trends turn in circles of about seven years [YT:FBDVzr0peO4, YT:w2mNSOWiZbU, YT:u01ZGoiLJ70] (2025-10, 2026-09, n.d.)

### References they cite
- Dieter Rams, Steve Jobs — great design is not made by asking the majority; Jobs predicted what people wanted [YT:f3qjhQG2prU]
- Teenage Engineering TP-7 and KO II recreations, Framer knob set with sound — praised tactile work [YT:w1kITFbUU1U]
- Dribbble — recreate popular shots as practice [YT:FBDVzr0peO4]
- Spotify disco-ball logo (a texture, not a trend), Figma balloon morphism (looked AI-generated) — trend examples [YT:psyw2_j_5jk]
- Shadcn + Tailwind — what AI-built systems look like [YT:6_t66Ef0Llk]

### Evolution and contradictions
- **Neumorphism** — 2026-08: red flag on every element, fine on a background [YT:Kqg3vN1ms2E]; 2026-06: accessibility issues are non-issues if contrast, hierarchy and typography are right, and he is building a full-neumorphic project [YT:psyw2_j_5jk]; 2025-10: not accessible, decoration only [YT:FBDVzr0peO4].
- **Field vs button radius** — 2026-09: fields radius 2 / 40 high, primary 4 / 44, secondary 36, so the rectangles differ [YT:w2mNSOWiZbU]; 2025-10: button radius equals field radius (4) [YT:ThmHV38Ecqk].
- **Label weight** — 2026-09: form label 14 bold, button label medium [YT:w2mNSOWiZbU]; 2025-10: form label 14 medium, button label bold [YT:FBDVzr0peO4, YT:ThmHV38Ecqk].
- **Button gap** — side by side 8 in the hi-fi modal [YT:FBDVzr0peO4] vs 16 in the beginner pop-ups [YT:ThmHV38Ecqk]; the hi-fi summary also says 16 between tappable items, 8 too small (2025-10).
- **Gradient direction** — beginner-course items disagree (lighter bottom-left to darker top-right vs darker bottom-left vs darker at the bottom); the hi-fi course says darker end at the bottom (majority). [YT:ThmHV38Ecqk, YT:FBDVzr0peO4] (2025-10)
- **Shadows** — 2025-10: default shadow looks bad, a shadow makes a rectangle read as a button [YT:ThmHV38Ecqk]; 2026-09: he avoids them in the flat dashboard [YT:w2mNSOWiZbU].
- **Line charts** — 5 pt sharp joins (2025-10), 3 pt round caps (2025-11), 6+ (2026-03), jagged data with round end caps (2026-09): thickness scales with the canvas [YT:FBDVzr0peO4, YT:N-34Q9mhwvs, YT:_PJLefMZwko, YT:w2mNSOWiZbU].
- **Design systems** — an item flagged as his 2024 view: UI is finite and strict, hence design systems; Dec 2025: AI made them obsolete, design for intent [YT:O_9m_pcPSuU, YT:6_t66Ef0Llk] (2025-12).

### Signature lines (verbatim, ≤15 words)
- "Don't go over the top." [YT:FBDVzr0peO4] (2025-10)
- "design is reduction" [YT:FBDVzr0peO4] (2025-10)
- "it really needs to look like a button" [YT:Kqg3vN1ms2E] (2026-08)
- "never sacrifice contrast for the sake of being original" [YT:FBDVzr0peO4] (2025-10)
- "If there is one thing that you should never complicate visually, it's navigation." [YT:FBDVzr0peO4] (2025-10)
- "adding effects to everything is a pretty good way for a really bad design" [YT:FBDVzr0peO4] (2025-10)
- "know which rules not to break and then break all of the other ones creatively" [YT:FBDVzr0peO4] (2025-10)
- "We don't really need another morphism" [YT:psyw2_j_5jk] (2026-06)
- "Detail is everything." [YT:w1kITFbUU1U] (2024-10)
