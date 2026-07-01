---
title: 3. Indexability
sidebar_position: 8
---

# 3. Indexability

Checklist: `generic-on-page-seo`

Source: `docs/checklists/generic-on-page-seo-checklist.md`

This page explains every checklist item in this section. Each item should still be verified with evidence before it is marked `pass` or `fail`.

## Item 1

Item ID: `generic-on-page-seo.3-indexability.07d645b3`

Original checklist item: The page returns a valid indexable response when it should rank.

### What It Means

Confirm whether the audited scope satisfies this requirement: "The page returns a valid indexable response when it should rank." In practice, this means the reviewer needs concrete evidence, not a general impression.

### Why It Affects SEO

Intent alignment affects whether the page deserves to show for the target query. This check keeps the page focused on the searcher's job instead of only matching keywords.

### How To Verify

1. Identify the exact URL, template, brand workspace, connector account, or page group in scope.
2. Collect evidence from: GSC, Firecrawl, Playwright, CMS/code, OSS, Shopify or CMS, GMC.
3. Compare visible page content, structured data, and feed or platform values for consistency.
4. Record pass, fail, not_applicable, or not_checked_blocked in the audit matrix with an artifact reference.

### Evidence Sources

GSC, Firecrawl, Playwright, CMS/code, OSS, Shopify or CMS, GMC

### Pass Criteria

The item is verified as true for the scoped URL, template, brand, connector account, or page group, and the audit row includes a specific evidence source and artifact reference.

### Fail Criteria

The evidence shows the requirement is missing, inconsistent, inaccurate, inaccessible, risky, or materially incomplete for the audited scope.

### Common Fix

Fix the product source of truth, page template, schema, or feed mapping so product data is complete and consistent.

### Owner

merchandising, marketing, or engineering

### Notes

If the required connector, browser rendering, platform export, or human context is unavailable, mark the audit row as `not_checked_blocked` and name the missing access or artifact.

## Item 2

Item ID: `generic-on-page-seo.3-indexability.bb5de822`

Original checklist item: The page does not have `noindex` in a robots meta tag or X-Robots-Tag header unless intentionally excluded.

### What It Means

Confirm whether the audited scope satisfies this requirement: "The page does not have `noindex` in a robots meta tag or X-Robots-Tag header unless intentionally excluded." In practice, this means the reviewer needs concrete evidence, not a general impression.

### Why It Affects SEO

Intent alignment affects whether the page deserves to show for the target query. This check keeps the page focused on the searcher's job instead of only matching keywords. Search engines cannot rank what they cannot discover, render, canonicalize, or keep indexable. This check protects crawl access, index coverage, and canonical signal quality.

### How To Verify

1. Identify the exact URL, template, brand workspace, connector account, or page group in scope.
2. Collect evidence from: GSC, Firecrawl, Playwright, CMS/code, OSS.
3. Record pass, fail, not_applicable, or not_checked_blocked in the audit matrix with an artifact reference.

### Evidence Sources

GSC, Firecrawl, Playwright, CMS/code, OSS

### Pass Criteria

The item is verified as true for the scoped URL, template, brand, connector account, or page group, and the audit row includes a specific evidence source and artifact reference.

### Fail Criteria

The evidence shows the requirement is missing, inconsistent, inaccurate, inaccessible, risky, or materially incomplete for the audited scope.

### Common Fix

Update the template, metadata, server response, robots policy, sitemap, or structured data source, then rerun rendered and crawl checks.

### Owner

engineering

### Notes

If the required connector, browser rendering, platform export, or human context is unavailable, mark the audit row as `not_checked_blocked` and name the missing access or artifact.

## Item 3

Item ID: `generic-on-page-seo.3-indexability.515e1d17`

Original checklist item: Thank-you, confirmation, checkout success, form success, unsubscribe, login, password reset, account, cart, internal search result, and other utility pages are reviewed for whether they should rank.

### What It Means

