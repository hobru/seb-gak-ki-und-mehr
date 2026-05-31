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

---

## 2026-05-31 — KI Page: Disclaimer First, NotebookLM First

**Trigger:** Holger Bruchelt reviewed the migrated KI page and found the "Einstieg & Überblick / Womit kann ich starten?" idea-card grid non-actionable — no links, no further documentation, and it blocked NotebookLM (the first useful tool) behind a wall of unclickable cards.

**Changes (2 files, bundled into commit 43774dd):**

1. **`content/ki/_index.md`** — Updated `intro:` text to user's exact wording:
   "**Wichtig:** KI-Tools sind Werkzeuge, keine Ersatz-Lehrer. Sie können dir helfen, Inhalte besser zu verstehen, Lernzettel zu erstellen oder dich auf Klausuren vorzubereiten. Aber: Immer kritisch prüfen, was die KI dir liefert – sie kann sich auch irren!"
   The "du" address (vs. the previous impersonal "man") better fits the target student audience. The `ideas:` YAML data was retained for potential future use.

2. **`layouts/ki/list.html`** — Removed the entire idea-cards rendering block (49 lines). The `{{ with .Params.ideas }}` section including the "Einstieg & Überblick / Womit kann ich starten?" header, idea-card loop, and badge dict was deleted. The intro warning box now flows directly into the NotebookLM tool section.

**Result:** Page flow is now: Hero → Subnav (starting with NotebookLM) → Disclaimer → NotebookLM → remaining tool sections → Prompting → Leitfragen.

**Build result:** `hugo --minify` → 34 pages, 116ms, zero warnings ✓

**Pattern learned:** Non-actionable overview cards (no links, no CTAs) placed before actionable tools are a UX anti-pattern — they add friction without value. When all ideas are covered by downstream tool sections, remove the cards rather than duplicating. Front matter data can stay for future reuse without harming the rendered output.

**Caveat:** The scribe agent swept my staged file changes into its own session-summary commit (`43774dd`). Content is correct and in HEAD; future Brand commits should be atomic and committed before the scribe runs to avoid message mismatch.


## 2026-05-31 — KI Bottom UX Consistency

- Converted the KI page bottom guidance from freeform Markdown into structured front matter (`audience_guidance`, `responsible_questions`) rendered by the KI list template.
- Reused the existing KI section heading/card language so “Was alle wissen sollten” and “Sechs Leitfragen” visually align with the stronger tool/prompt UX above while preserving the SEB framing.
- Pattern learned: keep repeatable KI page blocks in front matter and render them as cards; avoid ending a highly structured page with unstyled Markdown lists.


## 2026-05-31 — Removed Teacher Audience Framing

- Removed public-facing teacher/Lehrkräfte audience framing across homepage, KI, Informatik, news metadata, contribution copy, issue template, README, and site description per Holger's directive.
- Pattern learned: when audience scope narrows, update both rendered copy and hidden front matter/workflow options so future content suggestions cannot reintroduce removed audience tags.

## 2026-05-31 – Digitales-Fachressourcen wie KI-Seite aufgebaut

- Die Seite `content/informatik/_index.md` nutzt nun die gleiche kartenbasierte Struktur wie `KI in der Schule`, aber für Schülerinnen und Schüler sowie Eltern statt Lehrkräfte.
- Der unklare Block „Womit kann ich starten?“ wurde entfernt und durch fachbezogene, direkt verlinkte Lernangebote ersetzt.
- Externe Lernressourcen werden SEB-gerahmt und mit Datenschutz-/Kontoprüfhinweisen eingeführt; bevorzugt frei zugängliche öffentliche, gemeinnützige oder etablierte Angebote.
