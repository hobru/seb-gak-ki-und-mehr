# Mikey History

## Seed Context

- **User:** Holger Bruchelt
- **Project:** German-first website for pupils, teachers, and parents of Gymnasium am Kaiserdom Speyer.
- **Focus:** Computer science and AI tutorials, guidance, ideas, and a latest-news area that can be updated easily, ideally via GitHub issues.
- **Technology:** Not yet selected, but must run on GitHub.
- **Key concerns:** Stakeholder fit, maintainability, usability, security, newsletter privacy, and PII.

## Learnings

### Session 2026-05-31: Technology Platform Decision Frame

**Key Insight:** The tension between "low-friction publishing" and "school-appropriate quality control" drives the entire tech decision. Static site generators (Jekyll/Astro) solve this by keeping content as version-controlled markdown while using GitHub Actions to automate the issue→markdown→build→publish pipeline.

**Decision Criteria Validated:**
- Must run on GitHub (Pages + Actions) — eliminates most options
- GitHub-native publishing is non-negotiable (Holger's core requirement)
- German content quality = revision history, comments, review capability (not CMS)
- School safety = accessible, performant, offline-printable, no tracking

**MVP Platform Recommendation:** Static Site Generator (Jekyll preferred for GitHub Pages compatibility, or Astro for modern tooling)
- Reason: Markdown files = version control. GitHub Actions = low-friction news workflow. GitHub Pages = zero infrastructure.
- Risk mitigated: CMS deferral (Phase 2) prevents scope creep; non-technical editor concern addressed via markdown + GitHub Web UI initially.

**Stakeholder-Specific Risks Identified:**
- Holger: Publishing workflow friction → mitigate with issue template automation
- Mouth: Content quality control via GitHub → enable with branch protection, review approvals
- Chunk/Andy: Mobile UX and accessibility → Sloth audit + school device testing (MVP gate)
- Stef: Newsletter privacy → defer to Phase 2 (time for GDPR review)
- One-Eyed Willy: GitHub Actions security + external integrations → explicit vetting phase

**MVP Scope (2-week target):**
1. Homepage + news (auto-updated from issues)
2. Two static content areas (CS + AI) as markdown
3. Mobile-responsive, accessible design
4. Privacy baseline (no tracking, no cookies)
5. Issue template for submissions

**Defer to Phase 2+:** Newsletter, CMS UI, search, multi-language.

**Decision Timeline:**
- NOW: Confirm SSG choice (Jekyll vs. Astro), route to Data/Sloth/One-Eyed Willy for vetting
- EOW: Team consensus
- Week 2: Prototype + German content templates
- Week 3+: MVP launch, gather feedback

**Reusable Pattern:** "GitHub-first + static content + low-friction workflow" = ask: (1) Can we run on GitHub Pages? (2) Can content live as version-controlled files? (3) Can we automate publish triggers with Actions? If yes to all three, SSG wins.

### 2026-05-31 — Cross-Agent Convergence (Technology Review Session)

**Data's Input (Technology Architecture):**
- Hugo recommended for performance (50ms builds), zero npm dependencies, built-in i18n
- Full platform comparison: evaluated 6 options; static SSG best fits GitHub-native + school audience requirements
- Issue-to-news reliability depends on structured YAML forms (not freetext parsing)
- Fallbacks validated: Eleventy, Astro, Jekyll all acceptable with caveats

**Sloth's Input (UX & Accessibility):**
- Static HTML = deterministic accessibility (screen reader friendly, no JS surprises)
- Jekyll preferred for GitHub-native simplicity; Hugo acceptable and arguably better for dependencies/i18n
- Issue-to-news workflow feasible WITH moderation gate + editorial governance + strict templates
- WCAG 2.1 AA baseline non-negotiable; German legal requirement
- Category-first IA (not role-first); editorial board structure prerequisites

**One-Eyed Willy's Input (Security & Privacy):**
- 3 BLOCKERS identified: issue template (no PII), moderation gate, legal pages (Impressum + Datenschutzerklärung)
- 8 security guardrails = binding constraints for implementation
- Hugo's single binary preferred for security surface vs. Jekyll's 30+ gem dependencies
- Moderation gate = hard blocker; no auto-publish
- Newsletter deferred to Phase 2 (GDPR compliance review)

**Team Convergence:**
- Static Site Generator platform type validated by all agents
- Hugo vs. Jekyll choice: both meet requirements; team to vote by EOW
- Critical blockers: template design, moderation gate, legal content must be decided/ready before implementation
- Success metrics validated: <5 min publish, ≥90 Lighthouse accessibility, ≥85 mobile performance
- Phased roadmap: Phase 1 MVP (2 weeks) → Phase 2 (CMS UI, newsletter, 6 weeks) → Phase 3+ (i18n, analytics)

