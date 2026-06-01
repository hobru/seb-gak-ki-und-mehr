# Brand: GitHub Pages Deployment for New Repository

**Date:** 2026-06-01T10:42:47.128+02:00  
**Status:** Implemented  
**Owner:** Brand  

## Decision

Publish the Hugo site through GitHub Actions Pages at `https://hobru.github.io/seb-gak-ki-und-mehr/` while keeping the current `master` branch.

## Rationale

Holger created the GitHub repository and requested a first GitHub Pages preview before later custom-domain work. The existing Hugo + GitHub Actions Pages architecture already fits this, and the workflow triggers both `main` and `master`, so no branch rename is required.

## Implementation

- `hugo.toml` uses the GitHub Pages project URL as `baseURL`.
- `.github/workflows/deploy.yml` builds Hugo on pushes to `main` or `master` and deploys using GitHub Actions Pages permissions/artifacts.
- The Hugo setup action is pinned to the resolved commit behind `peaceiris/actions-hugo` tag `v3.0.0`.
- `README.md` documents the project URL, local production build command, and the required GitHub Pages source setting.

## Verification

Local validation command: `hugo --minify --baseURL "https://hobru.github.io/seb-gak-ki-und-mehr/"`
