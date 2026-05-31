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

**Recheck Outcome:** Hugo recommended — but see blank-slate revision below.

### 2026-05-31T17:16 — BLANK-SLATE REVISION (requested by Holger)

**Context:** Holger challenged whether Hugo is really better. I discarded prior reasoning and re-evaluated from scratch, asking: what serves a German school teacher maintaining a small site on GitHub *right now*?

**Revised Recommendation: Jekyll is the correct default for this project.**

**Why I was wrong before — the flawed arguments:**

1. **"Actions required anyway, so Jekyll's native Pages advantage disappears."**
   — This conflates Phase 0 (get the site live) with Phase 1 (add issue automation). For the MVP launch, Jekyll needs ZERO CI config. Push markdown, get a website. That's a real advantage measured in days of setup time saved. The issue pipeline comes later; when it does, both tools are equal.

2. **"Hugo has fewer dependencies / better security surface."**
   — On GitHub Pages native build, Jekyll's dependencies are *GitHub's problem*, not ours. GitHub patches them. With Hugo, we trust a third-party Action (`peaceiris/actions-hugo`) and pin versions ourselves. The security argument actually slightly favors Jekyll when using native Pages.

3. **"Hugo is easier on Windows."**
   — Only relevant if contributors build locally. They won't. The workflow is: edit markdown in GitHub Web UI → site rebuilds automatically (Jekyll native) or via Actions (Hugo). Nobody needs to install Ruby OR Hugo locally.

4. **"Hugo has built-in i18n."**
   — The site is German-only. Multi-language is deferred to Phase 3+. This is future-proofing for a scenario that may never arrive.

5. **"Hugo builds faster."**
   — At 20-50 pages, Jekyll builds in 2-3 seconds. Irrelevant.

**Where Jekyll genuinely wins for GAK:**

| Criterion | Jekyll | Hugo | Winner for GAK |
|-----------|--------|------|----------------|
| Time to first deploy | Push markdown, done | Write Actions YAML first | **Jekyll** |
| CI/CD for basic site | None needed | Required from day 1 | **Jekyll** |
| Build infrastructure maintenance | GitHub maintains it | We maintain Action config + Hugo version | **Jekyll** |
| Contributor editing (Web UI) | Edit → auto-build | Edit → needs working Actions | **Jekyll** |
| Template syntax for teachers | Liquid (HTML-like) | Go templates (programming) | **Jekyll** |
| Theme ecosystem for schools | Large, education themes exist | Large, fewer education themes | **Jekyll** |
| Issue-to-news (Phase 1) | Equally good via Actions | Equally good via Actions | Tie |
| Local preview (if wanted) | Needs Ruby | Single binary | **Hugo** |
| Site >200 pages, multi-language | Struggles | Excels | **Hugo** |

**The threshold where Hugo becomes necessary:**
- Site grows beyond ~200 pages AND build time becomes noticeable (>30s)
- Multi-language support is actually needed (not just "nice to have someday")
- Team wants advanced content organization (taxonomies, bundles)
- A developer joins who wants local workflow and prefers Go templates

None of these conditions exist or are likely within the next 6-12 months.

**Migration path if we outgrow Jekyll:**
Content is markdown + front matter. Moving from Jekyll to Hugo is a half-day task: rename `_posts/` to `content/news/`, adjust front matter slightly, switch Actions workflow. Low risk.

**Final verdict:** Start with Jekyll. It's the path of least resistance for getting this site live, and it stays correct for the foreseeable future. If the project grows significantly, migration is cheap.


### 2026-05-31T17:16:21.510+02:00 — Blank-slate stack retry: Jekyll as NOW-default

**Context:** Holger asked to try again after challenging whether Hugo is really better than Jekyll. I reopened the decision without defending the earlier Hugo recommendation and focused on the site that must be launched now: a German school website on GitHub with a homepage, news, Digital Stuff / Computer Science, AI, and later issue-template-driven news.

