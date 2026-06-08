# PRD: Strawesome Funnel Breakdown for Brian

**Project:** Strawesome Funnel Breakdown
**Client:** Brian Surowiec (Strawesome)
**Status:** Not Started
**Created:** January 12, 2026
**Last Updated:** January 12, 2026

---

## 1. Project Overview

### What We're Building

A comprehensive funnel breakdown that teaches Brian:
1. **What** each section of his funnel does
2. **Why** each section works (psychology, mechanism)
3. **How** to apply the patterns to future funnels

This mirrors the breakdown created for Ethan (CBDog funnel) but adapted for Strawesome's "Glass Is Safer Than Metal" funnel.

### Why This Matters

Brian isn't just getting a funnel — he's getting a playbook. The breakdown transforms a done-for-you deliverable into a teach-to-fish asset he can reuse.

### Success Criteria

- [ ] Brian can read the breakdown and understand WHY each section exists
- [ ] Brian can identify the patterns and apply them to a different product/market
- [ ] The breakdown matches the quality/depth of Ethan's CBDog breakdown
- [ ] All deliverables are live on GitHub Pages

---

## 2. Audience Context (CRITICAL)

Agents MUST understand the emotional difference between these two audiences to write appropriate breakdowns.

| | Ethan (CBDog) | Brian (Strawesome) |
|---|---|---|
| **Target** | Anxious dog owner | Metal straw user |
| **Primary emotion** | Guilt, desperation, exhaustion | Cognitive dissonance, defensiveness |
| **Core fear** | "I'm a bad dog parent" | "I made the wrong choice" |
| **What they've tried** | Training, thunder shirts, calming treats | Switched from plastic to metal |
| **Permission needed** | "You're not failing — the approach was wrong" | "You were misled, not stupid" |
| **Funnel job** | Remove self-blame | Remove ego threat |
| **Psychological barrier** | Guilt keeps them stuck | Pride keeps them defending metal |

### How This Affects the Breakdown

**For Ethan's breakdown**, we wrote things like:
> "Guilt is one of the biggest objections in any market. The reader is thinking 'maybe I just didn't try hard enough.'"

**For Brian's breakdown**, the parallel is:
> "Cognitive dissonance is the biggest barrier. The reader made a conscious choice to switch to metal, and now they're being told that choice was wrong. The copy must give them an off-ramp that doesn't make them feel stupid."

When writing "Why This Works" sections, always interpret through Brian's audience lens.

---

## 3. Source Materials

### Primary Sources (MUST READ)

| File | Purpose | Priority |
|------|---------|----------|
| `/Users/andrew/Downloads/july2025/clients/accelerator-site/brian-strawesome/funnel/presell/index.html` | The presell landing page (19 sections) | CRITICAL |
| `/Users/andrew/Downloads/july2025/clients/accelerator-site/brian-strawesome/ad-mockups/index.html` | The 3 ad drafts | CRITICAL |
| `/Users/andrew/Downloads/july2025/clients/brian-surowiec-strawesome/thesis-development-draft.md` | Two-layer thesis documentation | CRITICAL |

### HTML Templates (MUST USE for HTML build)

| File | Purpose |
|------|---------|
| `/Users/andrew/Downloads/july2025/clients/accelerator-site/ethan-gvn/cbdog-funnel/funnel-breakdown/index.html` | Breakdown page template — copy structure, adapt colors/content |
| `/Users/andrew/Downloads/july2025/clients/accelerator-site/ethan-gvn/cbdog-funnel/index.html` | Landing page template — copy structure, adapt colors/content |

### Reference (For Understanding Patterns)

| File | Purpose |
|------|---------|
| `/Users/andrew/Downloads/july2025/clients/accelerator-site/ethan-gvn/cbdog-funnel/funnel-breakdown-v3.md` | Markdown version — useful for understanding the thinking, not to be replicated |

---

## 4. Deliverables

### Deliverable 1: HTML Breakdown Page (PRIMARY)

**File:** `/Users/andrew/Downloads/july2025/clients/accelerator-site/brian-strawesome/funnel-breakdown/index.html`

**Requirements:**
- Copy Ethan's HTML structure exactly
- Replace Ethan's content with Brian's breakdown content
- Adapt colors to Strawesome brand:
  - Primary: `#FF6700` (orange)
  - Accent: `#1A7D65` (teal)
  - Background: `#FDF9F7` (cream)
