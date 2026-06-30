# Attention Ratio, Message Match, and Conversion Coupling

These three are the trio that decide whether paid traffic converts.
Attention Ratio is the math of the page itself. Message Match is the
joint between the ad and the page. Conversion Coupling is the joint
between the offer and the form. If any of the three is broken, the
spend is bleeding.

---

## PART 1 — ATTENTION RATIO

### Definition

> Attention Ratio = the total number of clickable elements on a
> landing page ÷ the number of campaign conversion goals on that
> landing page.

A real campaign landing page is **1:1**. One thing to click. One thing
to convert. That's it.

Anything higher than 1:1 means you have introduced choices. Every
choice is a chance for the visitor to do something other than the one
thing the campaign exists to make them do. Every choice is a leak.

### Why 1:1

- A campaign has one goal. Every dollar spent on the source ad was
  spent to drive that goal.
- The visitor arrived with one intent (or close to one, given message
  match).
- Hick's Law: decision time rises with the number of choices. More
  choices on a page = slower decisions = more bounces.
- Every secondary link is a non-converting click. Non-converting
  clicks have a real cost: they consume budget and produce nothing.

### How to count it

Open the page. Count every clickable element:
- Logo link in the header? +1
- Nav links? +1 each
- Skip nav / language toggle / accessibility link? +1 each
- Hero CTA? +1 (this is the goal — counted as a goal not a leak)
- Secondary CTA in hero? +1 (leak unless it serves the same goal)
- Inline links inside body copy? +1 each
- Testimonial author links? +1 each
- Footer links? +1 each
- Social media icons? +1 each
- Chat widget? +1
- Cookie banner CTAs? +1 each (yes, technically)

Divide by goals on the page.

### Typical numbers in the wild

- Homepage trying to be a landing page: AR 40:1 to 80:1. Catastrophic.
- "Service page" used as landing page: AR 20:1 to 35:1. Bad.
- Mediocre dedicated landing page with nav and footer: AR 10:1 to 15:1.
- Decent landing page with nav stripped, footer thinned: AR 3:1 to 5:1.
- Real conversion-centered page: AR 1:1.

### The public proof

The standard public example: VWO removed navigation from one of their
landing pages, dropping AR from 13:1 to 3:1, and conversions roughly
doubled. The Unbounce Attention Ratio definition page references this
publicly. The lesson is not "13:1 vs 3:1". The lesson is: every leak
you remove returns conversion rate, predictably.

### How to fix a high AR

In priority order:

1. **Strip the global nav.** This single act often halves AR.
2. **Strip the global footer.** Replace with a minimal footer:
   privacy, terms, copyright. Nothing clickable.
3. **Remove social icons.** They are not the goal.
4. **Remove "related articles", "you may also like", "more from us"
   blocks.** This is e-commerce thinking on a campaign page.
5. **Consolidate CTAs.** If three CTAs all link to the same form
   anchor, that's 3 leaks counted as 1 goal (or actually 3 leaks if
   one is "Learn More" and one is "Get Started" — different copy,
   different intent, even if same destination).
6. **Kill chat widgets** unless chat IS the conversion mechanism.
7. **Inline body copy links** to external resources: remove or
   convert to non-clickable bold text.
8. **Logo in header** — debate, but the conservative move is to leave
   the logo non-clickable (or linking to the same page anchor). If
   the visitor wants to look up the company they will Google it; they
   do not need an escape hatch from the campaign.

### What about "but visitors need to learn about us"

They do. Inside the page. Not by leaving the page. Build the "about"
into the page itself as proof. Visitor never has to leave.

### Edge cases

- **Two-step landing pages**: the first page has one CTA (start the
  flow). The second page has the form. AR is counted per page.
- **Video sales letters**: the video is not clickable in the
  conversion sense. The CTA below the video is the only click. AR 1:1.
- **E-commerce product pages used as landing pages**: this is a
  category violation. Product pages are by design many-to-many (cart,
  wishlist, related products, reviews tab, size guide, etc.). If
  paid traffic must land there, accept higher AR or build a
  dedicated PLP overlay.

---

## PART 2 — MESSAGE MATCH

### Definition

