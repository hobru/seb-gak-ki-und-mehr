# Sloth History

## Seed Context

- **User:** Holger Bruchelt
- **Project:** German-first website for pupils, teachers, and parents of Gymnasium am Kaiserdom Speyer.
- **Focus:** Computer science and AI tutorials, guidance, ideas, and a latest-news area that can be updated easily, ideally via GitHub issues.
- **Technology:** Not yet selected, but must run on GitHub.
- **Key concerns:** Stakeholder fit, maintainability, usability, security, newsletter privacy, and PII.

## Learnings

### Session 2026-05-31: Technology & UX Evaluation
- **Tech recommendation:** Jekyll + GitHub Pages is optimal for maintainability by non-technical contributors; avoids SPA complexity that harms accessibility
- **Issue-driven news requires bot + templates:** GitHub Issues can power a news feed, but success depends on strict validation (template enforcement, metadata checking, preview before publish)
- **Static sites have accessibility wins:** No JavaScript = more predictable keyboard navigation & screen reader support; deterministic rendering
- **IA should be category-first, not role-first:** Avoid separate landing pages for pupils/teachers/parents; use metadata (grade_level, audience tags) to let users self-filter
- **German language neutral:** No special tech barriers; Markdown + UTF-8 handles German perfectly; focus on localized UX (date formats, menu labels)
- **Accessibility must be enforced early:** WCAG 2.1 AA is baseline; require alt text templates, link-text guidelines, and monthly audits
- **Editorial governance is prerequisite:** Non-technical contributors need training on Markdown, front-matter, and accessibility checklist; a lightweight editorial board prevents chaos
- **Newsletter signup outside GitHub:** Use Netlify Forms or Formspree; keeps PII off GitHub and GDPR-compliant

### Key Assumptions Made
- Holger is comfortable with light technical setup (Jekyll, GitHub Actions)
- Contributors willing to learn Markdown basics
- Site starts with <100 pages; scaling decision comes later
- English translation is phase 2+ (German-only initially)

### Session 2026-05-31: Hugo vs Jekyll Re-evaluation (UX/Editorial Feasibility)

**Question raised:** Is Hugo really the best, or should we go with Jekyll?

**Analysis Framework:** Non-technical editors, German content, issue-to-news workflow, accessibility, maintenance friction.

#### Hugo Strengths (Editorial + UX)
1. **Issue parsing robustness:** Hugo's flexibility with custom front-matter makes it easier to enforce structured metadata (category, audience, grade_level). The Go templating is deterministic and forgiving.
2. **Single binary, no runtime:** Removes Ruby version conflicts—critical for a school deploying via GitHub Actions. Reduces contributor environment setup friction.
3. **Taxonomy + tagging native:** Hugo's built-in support for custom taxonomies (tags, categories, custom dimensions) simplifies category-first IA without hacks.
4. **Build speed visibility:** 50ms builds are negligible, but psychologically reassure contributors that "the publish just happened."
5. **Internationalization ready:** Hugo's i18n is cleaner than Jekyll for eventual bilingual pages (German + English side-by-side in Phase 3).

#### Jekyll Strengths (Editorial + UX)
1. **GitHub Pages native:** Eliminates one infrastructure dependency; Jekyll can deploy directly from `_config.yml` without custom Actions. Lower mental model for Holger.
2. **Markdown editing in GitHub Web UI:** School contributors can edit/preview Markdown directly in GitHub—no git clone, no local tooling. Jekyll is GitHub's own tool; UI/UX alignment is explicit.
3. **Familiar for educators:** Many German teachers have used Jekyll (via GitHub-hosted portfolios). Ecosystem feels less "programmer-y."
4. **Liquid templating (simpler):** Jekyll's Liquid is closer to Jinja; less steep than Go's html/template for non-technical contributors reading templates later.
5. **Collections paradigm:** Jekyll's `_posts` and custom collections map cleanly to "news," "tutorials," "guides"—no re-learning Hugo's content hierarchy.

#### Friction Audit: Contributor Experience

| Friction Point | Hugo | Jekyll | Winner |
|---|---|---|---|
| **Environment setup** | `brew install hugo` or binary | `gem install jekyll` → Ruby version conflicts | **Hugo** (single binary) |
| **Editing in GitHub Web UI** | Markdown ✓ but live preview weaker | Markdown ✓ + native preview | **Jekyll** |
| **Issue-to-markdown workflow** | Flexible (custom action) | Flexible (custom action) | **Tie** (both need bot) |
| **Taxonomy/filtering (category-first IA)** | Native taxonomies, clean | Collections + front-matter (workaround-y) | **Hugo** |
| **German date formatting** | Hugo i18n: date formatting via locale | Jekyll: plugins or manual `strftime` | **Hugo** |
| **Accessibility defaults** | Static HTML only ✓ | Static HTML only ✓ | **Tie** |
| **Monthly maintenance** | Go compiler updates (infrequent) | Ruby + gem updates (more churn) | **Hugo** |
| **Error messages (for newbies)** | Go errors can be terse | Ruby stack traces are verbose | **Tie** |

#### Accessibility & Performance: No Material Difference
- Both generate pure HTML; no runtime JavaScript.
- Both support semantic HTML5, alt text conventions, ARIA.
- Lighthouse scores will be nearly identical (both ≥90).
- German localization (dates, labels) requires custom templates in both; no advantage either way.