- Contains all 4 parts (Architecture, Section Map, Section Breakdowns, Patterns)
- Mobile responsive (already handled by Ethan's CSS)

### Deliverable 2: Landing Page

**File:** `/Users/andrew/Downloads/july2025/clients/accelerator-site/brian-strawesome/index.html`

**Requirements:**
- Copy Ethan's landing page structure
- Three buttons:
  1. Ad Mockups
  2. Education Page (Presell)
  3. Funnel Breakdown
- Strawesome branding

### NO Markdown Deliverable

We are NOT creating a separate markdown file. Write directly to HTML. The markdown is wasted effort — Brian will only see the HTML.

---

## 5. Section Breakdown Template (Presell Sections)

Every presell section breakdown MUST follow this exact format. Copy this structure into the HTML.

```html
<div class="section-card">
    <div class="section-card-header">
        <h3><span class="section-num">[#]</span> [Section Name]</h3>
    </div>
    <div class="section-body">
        <div class="section-left">
            <!-- Belief State Box -->
            <div class="belief-state-box">
                <div class="label">Belief Shift</div>
                <div class="before-after">
                    <span class="before">[What reader believes BEFORE]</span>
                    <span class="arrow">↓</span>
                    <span class="after">[What reader believes AFTER]</span>
                </div>
            </div>
            <!-- Copy excerpt goes here as blockquote or styled text -->
        </div>
        <div class="section-right">
            <!-- Technique Box -->
            <div class="technique-box">
                <div class="label">Key Technique</div>
                <p>[Technique Name] — [One sentence definition]</p>
            </div>

            <!-- What This Does -->
            <div class="subsection">
                <div class="subsection-title">What This Does</div>
                <p>[2-3 sentences on the purpose]</p>
            </div>

            <!-- Why This Works -->
            <div class="subsection">
                <div class="subsection-title">Why This Works</div>
                <p>[2-3 sentences on psychology/mechanism]</p>
            </div>

            <!-- How to Adapt -->
            <div class="subsection">
                <div class="subsection-title">How to Adapt This</div>
                <p>[Explanation + Formula]</p>
                <code>Formula: "[Fill-in-the-blank template]"</code>
            </div>

            <!-- Connection to Funnel Arc -->
            <div class="subsection">
                <div class="subsection-title">Connection to Funnel Arc</div>
                <p>[How it connects to previous section: [name]] and [sets up next section: [name]]</p>
            </div>

            <!-- Lines Worth Studying -->
            <div class="lines-box">
                <h4>Lines Worth Studying</h4>
                <ul>
                    <li><code>"[Exact quote]"</code> — [Why it works]</li>
                    <li><code>"[Exact quote]"</code> — [Why it works]</li>
                </ul>
            </div>
        </div>
    </div>
</div>
```

### Word Count Targets (Per Section Breakdown)

- Belief State: 15-25 words each (before/after)
- What This Does: 40-60 words
- Why This Works: 50-80 words
- How to Adapt: 60-100 words + formula
- Connection to Funnel Arc: 30-50 words
- Lines Worth Studying: 2 lines, 10-20 words explanation each

**Total per section: 200-300 words**

---

## 6. Ad Breakdown Template (Different from Presell)

Ads are structurally different. Use this template for the 3 ad breakdowns.

```html
<div class="section-card">
    <div class="section-card-header">
        <h3><span class="section-num">Ad [#]</span> [Violation Opener in Quotes]</h3>
    </div>
    <div class="section-body">
        <div class="section-left">
            <!-- Pattern Badge -->
            <div class="technique-box">
                <div class="label">Violation Pattern</div>
                <p>[Pattern Name: Flip Safety / Attack Decision / Flip Strength]</p>
            </div>
            <!-- Full ad copy excerpt -->
        </div>
        <div class="section-right">
            <!-- What Belief It Contradicts -->
            <div class="subsection">
                <div class="subsection-title">Belief It Contradicts</div>
                <p>[The specific belief the audience holds that this ad attacks]</p>
            </div>

            <!-- Why This Violation Works -->
            <div class="subsection">
                <div class="subsection-title">Why This Violation Works</div>
                <p>[Psychology of why contradicting this belief creates engagement]</p>
            </div>

            <!-- The Evidence Stack -->
            <div class="subsection">
                <div class="subsection-title">The Evidence Stack</div>
                <p>[How the ad builds its case after the opening violation]</p>
            </div>

            <!-- CTA Analysis -->
            <div class="subsection">
                <div class="subsection-title">CTA Analysis</div>
                <p>[Why "5 reasons you shouldn't use metal straws" works as a CTA]</p>
            </div>

            <!-- Lines Worth Studying -->
            <div class="lines-box">
                <h4>Lines Worth Studying</h4>
                <ul>
                    <li><code>"[Exact quote]"</code> — [Why it works]</li>
                    <li><code>"[Exact quote]"</code> — [Why it works]</li>
                </ul>
            </div>
        </div>
    </div>
</div>
```

**Word Count Target: 150-200 words per ad breakdown**

---

## 7. Two-Layer Thesis (Core Context)

Every agent MUST understand and reference this structure.

| Layer | Purpose | Thesis |
|-------|---------|--------|
| **Brand Thesis** | The deeper belief Strawesome stands for | "Reusable Should Mean Forever" |
| **Funnel Thesis** | Gets attention, contradicts market belief | "Glass Straws Are Safer Than Metal" |

- **Funnel thesis** brings people in (the ads + presell education)
- **Brand thesis** converts them into believers (Section 16 + footer)

The breakdown should make this two-layer structure explicit and teach Brian how to use it for future funnels.

---

## 8. Technique Glossary (Use These Terms Consistently)

Agents MUST use these exact technique names. Do not invent new names or use synonyms.

| Technique Name | Definition | Used In |
|----------------|------------|---------|
| **Opening Violation** | First line contradicts a belief the reader holds to be true | Section 2, All Ads |
| **Analogy Bridge** | Uses a familiar scenario to explain an unfamiliar concept | Sections 3, 4, 5, 6, 7 |
| **Permission Statement** | Removes guilt/blame from the reader, often formatted as "You shouldn't have to..." | End of Sections 3, 4, 5, 6, 7 |
| **Bridge Recap** | Summarizes all previous points before pivoting to solution | Section 8 |
| **Mechanism Reveal** | Names the technical/scientific differentiator | Section 9 |
| **Origin Story** | Founder narrative that creates authenticity and trust | Section 10 |
| **Hero Stat** | One compelling number that proves the core claim | Section 11 |
| **Feature-Problem Match** | Each product feature directly solves a problem seeded earlier | Section 12 |
| **Comparison Grid** | Side-by-side visual comparison with competitor | Section 13 |
| **Future Pacing** | "Picture this..." sensory description of life after purchase | Section 15 |
| **Brand Thesis Reveal** | States the deeper belief the brand stands for | Section 16 |
| **Risk Reversal** | Guarantee that removes purchase anxiety | Section 17 |
| **Binary Choice Close** | Presents only two options, one clearly better | Section 18 |
| **Flip Safety** | Ad pattern — claims the "safe" choice is actually dangerous | Ad 1 |
| **Attack Decision** | Ad pattern — attacks the reader's past decision (not the product) | Ad 2 |
| **Flip Strength** | Ad pattern — redefines what "strength" means | Ad 3 |

---

## 9. The 22 Sections to Break Down

### Presell Page (19 Sections)

| # | Section Name | Key Technique | Analogy Used |
|---|-------------|---------------|--------------|
| 1 | Hero + Contrarian Hook | Opening Violation | — |
| 2 | Opening Violation | Opening Violation | — |
| 3 | Reason 1: Temperature | Analogy Bridge + Permission Statement | Hot pan handle |
| 4 | Reason 2: Bacteria | Analogy Bridge + Permission Statement | Restaurant kitchen you can't see |
| 5 | Reason 3: Dental | Analogy Bridge + Permission Statement | Guardrail vs concrete wall |
| 6 | Reason 4: Leaching | Analogy Bridge + Permission Statement | Faucet ruining filtered water |
| 7 | Reason 5: Injury | Analogy Bridge + Permission Statement | Car crumple zones |
| 8 | Bridge | Bridge Recap | — |
| 9 | Mechanism | Mechanism Reveal | — |
| 10 | Product Reveal | Origin Story | — |
| 11 | The Proof | Hero Stat | — |
| 12 | Benefits | Feature-Problem Match | — |
| 13 | Comparison | Comparison Grid | — |
| 14 | Testimonials | Social Proof | — |
| 15 | Future Pacing | Future Pacing | — |
| 16 | Brand Promise | Brand Thesis Reveal | — |
| 17 | Guarantee | Risk Reversal | — |
| 18 | Two Options | Binary Choice Close | — |
| 19 | Final CTA | Trust Stack | — |

### Ad Mockups (3 Ads)

| # | Violation Opener | Pattern |
|---|------------------|---------|
| 20 | "Glass straws are safer than metal." | Flip Safety |
| 21 | "Metal straws are a dangerous choice." | Attack Decision |
| 22 | "Glass straws are stronger than metal straws." | Flip Strength |

---

## 10. Quality Standards

### Writing Style
- Clear, direct prose
- NO rhetorical questions — convert all to statements
- No emojis
- Professional but accessible tone

### Content Standards
- Every claim must match the actual funnel copy (see Appendix A)
- Use technique names from the glossary consistently
- "How to Adapt" must include an actual fill-in-the-blank formula
- Cross-references must name specific sections

### Self-Review Checklist (Before Marking Any Section Complete)

- [ ] Does the Belief State accurately capture the shift this section creates?
- [ ] Is the Key Technique name from the glossary?
- [ ] Does "Why This Works" explain the psychology for Brian's audience (cognitive dissonance, not guilt)?
- [ ] Does "How to Adapt" include a usable formula with brackets for fill-ins?
- [ ] Does "Connection to Funnel Arc" name the previous AND next sections?
- [ ] Are the "Lines Worth Studying" actually insightful, not just random quotes?
- [ ] Would Brian understand WHY this section exists after reading this breakdown?
- [ ] Could Brian apply the formula to a different product?

---

## 11. Progress Tracking

**IMPORTANT:** After completing any checklist item, immediately edit THIS PRD FILE to mark it complete. Do not rely on memory across sessions.

### Checklist

**Part 1: Funnel Architecture**
- [x] The Flow section written
- [x] Why This Order section written
- [x] Two-Layer Thesis section written
- [x] 3 Core Belief Shifts documented

**Part 2: Section Map**
- [x] All 19 presell sections listed with summaries
- [x] All 3 ads listed with summaries

**Part 3: Section Breakdowns (Presell)**
- [x] Section 1: Hero + Contrarian Hook
- [x] Section 2: Opening Violation
- [x] Section 3: Reason 1 (Temperature)
- [x] Section 4: Reason 2 (Bacteria)
- [x] Section 5: Reason 3 (Dental)
- [x] Section 6: Reason 4 (Leaching)
- [x] Section 7: Reason 5 (Injury)
- [x] Section 8: Bridge
- [x] Section 9: Mechanism
- [x] Section 10: Product Reveal
- [x] Section 11: The Proof
- [x] Section 12: Benefits
- [x] Section 13: Comparison
- [x] Section 14: Testimonials
- [x] Section 15: Future Pacing
- [x] Section 16: Brand Promise
- [x] Section 17: Guarantee
- [x] Section 18: Two Options
- [x] Section 19: Final CTA

**Part 3: Section Breakdowns (Ads)**
- [x] Ad 1: Flip Safety
- [x] Ad 2: Attack Decision
- [x] Ad 3: Flip Strength

**Part 4: Key Patterns**
- [x] All 12+ patterns documented

**HTML Build**
- [x] Breakdown page HTML complete
- [x] Landing page HTML complete
- [x] Colors adapted to Strawesome brand
- [x] All internal links working

**Deployment**
- [ ] Pushed to GitHub Pages
- [ ] All URLs tested and working

---

## 12. Agent Instructions

### Starting a Session

1. Read this PRD completely
2. Load the source materials (Section 3)
3. Check the progress checklist (Section 11)
4. Continue from where the last session stopped
5. Write directly to HTML (do not create markdown)

### Ending a Session

1. Update the progress checklist in THIS file
2. Save all work
3. Create a handoff at: `/Users/andrew/Downloads/july2025/handoffs/[DATE]-strawesome-breakdown-s[#]-handoff.md`

### Handoff Format

```markdown
# Strawesome Breakdown Session [#] Handoff

## Completed This Session
- [List what was done]

## Resume Point
- [Exact section/item to continue from]

## Decisions Made
- [Any choices that affect future work]

## Questions/Blockers
- [Anything needing Andrew's input]
```

### Writing Order

Write Part 3 sections IN ORDER (1 → 22). This ensures "Connection to Funnel Arc" references are accurate. Do not skip around.

---

## 13. File Paths Summary

### Outputs (Where to Write)
```
/Users/andrew/Downloads/july2025/clients/accelerator-site/brian-strawesome/
├── index.html                          # Landing page
└── funnel-breakdown/
    └── index.html                      # Breakdown page (main deliverable)
```

### Inputs (What to Read)
```
# Brian's Funnel (THE CONTENT)
/Users/andrew/Downloads/july2025/clients/accelerator-site/brian-strawesome/funnel/presell/index.html
/Users/andrew/Downloads/july2025/clients/accelerator-site/brian-strawesome/ad-mockups/index.html
/Users/andrew/Downloads/july2025/clients/brian-surowiec-strawesome/thesis-development-draft.md

# Ethan's HTML (THE TEMPLATE)
/Users/andrew/Downloads/july2025/clients/accelerator-site/ethan-gvn/cbdog-funnel/funnel-breakdown/index.html
/Users/andrew/Downloads/july2025/clients/accelerator-site/ethan-gvn/cbdog-funnel/index.html
```

### GitHub
- Repo: `theprompted/accelerator`
- Live URL: `https://theprompted.github.io/accelerator/brian-strawesome/`

---

## Appendix A: Pre-Extracted Section Copy

This appendix contains the exact copy from each section. Agents MUST quote from this — do not paraphrase or invent.

### Section 1: Hero + Contrarian Hook
```
Headline: "5 Reasons You Shouldn't Use Metal Straws"
Subtitle: "The 'safer' choice everyone switched to has problems no one talks about."
Byline: "By The Strawesome Team — Handcrafting Glass Straws in Michigan Since 2009"
```

### Section 2: Opening Violation
```
"The 'safe' straw in your tumbler is more dangerous than the one you're afraid of."

"Not a little."

"Not in some edge case."

"Metal straws have a documented fatality."

"Glass straws don't."

"That's not what you expected to read."

"You switched to metal because it seemed unbreakable."

"Sturdy. Reusable. Safe."

"But 'unbreakable' isn't the same as 'safe.'"

"And the straw you chose to protect yourself has five problems the one you've been avoiding doesn't have."
```

### Section 3: Reason 1 — Temperature
```
Header: "1. Metal Conducts Every Degree — Straight Into Your Lips"
Subhead: "The same property that makes it 'durable' makes it painful to drink through."

Key lines:
- "Metal is an excellent conductor of heat."
- "Hot coffee becomes a metal straw that burns your lips."
- "Iced drinks become a frozen rod against your teeth."
- "Your metal straw is the hot pan handle you keep grabbing — except it's against your lips."
- "The straw isn't supposed to be part of the temperature experience. It's supposed to be invisible."

Permission Statement:
"You shouldn't have to wait for your drink to reach a 'safe straw temperature' before taking a sip."
```

### Section 4: Reason 2 — Bacteria
```
Header: "2. You Can't See What's Growing Inside Your Metal Straw"
Subhead: "Opaque walls hide bacterial buildup you'd never tolerate if you could see it."

Key lines:
- "Research shows that reusable drinking containers can harbor 100,000 times more bacteria than a bathroom doorknob after regular use."
- "Your metal straw is a restaurant kitchen you can never inspect."
- "One material hides what's happening inside. The other shows you."

Permission Statement:
"You shouldn't have to guess whether your straw is sanitary."
```

### Section 5: Reason 3 — Dental
```
Header: "3. Metal Doesn't Give — Your Teeth Do"
Subhead: "One accidental bite costs more than every straw you'll ever buy."

Key lines:
- "Metal straws are concrete walls for your teeth."
- "In 2016, Starbucks recalled 2.5 million stainless steel straws after reports of children experiencing mouth lacerations."
- "'Unbreakable' sounds like a feature until you realize it just means something else has to break instead."

Permission Statement:
"You shouldn't have to treat your straw like a hazard."
```

### Section 6: Reason 4 — Leaching
```
Header: "4. That Metallic Taste Isn't Your Imagination"
Subhead: "Research shows chromium and nickel dissolve into acidic drinks with every sip."

Key lines:
- "That metallic taste you notice with your morning coffee isn't nothing. It's metal dissolving into your drink."
- "Your metal straw is the faucet ruining the filtered water."
- "'Stainless' steel is a marketing term — not a promise that nothing transfers."

Permission Statement:
"You shouldn't have to worry about what's dissolving into your drink."
```

### Section 7: Reason 5 — Injury
```
Header: "5. When Metal Straws Fail, They Fail Dangerously"
Subhead: "'Unbreakable' becomes 'unforgiving' the moment something goes wrong."

Key lines:
- "In November 2018, Elena Struthers-Gardner — a 60-year-old retired jockey in England — fell while carrying a Mason jar with a metal straw. The straw impaled her through her eye socket. It pierced her brain. She died two days later."
- "Metal straws have no crumple zones."
- "The safest tools aren't the ones that never fail — they're the ones that fail safely."

Permission Statement:
"You shouldn't have to accept increased injury risk for reusability."
```

### Section 8: Bridge
```
Header: "The Question Isn't Whether to Keep Using Metal"

Recap:
- Metal conducts dangerous temperatures.
- Metal hides bacterial growth.
- Metal chips teeth.
- Metal leaches into acidic drinks.
- Metal causes more severe injuries.

Key line:
"The question isn't whether to keep using metal. The question is what you've been missing about glass."
```

### Section 9: Mechanism
```
Header: "Why Glass Works (When Done Right)"

Key lines:
- "Most people are afraid of glass straws for one reason: breaking. That fear is reasonable — for cheap glass."
- "There's a process called annealing — slowly cooling glass in a kiln to remove internal stress."
- "This is what separates a glass straw you should trust from one you shouldn't."
- "The glass straws you see on Amazon for $8 a pack often skip proper annealing."

Conclusion:
"The glass straw you were afraid of is actually the safer choice. You just need to find one that's made right."
```

### Section 10: Product Reveal
```
Header: "Meet Strawesome — The Original Glass Straw Company"

Key lines:
- "In 2009, a woman named Daedra in Michigan started making glass straws by hand."
- "She learned lampworking at The Glass Academy in Dearborn."
- "She started in her garage with a torch, glass supplies, and a big vision."
- "Strawesome wasn't riding a trend. They were creating one."
- "Sixteen years later, they're the longest-running dedicated glass straw maker in the world."

Features list:
- Handcrafted by Daedra in the family workshop
- Properly annealed in a kiln for strength
- Seamless construction (no welded joints to harbor bacteria)
- Transparent (you can see it's clean)
- Non-reactive (nothing leaches into your drink)
- Non-conductive (no temperature transfer to your lips)
- Backed by a lifetime warranty
```

### Section 11: The Proof
```
Header: "The 16-Year Test"

Key stat: "1.5% replacement rate"

Key lines:
- "Over 16 years, Strawesome has had a 1.5% replacement rate on their straws."
- "98.5% of their straws are still out there, being used."
- "That's not marketing. That's materials science."
```

### Section 12: Benefits
```
Header: "What Strawesome Does For You"

Benefit 1: "Pure, Clean Taste"
- "Glass is completely non-reactive. Nothing leaches."

Benefit 2: "See-Through Safety"
- "You can see if your Strawesome is clean. No guessing."

Benefit 3: "Comfort at Any Temperature"
- "Glass doesn't conduct heat. Your lips touch glass, not temperature extremes."
```

### Section 13: Comparison Table
```
Header: "Glass vs. Metal: The Full Comparison"

Rows:
- Temperature: Conducts heat/cold vs Non-conductive
- Visibility: Opaque vs Transparent
- Teeth Safety: Rigid, 2.5M recalled vs Smooth, gentle
- Leaching: Chromium/nickel leach vs Non-reactive
- Injury Risk: Documented fatality vs Annealed, crumbles if broken
- Warranty: Usually 1 year or none vs Lifetime warranty
- Durability Proof: Unknown vs 1.5% replacement over 16 years
- Made In: Typically overseas vs Handmade in Michigan, USA
```

### Section 14: Testimonials
```
Header: "What Customers Notice"

Key quotes:
- "They somehow make my water seem fresher and colder."
- "They're thicker than Amazon ones so these are the ones I trust."
- "We are hooked — donating all of our copper and silicone straws and going all glass!"
- "Omg thank you for making these... I can finally have the cup I want w/o the plastic."
```

### Section 15: Future Pacing
```
Header: "Picture This"

Key lines:
- "Imagine waking up tomorrow and reaching for your Stanley tumbler."
- "Your lips don't burn on the hot metal."
- "You glance down and see through the straw itself. Crystal clear. Obviously clean."
- "You realize you're not thinking about the straw at all. Because it's just... working."
```

### Section 16: Brand Promise
```
Header: "Reusable Should Mean Forever"

Key lines:
- "The sustainability promise got watered down somewhere along the way."
- "'Reusable' started meaning 'replace less often.'"
- "That's not reusable. That's just slower disposable."
- "Strawesome believes reusable should mean you never buy another one."
```

### Section 17: Guarantee
```
Header: "Try Strawesome Completely Risk-Free"

Key lines:
- "Lifetime warranty against breakage."
- "If your Strawesome straw ever breaks — for any reason — we replace it."
- "No time limits. No fine print. No hassle."
- "You risk nothing by trying."
```

### Section 18: Two Options
```
Header: "You Have Two Options"

Option 1: Keep using metal.
- "Accept the temperature extremes."
- "Ignore what might be growing inside."
- "Hope your teeth survive the clinks."

Option 2: Make the switch.
- "Experience what glass straws — real glass straws, made properly — actually feel like."
- "Get a straw backed by 16 years of craftsmanship and a lifetime warranty."
```

### Section 19: Final CTA
```
Header: "Ready to Make the Safer Switch?"

Key lines:
- "Strawesome straws are handmade in Michigan."
- "Properly annealed. Backed by a lifetime warranty."
- "Free USA shipping on orders over $49."

CTA: "See The Strawesome Collection"
Subtext: "The last straw you'll ever need to buy."

Trust badges: Handmade in USA, Lifetime Warranty, Free Shipping $49+, 16 Years Trusted
```

### Ad 1: Flip Safety
```
Opening: "Glass straws are safer than metal."

Key lines:
- "Not what you expected to hear."
- "Metal conducts heat. Burns your lips on hot coffee. Freezes them on iced drinks."
- "In 2018, a woman in England fell while holding a jar with a metal straw. The straw didn't bend. Didn't give. It pierced her brain."
- "'Unbreakable' was never the same as 'safe.'"

CTA: "5 reasons you shouldn't use metal straws: {url}"
```

### Ad 2: Attack Decision
```
Opening: "Metal straws are a dangerous choice."

Key lines:
- "Because 'unbreakable' was never the same as 'safe.'"
- "Metal straws are concrete walls for your mouth."
- "In 2016, Starbucks recalled 2.5 million metal straws after reports of children with mouth lacerations."
- "'Unbreakable' sounds like a feature. Until you realize it just means something else breaks instead."
- "The safest materials aren't the hardest. They're the ones that fail safely."

CTA: "5 reasons you shouldn't use metal straws: {url}"
```

### Ad 3: Flip Strength
```
Opening: "Glass straws are stronger than metal straws."

Key lines:
- "Strength isn't about surviving a single impact. Strength is about lasting."
- "Metal corrodes over time. Metal develops micro-scratches that harbor bacteria. Metal leaches chromium and nickel into your acidic drinks."
- "Glass doesn't corrode. Glass doesn't scratch. Glass doesn't leach. Glass doesn't conduct."
- "Metal straws survive drops. Glass straws survive decades."
- "One is impact strength. The other is real strength."

CTA: "5 reasons you shouldn't use metal straws: {url}"
```

---

## Appendix B: Worked Example (Section Breakdown)

This shows what a GOOD section breakdown looks like. Use this as your quality benchmark.

### Section 3: Reason 1 — Temperature Conductivity

**Belief State:**
- Before: "Metal straws are sturdy and practical — temperature is a minor inconvenience I can manage"
- After: "The temperature transfer isn't a minor flaw — it's a fundamental material property that makes metal straws hostile to everyday use"

**What This Does:**
Opens with the first concrete problem. Temperature conductivity is something every metal straw user has experienced but rationalized away. This section names it, explains the physics, and uses the "hot pan handle" analogy to make the reader feel the absurdity of tolerating it.

**Key Technique:** Analogy Bridge — Uses a familiar scenario (grabbing a hot pan handle) to make an abstract concept (thermal conductivity) visceral and undeniable.

**Why This Works:**
The reader has likely burned their lips or winced at cold metal before. They've told themselves "it's fine." This section doesn't let them dismiss it anymore. The pan handle analogy works because it invokes an automatic response — you KNOW you wouldn't keep grabbing a hot pan. So why keep grabbing a hot straw? The cognitive dissonance creates discomfort with their current choice.

**How to Adapt This:**
Identify something your competitor's customers experience but rationalize. Find an everyday scenario where tolerating that problem would be obviously absurd. Connect them.

Formula: "Think about [everyday scenario]. You [natural reaction to avoid discomfort]. You don't keep [tolerating it] thinking 'maybe this time it won't [cause harm].' Your [competitor product] is the [everyday scenario] — except it's [location where harm is worse]."

**Connection to Funnel Arc:**
This is the first of five reasons. It needs to be immediately relatable (temperature is universal) to build momentum. It sets up Section 4 (bacteria) by establishing the pattern: each reason names a material property of metal that creates a problem.

**Lines Worth Studying:**
- "Your metal straw is the hot pan handle you keep grabbing — except it's against your lips." — The analogy lands because it's specific ("hot pan handle") and the stakes escalation is visceral ("against your lips").
- "The straw isn't supposed to be part of the temperature experience. It's supposed to be invisible." — Reframes expectations. Raises the standard for what a straw should do.

---

## Appendix C: Facts Reference (Do Not Hallucinate)

These are the exact facts from the funnel. Quote them accurately. Do not round, paraphrase, or invent similar-sounding facts.

| Fact | Source Section | Exact Wording |
|------|---------------|---------------|
| Starbucks recall | Section 5, Ad 2 | "In 2016, Starbucks recalled 2.5 million stainless steel straws" |
| UK fatality | Section 7, Ad 1 | "In November 2018, Elena Struthers-Gardner — a 60-year-old retired jockey in England" |
| Death details | Section 7 | "The straw impaled her through her eye socket. It pierced her brain. She died two days later." |
| Bacteria stat | Section 4 | "100,000 times more bacteria than a bathroom doorknob" |
| Years in business | Section 10, 11 | "16 years" / "Since 2009" |
| Replacement rate | Section 11 | "1.5% replacement rate" |
| Straws still in use | Section 11 | "98.5% of their straws are still out there" |
| Founder name | Section 10 | "Daedra" |
| Founder location | Section 10 | "Michigan" / "The Glass Academy in Dearborn" |
| Free shipping threshold | Section 19 | "$49" |

---

## Appendix D: Common Mistakes to Avoid

| Mistake | Why It's Wrong | Correct Approach |
|---------|---------------|------------------|
| Writing "This creates tension" without explaining WHY | Vague, doesn't teach Brian anything | Explain the specific psychological mechanism |
| Using "guilt removal" for Brian's audience | Wrong emotion — Brian's readers feel cognitive dissonance, not guilt | Use "ego protection" or "permission to change their mind" |
| Generic "How to Adapt" like "Find what works for your product" | Not actionable, no formula | Provide fill-in-the-blank template |
| Inventing statistics not in the funnel | Hallucination | Only use facts from Appendix C |
| Using technique names not in the glossary | Inconsistency | Only use names from Section 8 |
| Skipping "Connection to Funnel Arc" | Misses how sections work together | Always name previous and next sections |
| Writing Belief States that are too similar | Doesn't capture the real shift | Before/After should feel like different worldviews |

---

## Estimated Scope

- **Part 1:** ~600 words
- **Part 2:** ~500 words
- **Part 3 (Presell):** ~4,500 words (19 × ~240 words)
- **Part 3 (Ads):** ~500 words (3 × ~170 words)
- **Part 4:** ~700 words
- **Total content:** ~6,800 words
- **HTML:** ~2,000 lines

**Estimated Sessions:** 2-3 agent sessions

---

*PRD Created: January 12, 2026*
*Red-teamed and revised: January 12, 2026*
*Ready for agent execution*
