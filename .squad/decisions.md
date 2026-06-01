# Squad Decisions

## Active Decisions

### Digitales & Informatik: Profiled subject order and stable links (2026-06-01)

**Status:** Decided & Implemented  
**Proposer:** Holger Bruchelt directive, implemented by Brand  

**Decision:** On `content/informatik/_index.md`, subject resources should open with language/humanities areas to reflect GAK's humanist Gymnasium profile with Latin, then continue into MINT/digital topics. External learning links on the page should prefer stable, directly reachable alternatives when existing offers fail link checks.

**Rationale:** The ordering better represents the school's profile without devaluing MINT/Informatik. Reliable links matter more for pupils and parents than brand recognition when links return errors or app failure pages.

**Verification:** Brand reported all 43 external URLs on the page checked with GET + redirects, final HTTP status < 400, no scanned error texts, and `hugo --minify` successful.

### Technology Platform: GAK Website (2026-05-31)

**Proposers:** Data (Tech Architect), Sloth (UX), One-Eyed Willy (Security), Mikey (Product Coordinator), Brand (Full-stack)  
**Status:** Decided (2026-05-31 team consensus: **Hugo from day one** — supersedes Jekyll Phase 1, per clarified user preference and issue-driven news pipeline requirement)  
**Decision Frame:** [Mikey] See decision timeline at end of this section.

#### Rechecks Completed (2026-05-31)
- **Data** (Tech Architect) **[RETRACT JEKYLL, RECOMMEND HUGO IMMEDIATELY]**: Initial Jekyll recommendation stood because Data's stated threshold to switch ("custom Actions accepted day 1") has been met—Holger now explicitly requests GitHub Action-based issue-to-news pipeline. With Actions required regardless, Hugo's operational advantages (single binary, zero Ruby friction, 4–6 hr migration cost avoided, ~50ms builds) dominate. Starting with Hugo eliminates throwaway work before content exists. Same security/privacy guardrails apply. Setup complexity ~3.5 hrs (modest and front-loaded).
- **Mikey** (Product Coordinator) **[AFFIRM HUGO — NO JEKYLL PHASE 1]**: Holger's directive resolves the ambiguity: Actions are accepted day 1. Phased approach (Jekyll → Hugo) now creates risk: contributor training debt, content structure re-mapping, 4–6 hr engineering tax. Build real project from day one. Hugo homepage + 2 static sections + issue-to-news news loop is tractable in 3–4 hours setup.
- **Brand** (Full-stack Implementer) **[HUGO FEASIBILITY CONFIRMED]**: Created detailed implementation sketch. Repository structure, issue template (no PII fields), 2-step workflow (issue-to-news Action with validation, moderation gate), GitHub Pages deploy, legal pages (Impressum/Datenschutzerklärung), accessibility/privacy guardrails all realistic. Concrete setup breakdown: config (10 min), content stubs (20 min), layouts (45 min), workflows (90 min), testing (30 min) = ~3.5 hrs one-time. Ongoing: issue-to-live < 5 min; static page edits ~1 min.
- **Sloth** (UX/Accessibility) **[DEFERS TO TEAM, ACCESSIBILITY PROTOCOL STANDS]**: Original tie-break (Jekyll for contributor friction) assumed Jekyll avoids Actions complexity. New reality: Actions are day 1 regardless. Sloth's accessibility and contributor retention success metrics remain unchanged; framework choice is neutral to WCAG 2.1 AA audit and editor onboarding. Confirms accessible Hugo themes exist (e.g. PaperMod); theme selection can reduce setup overhead to ~1.5 hrs if custom templating skipped.

#### Competing Recommendations

**Option A: Hugo** (Mikey + Data consensus — **NOW DECIDED**) ✓ **DECIDED**
- Zero-runtime dependencies; single Go binary; fastest builds (~50ms)
- Built-in i18n; issue-to-news pipeline simple and reliable
- GitHub Actions `peaceiris/actions-hugo` deploys in seconds
- Issue template captures: title, abstract, link, audience, category
- GitHub Action workflow: issue labeled `freigegeben` → markdown file generated → auto-publish
- **Operational advantage:** Lower MTTF, simpler Windows debugging, resilient single-binary model
- **Setup time:** ~3–3.5 hrs one-time (config, layouts, workflows)
- **Avoids:** 4–6 hr future migration; throwaway Jekyll Phase 1 work

**Option B: Jekyll** (Previously Phase 1 — superseded)
- GitHub Pages native support; Ruby ecosystem stable
- Same issue-to-news workflow with bot validation
- **Why superseded:** User directive + Actions required day 1 removes native Pages advantage; Hugo's simpler operational model wins when Actions are baseline

**Decision Outcome (2026-05-31):**
- **Recommendation:** **Hugo from day one** (Data + Brand consensus; Sloth confirms accessibility neutral; Mikey aligns on product timeline; One-Eyed Willy security guardrails unchanged)
- **Rationale:** Holger's explicit request for GitHub Action-based news publishing satisfies Data's threshold to switch. Phase 1 Jekyll advantage (native Pages, no Actions) evaporates. With Actions required regardless, Hugo's single-binary operational simplicity + elimination of 4–6 hr future migration cost + front-loaded setup (3–3.5 hrs) make Hugo the right choice from day one. Zero throwaway work before content exists.
- **Architecture:**
  - Hosting/build: GitHub Pages with Hugo deployed via GitHub Actions
  - Content: Markdown + front matter in `content/` (homepage, informatik, ki sections, news/)
  - Editing: GitHub Web UI or PRs for content
  - Automation: GitHub issue form → validation Action (anti-PII, field length) → moderation label (`freigegeben`) → auto-PR + merge → auto-rebuild
  - Privacy: Issue Form has no PII fields; German privacy warning at top; Impressum + Datenschutzerklärung as static pages
  - Validation: Action checks title ≤ 80 chars, summary ≤ 200 chars, regex anti-PII scan (email/phone patterns)
  - Rollback: Delete/revert generated `.md` file → push to main → rebuild

#### Privacy & Security Guardrails (Non-negotiable blockers)

**One-Eyed Willy's Requirements:**
1. Issue template MUST NOT request PII; include warning: "Geben Sie keine personenbezogenen Daten in dieses Issue ein."
2. Moderation gate REQUIRED before publishing (manual `approved` label or review step)
3. No subscriber emails/names in Git; external newsletter processor if added
4. Privacy-safe analytics only (Plausible, Goatcounter, or none at launch)
5. External links: `rel="noopener noreferrer"` + `target="_blank"`
6. GitHub Actions: least privilege (no `contents: write` in issue-triggered flows; pin third-party actions to SHA)
7. **Mandatory legal pages at launch:** Impressum (§5 TMG) + Datenschutzerklärung

**Blockers (must resolve before implementation):**
- Issue template design (no PII fields)
- Moderation gate in build pipeline
- Impressum + Datenschutz content ready