Confirm whether the audited scope satisfies this requirement: "Thank-you, confirmation, checkout success, form success, unsubscribe, login, password reset, account, cart, internal search result, and other utility pages are reviewed for whether they should rank." In practice, this means the reviewer needs concrete evidence, not a general impression.

### Why It Affects SEO

Intent alignment affects whether the page deserves to show for the target query. This check keeps the page focused on the searcher's job instead of only matching keywords.

### How To Verify

1. Identify the exact URL, template, brand workspace, connector account, or page group in scope.
2. Collect evidence from: GSC, Firecrawl, Playwright, CMS/code, OSS.
3. Record pass, fail, not_applicable, or not_checked_blocked in the audit matrix with an artifact reference.

### Evidence Sources

GSC, Firecrawl, Playwright, CMS/code, OSS

### Pass Criteria

The item is verified as true for the scoped URL, template, brand, connector account, or page group, and the audit row includes a specific evidence source and artifact reference.

### Fail Criteria

The evidence shows the requirement is missing, inconsistent, inaccurate, inaccessible, risky, or materially incomplete for the audited scope.

### Common Fix

Have content or marketing make the smallest change that satisfies the evidence requirement, then rerun the check.

### Owner

content or marketing

### Notes

If the required connector, browser rendering, platform export, or human context is unavailable, mark the audit row as `not_checked_blocked` and name the missing access or artifact.

## Item 4

Item ID: `generic-on-page-seo.3-indexability.da9a8e9a`

Original checklist item: Utility pages that should not rank use `noindex` through a robots meta tag or X-Robots-Tag header.

### What It Means

Confirm whether the audited scope satisfies this requirement: "Utility pages that should not rank use `noindex` through a robots meta tag or X-Robots-Tag header." In practice, this means the reviewer needs concrete evidence, not a general impression.

### Why It Affects SEO

Intent alignment affects whether the page deserves to show for the target query. This check keeps the page focused on the searcher's job instead of only matching keywords. Search engines cannot rank what they cannot discover, render, canonicalize, or keep indexable. This check protects crawl access, index coverage, and canonical signal quality.

### How To Verify

1. Identify the exact URL, template, brand workspace, connector account, or page group in scope.
2. Collect evidence from: GSC, Firecrawl, Playwright, CMS/code, OSS.
3. Record pass, fail, not_applicable, or not_checked_blocked in the audit matrix with an artifact reference.

### Evidence Sources

GSC, Firecrawl, Playwright, CMS/code, OSS

### Pass Criteria

The item is verified as true for the scoped URL, template, brand, connector account, or page group, and the audit row includes a specific evidence source and artifact reference.

### Fail Criteria

The evidence shows the requirement is missing, inconsistent, inaccurate, inaccessible, risky, or materially incomplete for the audited scope.

### Common Fix

Update the template, metadata, server response, robots policy, sitemap, or structured data source, then rerun rendered and crawl checks.

### Owner

engineering

### Notes

If the required connector, browser rendering, platform export, or human context is unavailable, mark the audit row as `not_checked_blocked` and name the missing access or artifact.

## Item 5

Item ID: `generic-on-page-seo.3-indexability.63402b9e`

Original checklist item: Utility pages that use `noindex` are not blocked by `robots.txt`, because crawlers must be able to crawl the page to see the `noindex` directive.

### What It Means

Confirm whether the audited scope satisfies this requirement: "Utility pages that use `noindex` are not blocked by `robots.txt`, because crawlers must be able to crawl the page to see the `noindex` directive." In practice, this means the reviewer needs concrete evidence, not a general impression.

### Why It Affects SEO

Intent alignment affects whether the page deserves to show for the target query. This check keeps the page focused on the searcher's job instead of only matching keywords. Search engines cannot rank what they cannot discover, render, canonicalize, or keep indexable. This check protects crawl access, index coverage, and canonical signal quality.

### How To Verify

1. Identify the exact URL, template, brand workspace, connector account, or page group in scope.
2. Collect evidence from: GSC, Firecrawl, Playwright, CMS/code, OSS.
3. Record pass, fail, not_applicable, or not_checked_blocked in the audit matrix with an artifact reference.

