# Andy History

## Seed Context

- **User:** Holger Bruchelt
- **Project:** German-first website for pupils, teachers, and parents of Gymnasium am Kaiserdom Speyer.
- **Focus:** Computer science and AI tutorials, guidance, ideas, and a latest-news area that can be updated easily, ideally via GitHub issues.
- **Technology:** Not yet selected, but must run on GitHub.
- **Key concerns:** Stakeholder fit, maintainability, usability, security, newsletter privacy, and PII.

## Learnings

### 2026-05-31: Homepage Review for Teacher Perspective

**Task:** Review Mouth's homepage draft v1 from a classroom-fit and didactic angle.

**Key Finding:** The current teacher section is vague ("Inspirierende Materialien") and doesn't signal immediate utility. Teachers scan homepages for: **(1) grade alignment, (2) prep-time savings, (3) concrete examples, (4) audience matching in news/tutorials, (5) feedback channels**. All five are currently implicit or missing.

**Concrete Actions:** Provided 5 recommendations (quick-start card, audience tagging, sample lesson preview, grade-level clarity, maintenance transparency) + 3 sample news/tutorial frames showing how to write for teachers (e.g., "90 min für eine Doppelstunde" is more actionable than generic abstracts).

**Dependency Recognized:** GitHub issue form (from decisions.md) must capture "Audience," "Grade," "Duration," "Difficulty" before build—otherwise filtering & teacher trust suffers.

**For Next Review:** Sloth should audit homepage scanning time; Mouth can integrate teacher quick-start card and concrete sample URLs into v2 before implementation.

### 2026-05-31: Teacher Review Recommendations Integrated ✓

**Implementation status:** ✅ Complete  
**Commit:** 85c0032

**How Andy's recommendations were applied:**
- **Audience tagging in news front matter:** All posts include `audiences: ["Lehrkräfte", "Schülerinnen und Schüler", ...]` for future filtering
- **Grade-level metadata:** Idea cards in front matter include `audience:` field for teachers (e.g., "Lehrkräfte ab Jahrgangsstufe 9")
- **Sample lesson visible:** README.md and content structure enable easy linking to example lessons; 3 sample news posts included
- **Maintenance transparency:** README.md documents content authors + how to add posts + GitHub issue workflow
- **Issue template ready:** Will capture grade, duration, audience in Phase 2 automation

**For teacher onboarding (Phase 2):**
- Add explicit "For Teachers" quick-start card on homepage (deferred pending Holger input on specific grade ranges)
- Implement audience-based news filtering on `/news/` archive page
- Create downloadable lesson templates with rubrics (content author task)