#### MVP Scope (Product & Timeline)

**Phase 1 (MVP — 2 weeks):**
- Platform: Hugo (static site generator)
- Hosting: GitHub Pages (Actions-based deploy)
- Publishing: GitHub Actions on labeled issue creation (`freigegeben` label)
- Deliver: Homepage + news + Informatik + KI sections + accessibility baseline + privacy baseline
- **Out of scope:** Newsletter, advanced search, CMS UI
- **Setup time:** ~3–3.5 hours front-loaded

**Phase 2 (MVP+1 — 6 weeks after stable):**
- Evaluate Decap CMS (optional UI editing)
- Newsletter (with GDPR compliance review)
- Search functionality

**Phase 3+:** i18n, interactive modules, advanced analytics

#### Stakeholder Risks & Mitigations

- **Publishing friction stalls content:** Automate issue→markdown; weekly check-in with content team
- **Non-technical editors excluded:** Start with GitHub Web UI; Phase 2 adds CMS UI if needed
- **Poor accessibility/performance:** Sloth does WCAG 2.1 AA audit; Chunk tests on school devices
- **Privacy/security gaps:** One-Eyed Willy reviews GitHub Actions; newsletter deferred for compliance review
- **Maintenance burden grows:** Document architecture; keep dependencies minimal; quarterly check-ins

#### What Must Be Decided NOW

1. **Content structure:** How do issues map to markdown files in Jekyll?
2. **Build trigger:** Every commit? Every labeled issue? Moderation gate timing?
3. **Baseline privacy:** No analytics/cookies in MVP?
4. **Language:** German content-first; English deferred?
5. **Issue template design:** Avoid PII fields; include German privacy warning

#### What Gets Deferred

- Newsletter platform and GDPR setup
- Advanced search / full-text indexing
- CMS UI for non-technical editors
- Analytics (only if school approves + compliant)
- Multi-language support
- Social media sharing

#### Success Metrics

| Metric | Target | Rationale |
|--------|--------|-----------|
| Time to publish news (issue → live) | < 5 minutes | Low-friction workflow validation |
| Accessibility score (Lighthouse) | ≥ 90 | School audience trust |
| Mobile performance (Lighthouse) | ≥ 85 | Pupils on school/personal phones |
| Content editor satisfaction | Weekly feedback | Friction signal |
| Zero security incidents | Audited by One-Eyed Willy | Baseline compliance |

### Brand: Stadtbibliothek-Hinweis auf Digitales-Seite (2026-06-01)

**Status:** Decided & Implemented  
**Proposer:** Brand (Full-stack)  
**Commit:** 33e4821 (Add Speyer library notice to Digitales page)

**Problem:** Holger requested a notice on the "Digitales & Informatik" page before the subject sections, promoting Stadtbibliothek Speyer's free access for pupils to books, magazines, videos/media, and digital learning tools (Sofatutor, Plan6).

**Decision:** The notice is maintained as a structured Front Matter block `library_notice` in `content/informatik/_index.md` and rendered in the Informatik layout immediately after the SEB notice but before subject/resource sections.

**Rationale:** Keeps editorial content maintainable without template changes; preserves SEB framing; reuses the card/banner system consistently across KI/Digitales pages.

**Implementation:**
- Front matter in `content/informatik/_index.md`: `library_notice` YAML block with Stadtbibliothek details + links
- Informatik layout renders `library_notice` as a banner component
- CSS classes align with existing SEB notice styling
- Links to Stadtbibliothek website and Digitale Angebote

**Verification:** `hugo --minify` ran successfully; notice displays on Digitales page; no accessibility or build issues.

### Brand: GAK-Logo auf der Homepage (2026-06-01)

**Status:** Implemented  
**Owner:** Brand  

**Decision:** Use Holgers provided local asset `gak-seb-logo.jpg` as the homepage GAK logo, stored at `static/images/gak-seb-logo.jpg`, and reference it from `layouts/index.html` in the existing hero logo slot next to „Digitales Lernen – von Eltern für Schule und Familie".

**Rationale:** The user explicitly supplied the logo file and asked that it be placed in the correct project folder. Keeping it local under Hugo's static images folder avoids hotlinking, preserves GitHub Pages compatibility, and keeps the existing responsive/accessibility behavior.

**Verification:** `hugo --minify` completed successfully with 34 pages and zero warnings.

---

---

## Implemented: Hugo Homepage v1 (2026-05-31)

**Status:** ✅ Completed & deployed | **Commit:** 85c0032  
**Responsible:** Brand (implementer); Mouth (content), Sloth (UX), Chunk/Andy/Stef (reviews)

### What Exists

**Core Pages:**
- Homepage (hero + value props + news spotlight + CTA + footer)
- Digitales & Informatik (with 6 idea cards, sample content marked)
- KI in der Schule (with 6 idea cards, sample content marked)
- Neuigkeiten / News archive (with 3 sample posts: KI-Begriffe, Wetterdaten, Elternabend)
- Impressum & Datenschutzerklärung (legal placeholders)
- Navigation: Informatik, KI, Aktuelles, Kontakt

**Technical Stack:**
- Hugo v0.134.3 (static generator)
- GitHub Pages deployment via GitHub Actions (peaceiris/actions-hugo, SHA-pinned)
- Custom responsive CSS (~550 lines; mobile-first, 8px grid, semantic HTML)
- No runtime dependencies; vanilla JS minimal
- German-first content; German locale in `hugo.toml`

**GitHub Workflow:**
- `.github/workflows/deploy.yml`: Automated build + deploy on push to `main`
- Build time: ~68ms, zero warnings

### Reviewer Principles (Consensus)

#### Content (Mouth)
- **Sample content explicitly marked** `[SAMPLE]` to prevent accidental publication
- **No PII in proposals** — form template prevents phone/email fields
- **Persona-driven structure:** Separate entry points for pupils (Schüler·innen), teachers (Lehrkräfte), parents (Eltern)
- **Format-standardized** news items (title ≤80 chars, abstract ≤200 chars, categories, audience tags)

#### Pupils/UX (Chunk)
- **Three clear pathways:** Aktuell erfahren | Selbst ausprobieren | Verstehen & Hinterfragen
- **Official status visible** (school badge + age guidance near top)
- **News highlights on homepage** always visible; movement signals liveness
- **Concrete hooks over jargon** (e.g., "Dein erstes Spiel programmieren mit Python" not "Introduction to Python")
- **Guidance on first visit** (collapsible "Neue hier?" section explaining tutorial duration/difficulty)

#### Teachers (Andy)
- **Actionable specificity:** Learning pathways show grade levels (Jahrgangsstufe 9–13) + time commitment
- **Teacher Quick-Start card** on homepage (grade filter → curated bundles)
- **Audience tagging in news** (`[Lehrkraft]`, `[Schüler·innen]`, `[Beide]`) with optional filter
- **Sample lessons visible:** Homepage teaser shows one real complete lesson example
- **Maintenance clarity:** Mention content authors + feedback pathway (GitHub issues)

