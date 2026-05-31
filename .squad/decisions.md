# Squad Decisions

## Active Decisions

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

## Governance

- All meaningful changes require team consensus
- Document architectural decisions here
- Keep history focused on work, decisions focused on direction
