---
name: "Issue-Driven News Publishing for Static Sites"
category: "Content Management"
audience: "Teams maintaining blogs/news feeds on GitHub + Jekyll"
date: 2026-05-31
---

# Issue-Driven News Publishing for Static Sites

## Pattern

Use GitHub Issues as a lightweight CMS for non-technical contributors to publish news, blog posts, or announcements to a static site. A bot (GitHub Actions) validates the issue, transforms it to Markdown, and triggers a site rebuild.

**Best for:** Teams without dedicated DevOps; sites hosted on GitHub Pages; non-technical content creators.

## How It Works

1. **Issue template** (`.github/ISSUE_TEMPLATE/news.md`):
   - Defines required metadata fields (title, date, summary, link, audience)
   - Includes examples and validation rules
   - Prevents typos and incomplete posts

2. **GitHub Actions workflow** triggers on issue label `news:publish`:
   - Validates template compliance (required fields, max/min lengths)
   - Checks accessibility red flags (e.g., "click here" link text)
   - Generates preview URL so editor can review
   - Only publishes if validation passes

3. **Bot transforms issue to Jekyll post**:
   - Creates `/news/YYYY-MM-DD-title.md` with proper front-matter
   - Links back to source issue for audit trail
   - Rebases site; new post appears on homepage within 5 minutes

4. **Rollback via issue reversion** (if needed):
   - Edit the GitHub issue → bot re-publishes automatically
   - Or delete the generated `.md` file + trigger rebuild

## Accessibility Guardrails (Critical!)

Add these checks to your bot to prevent non-technical contributors from breaking WCAG compliance:

```yaml
# GitHub Actions validation pseudocode
- Check if link text is descriptive (not "click here", "read more", "link")
- Check if summary is ≤ 200 characters
- Check if category is in predefined list (enum)
- Warn if title has ALL CAPS (accessibility: hard to read for dyslexic users)
- Flag missing audience checkboxes (who is this for?)
```

## Trade-offs

### Advantages
- Non-developers can publish without `git` knowledge
- Version history built-in (issue edit history)
- Minimal infrastructure overhead
- GitHub notifications work as editorial alerts

### Risks (Mitigation Required)
- **Bot failures:** If validation fails, where does the error message go? → Set up Slack/Teams alerts
- **Metadata typos:** "Pupil" vs. "pupil" vs. "pupils" breaks filtering → Use checkboxes, not text fields
- **No preview before publish:** Contributor can't see rendered HTML → Bot generates preview link; editor clicks before approving
- **Editing complexity:** Fixing a typo requires editing issue + re-triggering bot → Document process clearly

## German Language Note

For German-language sites, adapt the issue template to use German field names and examples:

```markdown
**Datum:** 2026-05-31
**Kategorie:** [Informatik / KI / Allgemeines]
**Zielgruppe:** [ ] Schüler [ ] Lehrer [ ] Eltern
**Zusammenfassung (max. 200 Zeichen):**
```

## Minimal Implementation

If a bot feels like overkill, use **Markdown files instead:**

1. Contributor copies `_template_news.md` → `_posts/2026-05-31-title.md`
2. Edits locally, previews with `jekyll serve`
3. Submits pull request (one-step review)
4. Merge triggers auto-publish

**Trade-off:** Requires `git` and local Ruby setup; but eliminates bot complexity.

## Checklist Before Launch

- [ ] Issue template exists and is enforced
- [ ] Bot validates metadata (no typos, no empty fields)
- [ ] Bot checks accessibility rules (link text, capitalization, etc.)
- [ ] Preview link generated for manual review
- [ ] Failure notifications go to Slack/Teams (or email)
- [ ] Contributors trained on template & process
- [ ] Rollback process documented
- [ ] Monthly audit of published posts (accessibility, accuracy)

## Related

- GitHub Issue templates: https://docs.github.com/en/communities/using-templates-to-encourage-useful-issues-and-pull-requests
- GitHub Actions workflows: https://docs.github.com/en/actions
- Jekyll + GitHub Pages: https://docs.github.com/en/pages/setting-up-a-github-pages-site-with-jekyll