### Evidence Sources

GSC, Firecrawl, Playwright, CMS/code, OSS

### Pass Criteria

The item is verified as true for the scoped URL, template, brand, connector account, or page group, and the audit row includes a specific evidence source and artifact reference.

### Fail Criteria

The evidence shows the requirement is missing, inconsistent, inaccurate, inaccessible, risky, or materially incomplete for the audited scope.

### Common Fix

Update the template, metadata, server response, robots policy, sitemap, or structured data source, then rerun rendered and crawl checks.

### Owner

engineering

### Notes

If the required connector, browser rendering, platform export, or human context is unavailable, mark the audit row as `not_checked_blocked` and name the missing access or artifact.

## Item 6

Item ID: `generic-on-page-seo.3-indexability.29490315`

Original checklist item: Utility pages that should not rank are excluded from XML sitemaps and acquisition-focused internal linking.

### What It Means

Confirm whether the audited scope satisfies this requirement: "Utility pages that should not rank are excluded from XML sitemaps and acquisition-focused internal linking." In practice, this means the reviewer needs concrete evidence, not a general impression.

### Why It Affects SEO

Intent alignment affects whether the page deserves to show for the target query. This check keeps the page focused on the searcher's job instead of only matching keywords. Architecture controls how users and crawlers find important pages. Good internal linking helps distribute context, priority, and crawl paths.

### How To Verify

1. Identify the exact URL, template, brand workspace, connector account, or page group in scope.
2. Collect evidence from: GSC, Firecrawl, Playwright, CMS/code, OSS.
3. Record pass, fail, not_applicable, or not_checked_blocked in the audit matrix with an artifact reference.

### Evidence Sources

GSC, Firecrawl, Playwright, CMS/code, OSS

### Pass Criteria

The item is verified as true for the scoped URL, template, brand, connector account, or page group, and the audit row includes a specific evidence source and artifact reference.

### Fail Criteria

The evidence shows the requirement is missing, inconsistent, inaccurate, inaccessible, risky, or materially incomplete for the audited scope.

### Common Fix

Adjust navigation, breadcrumbs, contextual links, or taxonomy so priority pages are reachable and clearly related.

### Owner

content or marketing

### Notes

If the required connector, browser rendering, platform export, or human context is unavailable, mark the audit row as `not_checked_blocked` and name the missing access or artifact.

## Item 7

Item ID: `generic-on-page-seo.3-indexability.a5047554`

Original checklist item: Sensitive utility pages are protected by authentication or authorization. Do not rely on `robots.txt` for privacy or access control.

### What It Means

Confirm whether the audited scope satisfies this requirement: "Sensitive utility pages are protected by authentication or authorization. Do not rely on `robots.txt` for privacy or access control." In practice, this means the reviewer needs concrete evidence, not a general impression.

### Why It Affects SEO

Intent alignment affects whether the page deserves to show for the target query. This check keeps the page focused on the searcher's job instead of only matching keywords. Search engines cannot rank what they cannot discover, render, canonicalize, or keep indexable. This check protects crawl access, index coverage, and canonical signal quality.

### How To Verify

1. Identify the exact URL, template, brand workspace, connector account, or page group in scope.
2. Collect evidence from: GSC, Firecrawl, Playwright, CMS/code, OSS.
3. Record pass, fail, not_applicable, or not_checked_blocked in the audit matrix with an artifact reference.

### Evidence Sources

GSC, Firecrawl, Playwright, CMS/code, OSS

### Pass Criteria

The item is verified as true for the scoped URL, template, brand, connector account, or page group, and the audit row includes a specific evidence source and artifact reference.

### Fail Criteria

The evidence shows the requirement is missing, inconsistent, inaccurate, inaccessible, risky, or materially incomplete for the audited scope.

### Common Fix

Update the template, metadata, server response, robots policy, sitemap, or structured data source, then rerun rendered and crawl checks.

