# One-Eyed Willy History

## Seed Context

- **User:** Holger Bruchelt
- **Project:** German-first website for pupils, teachers, and parents of Gymnasium am Kaiserdom Speyer.
- **Focus:** Computer science and AI tutorials, guidance, ideas, and latest-news area via GitHub issues.
- **Technology:** Hugo + GitHub Pages
- **Key concerns:** Stakeholder fit, maintainability, usability, security, privacy, PII protection.

## Current Session (2026-06-01)

### Neuigkeiten MVP: Privacy & Security Constraints (Public GitHub Issue Intake)

**Verdict:** Public GitHub issues approved for news submissions WITH strict moderation gate.

**Binding Constraints:**
- Form must not request: name, email, phone, class, role, contact preference
- Required fields: public title, public short description, categories, no-PII checkbox
- Optional fields: details (max 1000 chars), external link (HTTPS only, max 300 chars)
- Initial label: 
ews-vorschlag; publishing label: maintainer-only reigegeben
- No direct publication from issue creation; validation + manual approval required
- Generated Markdown: sanitized (no GitHub metadata, no unapproved text, escaped YAML)
- External links: HTTPS, redirect review, render with 	arget="_blank" + el="noopener noreferrer"
- Issue-triggered workflows: no direct contents: write; use PR gate or maintainer-approved flow
- Approver notifications: GitHub-native only (issue assignment, mentions, PR reviews); no external SMTP

**Required Warning Text (German):**
> **Datenschutzhinweis:** Dieses GitHub-Issue ist öffentlich sichtbar. Bitte tragen Sie keine personenbezogenen Daten ein...

**Required Checkbox:**
> Ich bestätige, dass mein Vorschlag keine personenbezogenen Daten oder vertraulichen Schul-/SEB-Informationen enthält.

**Approval Checklist for Maintainers:**
1. No PII or confidential school/SEB information
2. Title/summary suitable for public display
3. Category from allow-list
4. External link reviewed and safe
5. Generated Markdown preview reviewed
6. reigegeben applied by maintainer only

## Previous Sessions Archive

See history-archive.md for earlier decisions (2026-05-31 and earlier).
