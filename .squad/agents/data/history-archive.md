# Data History Archive

**Generated:** 2026-05-31T15:44:09Z (Scribe)  
**Reason:** history.md reached 18954 bytes; archived pre-reversal entries

## Archived Sections

### Initial Technology Stack Evaluation (2026-05-31 early)
- Hugo recommended as primary SSG: zero npm dependencies, fastest builds, built-in i18n
- Issue-to-news pipeline feasible via GitHub YAML issue forms + Actions
- Content model: Three sections (news/, informatik/, ki/) under content/
- Key risk: Issue body parsing fragility — mitigated by structured YAML forms

### Hugo vs Jekyll Re-evaluation (2026-05-31 mid)
- Where Jekyll wins: native GitHub Pages build, familiar Liquid templates, lower contributor learning curve
- Where Hugo wins: no runtime dependency, build speed (~50ms), security surface (no 30+ gems), built-in i18n, Windows-friendly single binary
- Verdict at time: Hugo remains correct; Jekyll advantage (native Pages build) nullified by required issue-to-news Actions
- Threshold for Jekyll preference: if no Actions required, all contributors have Ruby, site <20 pages, no i18n

### Blank-Slate Revision (2026-05-31 17:16)
- Reconsidered from scratch per Holger's challenge
- Revised recommendation: Jekyll for Phase 1 (GitHub Pages native, minimize setup/contributor friction)
- Flawed Hugo arguments: "Actions required anyway", "better security", "Windows ease", "built-in i18n" (not needed)
- Jekyll advantages: time to first deploy, no CI/CD needed from day 1, template syntax (Liquid) simpler for non-developers
- Threshold for Hugo: >200 pages, actual multilingual needs, team developer, or Hugo theme clear fit
- Migration cost: ~4-6 hours (Liquid → Go templates)
- **Final verdict at time: Jekyll is best default NOW**

### Team Consensus: Jekyll Finalized (2026-05-31 15:24)
- Decision: Jekyll for Phase 1 MVP (Data + Sloth + Mikey consensus)
- Team Outcome: Jekyll minimizes contributor friction; operationally simpler Phase 1
- Reversibility: Phase 2 migration to Hugo = 4–6 hours if multilingual/scaling demands arise

## Final Entry (Pre-Archive)

**2026-05-31 17:44 — DECISION REVERSAL: Hugo from Day 1**
- Context: Holger clarified preference for real long-term stack from day 1, no throwaway MVP
- Key insight: Hugo can deliver homepage + 2 static pages + issue-driven news trivially
- Jekyll advantage (native Pages build) = zero when Actions required for issue-to-news regardless
- Hugo extra setup effort = ~30 minutes (deploy.yml workflow)
- Future migration cost avoided: 4–6 hours (Liquid → Go templates)
- Recommendation: Start with Hugo. Every hour of work is permanent.
- **Status: DECIDED — Hugo from day one (current decision)**

---

**Note:** Full entries retained in decisions.md for audit trail. This archive preserves reasoning history for future reference.
