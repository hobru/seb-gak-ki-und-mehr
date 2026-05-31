# Mouth History

## Seed Context

- **User:** Holger Bruchelt
- **Project:** German-first website for pupils, teachers, and parents of Gymnasium am Kaiserdom Speyer.
- **Focus:** Computer science and AI tutorials, guidance, ideas, and a latest-news area that can be updated easily, ideally via GitHub issues.
- **Technology:** Not yet selected, but must run on GitHub.
- **Key concerns:** Stakeholder fit, maintainability, usability, security, newsletter privacy, and PII.

## Learnings

### Homepage Content Framework (2026-05-31)
- **Three-persona approach works:** Separating value props by audience (Schüler/Lehrkräfte/Eltern) clarifies messaging and allows later segmentation of news, notifications, or CTAs.
- **Sample content must be explicit:** Marking all placeholder text with [SAMPLE] prevents accidental publication and signals to stakeholders that these are templates, not final content.
- **News structure → GitHub automation:** Standardizing news items (title ≤80 chars, abstract ≤200 chars, category, audience tags, link) makes it straightforward to map GitHub issue fields → markdown generation in Hugo via GitHub Action.
- **Accessibility is non-negotiable:** Flesch-Kincaid grade 8–9 language and H1–H3 heading hierarchy ensure Gymnasium pupils and parents (not just teachers) can engage with the site.
- **Policy risk mitigation:** Explicitly excluding made-up school rules or facts in draft content protects against publishing inaccuracies; stakeholder review upstream is faster than post-hoc edits.
- **German-first navigation labels:** Using consistent German labels (Entdecke / Erkunde / Lerne; Zu den [X] →) reduces confusion for non-English-native audiences and reinforces brand tone.

### 2026-05-31: Content Framework Integrated into Hugo v1 ✓

**Implementation status:** ✅ Complete  
**Commit:** 85c0032

**How the framework was applied:**
- **Sample flagging:** All placeholder content marked with `sample: true` in front matter + homepage banner controlled by `site.Params.sampleSite`
- **Persona-aware tagging:** News posts and idea cards tagged with `audiences: ["Schüler·innen", "Lehrkräfte", "Eltern"]` for later segmentation
- **News structure ready:** Front matter maps to GitHub issue form fields (title, abstract, category, audience) → workflow can auto-generate markdown in Phase 2
- **YAML-based editing:** Content editors update idea cards and news via YAML front matter, no HTML required → lowers barrier for school contributors
- **Three-section homepage:** Value props for pupils/teachers/parents presented immediately below hero

**Editor onboarding complete:**
- README.md includes instructions for adding news posts and idea cards
- Non-technical contributors can edit via GitHub Web UI + preview without git
- Moderation gate (Phase 1: manual `sample: false` flag; Phase 2: automated approval workflow)

