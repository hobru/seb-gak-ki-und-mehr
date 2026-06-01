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

---

## 2026-05-31T21:58:43Z – Digitales-Fachressourcen Build Complete

**Status:** ✅ **Implemented & Reviewed (Sloth UX approval)**  
**Commit:** 983ccac  
**Reviewer:** Sloth (UX & Accessibility Expert)

**What was completed:**
- Implemented full rebuild of `content/informatik/_index.md` with 13 subject sections (Informatik, Mathe, Physik, Deutsch, Englisch, Latein, Geschichte, Musik, Religion/Ethik, Französisch, Chemie, Biologie, + "Für Eltern")
- Mirrored KI page template: sticky subnav (15 anchors), section-card layout, responsive grid (1→2→3 col), guidance sections
- Replaced generic "Womit kann ich starten?" with actionable guidance: "Digitale Angebote sinnvoll nutzen" (3-card audience tips) + "Sechs Fragen zur Auswahl guter Lernangebote" (privacy-aware selection framework)
- Each subject section: 3–4 verified external tools (Serlo, PhET, Khan Academy, BBC, etc.)
- Removed teacher/Lehrkräfte framing; audience: Schülerinnen/Schüler + Eltern only
- Hugo build: 34 pages, 0 warnings, 274ms
- Responsive tested: 320px–1920px ✓

**Approval (Sloth):**
- ✅ WCAG 2.1 AA compliant (semantic HTML, color contrast ≥18:1, 44px+ targets, keyboard nav)
- ✅ Accessibility guardrails met; sticky nav mobile-friendly; no accessibility rework needed
- ✅ UX consistent with KI page design language and layout patterns
- ✅ Information architecture: 15-item sticky nav makes deep IA navigable
- ✅ Actionable content: guidance sections replace vague intros; privacy questions included
- ✅ Audience clarity: pupils find subjects, parents find "Für Eltern"
- ✅ Ready for public launch

**Key learning:** Reusable template architecture (`.ki-*` CSS classes) proves robust for subject-organized content beyond KI focus. Sticky nav with 10–15 anchors is right scoping for deep IA. Audience clarity + actionable guidance drive user confidence.

**Decision documentation:** Merged from `decisions/inbox/brand-digitales-subject-resources.md` and `.../sloth-digitales-ux-review.md` into `.squad/decisions.md`.

## 2026-06-01 – Stadtbibliothek-Hinweis vor Digitales-Fächerkarten

- Ergänzte auf `Digitales & Informatik` einen SEB-gerahmten Hinweis auf die Stadtbibliothek Speyer als kostenfreien Zugang zu Medien und, wo verfügbar, digitalen Lerntools wie Sofatutor und plan6.
- Pattern learned: Kommunale Zugänge zu sonst kostenpflichtigen Lernangeboten gehören als prominenter Hinweis vor Fachkarten, damit Schülerinnen und Schüler sowie Eltern zuerst niedrigschwellige öffentliche Angebote prüfen.

## 2026-06-01 – Digitales-Reihenfolge und Linkcheck

- Die Seite `Digitales & Informatik` beginnt nun passend zum humanistischen GAK-Profil mit Sprachen (Deutsch, Englisch, Französisch, Latein), danach Gesellschaft/Kultur, MINT und erst anschließend Informatik/Digitales.
- Stadtbibliothek-Hinweis präzisiert: Sofatutor oder plan6 können je nach Verfügbarkeit und Nutzungsbedingungen über digitale Angebote **kostenfrei** erreichbar sein.
- Pattern learned: Nach Nutzerhinweisen auf defekte Bildungslinks alle externen URLs per GET prüfen und auch sichtbare Fehlertexte scannen; bei 404/403/App-Fehlern lieber stabile Alternativen mit gleichem Schüler-/Elternnutzen einsetzen.

## Learnings

### 2026-06-01T09:48:44.273+02:00 – Homepage-GAK-Logo im SEB-Frame

- Homepage-Hero liegt in `layouts/index.html`; zugehörige responsive Styles liegen in `static/css/style.css`.
- GAK-Logo wurde lokal unter `static/images/gak-logo.png` abgelegt, mit festen `width`/`height`-Attributen gegen Layout Shift und Alt-Text für Barrierefreiheit.
- Pattern learned: Offizielle Schulmarken auf SEB-Initiativseiten als unterstützende Wiedererkennung einsetzen, nicht als Ownership-Signal; SEB-Label im Hero sichtbar lassen und Logo-Link extern mit `target="_blank" rel="noopener noreferrer"` absichern.

### 2026-06-01T10:29:46.920+02:00 – GAK-Logo aus Nutzerdatei übernommen

- Holgers temporäre Datei `gak-seb-logo.jpg` wurde aus dem Repository-Root nach `static/images/gak-seb-logo.jpg` verschoben; die Root-Kopie wurde entfernt.
- `layouts/index.html` referenziert nun die bereitgestellte JPG-Datei im Hero neben „Digitales Lernen – von Eltern für Schule und Familie“ mit intrinsischen Maßen `291x97` und bestehendem aussagekräftigem Alt-Text.
- Pattern learned: Wenn Holger ein temporäres Branding-Asset im Root ablegt, die Datei unverändert in `static/images/` übernehmen, Template-Referenzen auf diesen lokalen Pfad aktualisieren und die temporäre Root-Datei entfernen.

## 2026-06-01T10:29:46Z – SPAWN: Logo Asset Task (Scribe Orchestration)

**Spawn Source:** Scribe orchestration (Spawn Manifest)  
**Task Status:** Ready for execution  

**Objective:** Move `gak-seb-logo.jpg` into proper static asset folder and place it next to homepage hero title "Digitales Lernen – von Eltern für Schule und Familie".

**Expected Outcome:**
- Logo moved to `static/images/gak-seb-logo.jpg`
- Root copy removed
- Homepage updated with alt text and dimensions
- `hugo --minify` successful

**Note:** Scribe has recorded this task in the orchestration log and team memory (decisions.md) for asynchronous handoff.