**Revised recommendation:** Start with **Jekyll** now. Hugo remains a strong SSG, but Jekyll is the better default for this specific MVP because GitHub Pages supports it natively, non-specialist maintainers can edit Markdown in the GitHub Web UI, and the basic site can ship without custom build/deploy Actions.

**Why this changes the framing:**

- **GitHub Pages default matters now.** For the first version, Jekyll can publish from the repository with minimal configuration. Hugo requires a custom Action from day one.
- **Issue-to-news does not erase Jekyll's advantage.** Later automation can create Markdown files or pull requests while GitHub Pages still performs the native Jekyll build. Actions are needed for intake/moderation, not necessarily for the whole site deployment.
- **Local Windows setup is mostly irrelevant.** Likely contributors should use GitHub Issues and the Web UI, not local Ruby or Hugo. If no one builds locally, Hugo's single-binary advantage is weaker.
- **Security/dependency footprint is different under native Pages.** With Jekyll native Pages, GitHub manages the build environment. Hugo shifts responsibility to a custom workflow, pinned actions, and Hugo version maintenance.
- **Non-specialist maintenance favors boring defaults.** Liquid/Jekyll conventions are common in GitHub Pages examples, and there are many simple education/blog themes. Hugo's Go templates are more powerful but less approachable.
- **Privacy/newsletter constraints are generator-neutral.** The important choices are no PII in issue forms, moderation before publish, no subscriber data in Git, no cookies/analytics at launch, and legal pages. Jekyll does not make those harder.

**Recommended NOW architecture:**

- GitHub Pages + Jekyll native build.
- Markdown content in `_posts` or `_news` plus simple pages/collections for `digital-stuff` / `informatik` and `ki`.
- German-first front matter: title, date, summary, audience, category, source link, approved status if needed.
- Start with manual Markdown/Web UI publishing or PR review.
- Add issue-template-driven news as a guarded Action later: issue form → validation → generated Markdown PR or commit after approval → native Pages rebuild.
- Keep newsletter out of MVP; if added later, use an external GDPR-reviewed processor and never store emails in Git.

**Exact threshold for choosing Hugo instead:** Choose Hugo only if the team knowingly accepts custom GitHub Actions from day one and needs at least one of: real multilingual publishing soon, >200 pages or build times becoming material, advanced taxonomies/content bundles, strict single-binary local preview for developer-heavy maintenance, or a Hugo theme that clearly fits better than any Jekyll option. Those thresholds are not present for the current MVP.

**Bottom line:** Jekyll is not the abstract best SSG. It is the best default **now** because it minimizes setup, maintenance, and contributor friction for a small GitHub-hosted German school site. Hugo should stay as the migration path if scale or multilingual needs become real.

### 2026-05-31T15:24:57.022Z — Team Consensus: Jekyll Decision Finalized

**Status:** ✓ **DECIDED** — Jekyll chosen for Phase 1 MVP (Scribe merged decisions)

**Team Outcome:**
- Data (Tech Architect) + Sloth (UX) recommendation: Jekyll for Phase 1
- Mikey (Product Coordinator) documented Hugo rationale for Phase 2 migration
- Consensus: **Jekyll minimizes contributor friction for schools; operationally simpler Phase 1**

**Decision Finalized in `.squad/decisions.md`:**
- Hosting/build: GitHub Pages with native Jekyll
- Content: Markdown + front matter in `_posts/` or `_news` collection
- Editing: GitHub Web UI or PRs
- Automation: Issue form → validation Action → moderation label → auto-rebuild
- Privacy: No PII fields, German privacy warning in issue template

**Reversibility Confirmed:** Phase 2 migration to Hugo (if multilingual or scaling demands) = 4–6 hours (Liquid → Go templates), zero data loss.

**Next Blockers to Unblock:** Issue template design (One-Eyed Willy), Impressum + Datenschutzerklärung, moderation gate wiring.