### Owner

engineering

### Notes

If the required connector, browser rendering, platform export, or human context is unavailable, mark the audit row as `not_checked_blocked` and name the missing access or artifact.

## Item 8

Item ID: `generic-on-page-seo.3-indexability.edaaa930`

Original checklist item: The page does not use `nosnippet`, `max-snippet`, `max-image-preview`, or `max-video-preview` in a way that harms the desired search appearance.

### What It Means

Confirm whether the audited scope satisfies this requirement: "The page does not use `nosnippet`, `max-snippet`, `max-image-preview`, or `max-video-preview` in a way that harms the desired search appearance." In practice, this means the reviewer needs concrete evidence, not a general impression.

### Why It Affects SEO

Intent alignment affects whether the page deserves to show for the target query. This check keeps the page focused on the searcher's job instead of only matching keywords. Metadata, headings, and structured data help search systems understand the page and shape how it can appear in results, snippets, rich results, and AI summaries.

### How To Verify

1. Identify the exact URL, template, brand workspace, connector account, or page group in scope.
2. Collect evidence from: GSC, Firecrawl, Playwright, CMS/code, OSS.
3. Use browser-rendered evidence before claiming the item is absent or broken.
4. Record pass, fail, not_applicable, or not_checked_blocked in the audit matrix with an artifact reference.

### Evidence Sources

GSC, Firecrawl, Playwright, CMS/code, OSS

### Pass Criteria

The item is verified as true for the scoped URL, template, brand, connector account, or page group, and the audit row includes a specific evidence source and artifact reference.

### Fail Criteria

The evidence shows the requirement is missing, inconsistent, inaccurate, inaccessible, risky, or materially incomplete for the audited scope.

### Common Fix

Have content or marketing make the smallest change that satisfies the evidence requirement, then rerun the check.

### Owner

content or marketing

### Notes

If the required connector, browser rendering, platform export, or human context is unavailable, mark the audit row as `not_checked_blocked` and name the missing access or artifact.

## Item 9

Item ID: `generic-on-page-seo.3-indexability.448b7ade`

Original checklist item: The canonical URL points to the preferred version of this page.

### What It Means

Confirm whether the audited scope satisfies this requirement: "The canonical URL points to the preferred version of this page." In practice, this means the reviewer needs concrete evidence, not a general impression.

### Why It Affects SEO

Intent alignment affects whether the page deserves to show for the target query. This check keeps the page focused on the searcher's job instead of only matching keywords. Search engines cannot rank what they cannot discover, render, canonicalize, or keep indexable. This check protects crawl access, index coverage, and canonical signal quality.

### How To Verify

1. Identify the exact URL, template, brand workspace, connector account, or page group in scope.
2. Collect evidence from: GSC, Firecrawl, Playwright, CMS/code, OSS.
3. Record pass, fail, not_applicable, or not_checked_blocked in the audit matrix with an artifact reference.

### Evidence Sources

GSC, Firecrawl, Playwright, CMS/code, OSS

### Pass Criteria

The item is verified as true for the scoped URL, template, brand, connector account, or page group, and the audit row includes a specific evidence source and artifact reference.

### Fail Criteria

The evidence shows the requirement is missing, inconsistent, inaccurate, inaccessible, risky, or materially incomplete for the audited scope.

### Common Fix

Update the template, metadata, server response, robots policy, sitemap, or structured data source, then rerun rendered and crawl checks.

### Owner

engineering

### Notes

If the required connector, browser rendering, platform export, or human context is unavailable, mark the audit row as `not_checked_blocked` and name the missing access or artifact.

## Item 10

Item ID: `generic-on-page-seo.3-indexability.60a4df0e`

Original checklist item: Unique pages use self-referencing canonicals.

### What It Means

Confirm whether the audited scope satisfies this requirement: "Unique pages use self-referencing canonicals." In practice, this means the reviewer needs concrete evidence, not a general impression.

### Why It Affects SEO