Message Match is the alignment between the pre-click promise (the ad,
the email, the social post, the search result) and the post-click
delivery (the landing page hero). Strong message match means the
visitor's brain says "yes, this is the place" inside the first second.
Weak message match means the visitor's brain says "wait, what?" — and
the bounce starts.

Oli's standard public line: a huge percentage of paid ads are wasted
because the page they point at doesn't match the ad. The fix is
almost always on the page, not in the ad account.

### The two halves

1. **Copy match.** The ad headline and the page headline use
   substantially the same words, in substantially the same order. If
   the ad says "EB-5 Visa for Entrepreneurs", the page headline does
   not say "Welcome to Smith Immigration Law" — it says some version
   of "EB-5 Visa for Entrepreneurs" at the top.

2. **Design match.** The ad's hero visual and the page's hero visual
   are recognisably the same family. Same person if there's a person.
   Same colour palette. Same product shot. The visitor sees the page
   and visually confirms "yes, that's the thing the ad was about".

### Why it matters at the dollar level

Three things move when message match goes from weak to strong:

- **Bounce rate drops.** The visitor sees the promise repeated. They
  stay.
- **Quality Score / Relevance Score rises** (on Google and Meta).
  The platform sees lower bounce, longer dwell, higher post-click
  conversion. Both platforms reward this with lower CPC and better
  ad placement.
- **Conversion rate rises** because more visitors are reading the
  page, not bouncing.

Compound effect: a campaign with weak message match runs at, say,
$8 CPC and 1.5% conversion. The same campaign with strong message
match runs at $5 CPC and 3% conversion. The cost per conversion drops
roughly 3.2x. Same ad spend. Same offer. Different page.

### How to audit message match

Put the ad creative and the landing page hero side by side on one
screen. Then check:

1. **Headline match.** Does the page headline contain the same
   keywords as the ad headline? Same outcome? Same audience signal?
2. **Visual match.** Same hero image, or same visual family?
3. **Tone match.** Ad is direct and punchy → page is direct and
   punchy. Ad is warm and reassuring → page is warm and reassuring.
   Mismatch breaks trust.
4. **Offer match.** Ad promised a free assessment → page leads with
   the free assessment. Ad promised a discount → page leads with the
   discount, not buried below the fold.
5. **Audience match.** Ad targeted EB-5 applicants → page does not
   start by explaining what EB-5 is to people who already know.

### Common message match breaks

- **"One page for all our ads"** — the agency runs 12 ad variations
  pointing at the same landing page. The page can only match one of
  them. The other 11 are leaking. Solution: dedicated pages per ad
  family, or at least dynamic text replacement so the headline matches
  the ad's keyword.
- **Brand-led headlines on traffic-led campaigns** — the marketing
  team insists "Welcome to [Brand]" is the headline because that's
  what the brand book says. Brand book is wrong for a campaign page.
- **Funnel-mismatched offers** — the ad says "Buy Now" and the page
  says "Book a Consultation". You've changed the ask between the
  click and the land. Visitor exits.

### The scent metaphor

Information foraging theory (the academic underpinning here) calls
this "scent". The visitor is following a trail of cues from search
intent → ad → page → form → conversion. Strong scent = the cues line
up and the visitor stays on the trail. Weak scent = the visitor
loses the trail and starts a new search.

### The fix sequence

1. Pull the top-performing ad's headline. Make that the page headline.
2. Pull the ad's hero visual. Make that the page hero (or a near
   match).
3. Lead the page with the ad's strongest specific claim. If the ad
   said "48-hour eligibility check", lead with that, not with the
   firm's 30-year history.
4. If you have multiple ad variants you can't consolidate, set up
   dynamic text replacement: the page headline pulls in the keyword
   from the URL parameter.
5. If different audiences need different pages, build them. One page
   per audience-offer pair.

---

## PART 3 — CONVERSION COUPLING

### Definition

Conversion Coupling is the alignment between the size of the ask
(what the form requires) and the size of the offer (what the visitor
gets on the other side). The two must feel proportional.

This is not the same as "shorter forms convert better". It's the
opposite of a universal rule. The rule is **the form must be coupled
to the offer**. A two-field form for a $20,000 strategy session looks
suspicious. A twelve-field form for a free PDF looks insulting. Both
break trust.

