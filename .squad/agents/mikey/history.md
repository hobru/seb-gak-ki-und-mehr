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

### 2026-05-31 — Product Reframe: Hugo vs Jekyll From Risk & Momentum Lens

**The Real Question (Not Tech Beauty):**
This is a German school website. The stake is not engineering elegance but **team velocity and staying power**. Both Hugo and Jekyll work technically. The decision is: Which choice reduces the risk of stalling mid-project because a bottleneck emerges *after* we start?

**Risk Analysis (Product Lens):**

1. **Dependency Risk**: 
   - Hugo: Single Go binary. Zero package manager friction. No node_modules hell, no Ruby version conflicts, no dependency updates breaking builds mid-MVP.
   - Jekyll: Ruby + 30+ gems. Each gem is a potential point of failure. On Windows (team's OS), Ruby toolchain is notoriously fiddly. If a build breaks in week 2 due to a gem incompatibility, we lose a day to DevOps instead of shipping content.
   - **Winner: Hugo** (lower surface area = less chance of Friday-afternoon surprises).

2. **Operational Bus Factor**:
   - Hugo: One person can set up on Windows, macOS, Linux identically. Reproducible.
   - Jekyll: Requires Ruby expertise. If the person who owns the build setup leaves or isn't available, the next person faces environment hell.
   - **Winner: Hugo** (resilience = momentum insurance).

3. **Non-Technical Editor Onramp**:
   - Both platforms rely on GitHub Web UI initially (Phase 1). Neither is a CMS.
   - GitHub Web UI editing = markdown in browser. Teachers don't care if the generator is Hugo or Jekyll; they care if publishing works in <5 min.
   - Jekyll's "GitHub Pages native" advantage is moot because we're already using GitHub Actions for moderation + issue parsing. Native GitHub Pages only helps if you deploy from main branch with no pipeline logic. We have pipeline logic.
   - **Winner: Tie** (editorial friction is workflow design, not generator choice).

4. **Issue-to-News Pipeline Reliability**:
   - Hugo: Go binary + GitHub Actions = deterministic. One thing to debug if it breaks.
   - Jekyll: Ruby runtime + gems + GitHub Actions = multiple surfaces for failure (gem version drift, Ruby version mismatch, etc.). If a build fails, you're asking "Is it our Action? The gem? Ruby versioning?" More diagnostic burden.
   - **Winner: Hugo** (fewer moving parts = easier troubleshooting = faster mean-time-to-fix when news doesn't publish).

5. **Windows Deployment (Team's OS)**:
   - Hugo: Native Windows binary. Zero friction.
   - Jekyll: Windows Ruby support is notorious for friction. Not a blocker, but adds setup tax.
   - **Winner: Hugo** (Windows is the team's reality; plan for it).

6. **Future Scalability (Phase 2+)**:
   - Hugo: Built-in taxonomies and i18n primitives. Extending for multi-language content in Phase 2 is straight refactoring, not re-architecting.
   - Jekyll: Plugins can handle i18n, but less idiomatic. More custom code needed.
   - **Winner: Hugo** (easier to grow into Phase 2 without surprises).

**Momentum Calculation:**
- Week 1: Both platforms get the MVP shipped at roughly same speed if we nail the issue template and moderation gate. No difference in delivery.
- Week 2–3: If a build breaks or a non-technical editor gets stuck on setup, we need to debug fast.
  - Hugo: "Run `hugo` locally; if it works locally, GitHub Actions works too." Simple.
  - Jekyll: "Check your Ruby version, maybe reinstall gems, check the Gemfile.lock, look at the Action logs, check gem versions on the CI system..." Multiple layers.
- **Risk of stalling:** Hugo scenario is simpler to unblock.

**Recommendation:**

**CHOOSE HUGO NOW. Do NOT prototype both.**

**Rationale (Product Terms):**
1. **Lower operational risk** = fewer points of failure mid-project.
2. **Reproducible locally and on CI** = faster debugging if something breaks.
3. **Windows-friendly** = respects the team's actual OS (not theoretical).
4. **Editor friction is workflow design, not generator choice** = Jekyll's "GitHub-native" edge doesn't matter because we're doing custom issue parsing anyway.
5. **No technical elegance benefit** to Jekyll that justifies the operational complexity for a school project.

**Why NOT Prototype Both?**
Prototyping both consumes time without changing the outcome. Both generators produce identical HTML. The difference appears only in build failures, dependency drift, and Windows onboarding — not in feature exploration. Prototyping delays launch for zero new information. **One week of prototyping = one week of Hugo launch pushed back + still no Jekyll launch data because we haven't tested the real workflow on either.**

**What Unlocks Confidence:**
1. One person sets up Hugo locally on Windows, runs `hugo`, confirms the build.
2. Same person pushes to GitHub, confirms the Action works.
3. Test the issue-to-markdown pipeline with a test issue.
4. Done. No full prototype needed; just validation that the three pieces fit.

**Trade-offs Being Made (Explicit):**
- Accepting Hugo's steeper learning curve for the first Dev (Data) is outweighed by the long-term momentum gain and reduced bus factor.
- If the team later needs Jekyll-specific plugins or has strong Ruby expertise, Phase 2 can revisit—but starting with Jekyll for a "GitHub-native" advantage that's moot in our workflow is premature specialization.

**Success Criterion:**
By EOW, Holger green-lights Hugo. Data spends Monday set up + validation. By Wednesday, we have a working action that publishes a test issue to the staging site. By Friday, content templates for CS + AI sections are ready. Week 2: MVP goes live.

### 2026-05-31T15:24:57.022Z — Team Consensus: Jekyll Decision Finalized (Sloth's tie-break)

**Status:** ✓ **DECIDED** — Jekyll chosen for Phase 1 MVP despite Hugo's operational advantages (Scribe merged decisions)

**Team Outcome (Product Terms):**
- Mikey's Hugo rationale (lower MTTF, bus factor, Windows resilience) remains valid.
- Data reconsidered: Jekyll's GitHub-native advantage is REAL at Phase 0 (MVP launch without Actions).
- Sloth tie-break: **Editorial friction minimized with Jekyll for school context** (GitHub Web UI native, familiar mental model, no Action debugging in Week 2).
- **Team consensus:** Contributor usability + Phase 1 stabilization outweigh operational advantages. Start with Jekyll (simple); migrate to Hugo Phase 2 if scaling demands.

**Explicit Trade-off Being Made:**
- **Accepting:** Ruby maintenance burden, gem churn, Windows gem friction
- **Gaining:** Lower contributor friction, familiar GitHub culture, reliable moderation without Action debugging, school team retention

**Decision Finalized in `.squad/decisions.md`:**
- Static site generator: **Jekyll for Phase 1 MVP**
- Build: GitHub Pages native (no custom Actions for deployment)
- Issue automation: Actions for intake/validation only; Jekyll rebuilds automatically

**Risk Owned:** If Ruby becomes a real bottleneck in Phase 1, Team to unblock and document. Phase 2 migration path = 4–6 hours, reversible.

**Next:** Unblock issue template (One-Eyed Willy), Impressum, moderation gate. Begin Phase 1 implementation with Jekyll architecture.

