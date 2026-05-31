# Squad Decisions

## Active Decisions

### Technology Platform: GAK Website (2026-05-31)

**Proposers:** Data (Tech Architect), Sloth (UX), One-Eyed Willy (Security), Mikey (Product Coordinator)  
**Status:** Decided (2026-05-31 team consensus: Jekyll for Phase 1)  
**Decision Frame:** [Mikey] See decision timeline at end of this section.

#### Rechecks Completed (2026-05-31)
- **Data** (Tech Architect) **[RETRACT HUGO, RECOMMEND JEKYLL]**: GitHub Pages native defaults matter for non-specialist maintenance. Jekyll's native build advantage (avoiding custom Actions) is real. Issue-to-news still works with Jekyll + Actions for intake. Local setup (Hugo advantage) is secondary to actual contributor model (GitHub Web UI, issues, PRs). For a small school website, GitHub-managed Jekyll is simpler security/maintenance story than Hugo with custom Actions. **Threshold to switch to Hugo:** custom Actions accepted day 1, multilingual required soon, content >200 pages, i18n bundling needed, or developer-heavy maintenance becomes norm.
- **Mikey** (Product Coordinator) **[REAFFIRM HUGO]**: Product risk analysis: Hugo wins on operational surface area (single binary vs. Ruby + 30 gems), Windows friction, failure debugging speed, bus factor. Jekyll's "GitHub-native" advantage is moot because moderation gate requires custom Actions in both cases. Editorial workflow is generator-neutral (both tie). **Issue-to-news pipeline reliability favors Hugo** (fewer MTTF points). Prototyping both = 1 week lost with no winner; validation approach = 2–3 days, ship Friday EOW.
- **Sloth** (UX/Accessibility) **[TIE-BREAK: JEKYLL FOR PHASE 1]**: Jekyll minimizes **contributor friction** for schools. Editorial entry barrier (GitHub Web UI + direct edits), moderation gate predictability (native Pages vs. Action debugging), maintenance handoff (any GitHub-fluent teacher vs. Go expertise), "just works" in Phase 1 (30s from commit vs. Action debugging). **Concedes:** Hugo is technically superior on single-binary, taxonomies, i18n. **Reality:** school culture = GitHub fluency, not optimization. Reversible in Phase 2 (Liquid → Go templates = 4–6 hrs, no data loss). **Success metric:** contributor retention ≥2 trained editors by week 3 (Jekyll = higher likelihood).

#### Competing Recommendations

**Option A: Hugo** (Mikey's recommendation)
- Zero-runtime dependencies; single Go binary; fastest builds (~50ms)
- Built-in i18n; issue-to-news pipeline simple
- GitHub Actions `peaceiris/actions-hugo` deploys in seconds
- Issue template captures: title, abstract, link, audience, category
- GitHub Action workflow: issue labeled `news` → markdown file generated → auto-publish
- **Risk:** Issue parsing fragile without structured YAML templates
- **Operational advantage:** Lower MTTF, better Windows debugging, resilient bus factor

**Option B: Jekyll** (Sloth's recommendation, chosen for Phase 1) ✓ **DECIDED**
- GitHub Pages native support; Ruby ecosystem stable
- Same issue-to-news workflow with bot validation
- Accessibility baseline higher due to deterministic static HTML
- Markdown editing native to GitHub Web UI (low barrier for non-coders)
- **Strength:** Minimizes contributor friction for schools; GitHub-native culture alignment; safe fallback (direct file editing) when automation breaks
- **Risk:** Ruby ecosystem maintenance burden vs. Hugo's single binary
- **Reversible:** Phase 2 migration to Hugo if taxonomy scaling or multilingual demands justify it (Liquid → Go templates = 4–6 hours)
- **Note:** Sloth also approves Hugo as fallback ("if team prefers" or Phase 2+ scaling demands)

**Decision Outcome (2026-05-31):**
- **Recommendation:** **Jekyll for Phase 1 MVP** (Data + Sloth consensus; Mikey documents Hugo rationale for Phase 2 migration path)
- **Rationale:** Non-specialist maintainers (teachers, staff) benefit from GitHub-native editing, visible workflows, predictable failures, and lower Phase 1 friction. Operational resilience trade-off (Ruby maintenance burden) is accepted for contributor retention and simpler Phase 1 stabilization.
- **Architecture:**
  - Hosting/build: GitHub Pages with native Jekyll
  - Content: Markdown + front matter in `_posts/` or `_news` collection
  - Editing: GitHub Web UI or PRs for content
  - Automation: GitHub issue form → validation Action → moderation label → auto-rebuild
  - Privacy: no PII fields, visible German privacy warning in issue template

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
- Platform: Static site generator (Jekyll or Hugo TBD)
- Hosting: GitHub Pages
- Publishing: GitHub Actions on issue creation
- Deliver: Homepage + news + CS + AI sections + accessibility baseline + privacy baseline
- **Out of scope:** Newsletter, advanced search, CMS UI

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

## Governance

- All meaningful changes require team consensus
- Document architectural decisions here
- Keep history focused on work, decisions focused on direction
