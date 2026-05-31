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

## Governance

- All meaningful changes require team consensus
- Document architectural decisions here
- Keep history focused on work, decisions focused on direction
