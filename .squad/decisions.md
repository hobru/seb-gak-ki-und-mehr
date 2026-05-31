# Squad Decisions

## Active Decisions

### Technology Platform: GAK Website (2026-05-31)

**Proposers:** Data (Tech Architect), Sloth (UX), One-Eyed Willy (Security), Mikey (Product Coordinator)  
**Status:** Proposed (awaiting team consensus)  
**Decision Frame:** [Mikey] See decision timeline at end of this section.

#### Rechecks Completed (2026-05-31)
- **Data** (Tech Architect): Hugo remains correct choice. Jekyll's only real advantage—native GitHub Pages build—is irrelevant because issue-to-news workflow already requires GitHub Actions. Hugo wins on dependencies, build speed, Windows install, security surface, i18n, and template robustness for structured issue-parsing.
- **Sloth** (UX/Accessibility): Hugo remains stronger choice, but not by large margin. Decision hinges on editorial workflow automation (not generator choice). Jekyll viable if team/contributors have Ruby experience. Hugo preferred for single-binary deployment, native taxonomies, and maintenance simplicity. Key trade-off: Jekyll's GitHub Web UI editing advantage requires confirming if non-technical editors will actually edit directly in Web UI.

#### Competing Recommendations

**Option A: Hugo** (Data's recommendation)
- Zero-runtime dependencies; single Go binary; fastest builds (~50ms)
- Built-in i18n; issue-to-news pipeline simple
- GitHub Actions `peaceiris/actions-hugo` deploys in seconds
- Issue template captures: title, abstract, link, audience, category
- GitHub Action workflow: issue labeled `news` → markdown file generated → auto-publish
- **Risk:** Issue parsing fragile without structured YAML templates

**Option B: Jekyll** (Sloth's recommendation, favoring GitHub-native simplicity)
- GitHub Pages native support; Ruby ecosystem stable
- Same issue-to-news workflow with bot validation
- Accessibility baseline higher due to deterministic static HTML
- Markdown editing native to GitHub Web UI (low barrier for non-coders)
- **Risk:** Ruby ecosystem maintenance burden vs. Hugo's single binary
- **Note:** Sloth also approves Hugo as fallback ("if team prefers JavaScript" — though Hugo is Go-based)

**Product Frame:** (Mikey) Both options meet MVP requirements; defer final choice to EOW team vote.
- Static site generator (SSG) approach = best fit for GitHub-native + school audience + low friction
- Alternatives rejected: Next.js (complexity overkill), Headless CMS (vendor lock-in, defer to Phase 2)

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

1. **Static site generator:** Jekyll or Hugo?
2. **Content structure:** How do issues map to markdown files?
3. **Build trigger:** Every commit? Every labeled issue?
4. **Baseline privacy:** No analytics/cookies in MVP?
5. **Language:** German content-first; English deferred?

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
