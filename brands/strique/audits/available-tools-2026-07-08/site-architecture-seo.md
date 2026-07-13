# Site Architecture SEO Task

Date: 2026-07-08

Target URL: https://www.strique.io/

Checklist: `docs/checklists/site-architecture-seo-checklist.md`

Status: fix

## Evidence Used

- Fresh Playwright homepage render.
- Fresh `robots.txt` check.
- Fresh `sitemap.xml` check.
- Existing matrix: `brands/strique/audits/site-architecture-google-visible-audit.json`.

## Coverage

Stored item-level matrix:

- Items: 218
- Pass: 163
- Fail: 37
- Not applicable: 18
- Blocked in stored matrix: 0

Current-session blockers:

- GSC, GA4, CMS/code, and server logs were not refreshed in this session.

## Findings

### Sitemap And Robots Are Present

`robots.txt` allows `/`, blocks `/thank-you` and `/api/`, and declares `https://www.strique.io/sitemap.xml`. The sitemap returns `200` and includes 51 URLs.

### Canonical And Sitemap Mismatches Need Cleanup

Stored matrices report failures where sitemap inclusion and canonical targets do not align for some discovered URLs.

## Next Task

Run a fresh crawl across the sitemap URLs and create a URL-level table with status, canonical, indexability, sitemap inclusion, page type, and internal link count.