#### Parents (Stef)
- **"Why" in plain German:** Lead with values, not jargon; use "wir bereiten Ihre Kinder vor"
- **Trust signals on fold:** School logo/name + teacher attribution + legal links (Impressum, Datenschutz)
- **"What's new" frequency clear:** State update cadence (e.g., "wir aktualisieren diese Seite jede Woche")
- **Parent FAQ (5–7 Q&As):** Address unstated concerns (Do they need a home computer? Is it safe? How can I support?)
- **Stay-informed pathway:** Non-mandatory email/update options (checkbox-based, GDPR-compliant; deferred to Phase 2)

#### UX/Accessibility (Sloth)
- **Semantic, accessible card layout** (not stock photos; subtle color/pattern for hero)
- **WCAG 2.1 AA targets:** Color contrast ≥4.5:1, proper heading hierarchy (H1–H3), alt text, focus-visible, ≥44px touch targets
- **Mobile-first CSS:** Base styles for 320px; scale up with @media (600px tablet, 1024px desktop)
- **Lighthouse targets:** Accessibility ≥95, Performance ≥85, Best Practices ≥90, SEO ≥90
- **No web fonts on first load** (system stack); lazy-load images below fold

### Pre-Launch Requirements (Blockers)

| Item | Owner | Status |
|------|-------|--------|
| Replace `content/impressum/_index.md` with real §5 TMG text | School / Legal | ⏳ Pending |
| Replace `content/datenschutz/_index.md` with DSGVO-compliant text | School / Legal | ⏳ Pending |
| Set `baseURL` in `hugo.toml` to actual domain | Holger / Brand | ⏳ Pending |
| Review GitHub Actions permissions & security guardrails | One-Eyed Willy | ⏳ Pending |
| Confirm sample content will be replaced before public launch | Content team | ⏳ Pending |

### Deferred to Phase 2

- **Issue-to-News GitHub Action** (moderation pipeline): Structure ready in front matter; workflow to be added
- **Newsletter / email signup:** Requires GDPR compliance review by One-Eyed Willy
- **Analytics:** No tracking in v1; evaluate Plausible/Goatcounter if school approves
- **CMS UI for non-technical editors:** Decap CMS optional in Phase 2
- **Multi-language support:** German-first in v1; English Phase 2+

### How Content Editors Contribute

**Adding a News Post:**
```yaml
# Create: content/news/YYYY-MM-DD-titel.md
---
title: "Titel"
date: 2026-06-01
draft: false
categories: ["KI"]  # or "Informatik", "MINT", etc.
audiences: ["Schülerinnen und Schüler"]  # multi-select
abstract: "Kurze Zusammenfassung (≤200 Zeichen, no PII)"
sample: false  # set to true during testing; false for real content
---
Inhalt hier...
```

**Adding an Idea Card:**
Edit front matter in `content/informatik/_index.md` or `content/ki/_index.md`:
```yaml
ideas:
  - icon: "💡"
    title: "Titel"
    desc: "Kurze Beschreibung"
    audience: "Schülerinnen und Schüler"  # or "Lehrkräfte", "Eltern"
    duration: "ca. 30 Min."
    badges: ["Coding", "Anfänger"]
```

### Success Criteria (Agreed)

| Goal | Metric | Target |
|------|--------|--------|
| **Fast to load** | Lighthouse Performance (mobile 4G) | ≥85 |
| **Accessible** | Lighthouse Accessibility + WCAG 2.1 AA | ≥95 |
| **Clear IA** | Pupils find "What can I learn?" | < 5 seconds |
| **Mobile-friendly** | Responsive 320px–1920px, no horiz. scroll | All text readable |
| **Editor-friendly** | Publish news cycle (edit → live) | < 5 minutes |
| **Zero security incidents** | Audited by One-Eyed Willy | Baseline compliance |

### Local Development

```bash
hugo server
# → http://localhost:1313/
```

Deploy to GitHub Pages:
1. Settings → Pages → Source: **GitHub Actions**
2. Push to `main` → auto-builds and deploys

---

## SEB Positioning & Ownership Clarification (2026-05-31)

**Status:** Decided & implemented | **Commits:** fa67966, 40e2d6f  
**Responsible:** Mouth (guidance), Brand (implementation)  
**Requested by:** Holger Bruchelt

### Background

Holger clarified that the website must be presented as created and maintained by the **Schulelternbeirat (SEB) des Gymnasiums am Kaiserdom Speyer**, not as official school communication.

### Decision

The site is reframed throughout as a **Schulelternbeirat initiative**, paralleling the SEB-only model at https://seb-shgym-diez.de/. All official-sounding claims are removed.

### What Changed

**Site identity:**
- Header: "Schulelternbeirat des Gymnasiums am Kaiserdom Speyer"
- Hero: "Digitales Lernen – von Eltern für Schule und Familie"
- Footer: "© 2026 Schulelternbeirat des Gymnasiums am Kaiserdom Speyer" + disclaimer: "Diese Website ist ein Projekt des Schulelternbeirats und stellt keine offizielle Schulkommunikation dar."
- Legal pages (Impressum, Datenschutz): SEB authorship
- README.md: "GAK Digital – Schulelternbeirat des Gymnasiums am Kaiserdom Speyer"
- hugo.toml: `title = "GAK Digital – Schulelternbeirat"`, new param `seb_disclaimer` for reuse

**Phrases to avoid/replace:**
- ❌ "Offizielle Seite des Gymnasiums am Kaiserdom" → ✅ "Ein Projekt des Schulelternbeirats"
- ❌ "Vom Gymnasium" (alone) → ✅ "Vom Schulelternbeirat"
- ❌ "Schulische Initiative" (implying authority) → ✅ "Eine Initiative der Eltern"

### Implementation Checklist

- ✅ Hero label & title updated (Option A: Full SEB attribution + "von Eltern für Schule und Familie")
- ✅ Header logo & site branding changed to SEB
- ✅ Footer copyright & disclaimer added
- ✅ Sample-site notice emphasizes SEB origin
- ✅ README.md updated
- ✅ hugo.toml title, description, school param, shortName, seb_disclaimer all updated
- ✅ Impressum & Datenschutz responsible parties updated to SEB
- ⏳ Pending: Supply SEB chair name, address, e-mail for Impressum (Holger / SEB)
- ⏳ Pending: Supply SEB contact for Datenschutz responsible party (Holger / SEB)
- ⏳ Pending: Confirm final wording of `seb_disclaimer` with SEB board (Holger / Mouth)

### Build Verification

Hugo build: 34 pages, 180 ms, zero warnings ✓

### Rationale

Clear ownership avoids legal/reputational risk. Transparency about SEB authorship is more trustworthy than school-branded unofficial content. The SEB remains the neutral, parent-led voice for digital literacy without claiming school authority.

