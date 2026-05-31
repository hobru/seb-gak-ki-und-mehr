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

### SEB Ownership Reframing (2026-05-31)

**Context:** User clarified that the site is created by the Schulelternbeirat (SEB) des Gymnasiums am Kaiserdom, not official school communication. Site must be explicitly repositioned to reflect this independent, parent-led initiative.

**Guidance produced:** `.squad/decisions/inbox/mouth-seb-positioning.md`

**Key learnings:**
- **Ownership clarity prevents reputational risk:** Explicitly naming SEB in hero, footer, logo, and README avoids any impression of false school authority
- **Legal distinction matters:** SEB = independent parent council; communications are parent-association output, not school policy
- **Transparency builds trust:** Visitors immediately understand who authored content (parents, not school bureaucracy)
- **Multi-touchpoint reinforcement needed:** Hero + footer + logo + legal pages + config all must consistently reference SEB to avoid contradictory messaging
- **Persona structure survives reframe:** Three audiences (pupils/teachers/parents) and three content pillars remain effective; only attribution language changes
- **Phrases to audit:** Content claims like "Finde Anregungen für Unterricht" (implies school authority) should become "Entdecke Anregungen... vom Schulelternbeirat" (signals parent sourcing)

### Real Content Research & Draft (2026-05-31)

**Requested by:** Holger Bruchelt | **User:** Mouth (German Content Editor)

**Scope:** Replace sample content in two sections with real, actionable German-language resources for pupils, teachers, and parents.

**Deliverables:**
- **Draft files** created: `DRAFT_informatik_index.md`, `DRAFT_ki_index.md` (structured replacement copy ready for Brand to integrate)
- **Research document** created: `.squad/decisions/inbox/mouth-real-content-research.md` (source URLs, curated link lists, tone samples, approvals/blockers)
- **Content strategy:**
  - No verbatim copying from FMSG or KI-an-der-Schule; paraphrase + link + cite
  - Eight carefully selected external links per section (verified, live, German, school-appropriate, multi-audience)
  - Three tone samples provided (parent-friendly, student-practical, teacher-actionable)
  - Clear delineation: Informatik (FMSG-inspired parent safety + practical student tools) | KI (hobru-inspired practical guide + responsibility framework)

**Key decisions made:**
- **Informatik section:** Six idea cards (HTML starter, data viz, media literacy, teacher tools checklist, video/podcast production, parent explainer); parent FAQ added
- **KI section:** Six idea cards (prompt skills, critical evaluation, glossary, home support, data privacy, responsibility framework); six leitfragen for reflection included
- **Link curation:** Serlo, openHPI, BWINF for students | Medienkompetenzblog for teachers | klicksafe, Schau Hin!, Internet-ABC for parents | telli, ChatGPT, NotebookLM, Perplexity, KMK for KI topics

**Approvals pending:**
1. Parent link baseline (are klicksafe/Schau Hin!/Internet-ABC sufficient, or does GAK need school-specific FAQ?)
2. KI tool endorsement (telli as "official" vs. ChatGPT/Perplexity as "research tools"?)
3. Teacher curriculum mapping (do Informatik cards match actual Informatik syllabi? Verify with Andy/teachers in Phase 2)

**Tone/style learnings:**
- Parents respond to *concerns* (safety, learning outcomes, support pathways) not *features*
- Students prefer *concrete examples* (ChatGPT prompt tips) over *abstract concepts* (LLM definitions)
- Teachers need *actionable specificity* (grade levels, time commitments, DSGVO compliance) + *curriculum guardrails*
- Accessibility target (Flesch-Kincaid Grade 8–9) met in all drafts; heading hierarchy H1–H3 maintained

**Phase 2 follow-ups:**
- Parent FAQ creation (based on first month's questions)
- Quarterly link refresh (404 checks, new resources, privacy policy changes)
- Teacher audit of Informatik cards against actual syllabi (Andy coordination)
- Feedback loop from GitHub issues

**Status:** Ready for Brand integration. DRAFT files are fully structured; copy is ready-to-publish (set `sample: false` once stakeholder approvals confirmed).

