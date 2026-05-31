# One-Eyed Willy History

## Seed Context

- **User:** Holger Bruchelt
- **Project:** German-first website for pupils, teachers, and parents of Gymnasium am Kaiserdom Speyer.
- **Focus:** Computer science and AI tutorials, guidance, ideas, and a latest-news area that can be updated easily, ideally via GitHub issues.
- **Technology:** Not yet selected, but must run on GitHub.
- **Key concerns:** Stakeholder fit, maintainability, usability, security, newsletter privacy, and PII.

## Learnings

### 2026-05-31 — Initial Privacy & Security Review (Issue-Driven Static Site)

**Public Issue Templates — PII Exposure Risk:**
- GitHub issues are publicly visible. A news-submission template (title, abstract, link, category) is low-risk IF it avoids free-text "author name" or "contact email" fields.
- Guardrail: Template must NOT request personal data. Add a visible notice: "Do not include personal information in this issue."

**Moderation Gap:**
- Anyone with GitHub access can open an issue. Without moderation, spam, offensive content, or accidental PII could appear in the public record and be picked up by the build pipeline.
- Guardrail: Require manual label (e.g., `approved`) before any GitHub Action publishes content. Never auto-publish from issue creation alone.

**Newsletter / PII Forward-Looking:**
- If a newsletter is added later, email addresses are PII under GDPR/BDSG. Double opt-in is mandatory in Germany. No email storage in the repository or public issues.
- Guardrail: Use a privacy-respecting third-party (e.g., Buttondown, Sendinblue) with data-processing agreement (Auftragsverarbeitungsvertrag). Never store subscriber lists in Git.

**Analytics:**
- Standard Google Analytics is problematic for German school sites (GDPR, consent, data transfer to US).
- Guardrail: Use privacy-safe analytics (Plausible, Goatcounter, or none). No tracking pixels, no cookies requiring consent banners.

**GitHub Actions Permissions:**
- Existing workflows use `contents: read` and `issues: write` — minimal and appropriate.
- A `COPILOT_ASSIGN_TOKEN` secret exists; ensure it is scoped to issues/PRs only, not full repo admin.
- Guardrail: All workflows must use least-privilege `permissions:` blocks. Never grant `contents: write` to issue-triggered workflows to prevent injection attacks.

**External Links in News Items:**
- Links submitted via issues could point to malicious sites. Readers are school-age children.
- Guardrail: Add `rel="noopener noreferrer"` to all external links in templates. Consider a link-allow-list or domain validation in the build step.

**Dependency / Supply Chain:**
- Static site generators pull npm/gem packages. Lock files and Dependabot should be enabled from day one.
- Guardrail: Enable GitHub Dependabot alerts + security updates. Pin action versions to full SHA, not tags.

**Privacy-Safe Defaults:**
- No cookies, no login, no user tracking, no comment system with PII.
- Impressum and Datenschutzerklärung pages are legally required for German school web presence.
- Guardrail: Ship Impressum + Datenschutz as static pages from launch. Content must name the responsible person (Schulleitung) per TMG/TTDSG.

### 2026-05-31 — Cross-Agent Convergence (Technology Review Session)

**Data's Input (Technology Architecture):**
- Hugo recommended for zero npm dependencies, 50ms builds, built-in i18n, trivial GitHub Actions integration
- Full comparison matrix: Hugo wins on dependency weight and build speed; Jekyll fallback acceptable but adds Ruby maintenance burden
- Structured YAML issue forms = critical for reliable parsing; freetext parsing is fragile

**Sloth's Input (UX & Accessibility):**
- Static HTML approach = deterministic accessibility (no JavaScript surprises)
- Issue-driven workflow feasible IF strict validation bot + editorial checklist + moderation gate (non-negotiable)
- WCAG 2.1 AA baseline required; German law requirement for public school
- Editorial governance prerequisite; templates must enforce alt-text and link-text standards

**Mikey's Input (Product Coordination):**
- Platform choice: SSG (recommended) over Next.js (complexity) or Headless CMS (vendor lock-in)
- Stakeholder risk map: privacy/security risks are HIGH severity; One-Eyed Willy is mitigation owner
- MVP includes: legal pages (Impressum + Datenschutzerklärung) at launch as BLOCKER
- Newsletter deferred to Phase 2 for GDPR compliance review
- No analytics in MVP; privacy baseline = default

**Team Convergence:**
- All agents converged on Static Site Generator approach
- Security blockers identified and prioritized: (1) template design, (2) moderation gate, (3) legal content
- Moderation gate is non-negotiable blocker per One-Eyed Willy
- Privacy guardrails = binding constraints for implementation team

