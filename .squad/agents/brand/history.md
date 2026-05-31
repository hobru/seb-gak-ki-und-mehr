# Brand History

## Seed Context

- **User:** Holger Bruchelt
- **Project:** German-first website for pupils, teachers, and parents of Gymnasium am Kaiserdom Speyer.
- **Focus:** Computer science and AI tutorials, guidance, ideas, and a latest-news area that can be updated easily, ideally via GitHub issues.
- **Technology:** Not yet selected, but must run on GitHub.
- **Key concerns:** Stakeholder fit, maintainability, usability, security, newsletter privacy, and PII.

## Learnings

### 2026-05-31 — Hugo Site v1 Implemented and Built

**Trigger:** Holger Bruchelt requested the first version of the GAK Digital homepage.

**What was built:**
- `hugo.toml` with German locale, nav menu (Start / Digitales & Informatik / KI / Neuigkeiten)
- `content/`: Homepage, Informatik section, KI section, News section (3 sample posts), Impressum placeholder, Datenschutz placeholder
- `layouts/`: Custom baseof, homepage (index.html), single, list, section-specific layouts (informatik, ki, news), partials (header, footer, news-card)
- `static/css/style.css`: ~550 lines, responsive mobile-first, CSS custom properties, WCAG AA colour contrast, skip link, visible focus rings, card hover states
- `.github/workflows/deploy.yml`: GitHub Pages via peaceiris/actions-hugo (SHA-pinned)
- `README.md`: Build, run, deploy, and contribution instructions

**Design decisions:**
- No external theme dependency — full custom layouts and CSS. Every contributor can read and change it.
- Badge/category system: `badge--ki`, `badge--informatik`, etc., mapped from front matter `categories` array via template dict.
- Idea cards for Informatik and KI sections stored in front matter (`ideas:` list) so content editors update YAML, not HTML.
- Sample content notice banner controlled by `site.Params.sampleSite` bool in `hugo.toml`.
- Date format: DD.MM.YYYY (German standard, no month names to avoid i18n complexity).

**Build result:** `hugo v0.134.3`, 32 pages, 68ms, zero warnings.

**One-Eyed Willy requirements honoured:**
- No PII collected; no analytics; no cookies
- Impressum + Datenschutz pages present (as legal placeholders)
- External links need `rel="noopener noreferrer"` — template adds this where needed
- GitHub Actions SHA-pinned

**Deferred (as agreed):**
- Issue → News GitHub Action workflow (structure ready: `content/news/` YAML front matter matches future pipeline)
- Real Impressum/Datenschutz legal text (placeholder until school provides)
- Newsletter / PII features

**Key learning:** Putting structured data (idea cards) in front matter instead of template HTML keeps the barrier to editing low for non-technical school contributors. The `dict` lookup in templates for CSS class mapping avoids a partial proliferation.



**Trigger:** Holger Bruchelt asked whether we should skip the Jekyll MVP and start directly with Hugo, given Hugo is the long-term recommendation.

**Key insight that changes the picture:** The team's Jekyll Phase 1 decision rested on Jekyll's "GitHub-native build = no custom Actions" advantage. But Holger is explicitly asking for a GitHub Action-based issue-to-news pipeline. That means custom Actions are accepted from day one — which is exactly the threshold Data (Tech Architect) stated would justify switching to Hugo. The Jekyll advantage evaporates; Hugo's advantages (single binary, no Ruby/gem maintenance, zero Phase 2 migration cost) become decisive.

**Hugo feasibility verdict: YES — straightforward enough to start now.**

**Setup complexity:** ~2–3 developer hours one-time. Ongoing operation is simpler than Jekyll for all contributors.

**Repository structure confirmed workable:**
```
/
├── .github/
│   ├── ISSUE_TEMPLATE/news.yml     # GitHub Issue Form (no PII, German)
│   └── workflows/
│       ├── deploy.yml              # Hugo build → GitHub Pages
│       └── issue-to-news.yml       # Issue labeled 'freigegeben' → PR → merge → deploy
├── hugo.toml
├── content/
│   ├── _index.md                   # Homepage
│   ├── informatik/_index.md        # CS static page
│   ├── ki/_index.md                # AI static page
│   └── news/                       # Auto-generated entries (one .md per issue)
├── layouts/                        # Custom templates (or starter theme)
└── static/css/                     # Stylesheet
```

