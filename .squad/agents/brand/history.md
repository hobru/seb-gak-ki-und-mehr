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

### 2026-05-31 — Hugo Homepage v1 Delivered & Deployed (Commit 85c0032)

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