#### The Real UX Lever: Editorial Workflow, Not Generator
**Key insight:** The choice between Hugo/Jekyll matters less than *how* we structure the issue-to-news pipeline.
- Both require: strict GitHub issue template, validation bot, moderation gate, markdown file generation.
- Neither is inherently "easier" for a school editor—success depends on workflow training and automation quality.

#### Honest Assessment: When to Choose Each

**Choose Hugo if:**
- Build reliability and single-binary deployment are priorities for GitHub Actions.
- Taxonomy/category-first navigation is central to the design.
- Holger is willing to spend 2 hours learning `config.toml` basics.
- Future multilingual support (German↔English) is expected sooner rather than Phase 3+.

**Choose Jekyll if:**
- Holger or contributors already have Ruby experience (GitHub portfolios, etc.).
- Editing directly in GitHub Web UI (without `git clone`) is a hard requirement for non-technical staff.
- Preference for "GitHub's own tool" as a cultural signal to the school community.
- Simpler fallback: Jekyll runs locally, error messages are more familiar to web developers.

#### Recommendation: **Hugo, but not by conviction—by pragmatism.**
**Reasoning:**
1. Single binary removes environment friction for school CI/CD.
2. Native taxonomies align with category-first IA (best practice for school users).
3. Issue metadata parsing is more robust in Hugo's templating.
4. Ruby gem churn is real maintenance burden; Go is slower-moving.

**Caveat:** If the team or Holger have strong Jekyll experience, switching is not worth the friction. The issue-to-news workflow and editorial governance matter more than the generator brand.

#### Reversibility Note
If the team decides Jekyll later, migration is straightforward:
- Hugo `content/` → Jekyll `_posts/` (slight restructuring).
- Templating/theming must be rewritten (4–6 hours, not a blocker).
- No data loss; pure restructuring.

### 2026-05-31 — Cross-Agent Convergence (Technology Review Session)

**Data's Input (Technology Architecture):**
- Hugo recommended as primary choice for zero npm dependencies, fastest builds, built-in i18n, trivial GitHub Actions deploy
- Comparison matrix evaluated 6 platforms; Hugo wins on build speed (50ms), single binary, ecosystem scale
- Risk mitigation: structured YAML issue forms for reliable parsing
- Fallbacks: Eleventy (JS preference), Astro (interactive components), Jekyll (simplest but Ruby dependency)

**One-Eyed Willy's Input (Security & Privacy):**
- Identifies 3 BLOCKERS before implementation: (1) issue template design (no PII), (2) moderation gate, (3) legal pages
- Mandates 8 security guardrails; prefers Hugo's single binary over Jekyll's 30+ gem dependencies
- Moderation gate = BLOCKER; no auto-publish from issues alone

**Mikey's Input (Product Coordination):**
- Frames decision: SSG (recommended) vs. Next.js (future) vs. Headless CMS (deferred)
- Stakeholder lens: 7 key stakeholders mapped to risks and requirements
- MVP scope: homepage + news + CS + AI + accessibility + privacy baseline (2 weeks)
- Success metrics: <5 min publish time, Lighthouse ≥90 accessibility, ≥85 mobile
- Phased roadmap: Phase 1 MVP → Phase 2 (CMS UI, newsletter) → Phase 3+ (i18n, analytics)

**Team Convergence:**
- All agents agree SSG is correct platform choice
- Hugo vs. Jekyll: both viable, team to vote by EOW
- Issue-to-news workflow feasible WITH security gates + editorial governance
- Critical path: issue template design, moderation gate, legal content, build trigger decision by EOW

### 2026-05-31 — Hugo vs Jekyll: Editorial & UX Recheck

**Context:** Team needed second pass on Hugo vs Jekyll trade-offs. Holger questioned whether Jekyll's GitHub-native advantage justified its selection.

**Recheck Outcome:** **Hugo remains stronger choice, but decision is pragmatic, not by large margin.** Editorial workflow automation matters more than generator brand.

**Key Recheck Findings:**

**Hugo Wins On:**
1. **Single binary deployment:** Eliminates Ruby version conflicts in GitHub Actions; reduces contributor environment friction.
2. **Native taxonomies:** Built-in support for custom dimensions (category, audience, grade_level) aligns perfectly with category-first IA.
3. **Issue metadata parsing:** Go templating is more robust for enforcing structured issue-to-markdown workflows.
4. **Maintenance simplicity:** Go releases are infrequent; Ruby gem churn is ongoing friction for school IT.
5. **Future bilingual support:** Hugo's i18n is cleaner for German ↔ English side-by-side content (Phase 3+).

**Jekyll Wins On:**
1. **GitHub-native Web UI editing:** School staff can edit/preview Markdown in browser without `git clone`—significant UX advantage for non-technical editors.
2. **Familiarity for educators:** Many German teachers have GitHub portfolios; Jekyll feels less "programmer-y."
3. **Simpler fallback:** Local Jekyll setup is more forgiving; error messages familiar to web developers.
4. **Liquid templating:** Easier for non-technical contributors to read/understand templates later.

**Critical Clarification Needed:**
The decisive question for team: Is GitHub Web UI editing (Jekyll advantage) a hard requirement for non-technical editors? If Holger or contributors will use `git clone` + local editor, this advantage disappears entirely.

**Reversibility:** Migration from Hugo to Jekyll is straightforward—4–6 hours of restructuring; no data loss.

**Conclusion:** Decision hinges on editorial workflow design (automation quality, contributor training) more than generator choice itself. Proceed with Hugo confidence, knowing Jekyll is viable fallback if team circumstances change.

