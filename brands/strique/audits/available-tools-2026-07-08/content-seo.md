# Content SEO Task

Date: 2026-07-08

Target URL: https://www.strique.io/

Checklist: `docs/checklists/content-seo-checklist.md`

Status: fix

## Evidence Used

- Fresh Playwright homepage render.
- Fresh Firecrawl homepage extraction.
- Existing matrix: `brands/strique/audits/content-seo-google-visible-audit.json`.
- Section 7 note: `brands/strique/audits/content-seo-section-7-homepage-serp-promise-2026-07-08.md`.

## Coverage

Stored item-level matrix:

- Items: 173
- Pass: 146
- Fail: 12
- Not applicable: 15
- Blocked in stored matrix: 0

Current-session blocker:

- GSC was not refreshed in this session, so CTR, query intent, and search-result mismatch checks remain partial.

## Findings

### Homepage Content Signals Are Visible

The homepage has a clear title, meta description, H1, supporting H2s, CTAs, case-study links, FAQ content, trust signals, and social/legal links.

### SERP Promise Needs Follow-Up

Firecrawl/search extraction can serialize the hero H1 as `BrandsThat`, while Playwright sees the rendered H1 correctly. This is saved in the Section 7 note.

### Search Intent Needs Primary Query

The next content SEO step needs the primary query to judge against. Candidate query themes are `agentic AI marketing platform`, `AI marketing agent`, and `marketing agents for ecommerce brands`.

## Next Task

Pick the primary homepage query, reconnect GSC, then review query/page impressions, CTR, average position, and title/snippet alignment.
