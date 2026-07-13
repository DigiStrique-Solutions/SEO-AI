# Generic On-Page SEO Task

Date: 2026-07-08

Target URL: https://www.strique.io/

Checklist: `docs/checklists/generic-on-page-seo-checklist.md`

Status: fix

## Evidence Used

- Fresh Playwright homepage render.
- Fresh Firecrawl homepage extraction.
- Fresh `robots.txt` and `sitemap.xml` checks.
- Existing matrix: `brands/strique/audits/generic-on-page-google-visible-audit.json`.

## Coverage

Stored item-level matrix:

- Items: 381
- Pass: 255
- Fail: 89
- Not applicable: 37
- Blocked in stored matrix: 0

Current-session blocker:

- GSC and GA4 were not refreshed in this session.

## Findings

### Homepage Basics Pass

The homepage is indexable, returns `200`, has canonical `https://www.strique.io/`, has a title and meta description, and appears in `sitemap.xml`.

### Sitewide Template Issues Remain

The stored matrix flags sitewide issues around H1 usage, canonical/sitemap mismatches, image alt handling, performance, and mobile accessibility.

Fresh Playwright shows the homepage itself currently renders one H1, so the H1 issue needs a fresh sitewide crawl before changing homepage code.

## Next Task

Refresh a Playwright or Firecrawl crawl across the 51 sitemap URLs and isolate which pages still fail H1, canonical, sitemap, image alt, performance, and mobile tap-target checks.
