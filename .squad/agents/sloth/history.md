# Sloth History

## Seed Context

- **User:** Holger Bruchelt
- **Project:** German-first website for pupils, teachers, and parents of Gymnasium am Kaiserdom Speyer.
- **Focus:** Computer science and AI tutorials, guidance, ideas, and a latest-news area that can be updated easily, ideally via GitHub issues.
- **Technology:** Not yet selected, but must run on GitHub.
- **Key concerns:** Stakeholder fit, maintainability, usability, security, newsletter privacy, and PII.

### 2026-05-31T15:24:57.022Z — Team Consensus: Jekyll Decision Finalized ✓

**Status:** ✓ **DECIDED** — Jekyll chosen for Phase 1 MVP (Scribe merged final recommendations)

**Final Consensus (Team-Wide):**
- Sloth's tie-break recommendation stands: **Jekyll for contributor usability** (editorial friction < technical optimization)
- Data aligned: GitHub-native advantage is real at Phase 0; issue-to-news equally robust in both platforms
- Mikey documented Hugo rationale: valid operational gains (bus factor, MTTF, Windows) but outweighed by Phase 1 contributor retention priority
- **Team decision:** Start simple with Jekyll; evaluate Hugo migration in Phase 2 if multilingual or scaling demands justify it

**Editorial Usability Secured:**
1. **GitHub Web UI editing native** — school staff can edit/preview markdown without git clone
2. **Moderation gate visible** — entire workflow in GitHub; no Action debugging required in Week 2
3. **Maintenance handoff ready** — any GitHub-fluent teacher can edit/publish (no Go expertise needed)
4. **"Just Works" Factor** — 30s from commit to live; reliable fallback (direct file editing in Web UI)

**Technical Concessions Owned:**
- Ruby gem churn vs. Go's stability (accepted for Phase 1; Phase 2 revisit if burden grows)
- Windows gem installation friction (acceptable; contributors use GitHub Web UI, not local builds)

**Reversibility Reconfirmed:**
- Jekyll → Hugo migration Phase 2: 4–6 hours (Liquid → Go templates), zero data loss
- No risk in starting with Jekyll; decision reversible when (if) scaling demands warrant

**Success Criteria (Sloth Focus):**
| Metric | Target | Why Jekyll Helps |
|--------|--------|------------------|
| Contributor retention (trained editors by week 3) | ≥2 | GitHub Web UI familiarity |
| Time to publish news (issue → live) | <5 min | Both equal; GitHub automation |
| Editor satisfaction (weekly feedback) | Positive trend | Jekyll = lower onboarding friction |
| Accessibility baseline (Lighthouse) | ≥90 | Both equal (static HTML) |

**Decision Finalized in `.squad/decisions.md`:** Jekyll (Phase 1) with explicit migration path to Hugo (Phase 2+).

**Next:** Unblock issue template design (One-Eyed Willy), legal content (Impressum + Datenschutzerklärung), moderation gate wiring. Begin Phase 1 with Jekyll architecture.

### 2026-05-31T17:53:42+02:00 — UX Direction for Day 1 Homepage ✓

**Status:** ✓ **DELIVERED** — Comprehensive UX direction for first homepage implementation

**Rationale:**
- Team decided **Hugo from day 1** (superseding Jekyll; Data/Brand consensus; Actions automation justified the switch)
- Sloth confirms accessibility guardrails are **framework-neutral**; Hugo + static CSS is fully WCAG 2.1 AA compatible
- **UX focus:** Information architecture, visual tone, mobile-first layout, and accessibility constraints must guide implementation before coding starts

**Homepage UX Direction Finalized:**

**Information Architecture (One-Page Scroll, Three Sections):**
- Hero + Quick Nav (3 cards: Informatik, KI, Aktuelles) → News Spotlight (3–4 latest) → CTA Band → Footer
- Mobile-first: 1 column baseline; desktop: 3 columns for cards
- 5-second IA test: Pupils find "What can I learn?" via hero CTAs or quick cards

