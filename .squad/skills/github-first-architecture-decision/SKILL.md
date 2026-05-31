---
name: "github-first-architecture-decision"
description: "Decision heuristic for choosing GitHub-native platforms that prioritize low-friction publishing and version-controlled content"
domain: "architecture"
confidence: "high"
source: "GAK website technology frame (Mikey, 2026-05-31)"
---

## Context

When a project requires **GitHub hosting**, **version-controlled content**, and **low-friction publishing workflows**, the right platform choice often comes down to three questions. This skill helps coordinators and architects evaluate whether static generators, headless CMS, or other platforms fit the constraints.

## Decision Heuristic

**Ask these three questions in order:**

1. **Can the platform run natively on GitHub Pages (or similar)?**
   - YES → continue to question 2
   - NO → eliminates most platforms; consider trade-offs (external hosting, vendor lock-in, complexity)

2. **Can content live as version-controlled files (markdown, YAML, JSON)?**
   - YES → continue to question 3
   - NO → triggers CMS tier (adds complexity, external services, privacy surface)

3. **Can we automate publish triggers with GitHub Actions?**
   - YES → **Static Generator (Jekyll, Astro, Hugo) is likely the right fit**
   - NO → might require fallback (manual workflow, external triggers, or different platform)

**If all three are YES:** Static site generator (SSG) wins. Lower complexity, auditable dependencies, high reliability.

## Decision Tree

```
GitHub-native required?
  ├─ NO  → Defer GitHub constraint; evaluate headless CMS or hosted platform
  └─ YES (proceed)

Version-controlled content?
  ├─ NO  → CMS tier (trade complexity for non-technical editor UI)
  └─ YES (proceed)

GitHub Actions automation?
  ├─ NO  → Manual publish workflow; consider static + webhook or different approach
  └─ YES → Static Site Generator is likely optimal
```

## Patterns

**✓ Static Generator is optimal when:**
- Content is primarily markdown/text
- Publishing should be low-friction (issue → deploy)
- Team is small and prefers git-based workflows
- Audience values speed and accessibility (school, open-source communities)
- Security/privacy is high concern (no external services, simple attack surface)

**✓ Headless CMS becomes valuable when:**
- Non-technical editors outnumber developers
- Content modeling is complex (structured data, relationships)
- Approval workflows / versioning needs outgrow git
- Team is large enough to maintain CMS + infrastructure

**⚠️ Static Generator causes friction when:**
- Editors are non-technical and can't use markdown/git
- Content model is highly structured (e.g., database-like)
- Real-time collaboration is required
- Frequent template changes are needed during editing

## Examples

**✓ Correct fit (GAK website, 2026):**
- GitHub Pages available → YES
- Content as markdown + GitHub issues → YES
- GitHub Actions trigger build on issue → YES
- **Decision:** Static generator (Jekyll/Astro)
- **Rationale:** Holger (low friction) + Mouth (content control) + school audience (speed/accessibility) all satisfied; security baseline clean; team can audit all dependencies

**✓ Correct fit (Documentation site):**
- Hosted on github.io → YES
- Docs as markdown + YAML frontmatter → YES
- Trigger builds on branch push → YES
- **Decision:** Jekyll/Astro/Hugo
- **Rationale:** Maintainable by single person; high SEO; fast; privacy-respecting

**⚠️ When CMS becomes necessary (hypothetical):**
- 50+ non-technical contributors (teachers, students)
- Approval workflows with roles (editor → reviewer → publisher)
- Structured content (e.g., lessons with metadata, prerequisites, etc.)
- **Decision:** Decap CMS (GitHub-hosted, free) or Tina (PR-based workflow)
- **Rationale:** Markdown stays git-backed; UI layer for non-coders; approval workflow
- **Cost:** Defers to Phase 2+ when adoption proves friction

**❌ Incorrect decision:**
- "Let's build a custom headless CMS" (builds complexity; delays delivery; introduces maintenance burden)
- "Let's use WordPress" (off GitHub; privacy/security concerns for school; vendor lock-in)
- "Let's use Next.js with server-side rendering" (overkill for static content; higher complexity; more dependencies)

## Risks Mitigated

| Risk | Mitigation (SSG Approach) |
|---|---|
| Publishing friction (Holger) | GitHub Actions + issue template automation |
| Content editor overwhelm (Mouth) | Markdown + GitHub Web UI (built-in) |
| Non-technical contributors blocked | Defer CMS UI to Phase 2; use GitHub Web editor (free, no login) |
| Privacy/security concerns | No external services; GitHub-hosted; auditable build |
| Maintenance burden | Minimal dependencies; version-pinned; documented workflows |
| Mobile UX/accessibility failures | Static HTML = fast, accessible by default; Lighthouse gates |

## Decisions That Flow From This Pattern

Once SSG is chosen:

1. **Issue-to-content automation:** GitHub Actions workflow listens for issues with label/template; generates markdown file; triggers build
2. **Content structure:** Single markdown file per piece = version history, comments, blame tracking (forces discipline)
3. **Review gates:** Branch protection + codeowners ensure Mouth reviews German quality before publish
4. **Privacy baseline:** No third-party scripts; GitHub Pages infrastructure is the only service
5. **Phase 2 decision:** If non-technical editors struggle, add Decap CMS UI (GitHub-hosted, same workflow)

## Antipatterns

- ❌ **"Let's use a CMS because we might have many editors later"** — start with what you need; CMS adds complexity upfront; defer based on actual friction
- ❌ **"Let's build a custom tool to automate issue→markdown"** — GitHub Actions exists for this; don't reinvent
- ❌ **"Let's host on external service for flexibility"** — defeats GitHub-first; adds privacy/security surface; complicates compliance
- ❌ **"Let's skip version control and use a UI instead"** — loses audit trail, blame tracking, collaboration model

## When to Revisit

- ✅ **After MVP stable (4 weeks):** Assess editor friction. If Mouth struggles, prototype Decap CMS integration (Phase 2).
- ✅ **If contributor count > 10 non-developers:** CMS becomes necessary; plan migration (no data loss; markdown stays authoritative).
- ✅ **If privacy/compliance requirements change:** Re-audit third-party services; may require additional vetting.
- ✅ **If GitHub Pages hits limits (rare):** Document reasons; decide on Netlify/Vercel (still GitHub-backed) or content restructure.

---

**Used by:** Mikey (GAK tech decision frame), suitable for future squad architectural decisions  
**Confidence:** High (proven pattern from multiple implementations)