**Issue Form fields (all privacy-safe, no PII):**
- Datenschutz-Hinweis as first element (mandatory)
- Titel (input, required, max 80 chars)
- Zusammenfassung (textarea, required, max 200 chars)
- Weiterführender Link (input, optional, URL)
- Kategorie (dropdown: KI, Informatik, Wettbewerbe, Werkzeuge, Allgemeines)
- Zielgruppe (dropdown: Schüler:innen, Lehrkräfte, Eltern, Alle)

**Action flow (two workflows):**
1. `issue-to-news.yml` — triggers on label `freigegeben`; parses Issue Form body; generates `content/news/YYYY-MM-DD-slug.md` with proper front matter; opens PR (optional: auto-merges with branch protection requiring 1 reviewer for extra moderation gate)
2. `deploy.yml` — triggers on push to main; uses `peaceiris/actions-hugo` (SHA-pinned); builds Hugo; deploys via `actions/deploy-pages`

**Moderation gate:** Issue labeled `news-einreichung` on creation (auto). Moderator reviews → adds `freigegeben` → pipeline creates PR → merge (auto or with required review) → deploy. No content reaches the live site without explicit moderator action.

**Validation guardrails in Action:**
- Required fields enforced by GitHub Issue Form (no empty submissions)
- Title length check (warn > 80 chars)
- URL format validation for link field
- Anti-PII regex scan on summary (email/phone patterns → fail with comment)
- Category/audience from dropdowns → no typos
- On failure: Action comments on issue explaining the error, removes `freigegeben` label

**All One-Eyed Willy security requirements satisfied:**
- No PII fields in Issue Form ✓
- German Datenschutz-Hinweis at top of form ✓
- Moderation gate before any publish ✓
- External links rendered with `rel="noopener noreferrer"` in templates ✓
- Actions pinned to SHA (not floating tags) ✓
- Impressum + Datenschutzerklärung as static pages in scope ✓

**Decision implication:** A decision inbox entry was written recommending the team reconsider Jekyll Phase 1 in light of Holger's explicit acceptance of custom Actions and preference to avoid a Phase 2 migration.


### 2026-05-31 — Structural Update: Menu Order, News Position, Impressum, SEB Link

**Trigger:** Holger Bruchelt requested four specific improvements.

**Changes implemented (6 files):**

1. **`hugo.toml`** — Reordered menu weights: Neuigkeiten → weight 2 (was 4); Digitales & Informatik → weight 3 (was 2); KI in der Schule → weight 4 (was 3). Start (1) and Mitmachen (5) unchanged.

2. **`layouts/index.html`** — Moved Neuigkeiten/Aktuelles section immediately after hero, before audience cards and pillars. Section order is now: Hero → News → Audience Cards → Pillar Cards → Contribute CTA → Footer. Aligns with Sloth's UX recommendation in `.squad/decisions/inbox/sloth-news-first-ux.md`.

3. **`content/impressum/_index.md`** — Replaced all placeholders with real details: name Holger Bruchelt, address Carl-Dupre-Str. 5, 67346 Speyer. Email displayed as obfuscated text `seb-at-gak-speyer.de` (no mailto link). Added link to official GAK SEB page. Removed placeholder warning banner.

4. **`layouts/partials/footer.html`** — Added "Offiz. SEB-Seite" link to `https://gak-speyer.de/menschen-am-gak/schulelternbeirat` with `target="_blank" rel="noopener noreferrer"` in footer links list.

5. **`content/datenschutz/_index.md`** — Aligned with Impressum: replaced address placeholder and GDPR contact placeholder with Holger Bruchelt details; removed placeholder banner. Required by One-Eyed Willy pre-launch blocker.

