# Sloth History Archive

Archived entries from history.md before 2026-05-31T15:24:57.022Z (Jekyll decision finalized).

## Seed Context

- **User:** Holger Bruchelt
- **Project:** German-first website for pupils, teachers, and parents of Gymnasium am Kaiserdom Speyer.
- **Focus:** Computer science and AI tutorials, guidance, ideas, and a latest-news area that can be updated easily, ideally via GitHub issues.
- **Technology:** Not yet selected, but must run on GitHub.
- **Key concerns:** Stakeholder fit, maintainability, usability, security, newsletter privacy, and PII.

## Session 2026-05-31: Technology & UX Evaluation (Archived)

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

## Hugo vs Jekyll Evaluations (Archived)

### First Evaluation: UX/Editorial Feasibility Analysis

**Hugo Strengths:**
1. Issue parsing robustness (Go templating deterministic)
2. Single binary, no runtime
3. Taxonomy + tagging native
4. Build speed visibility
5. Internationalization ready

**Jekyll Strengths:**
1. GitHub Pages native
2. Markdown editing in GitHub Web UI
3. Familiar for educators
4. Liquid templating (simpler)
5. Collections paradigm

**Friction Audit (Hugo vs Jekyll):**
- Environment setup: **Hugo** (single binary) vs Jekyll (Ruby conflicts)
- Editing in GitHub Web UI: **Jekyll** (native preview) vs Hugo (weaker)
- Issue-to-markdown workflow: **Tie**
- Taxonomy/filtering: **Hugo** (native) vs Jekyll (workaround-y)
- German date formatting: **Hugo** (i18n) vs Jekyll (plugins)
- Accessibility defaults: **Tie**
- Monthly maintenance: **Hugo** (Go) vs Jekyll (gem churn)
- Error messages: **Tie**

**First Recommendation:** Hugo by pragmatism (single binary, native taxonomies, robust parsing), with caveat: Jekyll viable if team has Jekyll experience. Editorial workflow automation matters more than generator brand.

### Second Evaluation: Editorial & UX Recheck

**Context:** Team needed second pass. Holger questioned if Jekyll's GitHub-native advantage justified selection.

**Recheck Outcome:** Hugo remains stronger, but decision is pragmatic, not by large margin.

**Critical Clarification:** Is GitHub Web UI editing a hard requirement for non-technical editors? If yes, Jekyll wins. If contributors use git clone + local editor, advantage disappears.

**Reversibility:** Migration from Hugo to Jekyll Phase 2 = 4–6 hours of restructuring; no data loss.

**Conclusion:** Decision hinges on editorial workflow design (automation quality, contributor training) more than generator choice itself. Proceed with Hugo confidence, knowing Jekyll is viable fallback if team circumstances change.

### Third Evaluation: TIE-BREAK for MVP

**Context:** Data and Mikey reconsidered. Data recommended Jekyll (GitHub-native for Phase 0 launch). Mikey noted custom Actions erase Jekyll's infrastructure advantage. Team asked: which best serves **contributor usability** for a school?

**Final Reframe:** Not "Which is technically better?" but "Which minimizes friction for Holger in Phase 1?"

**Tie-Break Analysis:**

1. **Editorial Entry Barrier:**
   - Hugo: "Install binary. Learn GitHub Action debugging."
   - Jekyll: "Edit in GitHub Web UI. Teachers already do this."
   - **Winner: Jekyll** (familiar mental model)

2. **Moderation Gate (One-Eyed Willy's blocker):**
   - Both require: issue template + validation bot + moderation label + auto-publish
   - **Winner: Jekyll** (entire workflow visible; no Action debugging in Phase 1)

3. **Maintenance Handoff:**
   - Hugo: Requires Go knowledge
   - Jekyll: Any GitHub-fluent teacher can edit/publish
   - **Winner: Jekyll** (school culture = GitHub fluency)

4. **"Just Works" Factor (Week 2 Launch):**
   - Jekyll + GitHub Pages native: 30s, no Action debugging
   - Hugo + peaceiris Action: hidden failure modes if SHA breaks
   - **Winner: Jekyll** (school cannot afford Action YAML debugging during MVP)

**Why Hugo Is Not Wrong:**
- Technically superior: single binary, native taxonomies, i18n, build speed
- Appropriate if Holger were a CTO or Hugo expertise existed
- Reality: School prioritizes simplicity over optimization

**Reversibility:** Jekyll → Hugo Phase 2 = 4–6 hours, no data loss.

**Third Recommendation:** Choose Jekyll for MVP. Minimizes contributor friction, aligns with school culture (GitHub Web UI native), provides reliable moderation without Action debugging. Editorial workflow equally robust; generator brand matters less. Move with confidence; migration to Hugo is cheap insurance.

## Cross-Agent Convergence (Archived)

**Data's Input (Technology Architecture):**
- Hugo recommended as primary choice for zero npm dependencies, fastest builds, built-in i18n, trivial GitHub Actions deploy
- Comparison matrix evaluated 6 platforms; Hugo wins on build speed (50ms), single binary, ecosystem scale
- Risk mitigation: structured YAML issue forms for reliable parsing
- Fallbacks: Eleventy, Astro, Jekyll

**One-Eyed Willy's Input (Security & Privacy):**
- 3 BLOCKERS: issue template (no PII), moderation gate, legal pages
- 8 security guardrails; prefers Hugo's single binary over Jekyll's 30+ gem dependencies
- Moderation gate = BLOCKER; no auto-publish from issues alone

**Mikey's Input (Product Coordination):**
- Frames decision: SSG vs. Next.js vs. Headless CMS
- Stakeholder lens: 7 key stakeholders mapped to risks
- MVP scope: homepage + news + CS + AI + accessibility + privacy (2 weeks)
- Success metrics: <5 min publish, ≥90 Lighthouse accessibility, ≥85 mobile
- Phased roadmap: Phase 1 MVP → Phase 2 (CMS UI, newsletter) → Phase 3+ (i18n, analytics)

**Team Convergence:**
- All agents agree SSG is correct platform choice
- Hugo vs. Jekyll: both viable, team to vote by EOW
- Issue-to-news workflow feasible WITH security gates + editorial governance
- Critical path: issue template design, moderation gate, legal content by EOW

---

**Archive Summary:** This archive captures Sloth's initial UX evaluations and multiple Hugo vs Jekyll deliberations leading up to the final tie-break recommendation. The final consensus (Jekyll for Phase 1 MVP) is documented in active history.md.
