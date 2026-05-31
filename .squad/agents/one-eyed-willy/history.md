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

### 2026-05-31 — Impressum, Logo, & External Content Risk Review

**Holger's Request:** Practical security & privacy recommendations for Impressum/Datenschutz updates: SEB contact details, email obfuscation, GAK logo use (hotlink vs. download vs. permission), external content reuse guidelines, external link security, and Datenschutz wording implications.

**Key Findings:**

**1. Email & SEB Chair PII (Low-Medium Risk)**
- Impressum email must be plaintext per TMG §5 (German legal requirement); obfuscation is optional courtesy, not mitigation.
- **Blocker:** SEB chair personal home address creates legal/privacy concern. Recommendation: use organizational address (school office) + title instead of personal residence.
- Safe to display as plaintext; spam protocol deferred to Phase 2 if needed.

**2. GAK Logo Use (High Risk — Decision Required)**
- **Tier 1 (Recommended):** Text-only branding for launch. Zero licensing ambiguity; no availability risk; clear SEB separation from school.
- **Tier 2 (If Required):** Request written permission from Schulleitung → download image to `/static/images/` (version-controlled) → serve locally with attribution in Impressum.
- **Tier 3 (Avoid):** Hotlinking risks availability, bandwidth, and licensing liability. Not recommended.
- **Decision required from Holger/SEB before launch.**

**3. External Content Reuse (Low Risk)**
- ✅ **Safe:** Hyperlinks, paraphrasing with attribution, inspiration (concepts/tone).
- ❌ **Unsafe:** Verbatim copying, hotlinked images without license, scraped contact lists (PII).
- Recommend adding reuse policy to project docs (Phase 1 or 2).

**4. External Links (Low Risk — Compliant)**
- Current template already uses `rel="noopener noreferrer" target="_blank"` on GitHub privacy link (good practice).
- **Action:** Enforce template-level on all external links; add privacy note in Datenschutz explaining Referrer minimization.
- Issue-to-News validation bot (Phase 2): allow-list external domains to prevent phishing/malware submissions.

**5. Datenschutz Alignment (Medium Risk)**
- ✅ Correctly states no PII, no cookies, no tracking, no newsletter (Phase 1).
- **Blocker:** Datenschutz contact person must match Impressum. If SEB is data controller in Impressum, SEB must be clear in Datenschutz (GDPR Art. 13-14).
- **Action:** Clarify SEB chair as responsible person; add note on school independence (organizational separation already documented).
- Newsletter Phase 2: Update with double opt-in, processor DPA, unsubscribe/erasure rights.

**6. Pre-Launch Blockers**
- Confirm SEB chair name, contact, organizational address (not personal residence).
- **Logo decision: Tier 1 (text-only, recommended) or Tier 2 (permission + download)?** Holger + SEB board decision.
- Ensure Impressum + Datenschutz alignment on data controller identity.
- Validate issue form has "no PII" warning + email/phone pattern blocking (already compliant ✓).

**Green Light for Launch:** Once Impressum/Datenschutz details confirmed and logo decision made. No security blockers; all risks are best-practice mitigations.

### 2026-05-31 — Content Migration Gate: KI-an-der-Schule Source (Brand/Holger Request)

**Context:** Holger Bruchelt requested content migration from hobru.github.io/KI-an-der-Schule/ (external source repository) to this GAK project. Request includes replicating layout, functionality, and content structure.

**Assessment Scope:**
1. **Source ownership & licensing**: Is the requester authorized? Are there licensing obligations?
2. **Privacy & security of source**: Does source contain external scripts, analytics, tracking, or dependencies?
3. **Content overlap & redundancy**: Does GAK already have similar content?
4. **Safe replication path**: Can Brand migrate without introducing security/privacy debt?

**Key Findings:**

**1. Source Ownership — LOW RISK ✅**
- Requester is Holger Bruchelt (hobru), confirmed as original author of hobru/KI-an-der-Schule repo.
- No third-party copyright encumbrances detected.
- **Recommendation:** Treat as internal content reuse by source creator. Attribution to Holger/hobru in Impressum is courteous but not legally mandatory if SEB is owner of derivative work.

**2. Source Privacy/Security — LOW RISK ✅**
- Repository: Pure HTML, no npm/gem/external package managers.
- **Scripts analyzed:** Zero external tracking scripts, zero analytics (Google Analytics/Matomo/etc.), zero cookies, zero localStorage patterns, zero pixel tracking.
- No third-party dependencies, iframes, or embedded external tools.
- Source is privacy-native: safe to copy content without inheriting tracking/privacy debt.

**3. Content Overlap — MEDIUM RISK (Design Consideration)**
- GAK content/ki/_index.md already covers: AI tool recommendations (ChatGPT, NotebookLM, Perplexity, telli), datenschutz concerns, responsible use guidance.
- Source (hobru) adds: Detailed prompting guides, tool comparisons (Claude, Gemini, Copilot, DeepL, Canva, DALL-E), hallucination warnings, data privacy best practices, learning strategies per tool.
- **Overlap areas:** Approx. 40% (tools, datenschutz, responsible use). Unique content in source: ~60% (detailed prompts, learning strategies, tool comparisons).
- **Recommendation:** Content migration is defensible if GAK explicitly cites source in Impressum and avoids verbatim duplication of overlapping sections. Consider merge/deduplication before publishing.

**4. Safe Replication Path — APPROVE WITH CONDITIONS**
- ✅ **Content text:** Safe to copy; static markdown/HTML, no PII, no injection vectors.
- ✅ **Layout/CSS:** Safe to adapt; no external stylesheets detected, only local CSS.
- ⚠️ **Links:** Existing external links use `rel="noopener noreferrer"` (good). GAK must apply same standard to all migrated links.
- ⚠️ **Images/Assets:** If source uses external image URLs (hotlinks), do NOT copy URLs; download to `/static/images/`, version control locally, and cite source in captions/Impressum.

**Gate Verdict: APPROVE WITH CONDITIONS**

**Conditions for Brand/Holger:**
1. **Attribution:** Add a note in Impressum referencing hobru.github.io/KI-an-der-Schule as source inspiration for this section (courtesy + transparency).
2. **Content deduplication:** Review overlap between new content and existing GAK ki/_index.md. Merge/consolidate before publishing to avoid reader confusion.
3. **External link hygiene:** Audit all migrated links; apply `rel="noopener noreferrer" target="_blank"` universally.
4. **Asset localization:** No hotlinked images from source. Download any images to `/static/images/` with local references only.
5. **No external scripts:** If layout uses any JavaScript interactivity, verify source and bundle locally; do NOT hotlink external JS.
6. **Privacy notices:** If source links to external tools (DeepL, Canva, etc.), review Datenschutz notes; ensure consistency with GAK DSGVO guidance.

**Implementation Path:**
- Brand to copy content as markdown blocks or static HTML into new `/content/ki/` sections or subsections.
- Propose deduplication plan to Holger/SEB (e.g., "Move prompting guide to new /ki/prompting-guide/" or "Merge tool recommendations into expanded ki/_index.md").
- Pass through One-Eyed Willy final review before publishing to confirm link hygiene and privacy notices.

**Risk Residue:** None identified. Source is clean; conditions are operational best-practices, not security blockers.

**Approval Authority:** Holger (SEB/Project Lead). Conditions are non-negotiable guardrails to maintain privacy baseline and legal compliance.