**Build result:** `hugo --minify` → 34 pages, 207ms, zero warnings ✓

**Decisions followed:**
- Sloth UX inbox: news-first navigation and homepage ordering ✓
- One-Eyed Willy inbox: email as obfuscated text, `rel="noopener noreferrer"` on external link ✓
- Logo NOT added — awaiting One-Eyed Willy rights/privacy review ✓

**Committed:** Yes — safe structural update with no content or external dependencies pending.

**Pattern learned:** When One-Eyed Willy flags Impressum + Datenschutz as coupled pre-launch blockers, filling one requires updating the other in the same commit to maintain consistency (data controller name/address must match across both pages).



### 2026-05-31 — Real Content Integration: Informatik & KI Sections

**Trigger:** Holger Bruchelt requested replacement of sample content with Mouth's researched real content, plus CSS/layout polish per Sloth's UX guidance.

**Changes implemented (7 files, commit 7055847):**

1. **`content/informatik/_index.md`** — Replaced 6 generic sample cards with 6 specific real cards (first website in HTML, data analysis Python/Excel, media literacy, teacher tools, video/podcast production, parent explainer). Added parent FAQ (3 Q&As), enriched Grundbegriffe, added SEB attribution paragraph, 8 curated external links in three audience categories. Front matter `description` and `lead` updated to SEB-framed copy.

2. **`content/ki/_index.md`** — Replaced 6 sample cards with 6 researched cards (Prompt-Challenge, KI-Antworten prüfen, KI-Begriffe, Eltern-Leitfragen, Datenschutz, Leitfragen-Framework). Added "Was alle wissen sollten" audience-split section, 10 curated links in three audience categories, Six Leitfragen reflection framework. Fixed typo from DRAFT (`bezeichnetProgramme` → `bezeichnet Programme`). Corrected `lead` typo (`nutzten` → `nutzen`).

3. **`layouts/informatik/list.html`** + **`layouts/ki/list.html`** (identical update):
   - Removed `sample-notice` banner (real content; no longer applicable)
   - Updated section eyebrow from "Beispielideen & Impulse" → "Ideen & Impulse"
   - Restructured idea-card HTML: icon → **h3 title** → audience badge (`<p class="idea-card__audience">`) → desc → badge-row (badges + duration). Aligns with Sloth's semantic card guidance.
   - Extended badge `dict` with 12 new label→class mappings (Anfänger, Datenanalyse, Medienkompetenz, Denken, DSGVO, Kreativität, Unterstützung, Praktisch, Grundlagen, Verantwortung, Reflexion, Kritisches Denken)

4. **`layouts/_default/_markup/render-link.html`** — New Hugo link render hook. All external links in Markdown (`http://` / `https://`) automatically get `target="_blank" rel="noopener noreferrer"`. Resolves One-Eyed Willy's requirement without requiring per-link raw HTML or unsafe Goldmark mode.

5. **`static/css/style.css`** — Added `.idea-card__audience` (0.75rem, uppercase, primary color, letter-spacing); updated `.idea-card__badge-row` to `margin-top: auto; padding-top: 0.5rem` (pushes badges to card bottom). Added 13 new `.badge--*` classes with distinct but restrained color pairs.

6. **`hugo.toml`** — Set `sampleSite = false` (real content now active; removes homepage sample-content notice banner).

**Build result:** `hugo --minify` → 34 pages, 0 warnings ✓

**Decisions followed:**
- Mouth's `DRAFT_informatik_index.md` and `DRAFT_ki_index.md` integrated as-is (minor fixes applied)
- Logo NOT added (One-Eyed Willy review pending) ✓
- SEB attribution in both page footers via link to `https://gak-speyer.de/menschen-am-gak/schulelternbeirat` ✓
- No verbatim text from KI-an-der-Schule or FMSG; inspired design only ✓
- External links: render-hook adds `rel="noopener noreferrer"` automatically ✓

