---
name: "Issue-Driven News Publishing for Hugo + GitHub Pages"
category: "Content Management"
audience: "Teams maintaining Hugo news feeds on GitHub Pages"
date: 2026-06-01
---

# Issue-Driven News Publishing for Hugo + GitHub Pages

## Pattern

Use GitHub Issues as a lightweight intake queue for non-technical contributors to propose news, blog posts, or announcements. A GitHub Action validates an approved issue, transforms it to Hugo Markdown, and opens a pull request. Publishing happens only after PR review and merge.

**Best for:** Teams without dedicated DevOps; Hugo sites hosted on GitHub Pages; school/community sites where privacy review matters.

## How It Works

1. **Issue template** (`.github/ISSUE_TEMPLATE/news.yml`):
   - Defines required metadata fields: title, summary, target audience, category, relevance, no-PII confirmation.
   - Separates `Zielgruppe` from `Thema/Kategorie` to avoid confusing filter semantics.
   - Includes German examples, visible character limits, and clear warnings against names, emails, phone numbers, addresses, photos, or private data.

2. **GitHub Actions workflow** triggers on a maintainer-only approval label such as `freigegeben`:
   - Validates template compliance, allowed choices, date format, and required privacy acknowledgement.
   - Checks privacy red flags such as email/phone patterns.
   - Creates `content/news/YYYY-MM-DD-slug.md` with sanitized front matter/content.
   - Opens a pull request instead of publishing directly from the label.

3. **Review and publish**:
   - Editors review the generated Markdown, external links, categories, and audience filters in the PR.
   - Merge triggers the existing GitHub Pages deploy workflow.
   - Rollback is a normal Git revert or a PR deleting the generated Markdown file.

## Guardrails

```yaml
# GitHub Actions validation pseudocode
- Require issue label: news-vorschlag
- Require approval label: freigegeben
- Require no-PII checkbox checked
- Check title and summary length
- Check category/audience are in predefined lists
- Reject email and phone-number patterns
- Sanitize Markdown/front matter before writing files
- Open PR; do not publish directly
```

## Trade-offs

### Advantages
- Non-developers can propose news without `git` knowledge.
- GitHub issue history and PR review provide an audit trail.
- GitHub notifications work as editorial alerts via watching, assignment, mentions, CODEOWNERS, or review requests.
- No external mail, CMS, analytics, or tracking infrastructure is required.

### Risks (Mitigation Required)
- **Validation failures:** Comment on the issue or rely on failed workflow notifications; keep the error actionable.
- **Metadata typos:** Use dropdowns/checkboxes, not free text, for filter values.
- **External link risk:** Require editorial review before merging the PR.
- **Editing complexity:** Fix generated content in the PR or update the issue and re-trigger by re-labeling.

## German Language Note

Use concise German labels and helper text:

```markdown
**Titel:** KI-Begriffe einfach erklärt
**Kurzbeschreibung:** Max. 220 Zeichen.
**Zielgruppe:** Schüler:innen / Eltern / Lehrkräfte / SEB / Allgemein
**Thema/Kategorie:** KI / Informatik / Veranstaltung / Wettbewerb / Material / Empfehlung / Hinweis / Sonstiges
**Datenschutz:** Keine Namen, E-Mails, Telefonnummern, Adressen, Fotos oder privaten Angaben.
```

## Checklist Before Launch

- [ ] Issue template exists and is enforced by workflow validation.
- [ ] Approval label is documented and maintainers know who may apply it.
- [ ] Workflow opens a PR, not a direct commit to the publishing branch.
- [ ] Generated content has sanitized front matter and no raw HTML.
- [ ] External links are reviewed before merge.
- [ ] Approver notifications stay GitHub-native.
- [ ] Rollback process is documented.
