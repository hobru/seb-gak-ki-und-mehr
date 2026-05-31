# Sloth History

## Seed Context

- **User:** Holger Bruchelt
- **Project:** German-first website for pupils, teachers, and parents of Gymnasium am Kaiserdom Speyer.
- **Focus:** Computer science and AI tutorials, guidance, ideas, and a latest-news area that can be updated easily, ideally via GitHub issues.
- **Technology:** Not yet selected, but must run on GitHub.
- **Key concerns:** Stakeholder fit, maintainability, usability, security, newsletter privacy, and PII.

### 2026-05-31T15:24:57.022Z — Team Consensus: Jekyll Decision Finalized ✓

**Status:** ✓ **DECIDED** — Jekyll chosen for Phase 1 MVP (Scribe merged final recommendations)

**Final Consensus (Team-Wide):**
- Sloth's tie-break recommendation stands: **Jekyll for contributor usability** (editorial friction < technical optimization)
- Data aligned: GitHub-native advantage is real at Phase 0; issue-to-news equally robust in both platforms
- Mikey documented Hugo rationale: valid operational gains (bus factor, MTTF, Windows) but outweighed by Phase 1 contributor retention priority
- **Team decision:** Start simple with Jekyll; evaluate Hugo migration in Phase 2 if multilingual or scaling demands justify it

**Editorial Usability Secured:**
1. **GitHub Web UI editing native** — school staff can edit/preview markdown without git clone
2. **Moderation gate visible** — entire workflow in GitHub; no Action debugging required in Week 2
3. **Maintenance handoff ready** — any GitHub-fluent teacher can edit/publish (no Go expertise needed)
4. **"Just Works" Factor** — 30s from commit to live; reliable fallback (direct file editing in Web UI)

**Technical Concessions Owned:**
- Ruby gem churn vs. Go's stability (accepted for Phase 1; Phase 2 revisit if burden grows)
- Windows gem installation friction (acceptable; contributors use GitHub Web UI, not local builds)

**Reversibility Reconfirmed:**
- Jekyll → Hugo migration Phase 2: 4–6 hours (Liquid → Go templates), zero data loss
- No risk in starting with Jekyll; decision reversible when (if) scaling demands warrant

**Success Criteria (Sloth Focus):**
| Metric | Target | Why Jekyll Helps |
|--------|--------|------------------|
| Contributor retention (trained editors by week 3) | ≥2 | GitHub Web UI familiarity |
| Time to publish news (issue → live) | <5 min | Both equal; GitHub automation |
| Editor satisfaction (weekly feedback) | Positive trend | Jekyll = lower onboarding friction |
| Accessibility baseline (Lighthouse) | ≥90 | Both equal (static HTML) |

**Decision Finalized in `.squad/decisions.md`:** Jekyll (Phase 1) with explicit migration path to Hugo (Phase 2+).

**Next:** Unblock issue template design (One-Eyed Willy), legal content (Impressum + Datenschutzerklärung), moderation gate wiring. Begin Phase 1 with Jekyll architecture.