Intent alignment affects whether the page deserves to show for the target query. This check keeps the page focused on the searcher's job instead of only matching keywords.

### How To Verify

1. Identify the exact URL, template, brand workspace, connector account, or page group in scope.
2. Collect evidence from: GSC, Firecrawl, Playwright, CMS/code, OSS.
3. Record pass, fail, not_applicable, or not_checked_blocked in the audit matrix with an artifact reference.

### Evidence Sources

GSC, Firecrawl, Playwright, CMS/code, OSS

### Pass Criteria

The item is verified as true for the scoped URL, template, brand, connector account, or page group, and the audit row includes a specific evidence source and artifact reference.

### Fail Criteria

The evidence shows the requirement is missing, inconsistent, inaccurate, inaccessible, risky, or materially incomplete for the audited scope.

### Common Fix

Have content or marketing make the smallest change that satisfies the evidence requirement, then rerun the check.

### Owner

content or marketing

### Notes

If the required connector, browser rendering, platform export, or human context is unavailable, mark the audit row as `not_checked_blocked` and name the missing access or artifact.

## Item 11

Item ID: `generic-on-page-seo.3-indexability.29589b2c`

Original checklist item: Near-duplicate pages canonicalize to the best representative URL.

### What It Means

Confirm whether the audited scope satisfies this requirement: "Near-duplicate pages canonicalize to the best representative URL." In practice, this means the reviewer needs concrete evidence, not a general impression.

### Why It Affects SEO

Intent alignment affects whether the page deserves to show for the target query. This check keeps the page focused on the searcher's job instead of only matching keywords.

### How To Verify

1. Identify the exact URL, template, brand workspace, connector account, or page group in scope.
2. Collect evidence from: GSC, Firecrawl, Playwright, CMS/code, OSS.
3. Record pass, fail, not_applicable, or not_checked_blocked in the audit matrix with an artifact reference.

### Evidence Sources

GSC, Firecrawl, Playwright, CMS/code, OSS

### Pass Criteria

The item is verified as true for the scoped URL, template, brand, connector account, or page group, and the audit row includes a specific evidence source and artifact reference.

### Fail Criteria

The evidence shows the requirement is missing, inconsistent, inaccurate, inaccessible, risky, or materially incomplete for the audited scope.

### Common Fix

Have content or marketing make the smallest change that satisfies the evidence requirement, then rerun the check.

### Owner

content or marketing

### Notes

If the required connector, browser rendering, platform export, or human context is unavailable, mark the audit row as `not_checked_blocked` and name the missing access or artifact.

## Item 12

Item ID: `generic-on-page-seo.3-indexability.efdbc920`

Original checklist item: Canonical tags are not contradictory with redirects, hreflang, sitemap URLs, or internal links.

### What It Means

Confirm whether the audited scope satisfies this requirement: "Canonical tags are not contradictory with redirects, hreflang, sitemap URLs, or internal links." In practice, this means the reviewer needs concrete evidence, not a general impression.

### Why It Affects SEO

Intent alignment affects whether the page deserves to show for the target query. This check keeps the page focused on the searcher's job instead of only matching keywords. Search engines cannot rank what they cannot discover, render, canonicalize, or keep indexable. This check protects crawl access, index coverage, and canonical signal quality.

### How To Verify

1. Identify the exact URL, template, brand workspace, connector account, or page group in scope.
2. Collect evidence from: GSC, Firecrawl, Playwright, CMS/code, OSS.
3. Use browser-rendered evidence before claiming the item is absent or broken.
4. Use Search Console data when access exists; otherwise mark the row as blocked with the missing property or permission.
5. Record pass, fail, not_applicable, or not_checked_blocked in the audit matrix with an artifact reference.

### Evidence Sources

GSC, Firecrawl, Playwright, CMS/code, OSS

### Pass Criteria

The item is verified as true for the scoped URL, template, brand, connector account, or page group, and the audit row includes a specific evidence source and artifact reference.

### Fail Criteria

The evidence shows the requirement is missing, inconsistent, inaccurate, inaccessible, risky, or materially incomplete for the audited scope.

