# Data History

## Seed Context

- **User:** Holger Bruchelt
- **Project:** German-first website for pupils, teachers, and parents of Gymnasium am Kaiserdom Speyer.
- **Focus:** Computer science and AI tutorials, guidance, ideas, and a latest-news area that can be updated easily, ideally via GitHub issues.
- **Technology:** Not yet selected, but must run on GitHub.
- **Key concerns:** Stakeholder fit, maintainability, usability, security, newsletter privacy, and PII.

## Learnings

### 2026-05-31 — Technology Stack Evaluation

- **Reference site** (hobru.github.io/KI-an-der-Schule/) is a simple single-page layout, Markdown-style, German, focused on AI tool guidance for students. No complex framework needed.
- **Hugo recommended** as primary SSG: zero npm dependencies, fastest builds, built-in i18n, trivial GitHub Actions deploy, excellent Markdown content workflow.
- **Issue-to-news pipeline** is feasible: GitHub YAML issue forms → Action parses fields → commits `content/news/*.md` → Hugo rebuilds. Structured issue forms (not freetext) are critical for reliable parsing.
- **Fallbacks:** Eleventy (JS ecosystem preference), Astro (if interactive components needed later), Jekyll (simplest but Ruby dependency).
- **Key risk:** Issue body parsing fragility — mitigated by using GitHub's structured YAML issue forms which produce predictable field IDs.
- **Content model:** Three sections (`news/`, `digital/`, `ki/`) under `content/`. News items have front matter with title, date, abstract, link, audience, category.

### 2026-05-31 — Hugo vs Jekyll Re-evaluation (requested by Holger)

Holger questioned whether Hugo is truly the best choice or whether Jekyll would serve better. Full comparison below.

**Where Jekyll wins:**
1. **GitHub Pages native build** — Jekyll is the only SSG that GitHub Pages builds natively without Actions. Push markdown, get a site. Zero CI config needed for the simplest case.
2. **Familiar to GitHub ecosystem** — GitHub's own docs use Jekyll. Many school/educator projects already use it.
3. **Liquid templates** — simpler mental model for non-developers vs Hugo's Go templates.
4. **Lower learning curve for contributors** — if a teacher already used GitHub Pages, they likely touched Jekyll.

**Where Hugo wins (and why it still wins for THIS project):**
1. **No runtime dependency** — Jekyll needs Ruby + Bundler + gems. Hugo is a single binary. For a school project maintained by rotating contributors, "install Ruby" is a real friction point on Windows school PCs.
2. **Build speed** — Jekyll: 5-30s for small sites; Hugo: <100ms. Matters for the issue-to-news pipeline where we want <5 min publish time including CI.
3. **GitHub Actions required anyway** — The issue-to-news workflow (parse issue → commit markdown → deploy) already requires Actions. Once you need Actions, Jekyll's "native Pages build" advantage disappears — you're running a custom workflow regardless.
4. **Security surface** — Jekyll pulls in 30+ Ruby gems (nokogiri, etc.) with C extensions. Hugo has zero dependencies. For One-Eyed Willy's security posture, Hugo is clearly better.
5. **i18n built-in** — Hugo has native multi-language support. Jekyll needs plugins (jekyll-multiple-languages-plugin) which aren't supported on native Pages.
6. **Long-term flexibility** — Hugo's module system, asset pipeline, and content organization scale better if the site grows.
7. **Windows friendliness** — Hugo installs via single binary or `winget`. Jekyll on Windows requires Ruby DevKit, MSYS2, gem install… historically painful.

**Verdict: Hugo remains the correct choice.** The one genuine advantage Jekyll has (native Pages build) is nullified by the fact that our issue-to-news automation already mandates GitHub Actions. Once Actions are in play, we might as well use the tool with fewer dependencies, faster builds, and less maintenance burden.