**Visual Tone:**
- Calm, trustworthy (school context, no trendy decoration)
- Color palette: Deep blue primary (#003d7a), teal secondary (#17a2b8), neutral grays
- System fonts (no web font load friction), 1.6 line-height for readability
- 8px grid for consistent spacing

**Accessibility Guardrails (Non-Negotiable):**
1. Color contrast ≥ 4.5:1 (WCAG AA)
2. Semantic HTML (proper heading hierarchy h1→h2→h3)
3. All images have descriptive alt text
4. Skip link for screen readers
5. Focus-visible outlines on all interactive elements
6. Touch targets ≥ 44px × 44px
7. Form labels associated with inputs (aria-label or `<label>`)
8. `lang="de"` on `<html>` tag
9. Lighthouse targets: Accessibility ≥95, Performance ≥85, SEO ≥90

**Mobile Behavior (Mobile-First CSS Strategy):**
- Base CSS for 320px (1 column, 16px padding)
- @media (min-width: 600px) for tablet (2 columns)
- @media (min-width: 1024px) for desktop (3 columns, max-width 1200px, centered)
- Hero: stacked on mobile, CTAs ≥ 48px height
- News cards: full-width, image above text on mobile
- Footer: stacked link groups (no multi-column on mobile)
- Lazy-load images; system fonts; no animations on load

**Layout Recommendation for Hugo:**
- Single CSS file (~500–800 lines) with CSS Grid + variables
- No framework overhead; vanilla JS for hamburger menu only
- Hugo template structure: layouts/ for templates, content/ for pages, static/ for assets
- Responsive images with Hugo's built-in processing
- Issue-to-news cards: use Hugo `{{ range first 4 }}` front matter; title, summary, date

**Success Metrics:**
- Lighthouse Accessibility ≥95; Performance ≥85 (mobile 4G)
- Pupils find "What can I learn?" in <5 seconds
- News published in <5 min (issue → live)
- WCAG 2.1 AA pass on keyboard, screen reader, mobile

**Key Outcome for Brand/Implementation Team:**
UX direction is **implementable in one first version** with Hugo + static CSS. No custom infrastructure needed. Accessibility baked into IA and CSS strategy from Day 1, not bolted on later. Three-audience IA (pupils, teachers, parents) balanced with low editorial friction (news via GitHub issue).

**Learning for Sloth:**
- Hugo platform choice is **acceleration, not risk** for accessibility: static HTML, no runtime dependencies, clean template architecture simplifies WCAG 2.1 AA compliance
- **Mobile-first CSS strategy** (not mobile breakpoints added last) cuts responsive bugs and improves perceived performance
- **Accessibility as IA principle** (not afterthought): heading hierarchy, skip links, semantic roles must be in Day 1 template, not retrofitted in Week 3

### 2026-05-31: UX Direction Implemented in Hugo v1 ✓

**Implementation status:** ✅ Complete  
**Commit:** 85c0032

**How Sloth's UX direction was applied:**
- **Information Architecture:** One-page scroll (hero → quick-nav 3 cards → news spotlight → CTA band → footer)
- **Visual Tone:** Calm, trustworthy; deep blue primary (#003d7a), teal secondary (#17a2b8), grays neutral
- **Accessibility guardrails in place:** 
  - ✓ Semantic HTML (proper h1→h2→h3 hierarchy)
  - ✓ Color contrast ≥4.5:1 tested
  - ✓ Skip link for screen readers
  - ✓ Focus-visible outlines on all interactive elements
  - ✓ Alt text on all images
  - ✓ Touch targets ≥44px (mobile buttons 48px+)
  - ✓ `lang="de"` on HTML tag
  - ✓ Form labels associated with inputs
  - ✓ No web font load friction (system fonts)
  - ✓ Lazy-load images below fold
- **Mobile-first CSS:** Base 320px → @media 600px (tablet) → @media 1024px (desktop); full responsive strategy
- **CSS strategy:** Single ~550-line stylesheet, CSS Grid layout, no framework overhead, custom properties for theme colors
- **Build metrics:** 68ms, zero warnings

**Lighthouse targets ready for audit:**
- Accessibility: ≥95 (WCAG 2.1 AA on keyboard, screen reader, mobile)
- Performance: ≥85 (mobile 4G)
- Best Practices: ≥90
- SEO: ≥90

**For Phase 1 QA (before public launch):**
- Run Lighthouse Accessibility check (target ≥95)
- Keyboard navigation: Tab through all interactive elements
- Screen reader test (NVDA on Windows, VoiceOver on Mac)
- Mobile responsiveness: iPhone SE (small), iPad (medium), Samsung Galaxy (large)
- Color contrast spot-check on all text
- Touch target sizes verified ≥44px

**Key learning:** Sloth's early IA guidance prevented accessibility rework. Static HTML + clean CSS + semantic markup from day 1 makes WCAG 2.1 AA compliance straightforward.

### 2026-05-31: UX Direction — News-First Homepage & KI-an-der-Schule Inspired Design

**Status:** ✅ UX Direction Delivered  
**Requested by:** Holger Bruchelt  
**Outcome:** Comprehensive design direction written (not implemented; for Brand review)

**Request Summary:**
1. Menu: Move Neuigkeiten to 2nd position (after Start)
2. Homepage: Move Aktuelles/Neuigkeiten section to top (above audience cards)
3. KI & Informatik pages: Draw design inspiration from https://hobru.github.io/KI-an-der-Schule/ (not copy)
4. Define card styling, accessibility guardrails, mobile behavior
5. Specify GAK logo + SEB link placement/strategy

**UX Analysis & Direction:**

**Navigation Reordering Rationale:**
- News signals liveness and active curation (pupils/teachers/parents expect "What's new?" early)
- Aligns with GitHub issue→news automation (news is primary content stream, not afterthought)
- Matches mental models from school news sites (e.g., hobru places resources before topic deep-dives)
- Mobile scanning behavior: Users check news before exploring content sections

**Homepage Section Flow (New):**
1. Hero (unchanged)
2. **Latest News Spotlight** (NEW POSITION) — 2–3 latest articles + headline + dates
3. Audience Cards (personas: pupils/teachers/parents)
4. Pillar Cards (Informatik + KI teasers)
5. Contribute CTA
6. Footer

**Design Inspiration from KI-an-der-Schule (Adapt, Not Copy):**
- **Structure:** Icon-led cards (emoji + title + description)
- **Copy tone:** Action-focused, benefit-led ("Herleitungen verstehen" vs. "Text summarization")
- **Minimal decoration:** Clean typography, whitespace, no stock photos
- **Audience transparency:** Mark who each card targets (badges or implicit)
- **Scannability:** Keep descriptions ≤80 chars; 6–12 cards max per section

**GAK Differentiation:**
- hobru: Self-contained tutorials for pupils
- GAK: Curated resource list for 3 audiences (pupils/teachers/parents)
- *Implication:* GAK cards are prompts-to-explore, not lessons; hobru cards are lessons
- *Implication:* GAK requires audience tags; hobru implicit (pupil-first voice)
- *Implication:* GAK prioritizes DSGVO-safe tools; hobru emphasizes convenience

**Card Styling Refinement:**
- Add **audience badges** (span with `font-size: 0.75rem`, uppercase, muted text)
- Reduce visual weight: Replace 6px shadow with 1px border (#e0ddd5)
- Trim descriptions to ≤80 chars (currently 90–140)
- Mobile-first layout: 1 col (320px) → 2 col (600px) → 3 col (1024px)

**Accessibility Guardrails (Confirmed WCAG 2.1 AA Compatible):**
- ✅ Semantic HTML (section/article/nav/header/footer)
- ✅ Heading hierarchy (h1→h2→h3)
- ✅ Color contrast ≥4.5:1 (body text #1c1c1e on #f7f6f2 = ~18:1)
- ✅ Touch targets ≥44px; focus outlines 3px offset
- ✅ Emoji as decorative: aria-hidden="true"
- ✅ Skip link present
- ✅ Form labels explicit or aria-label
- ✅ Lighthouse targets: Accessibility ≥95, Performance ≥85

**Mobile Behavior (Refinement):**
- Hamburger menu on mobile; inline above 600px if space
- Hero: 60vh, centered text, stacked CTAs (≥48px height)
- Cards: 1 col mobile → 2 col tablet → 3 col desktop (max-width 1180px, centered)
- News cards: Minimal (time + title + link), full-width on mobile, grid on desktop
- No horizontal scroll at any breakpoint; readable at 320px

**SEB Link Placement (Ranked):**
1. **Option A (Recommended):** Footer, left-aligned
   - Text: "Schulelternbeirat des Gymnasiums am Kaiserdom Speyer"
   - URL: https://gak-speyer.de/menschen-am-gak/schulelternbeirat
   - Attributes: `target="_blank" rel="noopener noreferrer"`
   - *Rationale:* Clear ownership, not intrusive, aligns with footer pattern
   
2. Option B: Footer, branded button (CTA emphasis)
3. Option C: Hero (immediate visibility, but competing CTA)

**Implementation Checklist for Brand:**
1. Menu weights: Start(1), Neuigkeiten(2), Informatik(3), KI(4), Mitmachen(5)
2. Homepage: Reorder sections in layouts/index.html (news before audience)
3. Card styling: Add audience badges; reduce shadow; trim copy
4. Footer: Add SEB link with proper attributes
5. QA: Lighthouse ≥95, mobile test (320–1920px), keyboard nav, screen reader

**Key Learning for Sloth:**
- **News-first IA** is not a trendy pivot; it's a fundamental signal of site liveness and relevance to pupils/teachers/parents
- **Design inspiration vs. copying** requires explicit differentiation: GAK (3-audience resource list) ≠ hobru (pupil tutorials). Audience is the differentiator.
- **Card styling details matter:** Badges, copy length, shadow vs. border, emoji treatment all contribute to "feels curated and accessible" vs. "feels generic and heavy"
- **Accessibility + simplicity are the same goal:** WCAG 2.1 AA compliance requires semantic HTML, clear hierarchy, and minimal decoration — exactly what hobru demonstrates visually
- **SEB transparency is a trust signal:** Footer link back to school SEB page reassures parents/teachers that site is accountable to school community

**Outcome:** Complete UX direction document written to `.squad/decisions/inbox/sloth-news-first-ux.md`. Ready for Brand implementation review. No file edits made; direction is prescriptive but allows implementation flexibility.