### Common Fix

Update the template, metadata, server response, robots policy, sitemap, or structured data source, then rerun rendered and crawl checks.

### Owner

engineering

### Notes

If the required connector, browser rendering, platform export, or human context is unavailable, mark the audit row as `not_checked_blocked` and name the missing access or artifact.

## Item 13

Item ID: `generic-on-page-seo.3-indexability.a635f18f`

Original checklist item: The canonical URL returns a successful response and is not noindexed or blocked.

### What It Means

Confirm whether the audited scope satisfies this requirement: "The canonical URL returns a successful response and is not noindexed or blocked." In practice, this means the reviewer needs concrete evidence, not a general impression.

### Why It Affects SEO

Intent alignment affects whether the page deserves to show for the target query. This check keeps the page focused on the searcher's job instead of only matching keywords. Search engines cannot rank what they cannot discover, render, canonicalize, or keep indexable. This check protects crawl access, index coverage, and canonical signal quality.

### How To Verify

1. Identify the exact URL, template, brand workspace, connector account, or page group in scope.
2. Collect evidence from: GSC, Firecrawl, Playwright, CMS/code, OSS, Shopify or CMS, GMC.
3. Compare visible page content, structured data, and feed or platform values for consistency.
4. Record pass, fail, not_applicable, or not_checked_blocked in the audit matrix with an artifact reference.

### Evidence Sources

GSC, Firecrawl, Playwright, CMS/code, OSS, Shopify or CMS, GMC

### Pass Criteria

The item is verified as true for the scoped URL, template, brand, connector account, or page group, and the audit row includes a specific evidence source and artifact reference.

### Fail Criteria

The evidence shows the requirement is missing, inconsistent, inaccurate, inaccessible, risky, or materially incomplete for the audited scope.

### Common Fix

Fix the product source of truth, page template, schema, or feed mapping so product data is complete and consistent.

### Owner

merchandising, marketing, or engineering

### Notes

If the required connector, browser rendering, platform export, or human context is unavailable, mark the audit row as `not_checked_blocked` and name the missing access or artifact.

## Item 14

Item ID: `generic-on-page-seo.3-indexability.9cc76809`

Original checklist item: The page is not a soft 404: thin, empty, unavailable, or error-like content returning 200.

### What It Means

Confirm whether the audited scope satisfies this requirement: "The page is not a soft 404: thin, empty, unavailable, or error-like content returning 200." In practice, this means the reviewer needs concrete evidence, not a general impression.

### Why It Affects SEO

Intent alignment affects whether the page deserves to show for the target query. This check keeps the page focused on the searcher's job instead of only matching keywords.

### How To Verify

1. Identify the exact URL, template, brand workspace, connector account, or page group in scope.
2. Collect evidence from: GSC, Firecrawl, Playwright, CMS/code, OSS.
3. Record pass, fail, not_applicable, or not_checked_blocked in the audit matrix with an artifact reference.

### Evidence Sources

GSC, Firecrawl, Playwright, CMS/code, OSS

### Pass Criteria

The item is verified as true for the scoped URL, template, brand, connector account, or page group, and the audit row includes a specific evidence source and artifact reference.

### Fail Criteria

The evidence shows the requirement is missing, inconsistent, inaccurate, inaccessible, risky, or materially incomplete for the audited scope.

### Common Fix

Rewrite the affected copy or page structure so the primary intent, answer, and next step are clear and evidence-backed.

### Owner

content or marketing

### Notes

If the required connector, browser rendering, platform export, or human context is unavailable, mark the audit row as `not_checked_blocked` and name the missing access or artifact.

## Item 15

Item ID: `generic-on-page-seo.3-indexability.979c9240`

Original checklist item: If the page is removed permanently, it returns 404 or 410 rather than redirecting every missing URL to the homepage.

### What It Means

Confirm whether the audited scope satisfies this requirement: "If the page is removed permanently, it returns 404 or 410 rather than redirecting every missing URL to the homepage." In practice, this means the reviewer needs concrete evidence, not a general impression.

