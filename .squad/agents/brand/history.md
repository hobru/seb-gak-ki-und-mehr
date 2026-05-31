# Brand History

## Seed Context

- **User:** Holger Bruchelt
- **Project:** German-first website for pupils, teachers, and parents of Gymnasium am Kaiserdom Speyer.
- **Focus:** Computer science and AI tutorials, guidance, ideas, and a latest-news area that can be updated easily, ideally via GitHub issues.
- **Technology:** Not yet selected, but must run on GitHub.
- **Key concerns:** Stakeholder fit, maintainability, usability, security, newsletter privacy, and PII.

## Learnings

### 2026-05-31 — Hugo Real-Project Feasibility Assessment

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