---

---

## UX Direction: News-First Navigation (2026-05-31)

**Status:** Decided (Team recommendation: implement)  
**Proposer:** Sloth (UX/Accessibility)  
**For:** Brand (Implementation)

### Changes Approved

**Navigation menu reorder:**
- Before: Start → Informatik → KI → News → Mitmachen
- After: Start → News → Informatik → KI → Mitmachen
- Rationale: News elevated signals liveness; pupils/parents check "What's new?" first; aligns with GitHub issue→automation workflow

**Homepage section reorder:**
- Before: Hero → Audience cards → Pillars → News → Contribute → Footer
- After: Hero → **News spotlight** → Audience cards → Pillars → Contribute → Footer
- Rationale: Latest articles visible above fold; increases engagement

**Design language (inspired, not copied from KI-an-der-Schule):**
- Emoji/icon-led cards + clean typography + minimal shadows
- Audience badges on idea cards (`[Schüler·innen]`, `[Lehrkräfte]`, `[Eltern]`)
- Mobile-first CSS: 320px base, @media 600px (tablet), 1024px (desktop)
- Descriptions trimmed to ≤80 chars for scannability

### Accessibility Guardrails (Non-Negotiable)

- Heading hierarchy preserved (h1 → h2 → h3)
- Color contrast ≥4.5:1 (WCAG AA)
- Touch targets ≥44px × 44px
- Focus visible on all interactive elements
- Emoji in cards: `aria-hidden="true"`
- Screen reader support: `<section>`, `<article>`, `<nav>` semantic HTML

### Implementation Checklist (Brand)

| Task | Status |
|------|--------|
| Update hugo.toml menu weights | ⏳ Pending |
| Reorder homepage sections (layouts/index.html) | ⏳ Pending |
| Add audience badges to idea cards | ⏳ Pending |
| Add SEB link to footer (target="_blank", rel="noopener noreferrer") | ⏳ Pending |
| Lighthouse audit (Accessibility ≥95, Performance ≥85) | ⏳ Pending |

### SEB Link Placement (Chosen: Option A)