### Why It Affects SEO

Intent alignment affects whether the page deserves to show for the target query. This check keeps the page focused on the searcher's job instead of only matching keywords.

### How To Verify

1. Identify the exact URL, template, brand workspace, connector account, or page group in scope.
2. Collect evidence from: GSC, Firecrawl, Playwright, CMS/code, OSS, Shopify or CMS, GMC.
3. Compare visible page content, structured data, and feed or platform values for consistency.
4. Record pass, fail, not_applicable, or not_checked_blocked in the audit matrix with an artifact reference.

### Evidence Sources

GSC, Firecrawl, Playwright, CMS/code, OSS, Shopify or CMS, GMC

### Pass Criteria

The item is verified as true for the scoped URL, template, brand, connector account, or page group, and the audit row includes a specific evidence source and artifact reference.

### Fail Criteria

The evidence shows the requirement is missing, inconsistent, inaccurate, inaccessible, risky, or materially incomplete for the audited scope.

### Common Fix

Fix the product source of truth, page template, schema, or feed mapping so product data is complete and consistent.

### Owner

merchandising, marketing, or engineering

### Notes

If the required connector, browser rendering, platform export, or human context is unavailable, mark the audit row as `not_checked_blocked` and name the missing access or artifact.

## Item 16

Item ID: `generic-on-page-seo.3-indexability.ac57a240`

Original checklist item: If the page moved permanently, it redirects with a permanent redirect to the closest matching replacement.

### What It Means

Confirm whether the audited scope satisfies this requirement: "If the page moved permanently, it redirects with a permanent redirect to the closest matching replacement." In practice, this means the reviewer needs concrete evidence, not a general impression.

### Why It Affects SEO

Intent alignment affects whether the page deserves to show for the target query. This check keeps the page focused on the searcher's job instead of only matching keywords. Search engines cannot rank what they cannot discover, render, canonicalize, or keep indexable. This check protects crawl access, index coverage, and canonical signal quality.

### How To Verify

1. Identify the exact URL, template, brand workspace, connector account, or page group in scope.
2. Collect evidence from: GSC, Firecrawl, Playwright, CMS/code, OSS.
3. Record pass, fail, not_applicable, or not_checked_blocked in the audit matrix with an artifact reference.

### Evidence Sources

GSC, Firecrawl, Playwright, CMS/code, OSS

### Pass Criteria

The item is verified as true for the scoped URL, template, brand, connector account, or page group, and the audit row includes a specific evidence source and artifact reference.

### Fail Criteria

The evidence shows the requirement is missing, inconsistent, inaccurate, inaccessible, risky, or materially incomplete for the audited scope.

### Common Fix

Update the template, metadata, server response, robots policy, sitemap, or structured data source, then rerun rendered and crawl checks.

### Owner

engineering

### Notes

If the required connector, browser rendering, platform export, or human context is unavailable, mark the audit row as `not_checked_blocked` and name the missing access or artifact.

## Item 17

Item ID: `generic-on-page-seo.3-indexability.6544f743`

Original checklist item: PDFs, documents, images, feeds, and other non-HTML assets are reviewed for whether they should be indexed.

### What It Means

Confirm whether the audited scope satisfies this requirement: "PDFs, documents, images, feeds, and other non-HTML assets are reviewed for whether they should be indexed." In practice, this means the reviewer needs concrete evidence, not a general impression.

### Why It Affects SEO

Intent alignment affects whether the page deserves to show for the target query. This check keeps the page focused on the searcher's job instead of only matching keywords.

### How To Verify

1. Identify the exact URL, template, brand workspace, connector account, or page group in scope.
2. Collect evidence from: GSC, Firecrawl, Playwright, CMS/code, OSS.
3. Use browser-rendered evidence before claiming the item is absent or broken.
4. Record pass, fail, not_applicable, or not_checked_blocked in the audit matrix with an artifact reference.

