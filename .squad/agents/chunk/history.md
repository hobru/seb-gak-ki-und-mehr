# Chunk History

## Seed Context

- **User:** Holger Bruchelt
- **Project:** German-first website for pupils, teachers, and parents of Gymnasium am Kaiserdom Speyer.
- **Focus:** Computer science and AI tutorials, guidance, ideas, and a latest-news area that can be updated easily, ideally via GitHub issues.
- **Technology:** Not yet selected, but must run on GitHub.
- **Key concerns:** Stakeholder fit, maintainability, usability, security, newsletter privacy, and PII.

## Learnings

### 2026-05-31: Homepage Design Review
- **Learning:** Pupils need three things instantly: credibility (official status), clarity (why am I here?), and proof of life (recent activity). Generic navigation fails all three.
- **Key insight:** Concrete outcomes beat aspirational language. "Build a chatbot" outperforms "Explore AI." Pupils self-select entry points via three clear pathways (News → Tutorials → Deeper Learning), not menus.
- **Risk discovered:** Empty homepage is worse than no homepage. Prepopulated news/tutorials are critical for launch credibility.
- **Tone success factor:** Friendly peer/mentor voice ("Probier mal") outperforms corporate tone ("Lass dich inspirieren"). Pupils respond to transparency and actionable steps.
- **Recommendation:** Involve 1–2 pupils in UX validation before final design; audit all headlines for 11-year-old readability.

### 2026-05-31: Review Applied to Hugo v1 ✓

**Implementation status:** ✅ Complete  
**Commit:** 85c0032

**How Chunk's recommendations were applied:**
- **Three pathways on homepage:** Quick-nav cards for Informatik, KI, Aktuelles visible immediately under hero
- **Official status visible:** School name, logo anchor point, clear section headers
- **News always live:** 3 sample German news items prepopulated (KI-Begriffe, Wetterdaten, Elternabend) to signal active, maintained site
- **Concrete language:** Titles use action verbs and relatable outcomes (e.g., "Trainiere dein erstes Mini-Modell" not abstract concepts)
- **Homepage prominently shows activity:** News section renders 3 most recent with dates and category badges

**For Phase 2 UX validation:**
- Test with 1–2 real pupils (ages 12–14) on desktop and mobile
- Audit all headlines with 11-year-old reading level tool
- Validate 3-pathway self-sorting (measure time to goal)