**When would Jekyll be better?**
- If we dropped the issue-to-news pipeline entirely and just wanted teachers to edit markdown via GitHub Web UI with zero CI.
- If all contributors already had Ruby environments and Jekyll experience.
- If the site would never need i18n or grow beyond ~20 pages.

None of these conditions apply here.

### 2026-05-31 — Cross-Agent Convergence (Technology Review Session)

**Sloth's Input (UX & Accessibility):**
- Prefers Jekyll for GitHub-native simplicity and accessibility defaults
- Validates static HTML approach (no JavaScript = better screen reader support)
- Confirms issue-driven news feasible IF strict templates + bot validation + moderation gate
- Recommends WCAG 2.1 AA baseline (non-negotiable for German school)
- Notes: Editorial governance prerequisite; templates must include alt-text guidelines and link-text validation

**One-Eyed Willy's Input (Security & Privacy):**
- Identifies 3 BLOCKERS before implementation: (1) issue template design (no PII fields), (2) moderation gate in build pipeline, (3) legal pages (Impressum + Datenschutzerklärung)
- Mandates 8 guardrails: no PII in templates, moderation before publishing, no emails in repo, privacy-safe analytics only, external links with rel="noopener noreferrer", GitHub Actions least-privilege, dependency hygiene (Dependabot)
- Concludes: Hugo's single binary + zero npm deps = better security surface than Jekyll's 30+ gems

**Mikey's Input (Product Coordination):**
- Frames decision as SSG (Hugo/Jekyll/Astro) vs. Next.js vs. Headless CMS
- Validates MVP scope: homepage + news + 2 sections (CS + AI) + accessibility + privacy baseline
- Stakeholder risk inventory: publishing friction, non-technical editor exclusion, accessibility/performance gaps, privacy/security, maintenance burden
- Decision timeline: confirm SSG choice by EOW; prototype Week 2; launch Week 3+
- Success metrics: <5 min issue→live, Lighthouse ≥90 accessibility, ≥85 mobile performance

**Team Convergence:**
- All agents agree SSG is correct platform type for this project
- Hugo vs. Jekyll choice deferred to team vote; both viable
- Issue-to-news workflow feasible but REQUIRES security gates and editorial governance
- Phased roadmap: Phase 1 (MVP, 2 weeks) → Phase 2 (CMS UI, newsletter, 6 weeks) → Phase 3+ (i18n, analytics)

### 2026-05-31 — Hugo vs Jekyll: Decision Confidence Recheck

**Context:** Holger remained uncertain about Hugo after initial evaluation. Requested second pass to stress-test Jekyll's claims.

**Recheck Outcome:** **Hugo remains correct choice. Recommendation strengthened.**

**Key Insight:** Jekyll's only real advantage—native GitHub Pages build without Actions—is irrelevant to GAK's actual project constraints. The issue-to-news pipeline already requires GitHub Actions, making Jekyll's "zero CI" benefit disappear. Once Actions are mandatory, the comparison shifts entirely in Hugo's favor.

**Comparative Analysis (refined):**
| Criterion | Hugo | Jekyll | Winner |
|-----------|------|--------|--------|
| Dependencies | Single binary | Ruby + Bundler + 30+ gems | **Hugo** |
| Build speed | <100ms | 5-30s | **Hugo** |
| Windows install | `winget install Hugo` | Ruby DevKit + MSYS2 + gem install | **Hugo** |
| Security surface | Minimal | Nokogiri + C extensions | **Hugo** |
| i18n support | Built-in | Plugin (unsupported on native Pages) | **Hugo** |
| GitHub Actions required? | Yes (but trivial) | Yes (for our workflow) | Tie |
| Template syntax | Go templates (steeper) | Liquid (gentler) | **Jekyll** |

**Conditions That Would Favor Jekyll:**
1. No issue-to-news pipeline (pure manual markdown editing via GitHub Web UI)
2. All contributors already have Ruby environments
3. Site never needs i18n or grows beyond ~20 pages

**None of these apply to GAK.** Decision rationale is now defensible for team vote EOW.