### Evidence Sources

GSC, Firecrawl, Playwright, CMS/code, OSS

### Pass Criteria

The item is verified as true for the scoped URL, template, brand, connector account, or page group, and the audit row includes a specific evidence source and artifact reference.

### Fail Criteria

The evidence shows the requirement is missing, inconsistent, inaccurate, inaccessible, risky, or materially incomplete for the audited scope.

### Common Fix

Have content or marketing make the smallest change that satisfies the evidence requirement, then rerun the check.

### Owner

content or marketing

### Notes

If the required connector, browser rendering, platform export, or human context is unavailable, mark the audit row as `not_checked_blocked` and name the missing access or artifact.

## Item 18

Item ID: `generic-on-page-seo.3-indexability.53e468d3`

Original checklist item: Non-HTML assets that should not be indexed use `X-Robots-Tag` or access control where appropriate.

### What It Means

Confirm whether the audited scope satisfies this requirement: "Non-HTML assets that should not be indexed use `X-Robots-Tag` or access control where appropriate." In practice, this means the reviewer needs concrete evidence, not a general impression.

### Why It Affects SEO

Intent alignment affects whether the page deserves to show for the target query. This check keeps the page focused on the searcher's job instead of only matching keywords. Search engines cannot rank what they cannot discover, render, canonicalize, or keep indexable. This check protects crawl access, index coverage, and canonical signal quality.

### How To Verify

1. Identify the exact URL, template, brand workspace, connector account, or page group in scope.
2. Collect evidence from: GSC, Firecrawl, Playwright, CMS/code, OSS.
3. Record pass, fail, not_applicable, or not_checked_blocked in the audit matrix with an artifact reference.

### Evidence Sources

GSC, Firecrawl, Playwright, CMS/code, OSS

### Pass Criteria

The item is verified as true for the scoped URL, template, brand, connector account, or page group, and the audit row includes a specific evidence source and artifact reference.

### Fail Criteria

The evidence shows the requirement is missing, inconsistent, inaccurate, inaccessible, risky, or materially incomplete for the audited scope.

### Common Fix

Update the template, metadata, server response, robots policy, sitemap, or structured data source, then rerun rendered and crawl checks.

### Owner

engineering

### Notes

If the required connector, browser rendering, platform export, or human context is unavailable, mark the audit row as `not_checked_blocked` and name the missing access or artifact.

## Item 19

Item ID: `generic-on-page-seo.3-indexability.b507ca3b`

Original checklist item: Non-HTML duplicates use HTTP canonical headers where needed.

### What It Means

Confirm whether the audited scope satisfies this requirement: "Non-HTML duplicates use HTTP canonical headers where needed." In practice, this means the reviewer needs concrete evidence, not a general impression.

### Why It Affects SEO

Intent alignment affects whether the page deserves to show for the target query. This check keeps the page focused on the searcher's job instead of only matching keywords. Search engines cannot rank what they cannot discover, render, canonicalize, or keep indexable. This check protects crawl access, index coverage, and canonical signal quality.

### How To Verify

1. Identify the exact URL, template, brand workspace, connector account, or page group in scope.
2. Collect evidence from: GSC, Firecrawl, Playwright, CMS/code, OSS.
3. Record pass, fail, not_applicable, or not_checked_blocked in the audit matrix with an artifact reference.

### Evidence Sources

GSC, Firecrawl, Playwright, CMS/code, OSS

### Pass Criteria

The item is verified as true for the scoped URL, template, brand, connector account, or page group, and the audit row includes a specific evidence source and artifact reference.

### Fail Criteria

The evidence shows the requirement is missing, inconsistent, inaccurate, inaccessible, risky, or materially incomplete for the audited scope.

### Common Fix

Update the template, metadata, server response, robots policy, sitemap, or structured data source, then rerun rendered and crawl checks.

### Owner

engineering

### Notes

If the required connector, browser rendering, platform export, or human context is unavailable, mark the audit row as `not_checked_blocked` and name the missing access or artifact.