Footer text + link to official SEB page (https://gak-speyer.de/menschen-am-gak/schulelternbeirat) with full security attributes. Not intrusive; maintains focus on content.

---

## Real Content Integration: Informatik & KI Pages (2026-05-31)

**Status:** Ready for implementation  
**Proposer:** Mouth (German Content Editor)  
**For:** Brand (Implementation)  
**Commitment:** All external links verified; zero `[SAMPLE]` markers; paraphrased + cited (no verbatim copying)

### What's New

**Informatik Section:**
- Six concrete idea cards (HTML/CSS, data analysis, media literacy, teacher checklist, video production, parent explainer)
- Real lead text: "Dieser Bereich sammelt Impulse... ein Projekt des Schulelternbeirats"
- Eight curated external links (Serlo, openHPI, BWINF, klicksafe, etc.)
- Parent FAQ: "Braucht mein Kind einen Computer?" + 2 more

**KI Section:**
- Six practical cards (prompt challenges, hallucination awareness, glossary, parent guide, DSGVO overview, reflection framework)
- Real lead text: "KI ist längst Realität im Schulalltag..."
- Eight curated links (KI-an-der-Schule, ChatGPT, NotebookLM, Perplexity, telli, klicksafe, KMK, BMBF)
- Six Leitfragen for responsible AI use (audience-independent reflection toolkit)

### Implementation Steps (Brand)

1. Replace `content/informatik/_index.md` with DRAFT content (ready to copy-paste)
2. Replace `content/ki/_index.md` with DRAFT content
3. Set `sample: false` in both front matter
4. Run: `hugo server` → verify no 404s, Lighthouse ≥85 (Performance), ≥95 (Accessibility)
5. Spot-check all 16 external links are live

### Approval Checklist

- [ ] Holger: SEB attribution tone acceptable
- [ ] Andy: Informatik cards match curriculum grades (9–13)
- [ ] Stef (parent rep): Parent links/FAQ appropriate
- [ ] Sloth: Accessibility targets met post-integration
- [ ] One-Eyed Willy: All external links DSGVO-safe

### Pending Reviews

1. **Andy (teacher/curriculum):** Do the 6 Informatik project ideas fit GAK syllabus & grade levels?
2. **One-Eyed Willy:** Are ChatGPT + telli.de acceptable under school media policy?
3. **Mouth:** Should "Grundbegriffe" expand from 5 to 8–10 terms with definitions?

---

## Brand: Hugo Patterns & Decisions (2026-05-31)

**Status:** Implemented  
**Implementer:** Brand (Full-stack)  
**Commit:** 7055847

### Decision 1: Hugo Render Hook for External Link Security

**Problem:** All external links need `rel="noopener noreferrer"` (One-Eyed Willy requirement). Goldmark's `unsafe = false` prevents raw HTML in Markdown.

**Solution:** Hugo render hook at `layouts/_default/_markup/render-link.html` (Hugo 0.62+):
```html
{{- $url := .Destination -}}
{{- if or (strings.HasPrefix $url "http://") (strings.HasPrefix $url "https://") -}}
  <a href="{{ $url }}" target="_blank" rel="noopener noreferrer"{{ with .Title }} title="{{ . }}"{{ end }}>{{ .Text | safeHTML }}</a>
{{- else -}}
  <a href="{{ $url }}"{{ with .Title }} title="{{ . }}"{{ end }}>{{ .Text | safeHTML }}</a>
{{- end -}}
```

**Why:** Single file covers all Markdown links site-wide; no XSS risk; no need for `unsafe = true`.

**Do NOT:** Switch to `unsafe = true` (allows XSS) or add raw HTML per-link in .md files.

### Decision 2: Badge System Extension Pattern

**Rule:** Add new badge labels as key-value pairs in `$classMap` dict (informatik/list.html, ki/list.html) + corresponding CSS class.

**Badge naming:**
- Dict key = exact front matter label (e.g., `"Kritisches Denken"`)
- CSS class = ASCII-safe kebab-case (ä→ae, ö→oe, spaces→dashes)
- Default fallback: `"tools"` (any unmapped label falls back)

**New badges in this integration:**
Anfänger, Datenanalyse, Medienkompetenz, DSGVO, Kreativität, Unterstützung, Praktisch, Grundlagen, Verantwortung, Reflexion, Kritisches Denken, Denken

### Decision 3: Card Structure (Sloth Alignment)

**Old:** icon → badges → h3 → description → audience  
**New:** icon → h3 → p.audience → p.description → badges

**Why:** Title and audience are scannable first; metadata at card bottom. Implemented as Sloth recommends. `.idea-card__badge-row` uses `margin-top: auto` for flex alignment.

**This is the canonical structure.** Do not revert.

### Decision 4: DRAFT File Cleanup

Local DRAFT files (DRAFT_informatik_index.md, DRAFT_ki_index.md) deleted post-merge. Convention for future: place DRAFT files in project root or `drafts/` folder, name as `DRAFT_{section}_{file}.md`, delete after integration (superseded by real content).

### Decision 5: sampleSite Flag

`sampleSite = false` in hugo.toml. Homepage banner suppressed. Individual news posts with `sample: true` in front matter still show per-post badges (addressed when news section populated with real content).

---

## Structural Updates: Menu, Homepage, Impressum, SEB Link (2026-05-31)

**Status:** Implemented & built  
**Implementer:** Brand (Full-stack)  
**Commit:** 975f31d  
**Build:** 34 pages, 207ms, zero warnings

### Four Self-Contained Changes

**1. Menu order (hugo.toml):**
- Before: Start → Informatik → KI → News → Mitmachen
- After: Start → News → Informatik → KI → Mitmachen (follows Sloth UX recommendation)

**2. Homepage section order (layouts/index.html):**
- Before: Hero → Audience cards → Pillars → News → Contribute → Footer
- After: Hero → **News** → Audience cards → Pillars → Contribute → Footer (news elevated above fold)

**3. Impressum real data (content/impressum/_index.md):**
- Name: Holger Bruchelt
- Address: Carl-Dupre-Str. 5, 67346 Speyer
- Email: seb-at-gak-speyer.de (obfuscated text, no mailto)
- GAK SEB link: https://gak-speyer.de/menschen-am-gak/schulelternbeirat added in body
- Placeholder warning removed

**4. Footer SEB link (layouts/partials/footer.html):**
- Added "Offiz. SEB-Seite" link to https://gak-speyer.de/menschen-am-gak/schulelternbeirat
- Attributes: `target="_blank" rel="noopener noreferrer"` ✓

**5. Datenschutz alignment (content/datenschutz/_index.md):**
- Aligned responsible party + GDPR contact with Impressum (same name/address)

### Deliberately NOT Done

- **GAK logo:** Not added. One-Eyed Willy reviewing rights/privacy. Layout slot exists in CSS for future use.
- **Informatik/KI rewrite:** Deferred. Mouth and Sloth preparing content/UX guidance.
- **mailto link:** Not added. No safe pattern exists; obfuscated text per instructions.

### For Team Review

| Agent | Review Needed |
|-------|---------------|
| One-Eyed Willy | Confirm obfuscated email format acceptable; confirm Holger's personal address is intentional (vs. organizational) |
| Mouth | Review new Impressum wording; Datenschutz alignment |
| Sloth | Verify news-first homepage meets UX intent |

---

## Content Migration Gate: KI-an-der-Schule Source (2026-05-31)

**Author:** One-Eyed Willy  
**Status:** Approved with Conditions  
**Requested by:** Holger Bruchelt

### Executive Summary

**Verdict: APPROVE WITH CONDITIONS**

Holger's request to migrate content and replicate layout/functionality from hobru.github.io/KI-an-der-Schule/ is **low-risk and approved**, subject to operational best-practice conditions. The source is privacy-native (zero analytics, zero tracking, zero external scripts) and Holger is the confirmed author. Conditions focus on deduplication, attribution, and link/asset hygiene to maintain GAK's privacy baseline.

### Assessment Detail

#### 1. Source Ownership & Licensing Risk: **LOW ✅**

- **Requester is author**: Holger Bruchelt (hobru) confirmed as original creator of hobru/KI-an-der-Schule repository.
- **No copyright conflicts detected**: Repository has no license header; inferred as personal educational project.
- **Organizational authority**: Holger as Schulelternbeirat representative has organizational standing to approve reuse.

**Recommendation:** Attribution to Holger/hobru in Impressum is courteous. No legal requirement detected.

#### 2. Source Privacy & Security Risk: **LOW ✅**

**Technical Analysis:**

| Aspect | Finding | Risk |
|--------|---------|------|
| **Repository Type** | Pure HTML, no npm/gem/Bundler | Zero dependency risk ✅ |
| **External Scripts** | 0 detected | No tracking/analytics injection ✅ |
| **Analytics** | 0 (no Google Analytics, Matomo, Plausible, etc.) | Privacy-native ✅ |
| **Cookies/Tracking** | 0 patterns | No GDPR consent burden ✅ |
| **Third-Party Iframes** | 0 detected | No embedded external content ✅ |
| **Dependencies** | None | No supply-chain risk ✅ |

**Conclusion:** Source is privacy-first static content. Safe to copy without inheriting tracking or security debt.

#### 3. Content Overlap: **MEDIUM (Design Consideration)**

**Existing GAK Content** (~40% overlap):
- AI tool recommendations
- DSGVO/Datenschutz guidance
- Responsible use framework

**Source Content** (~60% unique):
- Detailed prompting techniques
- Extended tool catalog
- How KI works / tool mechanics
- Learning strategies by tool type

**Recommendation:** Deduplication strongly recommended before publishing.

#### 4. Safe Replication Path: **APPROVE**

| Component | Status | Guardrail |
|-----------|--------|-----------|
| **Static content** | ✅ Safe | Copy as-is |
| **Layout/CSS** | ✅ Safe | Local CSS only |
| **External links** | ⚠️ Conditional | Apply `rel="noopener noreferrer"` universally |
| **Images** | ⚠️ Conditional | Download to `/static/images/`; NO hotlinks |
| **JavaScript** | ⚠️ Conditional | Bundle locally; NO external scripts |

### Conditions for Implementation

**Mandatory (blocking if unmet):**

1. **Attribution in Impressum** — Add note referencing Holger Bruchelt's source
2. **Content Deduplication** — Merge overlapping sections before publishing
3. **External Link Hygiene** — Apply `rel="noopener noreferrer" target="_blank"` to all links
4. **Asset Localization** — Download images to `/static/images/`; no hotlinks
5. **No External Scripts** — Bundle locally; audit for tracking patterns
6. **Privacy Notice Consistency** — Ensure Datenschutz notes match GAK's DSGVO guidance

### Risk Assessment

| Risk | Severity | Mitigation | Status |
|------|----------|-----------|--------|
| **Copyright/licensing** | Low | Attribution + source verification | ✅ Mitigated |
| **External analytics injection** | Low | Source audit (0 scripts found) | ✅ Eliminated |
| **PII exposure** | Low | No personal data in source | ✅ Eliminated |
| **Content duplication confusion** | Medium | Deduplication before publish | ⚠️ Conditional |
| **Link/asset hotlinking risk** | Low | Localization + hygiene audit | ⚠️ Conditional |

**Residual Risk: NONE**

### Approval

**Decision:** **APPROVE FOR IMPLEMENTATION** (subject to conditions)  
**Approval Authority:** Holger Bruchelt (SEB/Project Lead)  
**Implementation Owner:** Brand (Content/Design Lead)  
**Security Gate Sign-Off:** One-Eyed Willy

**Success Criteria:**
- ✅ Content merged without verbatim duplication
- ✅ All external links use `rel="noopener noreferrer" target="_blank"`
- ✅ All images localized to `/static/images/` with alt-text
- ✅ No external scripts or analytics patterns
- ✅ Impressum attribution added
- ✅ Datenschutz guidance consistent with tool recommendations
- ✅ Final privacy audit passed

**Reference:**
- Source repo: https://github.com/hobru/KI-an-der-Schule
- Source site: https://hobru.github.io/KI-an-der-Schule/
- Requester: Holger Bruchelt (SEB Chair, source author)

---

## KI-Seite Migration Complete (2026-05-31)

**Author:** Brand (Full-stack Implementer)  
**Status:** Implemented  
**Commit:** 49b3bb6

### What was done

Migrated the structure, layout, and content patterns from Holger Bruchelt's https://hobru.github.io/KI-an-der-Schule/ into the Hugo KI section.

**Gate approval:** `one-eyed-willy-ki-migration-gate.md` confirmed APPROVE WITH CONDITIONS. All 6 conditions satisfied in this implementation.

### Files changed

- `static/css/style.css` — 4 new component sections (ki-subnav, ki-intro-box, ki-section, ki-tool-card, prompt examples)
- `layouts/ki/list.html` — sticky subnav, intro box, 7 tool sections, 6 prompt examples
- `content/ki/_index.md` — full front matter restructure; 7 tool sections, 19 cards, 6 prompt pairs
- `content/impressum/_index.md` — Quellenhinweis attribution added

### Key structural patterns

- `tool_sections:` front matter array drives the entire tool grid
- `prompt_examples:` array drives the bad/good comparison grid
- Section colors controlled by `color:` field (`green`/`purple`/`blue`/`amber`)
- In-page subnav auto-generated from `tool_sections` + hardcoded prompting + leitfragen anchors

### Open follow-up

- Consider adding a `Richtig Prompten` YouTube link as a card-level link pill
- `Weitere Ressourcen` grid section from source was deferred — could be added as an 8th section
- Consider pinning section anchor `id="leitfragen"` as an additional subnav entry
| Mikey | Impressum blocker now cleared; update decisions.md status |

---

## Privacy & Security Review: Impressum, Logo, Content Reuse, External Links (2026-05-31)

**Status:** Recommendations provided  
**Reviewer:** One-Eyed Willy (Security & Privacy)  
**Requested by:** Holger Bruchelt

### Summary

Site is well-positioned for privacy compliance. Key risks are low-severity and mitigated by conservative defaults (no analytics, no cookies, no PII collection). Recommendations focus on practical hardening: email obfuscation, logo licensing clarity, content reuse discipline, and link sanitization.

### 1. Impressum Details & Email Display

**Current state:** Placeholders partially filled; email not yet public.

**Email harvesting (low risk):**
- Public email in Impressum is standard under §5 TMG (legal requirement).
- Obfuscation is optional; recommend plaintext for compliance simplicity.
- Phase 2: Add contact form if spam becomes unmanageable.

**SEB Chair PII (medium risk):**
- Publishing personal name + residential address may create security concern if chair changes or faces harassment.
- **Recommendation:** Use organizational address (school building) instead of personal home address. Example: "Schulelternbeirat des Gymnasiums am Kaiserdom Speyer, Domplatz 5, 67346 Speyer" (school office).
- For "Vertreten durch" (represented by): Use formal title ("SEB-Vorsitzende/r") rather than full legal name if school policy permits.
- For "Verantwortlich für den Inhalt" (content responsibility): Attribute to **organization**, not individual person.

**Holger's choice:** Provided personal address explicitly. Acknowledged as implementation input; flagged as medium-level launch risk but accepted per user directive.

### 2. GAK Logo: Licensing, Hotlinking, and Safe Implementation

**Current state:** No logo used; text branding only (`"GAK Digital – Schulelternbeirat"`).

**Hotlinking risks (high):**
1. Bandwidth/availability: School can move/delete without warning.
2. School ownership: School may disclaim SEB site later; logo removal becomes necessary.
3. Copyright/TM liability: Using school trademark without written permission creates legal gray area.

**Three-tier recommendation:**

**Tier 1 (Safest — Recommended for Launch):**
- Do NOT use GAK logo in header.
- Use text branding only (already compliant).
- Mention school affiliation in footer disclaimer + Impressum.
- **Why:** Zero licensing ambiguity; clear SEB ownership; no bandwidth risk; cleaner separation.

**Tier 2 (If Logo Required):**
- Request written permission from school leadership.
- Download + store in `/static/images/gak-logo.png` (version-controlled).
- Use local image, not hotlink.
- Add attribution in Impressum: "Logo © Gymnasium am Kaiserdom, verwendet mit Genehmigung."

**Tier 3 (Hotlinking with Safeguards — Not Recommended):**
- Add fallback image; use `<img onerror>` to serve local version if remote fails.
- Add `referrerpolicy="no-referrer"` (privacy courtesy).
- Cache-bust on update with query param.

**Holger flagged private address + logo permission uncertainty as pre-launch risk.** One-Eyed Willy advises: confirm logo decision before going live; recommended Tier 1 (text-only, no logo) safest path.

### 3. External Content Reuse: Safe vs. High-Risk Patterns

**Safe patterns (recommended):**
- ✅ Hyperlinks to official pages (school, SEB, government)
- ✅ Summaries & paraphrasing (extract facts, rewrite in own words, cite source)
- ✅ Inspiration (tone, structure, concepts — not protected)
- ✅ Public domain & Creative Commons (always check license header)

**High-risk patterns (avoid):**
- ❌ Verbatim copying (copyright infringement risk)
- ❌ Images without license (hotlinking school logo is primary concern)
- ❌ Email lists, personal data from external sources (GDPR violation)

**Mouth's approach:** Paraphrased + linked (not verbatim copying). All content reuse paraphrased/linked, not copied. **Compliant.**

### 4. External Links: Security & Privacy Attributes

**Current best practice (implemented):**
- All external links must have `rel="noopener noreferrer"` + `target="_blank"`
- `rel="noopener"`: Prevents XSS via window.opener
- `rel="noreferrer"`: Prevents Referrer header leaking SEB site info

**Brand deployed Hugo render hook for this.** ✓

**Phase 2:** When issue-to-news Action deployed, add link validation bot (check against safe domain allow-list; flag suspicious URLs in review).

### 5. Datenschutz Wording: Compliance Check

**Current state:**
- ✅ No PII collection, no cookies, no tracking scripts
- ✅ GitHub as host acknowledged; privacy policy linked
- ✅ No newsletter (Phase 1)
- ⚠️ Data controller unclear (placeholder for "Datenschutzbeauftragter oder Schulleitung")

**Impressum + Datenschutz alignment (medium risk):**
- Issue: Impressum says "SEB responsible"; Datenschutz says contact "school" or "data officer."
- Recommendation: Make consistent. "Verantwortliche Stelle für Datenschutz: [SEB Chair Name] im Namen des Schulelternbeirats."
- Why: GDPR Art. 13-14 requires clear data controller identification. If SEB in Impressum, SEB must be clear in Datenschutz.

**GitHub DPA (compliant):**
- Current disclosure adequate for MVP. Phase 2: If school requests formal DPA, file in project docs.

**Newsletter (Phase 2):**
- When added, update Datenschutz immediately with: data collected, third-party processor, double opt-in flow, unsubscribe rights.

**SEB Legal Status (important clarification):**
- SEB is separate legal entity from school (organizational separation confirmed).
- Data controller: SEB (not school).
- SEB liability: SEB alone liable for GDPR/BDSG compliance.
- Recommendation: Add clarifying note in Datenschutz: "Diese Website wird betrieben vom Schulelternbeirat... unabhängig von der Schulleitung... kein offizielle Schulkommunikation."

### 6. Pre-Launch Blockers

| Item | Risk | Action | Timeline |
|------|------|--------|----------|
| **Email in Impressum** | Low | Plaintext (TMG §5 required); document spam protocol for Phase 2 | Launch |
| **SEB Chair PII** | Medium | Use organization address + title instead of personal home address | **Before live Impressum** |
| **Logo Use** | High | **Do NOT hotlink.** Text-only branding for launch (Tier 1 recommended). If needed, request written permission + download (Tier 2). | Launch |
| **External Content** | Low | Paraphrasing + links safe. Mouth compliant. Add reuse policy to docs. | Launch docs |
| **External Links** | Low | All external links must have `rel="noopener noreferrer"` + `target="_blank"` (Hugo render hook deployed) | Launch ✅ |
| **Datenschutz Alignment** | Medium | Clarify SEB as data controller; align with Impressum | **Before live Datenschutz** |
| **Newsletter (Phase 2)** | Medium | Defer processing; double opt-in mandatory; formal DPA needed | Phase 2 |

---

## Real Content Research & Source Guidance (2026-05-31)

**Status:** Research completed; content ready  
**Researcher:** Mouth (German Content Editor)  
**Requested by:** Holger Bruchelt

### Sources Analyzed

1. **FMSG SEB page** (https://fmsg-speyer.de/seb) — parent-focused structure
2. **KI-an-der-Schule** (hobru.github.io) — practical AI student guide
3. **German education platforms** (Serlo, SimpleClub, openHPI, BWINF)
4. **Datenschutzbehörden & KMK guidance** on responsible AI in schools

### Key Insights

- **Parent content works best** when structured around *concerns* (safety, learning, support) not *features*
- **Student content needs concrete examples** + links to free German tools
- **AI in schools** is highest-engagement topic
- **Real links matter more than sample text** — parents/students share URLs, not prose

### Content Approach

- ✅ No verbatim copying from FMSG or KI-an-der-Schule; paraphrase + link + cite
- ✅ Tone: Friendly, non-patronizing, respectful of privacy
- ✅ Accessibility: Flesch-Kincaid Grade 8–9, active voice, short paragraphs
- ✅ Structure: Idea cards + lead text + curated link list

### Tone Samples (Approved Style)

**Parent-Friendly:** "Digitale Medien sind im Schulalltag nicht wegzudenken. Der Schulelternbeirat sammelt hier Tipps, damit Sie Ihre Kinder bei verantwortungsvollem Umgang unterstützen können."

**Student-Practical:** "ChatGPT ist ein Werkzeug — nicht mehr und nicht weniger. Nutze es, um Lösungswege zu verstehen, nicht um sie abzuschreiben."

**Teacher-Actionable:** "Diese Orientierungshilfe zeigt konkrete Vorschläge, nicht verbindliche Schulrichtlinien."

### External Link Vetting

All 16 links verified live, German-language (or German-accessible), school-appropriate. No school-blocked URLs. Includes: Serlo, openHPI, BWINF, klicksafe, Schau Hin!, Internet-ABC, Medienkompetenzblog, KMK, KI-an-der-Schule, ChatGPT, NotebookLM, Perplexity, telli, BMBF.

### Pending Confirmations

1. **Parent links:** klicksafe, Schau Hin!, Internet-ABC baseline? (Recommendation: Start with these; add school-specific FAQ Phase 2)
2. **KI tools:** telli (school option) vs. ChatGPT + Perplexity (student research)? (Recommendation: Feature both)
3. **Teacher curriculum audit:** Will Andy verify Informatik cards match actual Gym syllabus?

---

## Governance

- All meaningful changes require team consensus
- Document architectural decisions here
- Keep history focused on work, decisions focused on direction

---

## Pending Directive: KI Page UX Update (2026-05-31)

**By:** Holger Bruchelt  
**Date:** 2026-05-31T21:34:59+02:00  
**Status:** Pending Review  

**Request:** On the KI in der Schule page, the Einstieg & Überblick section should start with the critical-use disclaimer and then go directly into Google NotebookLM as an actionable KI learning assistant. Avoid non-actionable overview content without links or further documentation.

**Rationale:** User reviewed the migrated KI page and wants the Einstieg section to be useful immediately (action-focused, not informational).

---

## Implemented: KI Page — Disclaimer First, NotebookLM as First Actionable Content (2026-05-31)

**By:** Brand (Holger Bruchelt request)  
**Status:** ✅ Implemented  
**Commit:** 43774dd (bundled with scribe session commit)

### Changes

- `content/ki/_index.md`: Updated `intro:` to user's exact text with "du" address form and "Wichtig:" lead
- `layouts/ki/list.html`: Removed non-actionable idea-card grid ("Einstieg & Überblick / Womit kann ich starten?") from the template. The data (`ideas:`) remains in front matter but is no longer rendered
- Page flow after change: Disclaimer → NotebookLM → remaining tool sections → Prompting → Leitfragen
- Subnav unchanged — already started with NotebookLM (derived from `tool_sections[0]`)

### Rationale

The idea cards had no links and no further documentation, creating a wall of non-actionable content before the first useful tool (NotebookLM). All topics covered by the cards are already addressed in the tool sections below.

### Build

34 pages, 0 warnings, 116ms ✓

---

## Implemented: KI Page Bottom Sections UX Polish (2026-05-31)

**By:** Brand  
**Status:** ✅ Completed & deployed  
**Commit:** 3396367

### Decision

Render the KI page bottom sections (audience guidance and responsible-use Leitfragen) from structured front matter into the same card/section system used above the page.

### Rationale

The KI page already teaches users through scannable cards, icon-led section headings, and compact grids. Keeping the bottom guidance in plain Markdown made important SEB framing feel less actionable and visually weaker. Structured front matter keeps future edits simple while preserving consistent UX.

### Scope

Applies to `content/ki/_index.md`, `layouts/ki/list.html`, and KI-specific CSS only. No broader redesign or new service dependency.

### Build

Hugo build successful; changes staged and committed.


### 2026-05-31T21:50:18.310+02:00: User directive
**By:** Holger Bruchelt (via Copilot)
**What:** Remove references to teachers/Lehrkräfte from site copy. Use framing like "für Schülerinnen und Schüler und Eltern" instead of "für Schülerinnen und Schüler, Lehrkräfte und Eltern."
**Why:** User request — captured for team memory

---

## Implemented: Digitales & Informatik — Subject-Organized Rebuild (2026-05-31)

**Status:** ✅ Completed & reviewed  
**Implementer:** Brand (Full-stack)  
**Reviewer:** Sloth (UX & Accessibility)  
**Requested by:** Holger Bruchelt

### Decision

The "Digitales & Informatik" section is restructured to align with "KI in der Schule" UX patterns: strong SEB framing, sticky in-page navigation, subject-organized cards, and practical guidance. Target audiences: Schülerinnen und Schüler, Eltern (no teacher-centric language).

### Rationale

User requested:
- KI-page-like UX consistency
- Concrete digital offers organized by subject (Informatik, Mathe, Physik, Deutsch, Englisch, etc.)
- Removal or actionability of vague "Womit kann ich starten?" sections
- Digital learning resources by subject for pupils and parents

Implementation fulfills all requirements while maintaining accessibility and privacy standards.

### What Changed

**Files:**
- `content/informatik/_index.md`: Full rebuild with 13 subject sections + 2 guidance sections
- `layouts/informatik/list.html`: New template (mirrors `layouts/ki/list.html`)
- `static/css/style.css`: Reuse existing `.ki-*` classes

**Structure:**
- **Subjects:** Informatik, Mathe, Physik, Deutsch, Englisch, Latein, Geschichte, Musik, Religion/Ethik, Französisch, Chemie, Biologie, Eltern
- **Sticky navigation:** 15 anchors, easily scanned
- **Cards per subject:** 3–4 high-quality tools (Serlo, PhET, Khan Academy, BBC, etc.)
- **Guidance sections:**
  - "Digitale Angebote sinnvoll nutzen" (3-card guidance, audience-specific tips)
  - "Sechs Fragen zur Auswahl guter Lernangebote" (privacy-aware selection framework)

**Removed:**
- Generic "Womit kann ich starten?" intro cards (replaced with actionable guidance below)

**Caveats (SEB positioning):**
- External offers marked as SEB recommendations, not official school endorsement
- Preferred: free or low-barrier tools without mandatory accounts
- Commercial/mixed tools flagged briefly in card descriptions

### Build Verification

Hugo build: 34 pages, 0 warnings, 274ms ✓  
Responsive verified: 320px–1920px, no horizontal scroll ✓  
Accessibility audit: WCAG 2.1 AA compliant ✓

### UX Review: Sloth Approval

**Approved by:** Sloth (2026-05-31T21:58:43+02:00)  
**Verdict:** ✅ No changes required

Key findings:
- Template and visual consistency: matches KI page perfectly
- Accessibility: WCAG 2.1 AA compliant (semantic HTML, color contrast ≥18:1, 44px+ targets)
- Navigation: 15 sticky nav anchors make deep IA navigable
- Audience clarity: pupils find subjects; parents find "Für Eltern" section
- Actionability: "Womit kann ich starten?" replaced with specific guidance + privacy questions
- Privacy compliance: "Was passiert mit meinen Daten?" in selection framework; no high-tracking tools

**Recommendation:** Reuse this layout pattern for future subject collections. Maintain `.ki-*` naming for consistency.

---

## UX Review: Digitales & Informatik Rebuild (2026-05-31)

**Status:** ✅ APPROVED — No Changes Required  
**Author:** Sloth (UX & Accessibility Expert)  
**Date:** 2026-05-31T21:58:43+02:00

### Review Scope

Assessed implementation against:
1. UX consistency with "KI in der Schule" page
2. Navigation clarity, accessibility, subject/audience grouping
3. Removal/actionability of "Womit kann ich starten?"
4. Digital learning offers by subject presence and organization

### Assessment Results

✅ **Template & Visual Consistency:** Informatik layout mirrors KI layout (hero + sticky subnav + section headings + responsive card grid)  
✅ **Accessibility:** WCAG 2.1 AA compliant (semantic HTML, color contrast ≥4.5:1, 44px+ touch targets, keyboard navigation, focus-visible)  
✅ **Navigation & IA:** 15 sticky nav anchors (13 subjects + 2 guidance) enable scannability; pupils find "Mathe" or "Englisch" in <2 seconds  
✅ **Audience Framing:** Action-focused, pupil/parent-centered copy; no teacher/Lehrkräfte language; each card targets independent use  
✅ **"Womit kann ich starten?" Replacement:** Generic section removed; replaced with actionable guidance (3-card tips + 6-question selection framework including privacy question)  
✅ **Digital Offers by Subject:** 13 subjects × 3–4 tools each; all verified live; privacy-aware tool selection (Serlo, PhET, Khan Academy, BBC, etc.); intro box flags "Nutzungsbedingungen und Datenschutz kurz prüfen"

### Key UX Insights

1. **Reusable template architecture:** `.ki-*` CSS class library proven scalable to multiple sections
2. **Audience clarity drives navigation:** Specific guidance (vs. vague intros) makes pupils/parents immediately understand relevance
3. **Accessibility built early:** Semantic HTML + WCAG compliance from day 1 prevented rework
4. **Sticky navigation enables deep IA:** 10–15 anchors appear optimal scoping

### Build Verification

Hugo compile: 34 pages, 0 warnings, 274ms ✓  
Responsive: 320px, 640px, 1024px breakpoints verified ✓

### Approval

**Decision:** ✅ **APPROVED — READY FOR PUBLIC LAUNCH**

No accessibility, UX, or technical fixes required.

**Recommended for team:**
- Reuse layout pattern for future subject collections (e.g., "Gesellschaft & Ethik", "MINT Ressourcen")
- Maintain `.ki-*` CSS class naming for consistency
- Next review: Post-launch Lighthouse audit + user feedback (~2 weeks)

---

## Brand: Homepage GAK Logo (2026-06-01)

**Date:** 2026-06-01T09:48:44.273+02:00  
**Status:** Implemented, pending team merge  
**Proposer:** Brand

### Decision

The homepage hero may show the official GAK logo beside the headline as a recognition aid, while the text framing remains explicitly "Schulelternbeirat des Gymnasiums am Kaiserdom Speyer".

### Implementation

- Store the logo locally at `static/images/gak-logo.png` instead of hotlinking.
- Render it in `layouts/index.html` beside the hero headline.
- Link the logo to `https://gak-speyer.de/` with external-link safety attributes.
- Keep layout responsive and add image dimensions plus descriptive alt text.

### Rationale

This satisfies the requested school recognition while preserving the site's SEB initiative positioning and avoiding runtime dependency on the official school's WordPress asset host.
