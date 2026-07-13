# AI SEO / AEO / GEO Task

Date: 2026-07-08

Target URL: https://www.strique.io/

Checklist: `docs/checklists/ai-seo-aeo-geo-checklist.md`

Status: fix

## Evidence Used

- Fresh Playwright homepage render.
- Fresh Firecrawl homepage extraction.
- Raw HTML JSON-LD check.
- Existing matrix: `brands/strique/audits/ai-seo-aeo-geo-google-visible-audit.json`.

## Coverage

Stored item-level matrix:

- Items: 133
- Pass: 96
- Fail: 9
- Not applicable: 28
- Blocked in stored matrix: 0

Current-session blockers:

- Fresh GSC and live AI-answer visibility sources were not connected.

## Findings

### Extractable Homepage Content Exists

The homepage has extractable title, description, H1, H2s, FAQ content, case-study proof points, CTAs, trust signals, and internal links.

### Structured Data Exists But Needs Validation

Raw HTML includes two `application/ld+json` scripts with Organization and SoftwareApplication-style entities. Firecrawl also reports schema types. A dedicated schema/rich result validator was not run in this pass.

### Accessibility And Answerability Issues Remain

Stored matrices flag heading semantics, accessible controls, blocking overlays, and machine-readability issues across the site.

## Next Task

Validate schema fields, confirm ratings/review claims are source-backed, and rerun rendered accessibility checks across the sitemap.
