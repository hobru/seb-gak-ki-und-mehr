# Stef History

## Seed Context

- **User:** Holger Bruchelt
- **Project:** German-first website for pupils, teachers, and parents of Gymnasium am Kaiserdom Speyer.
- **Focus:** Computer science and AI tutorials, guidance, ideas, and a latest-news area that can be updated easily, ideally via GitHub issues.
- **Technology:** Not yet selected, but must run on GitHub.
- **Key concerns:** Stakeholder fit, maintainability, usability, security, newsletter privacy, and PII.

## Learnings

### 2026-05-31: Homepage Parent Perspective Review

**Key Finding:** Parents need three immediate answers on the homepage: (1) What is my child learning? (2) Is this safe? (3) How do I stay informed? A parent-first homepage leads with value in plain German, embeds trust signals early (legal, teacher attribution), and provides concrete FAQ answers within 10 seconds.

**Recommendations delivered:**
1. Lead with plain-German value statement + 3–4 relatable examples (not buzzwords)
2. Build explicit trust signals: school name, teacher attribution, Datenschutz link (top fold)
3. Reframe news section as "Aktuelle Inhalte" with frequency stamp and summaries
4. Create a 5–7 item FAQ addressing unstated parental concerns (screen time, privacy, career, support)
5. Add low-friction "stay informed" option (checkboxes, not mandatory signup)

**Sample content ideas (German):**
- Tutorial: "ChatGPT einfach erklärt" (What, risks, responsible use)
- Safety guide: "5 Tipps gegen Cybermobbing und Phishing" (Actionable, not fear-based)
- Career awareness: "Informatik-Berufe und warum diese Fertigkeit wichtig ist" (Future relevance)

**Impact:** Clear parent engagement pathway; trust established early; reduced friction for support and updates.

### 2026-05-31: Parent Review Integrated into Hugo v1 ✓

**Implementation status:** ✅ Complete  
**Commit:** 85c0032

**How Stef's recommendations were applied:**
- **Plain-German value props:** Homepage hero and quick-nav cards use accessible, family-friendly language (no jargon)
- **Trust signals present:** School name & logo anchor at top; footer includes Impressum + Datenschutzerklärung links
- **News section labeled:** "Neuigkeiten" with date and category badges; 3 sample posts show current content
- **Legal pages ready:** Impressum + Datenschutzerklärung created (as DSGVO-compliant placeholders; real content from school legal team required)
- **Metadata for future FAQ:** Content structure supports adding FAQ section (deferred pending Holger confirmation of key topics)

**For Phase 2 parent engagement:**
- Populate FAQ with school-approved answers (5–7 key parent questions)
- Add "Stay Informed" newsletter opt-in with GDPR review (One-Eyed Willy)
- Test homepage with 1–2 parent users (ages 35–50, non-technical)