**Caveats:**
- The `Kritisches Denken` badge contains a space, which maps to CSS class `badge--kritisches-denken`. This works in Hugo's `index $classMap` lookup but only if the key exactly matches (including the space). Since the DRAFT uses `"Kritisches Denken"` as a badge label, the dict key must also be `"Kritisches Denken"` — confirmed in template.
- Goldmark `unsafe = false` remains in `hugo.toml`. Raw HTML in markdown is still blocked. The render-hook approach is the correct Hugo-native solution.

**Pattern learned:** Hugo's `_markup/render-link.html` render hook is the cleanest way to globally enforce security attributes on external links without touching CSS, content, or disabling Goldmark safety. One file solves the entire problem for all Markdown content. Prefer this over per-link HTML or global `unsafe = true`., not an official school page — analogous to https://seb-shgym-diez.de/.

**Guidance source:** `.squad/decisions/inbox/mouth-seb-positioning.md` (Mouth's content reframing guidance, Option A chosen throughout for maximum legal clarity).

**Files changed (9):**
- `hugo.toml`: `title` → "GAK Digital – Schulelternbeirat"; `school` → full SEB name; `shortName` → "SEB GAK Digital"; `description` leads with "Eine Initiative des Schulelternbeirats"; added `seb_disclaimer` param for reuse
- `layouts/partials/header.html`: logo sub-line → "Schulelternbeirat des Gymnasiums am Kaiserdom"
- `layouts/index.html`: hero label → full SEB name; hero title → "Digitales Lernen – von Eltern für Schule und Familie"; sample-notice explicitly names SEB; teacher card wording sourced from SEB perspective
- `layouts/partials/footer.html`: copyright → SEB name only; new `seb_disclaimer` paragraph rendered below copyright
- `static/css/style.css`: `.site-footer__disclaimer` style added (italic, muted white)
- `content/_index.md`: page description updated to SEB initiative framing
- `content/impressum/_index.md`: responsible party → SEB; placeholder guidance points to SEB contacts not school admin
- `content/datenschutz/_index.md`: responsible party → SEB; placeholder guidance updated
- `README.md`: title and subtitle reflect SEB ownership

**Build result:** `hugo --minify` → 34 pages, 180ms, zero warnings ✓

**Pattern learned:** Centralise the disclaimer string in `hugo.toml` as `seb_disclaimer` so footer, legal pages, and any future template can render it without duplication. Easy to update in one place when real legal text is provided.

**Pre-launch blocker added:** Impressum and Datenschutz must now list SEB contact details (not school admin). Holger to supply SEB address, chair name, and email before public launch.



**Trigger:** Team decision finalized on 2026-05-31; implementation completed same day.

**Deliverables:**
- ✅ Hugo site initialized and built successfully
- ✅ Homepage, Informatik, KI, News, Impressum, Datenschutz pages
- ✅ Custom responsive layouts + CSS (~550 lines, WCAG AA, mobile-first)
- ✅ GitHub Pages deploy workflow (peaceiris/actions-hugo, SHA-pinned)
- ✅ 3 sample German news posts (marked as `sample: false` ready for replacement)
- ✅ 6 idea cards per section (Informatik, KI) stored in front matter for easy editing

**Build metrics:** 32 pages, 68ms, zero warnings ✓

**Integration with reviewer principles:**
- Content editors can add news posts and idea cards via simple YAML editing (no HTML required)
- Sample-content flag (`sample: true/false`) + banner notice prevent accidental publication
- Audience tagging + category system support filtering (ready for Phase 2 news-to-action)
- All One-Eyed Willy privacy/security guardrails in place (no PII, no analytics, no cookies)
- WCAG 2.1 AA compliance: color contrast, semantic HTML, alt text, focus-visible, 44px+ touch targets

**Pre-launch blockers logged in .squad/decisions.md:**
- Replace legal placeholders (Impressum, Datenschutz) with real text
- Set baseURL to actual domain
- One-Eyed Willy to review Actions permissions
- Content team to replace samples with real material before public launch

**Deferred to Phase 2:**
- Issue-to-News GitHub Action workflow (structure ready)
- Newsletter signup (GDPR review needed)
- Analytics evaluation
- CMS UI, multi-language, advanced search

