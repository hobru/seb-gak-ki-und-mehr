---
name: "local-brand-assets"
description: "Use locally stored institutional brand assets without weakening SEB/non-official framing"
domain: "hugo-static-site"
confidence: "medium"
source: "brand-homepage-logo"
---

## Pattern

When adding official school or partner branding to this Hugo site:

1. Prefer a local copy under `static/images/` over hotlinking.
2. Add intrinsic `width` and `height` attributes to avoid layout shift.
3. Use descriptive alt text for meaningful logos.
4. If linking externally, use `target="_blank" rel="noopener noreferrer"`.
5. Keep nearby copy explicit that this is a Schulelternbeirat initiative, not the official school website.
6. When a stakeholder provides a temporary root-level asset, move/copy it into `static/images/`, update template references to that local file, and remove the root temporary copy.

## Key paths

- Homepage template: `layouts/index.html`
- Main stylesheet: `static/css/style.css`
- Static images: `static/images/`
- Current homepage GAK logo: `static/images/gak-seb-logo.jpg`
