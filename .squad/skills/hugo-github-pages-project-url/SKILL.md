---
name: "hugo-github-pages-project-url"
description: "Configure Hugo for GitHub Pages project sites with repository subpaths"
domain: "hugo-static-site"
confidence: "medium"
source: "brand-github-pages-deploy"
---

## Context

Use this when a Hugo site is published as a GitHub Pages project site, for example `https://owner.github.io/repository/`, rather than as an organization/user root site.

## Patterns

1. Set `baseURL` in `hugo.toml` to the full project URL with a trailing slash.
2. In GitHub Actions Pages workflows, run Hugo with `--baseURL` or `HUGO_BASEURL` from `actions/configure-pages` so future custom domains are picked up automatically.
3. Keep workflow triggers aligned with the current default branch; if the project still uses `master`, include `master`.
4. Build locally with the same project URL before pushing:
   ```bash
   hugo --minify --baseURL "https://owner.github.io/repository/"
   ```
5. Document that repository Settings → Pages must use “GitHub Actions” as the source.
6. Audit generated HTML for root-relative links after changing `baseURL`; template strings like `{{ "/path/" | relURL }}` can still render as `/path/` and should use `{{ "path/" | relURL }}` or page/menu permalinks for project sites.
7. When SHA-pinning Actions, verify annotated tags resolve to a commit SHA and pin the commit object, not the tag object or a copied/truncated hash.

## Examples

- Config: `baseURL = "https://hobru.github.io/seb-gak-ki-und-mehr/"`
- Local validation: `hugo --minify --baseURL "https://hobru.github.io/seb-gak-ki-und-mehr/"`
- Workflow trigger: `branches: ["main", "master"]` while the default branch is still `master`.
- Template links: prefer `{{ "informatik/" | relURL }}` over `{{ "/informatik/" | relURL }}` for project Pages paths.
- Action pin: `peaceiris/actions-hugo@75d2e84710de30f6ff7268e08f310b60ef14033f` is the commit behind tag `v3.0.0`.

## Anti-Patterns

- Do not leave `baseURL = "/"` for a project Pages URL unless every generated link has been audited.
- Do not assume `relURL` fixes strings that begin with `/`; verify generated `href` and `src` attributes under the repository subpath.
- Do not trust a pinned action hash until a real workflow run resolves it successfully.
- Do not rename `master` to `main` just to satisfy a workflow if the user did not request a branch migration.
- Do not switch to a third-party deploy service for a basic GitHub Pages launch.
