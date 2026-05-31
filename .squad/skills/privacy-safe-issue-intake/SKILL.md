# Skill: Privacy-Safe Issue Intake

## When to Use

When designing GitHub issue templates that feed into automated pipelines (news, blog posts, content submission) on a public repository — especially for German/EU audiences or sites serving minors.

## Rules

1. **Never request PII in issue fields.** No name, email, phone, address, or identifiers.
2. **Add a visible privacy notice** in the template body: "Do not include personal data."
3. **Require a moderation step** (manual label, PR review, or approval) before content reaches the live site.
4. **Treat all issue content as untrusted input.** Sanitize before rendering (XSS, link injection).
5. **External links from user input** must be rendered with `rel="noopener noreferrer"`.
6. **Audit trail:** Issues are immutable public records. Assume anything written will be indexed by search engines within minutes.

## Template Design Pattern

```yaml
name: "News Item"
description: "Submit a news/link item for the site"
labels: ["news-submission"]
body:
  - type: markdown
    attributes:
      value: |
        ⚠️ **Datenschutz-Hinweis:** Geben Sie keine personenbezogenen Daten ein.
        Dieses Issue ist öffentlich sichtbar.
  - type: input
    id: title
    attributes:
      label: "Titel"
      placeholder: "Kurzer, beschreibender Titel"
    validations:
      required: true
  - type: textarea
    id: abstract
    attributes:
      label: "Zusammenfassung"
      description: "2-3 Sätze, worum es geht"
    validations:
      required: true
  - type: input
    id: link
    attributes:
      label: "Link (URL)"
      placeholder: "https://..."
  - type: dropdown
    id: category
    attributes:
      label: "Kategorie"
      options:
        - KI / Künstliche Intelligenz
        - Informatik allgemein
        - Wettbewerbe & Events
        - Werkzeuge & Tutorials
    validations:
      required: true
  - type: dropdown
    id: audience
    attributes:
      label: "Zielgruppe"
      options:
        - Schüler:innen
        - Lehrkräfte
        - Eltern
        - Alle
    validations:
      required: true
```

## Anti-Patterns

- ❌ Free-text "Your name" or "Contact email" fields
- ❌ Auto-publishing issue content without review
- ❌ Rendering raw markdown from issues without sanitization
- ❌ Storing issue-submitter GitHub usernames as "author" on the public site