### The coupling principle

| Offer size | Appropriate form |
|---|---|
| Free PDF / checklist | 1–2 fields (email; maybe first name) |
| Free webinar / video | 2–3 fields (email, name, maybe role) |
| Free assessment / quiz | 3–5 fields (enough to personalise the result) |
| Free consultation call | 5–8 fields (qualify the lead at the form) |
| Custom proposal / strategy session | 7–12 fields (the form IS qualification) |
| Demo for enterprise software | 6–10 fields plus company info |

If your form is shorter than this table for the size of your offer,
the form looks weirdly easy and the visitor smells a bait-and-switch.
If your form is longer, the visitor sees the form as the price and
bounces.

### Why under-asking hurts

Counterintuitive but real. If you give away something genuinely
valuable in exchange for one email field, sophisticated buyers
discount the value. "If it were really worth $5,000, they'd ask for
more than my email." The form length is a credibility signal. Ask in
proportion to what you're giving.

### Why over-asking hurts

Standard friction. Every additional field drops completion. The
question is not "should I ask?" but "does this field justify the
friction it adds?"

Justification test for each field:
- **Does the answer change what we deliver?** If yes, keep it.
- **Does the answer change how we qualify or route the lead?** If
  yes, keep it.
- **Are we asking it because the sales team always asks it?** If yes,
  push back. The sales team can ask it on the call.

### Field-by-field guidance

- **Email**: always keep.
- **Name**: keep — used for personalisation in the next email.
- **Phone**: only if phone follow-up is the next step. Adds heavy
  friction. Pre-warn with microcopy ("We'll call within 24 hours")
  to convert friction into value.
- **Company**: keep for B2B. Optional for B2C.
- **Role / job title**: keep for B2B routing.
- **Company size**: keep for B2B qualification. Use a dropdown, not
  free text.
- **Budget**: only on high-ticket pages. Always optional or
  range-based.
- **"How did you hear about us?"**: marketing wants this. Visitors
  hate it. Cut it or move it to the thank-you page.
- **"Tell us about your project"** (free-text textarea): kills
  conversion on cold traffic. Keep for warm traffic only.

### Form layout rules

- **One column unless you have a hard reason for two.** Two-column
  forms feel longer and slower because the eye has to scan sideways.
- **Labels above fields, not beside.** Reading top-to-bottom is
  faster than reading left-to-right.
- **Inline validation.** Show errors as the visitor types, not after
  submit.
- **Required vs optional**: mark required, not optional. Less visual
  noise.
- **The button is part of the form.** Button copy matches the offer
  ("Get My Assessment"), not the action ("Submit").

### Coupling the CTA to the offer

The button copy is the final coupling check. Read the button copy
out loud. Does it match the headline? Does it match the ad? Does it
match the form? If the headline promised an "eligibility assessment"
and the button says "Submit", you broke coupling at the last step.
The visitor's brain notices.

### Microcopy as coupling glue

The small text near the form and the button does coupling work:
- "Takes 90 seconds." (couples time-cost to ask-size)
- "We'll respond within 24 hours." (couples response time to
  expectation)
- "No credit card required." (couples low-commitment ask to
  trial offer)
- "Your information stays private." (couples privacy concern to
  the ask)

Each line of microcopy is doing a job. If it's not doing a job,
delete it.

---

## SYNTHESIS — How These Three Interact

A perfect campaign landing page is:

- **Attention Ratio 1:1** (no leaks)
- **Message Match strong** (ad → page → page → form, all on the same
  promise)
- **Conversion Coupling tight** (the form matches the offer, the
  button matches the form, the microcopy matches the visitor's
  doubts)

Break any one and the others can't save the page.

Break all three and you have what most agencies are running for their
clients right now — and what the Oli Gardner public corpus has been
yelling about for fifteen years.

The fix order in an audit is always:

1. Attention Ratio (the page itself)
2. Message Match (the joint to the ad)
3. Conversion Coupling (the joint to the conversion)

Fix in that order because each fix raises the ceiling for the next.
A page with AR 30:1 cannot be saved by message match — the leaks
swamp the lift. Fix the leaks first. Then make the page match the
ad. Then make the form match the offer. Then run traffic.
