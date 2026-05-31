# Brand KI Bottom UX Decision

**Date:** 2026-05-31
**Proposer:** Brand

## Decision
Render the KI page bottom sections (audience guidance and responsible-use Leitfragen) from structured front matter into the same card/section system used above the page.

## Rationale
The KI page already teaches users through scannable cards, icon-led section headings, and compact grids. Keeping the bottom guidance in plain Markdown made important SEB framing feel less actionable and visually weaker. Structured front matter keeps future edits simple while preserving consistent UX.

## Scope
Applies to `content/ki/_index.md`, `layouts/ki/list.html`, and KI-specific CSS only. No broader redesign or new service dependency.
