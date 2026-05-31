# Brand History

## Project Summary

**User:** Holger Bruchelt  
**Project:** German-first website for Gymnasium am Kaiserdom Speyer covering computer science and AI education for pupils, teachers, and parents.  
**Technology:** Hugo + GitHub Pages + GitHub Actions  
**Status:** MVP launched 2026-05-31 with real content integrated and KI page migration complete.

## 2026-05-31 Session Summary

**What was accomplished:**

1. **Hugo Site v1 Implemented** — Complete site with 34 pages, responsive CSS (~550 lines, WCAG AA), GitHub Pages deploy, custom layouts (no external themes).

2. **Real Content Integration** — Informatik and KI sections replaced sample content with researched material from Mouth (6 cards each) + curated links and audience-specific guidance.

3. **KI Page Migration** — Full integration of hobru.github.io/KI-an-der-Schule content patterns: 7 tool sections (19 cards), sticky subnav, bad/good prompt comparison grid, attribution in Impressum. All One-Eyed Willy security conditions satisfied.

4. **Structural Updates** — News-first homepage (Sloth UX), SEB positioning (Mouth guidance), menu reordering, real Impressum/Datenschutz (Holger contact details).

**Key Decisions Embedded:**
- Hugo render hook (`_markup/render-link.html`) for automatic `rel="noopener noreferrer"` on all external links — solves security requirement without `unsafe = true`
- Badge system: label→CSS class mapping via template dict; extensible for new badges
- Card structure: icon → h3 → audience badge → description → badges (Sloth alignment)
- Front matter patterns: `tool_sections`, `prompt_examples`, `ideas` arrays for content-editor-friendly editing

**Patterns Learned:**
- Put structured data (idea cards, tool cards) in YAML front matter, not template HTML — reduces editing friction for non-technical contributors
- Sticky offset `3.75rem` correct for hero height
- Goldmark render hooks > unsafe mode for security attributes
- YAML single-quoted strings for German text with `"` and typographic quotes
- Template links need manual `target="_blank" rel="noopener noreferrer"` — render hooks don't apply to template-generated `<a>` tags
- Centralise reusable strings (`seb_disclaimer`) in `hugo.toml` to avoid duplication across footer, legal pages, notices

**Build Metrics:**
- 34 pages, 180–307ms build time, zero warnings
- GitHub Actions deploy workflow SHA-pinned
- 100% privacy-safe (no PII, no analytics, no cookies)

**Pre-Launch Blockers:**
- SEB legal contact details (Holger to provide chair name, address, email)
- baseURL to actual domain
- One-Eyed Willy Actions permissions audit
- Real news content replacing samples

**Deferred to Phase 2:**
- Issue-to-News GitHub Action workflow
- Newsletter (GDPR review needed)
- Analytics / CMS UI / i18n

