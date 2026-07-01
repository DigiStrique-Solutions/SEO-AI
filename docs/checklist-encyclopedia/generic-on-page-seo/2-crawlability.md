---
title: 2. Crawlability
sidebar_position: 7
---

# 2. Crawlability

Checklist: `generic-on-page-seo`

Source: `docs/checklists/generic-on-page-seo-checklist.md`

This page explains every checklist item in this section. Each item should still be verified with evidence before it is marked `pass` or `fail`.

## Item 1

Item ID: `generic-on-page-seo.2-crawlability.57f2a5f8`

Original checklist item: The page is reachable through normal HTML links, not only search, filters, JavaScript actions, forms, or internal APIs.

### What It Means

Confirm whether the audited scope satisfies this requirement: "The page is reachable through normal HTML links, not only search, filters, JavaScript actions, forms, or internal APIs." In practice, this means the reviewer needs concrete evidence, not a general impression.

### Why It Affects SEO

Intent alignment affects whether the page deserves to show for the target query. This check keeps the page focused on the searcher's job instead of only matching keywords.

### How To Verify

1. Identify the exact URL, template, brand workspace, connector account, or page group in scope.
2. Collect evidence from: Firecrawl, Playwright, GSC, CMS/code, OSS.
3. Use browser-rendered evidence before claiming the item is absent or broken.
4. Record pass, fail, not_applicable, or not_checked_blocked in the audit matrix with an artifact reference.

### Evidence Sources

Firecrawl, Playwright, GSC, CMS/code, OSS

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

## Item 2

Item ID: `generic-on-page-seo.2-crawlability.f55f8c16`

Original checklist item: Important links use valid `href` values that crawlers can discover.

### What It Means

Confirm whether the audited scope satisfies this requirement: "Important links use valid `href` values that crawlers can discover." In practice, this means the reviewer needs concrete evidence, not a general impression.

### Why It Affects SEO

Intent alignment affects whether the page deserves to show for the target query. This check keeps the page focused on the searcher's job instead of only matching keywords.

### How To Verify

1. Identify the exact URL, template, brand workspace, connector account, or page group in scope.
2. Collect evidence from: Firecrawl, Playwright, GSC, CMS/code, OSS.
3. Use browser-rendered evidence before claiming the item is absent or broken.
4. Record pass, fail, not_applicable, or not_checked_blocked in the audit matrix with an artifact reference.

### Evidence Sources

Firecrawl, Playwright, GSC, CMS/code, OSS

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

## Item 3

Item ID: `generic-on-page-seo.2-crawlability.87c1b33d`

Original checklist item: Navigation, breadcrumbs, related content, and pagination expose crawlable URLs.

### What It Means

Confirm whether the audited scope satisfies this requirement: "Navigation, breadcrumbs, related content, and pagination expose crawlable URLs." In practice, this means the reviewer needs concrete evidence, not a general impression.

### Why It Affects SEO

Intent alignment affects whether the page deserves to show for the target query. This check keeps the page focused on the searcher's job instead of only matching keywords. Architecture controls how users and crawlers find important pages. Good internal linking helps distribute context, priority, and crawl paths.

### How To Verify

1. Identify the exact URL, template, brand workspace, connector account, or page group in scope.
2. Collect evidence from: Firecrawl, Playwright, GSC, CMS/code, OSS.
3. Use browser-rendered evidence before claiming the item is absent or broken.
4. Record pass, fail, not_applicable, or not_checked_blocked in the audit matrix with an artifact reference.

### Evidence Sources

Firecrawl, Playwright, GSC, CMS/code, OSS

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

## Item 4

Item ID: `generic-on-page-seo.2-crawlability.a5f28a6e`

Original checklist item: The page is not blocked by `robots.txt` if it should rank.

### What It Means

Confirm whether the audited scope satisfies this requirement: "The page is not blocked by `robots.txt` if it should rank." In practice, this means the reviewer needs concrete evidence, not a general impression.

### Why It Affects SEO

Intent alignment affects whether the page deserves to show for the target query. This check keeps the page focused on the searcher's job instead of only matching keywords. Search engines cannot rank what they cannot discover, render, canonicalize, or keep indexable. This check protects crawl access, index coverage, and canonical signal quality.

### How To Verify

1. Identify the exact URL, template, brand workspace, connector account, or page group in scope.
2. Collect evidence from: Firecrawl, Playwright, GSC, CMS/code, OSS.
3. Record pass, fail, not_applicable, or not_checked_blocked in the audit matrix with an artifact reference.

### Evidence Sources

Firecrawl, Playwright, GSC, CMS/code, OSS

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

Item ID: `generic-on-page-seo.2-crawlability.01f80249`

Original checklist item: The page's critical CSS, JavaScript, image, and API resources are not blocked in a way that prevents rendering or content discovery.

### What It Means

Confirm whether the audited scope satisfies this requirement: "The page's critical CSS, JavaScript, image, and API resources are not blocked in a way that prevents rendering or content discovery." In practice, this means the reviewer needs concrete evidence, not a general impression.

### Why It Affects SEO

Intent alignment affects whether the page deserves to show for the target query. This check keeps the page focused on the searcher's job instead of only matching keywords.

### How To Verify

1. Identify the exact URL, template, brand workspace, connector account, or page group in scope.
2. Collect evidence from: Firecrawl, Playwright, GSC, CMS/code, OSS.
3. Use browser-rendered evidence before claiming the item is absent or broken.
4. Record pass, fail, not_applicable, or not_checked_blocked in the audit matrix with an artifact reference.

### Evidence Sources

Firecrawl, Playwright, GSC, CMS/code, OSS

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

Item ID: `generic-on-page-seo.2-crawlability.425fab77`

Original checklist item: The page is linked from at least one relevant internal page.

### What It Means

Confirm whether the audited scope satisfies this requirement: "The page is linked from at least one relevant internal page." In practice, this means the reviewer needs concrete evidence, not a general impression.

### Why It Affects SEO

Intent alignment affects whether the page deserves to show for the target query. This check keeps the page focused on the searcher's job instead of only matching keywords.

### How To Verify

1. Identify the exact URL, template, brand workspace, connector account, or page group in scope.
2. Collect evidence from: Firecrawl, Playwright, GSC, CMS/code, OSS.
3. Record pass, fail, not_applicable, or not_checked_blocked in the audit matrix with an artifact reference.

### Evidence Sources

Firecrawl, Playwright, GSC, CMS/code, OSS

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

## Item 7

Item ID: `generic-on-page-seo.2-crawlability.9cfcf17c`

Original checklist item: The page is no more than 3 clicks from an important hub when it is a priority page.

### What It Means

Confirm whether the audited scope satisfies this requirement: "The page is no more than 3 clicks from an important hub when it is a priority page." In practice, this means the reviewer needs concrete evidence, not a general impression.

### Why It Affects SEO

Intent alignment affects whether the page deserves to show for the target query. This check keeps the page focused on the searcher's job instead of only matching keywords. Architecture controls how users and crawlers find important pages. Good internal linking helps distribute context, priority, and crawl paths.

### How To Verify

1. Identify the exact URL, template, brand workspace, connector account, or page group in scope.
2. Collect evidence from: Firecrawl, Playwright, GSC, CMS/code, OSS.
3. Record pass, fail, not_applicable, or not_checked_blocked in the audit matrix with an artifact reference.

### Evidence Sources

Firecrawl, Playwright, GSC, CMS/code, OSS

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

## Item 8

Item ID: `generic-on-page-seo.2-crawlability.c0da4b7c`

Original checklist item: The page is included in the relevant XML sitemap if it is canonical and indexable.

### What It Means

Confirm whether the audited scope satisfies this requirement: "The page is included in the relevant XML sitemap if it is canonical and indexable." In practice, this means the reviewer needs concrete evidence, not a general impression.

### Why It Affects SEO

Intent alignment affects whether the page deserves to show for the target query. This check keeps the page focused on the searcher's job instead of only matching keywords. Search engines cannot rank what they cannot discover, render, canonicalize, or keep indexable. This check protects crawl access, index coverage, and canonical signal quality.

### How To Verify

1. Identify the exact URL, template, brand workspace, connector account, or page group in scope.
2. Collect evidence from: Firecrawl, Playwright, GSC, CMS/code, OSS.
3. Use Search Console data when access exists; otherwise mark the row as blocked with the missing property or permission.
4. Record pass, fail, not_applicable, or not_checked_blocked in the audit matrix with an artifact reference.

### Evidence Sources

Firecrawl, Playwright, GSC, CMS/code, OSS

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

## Item 9

Item ID: `generic-on-page-seo.2-crawlability.c57f9681`

Original checklist item: The sitemap entry uses the canonical URL, returns a successful status, and is not blocked or noindexed.

### What It Means

Confirm whether the audited scope satisfies this requirement: "The sitemap entry uses the canonical URL, returns a successful status, and is not blocked or noindexed." In practice, this means the reviewer needs concrete evidence, not a general impression.

### Why It Affects SEO

Intent alignment affects whether the page deserves to show for the target query. This check keeps the page focused on the searcher's job instead of only matching keywords. Search engines cannot rank what they cannot discover, render, canonicalize, or keep indexable. This check protects crawl access, index coverage, and canonical signal quality.

### How To Verify

1. Identify the exact URL, template, brand workspace, connector account, or page group in scope.
2. Collect evidence from: Firecrawl, Playwright, GSC, CMS/code, OSS, Shopify or CMS, GMC.
3. Use Search Console data when access exists; otherwise mark the row as blocked with the missing property or permission.
4. Compare visible page content, structured data, and feed or platform values for consistency.
5. Record pass, fail, not_applicable, or not_checked_blocked in the audit matrix with an artifact reference.

### Evidence Sources

Firecrawl, Playwright, GSC, CMS/code, OSS, Shopify or CMS, GMC

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

## Item 10

Item ID: `generic-on-page-seo.2-crawlability.3083eeb5`

Original checklist item: The page is discoverable by Bing as well as Google when Bing traffic matters.

### What It Means

Confirm whether the audited scope satisfies this requirement: "The page is discoverable by Bing as well as Google when Bing traffic matters." In practice, this means the reviewer needs concrete evidence, not a general impression.

### Why It Affects SEO

Intent alignment affects whether the page deserves to show for the target query. This check keeps the page focused on the searcher's job instead of only matching keywords. SEO decisions need reliable measurement. This check prevents prioritization based on incomplete, unscoped, or misleading data.

### How To Verify

1. Identify the exact URL, template, brand workspace, connector account, or page group in scope.
2. Collect evidence from: Firecrawl, Playwright, GSC, CMS/code, OSS.
3. Record pass, fail, not_applicable, or not_checked_blocked in the audit matrix with an artifact reference.

### Evidence Sources

Firecrawl, Playwright, GSC, CMS/code, OSS

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

Item ID: `generic-on-page-seo.2-crawlability.5138e1b0`

Original checklist item: Paginated series expose unique crawlable URLs for each page, use sequential links with real `href` values, and avoid URL fragments for page numbers.

### What It Means

Confirm whether the audited scope satisfies this requirement: "Paginated series expose unique crawlable URLs for each page, use sequential links with real `href` values, and avoid URL fragments for page numbers." In practice, this means the reviewer needs concrete evidence, not a general impression.

### Why It Affects SEO

Intent alignment affects whether the page deserves to show for the target query. This check keeps the page focused on the searcher's job instead of only matching keywords.

### How To Verify

1. Identify the exact URL, template, brand workspace, connector account, or page group in scope.
2. Collect evidence from: Firecrawl, Playwright, GSC, CMS/code, OSS.
3. Use browser-rendered evidence before claiming the item is absent or broken.
4. Record pass, fail, not_applicable, or not_checked_blocked in the audit matrix with an artifact reference.

### Evidence Sources

Firecrawl, Playwright, GSC, CMS/code, OSS

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

Item ID: `generic-on-page-seo.2-crawlability.2ab36b62`

Original checklist item: Infinite scroll or "load more" experiences have crawlable paginated URLs or equivalent linked pages.

### What It Means

Confirm whether the audited scope satisfies this requirement: "Infinite scroll or "load more" experiences have crawlable paginated URLs or equivalent linked pages." In practice, this means the reviewer needs concrete evidence, not a general impression.

### Why It Affects SEO

Intent alignment affects whether the page deserves to show for the target query. This check keeps the page focused on the searcher's job instead of only matching keywords.

### How To Verify

1. Identify the exact URL, template, brand workspace, connector account, or page group in scope.
2. Collect evidence from: Firecrawl, Playwright, GSC, CMS/code, OSS.
3. Record pass, fail, not_applicable, or not_checked_blocked in the audit matrix with an artifact reference.

### Evidence Sources

Firecrawl, Playwright, GSC, CMS/code, OSS

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

## Item 13

Item ID: `generic-on-page-seo.2-crawlability.3851b787`

Original checklist item: Faceted and filtered URL patterns are classified as indexable or non-indexable before audit recommendations are made.

### What It Means

Confirm whether the audited scope satisfies this requirement: "Faceted and filtered URL patterns are classified as indexable or non-indexable before audit recommendations are made." In practice, this means the reviewer needs concrete evidence, not a general impression.

### Why It Affects SEO

Intent alignment affects whether the page deserves to show for the target query. This check keeps the page focused on the searcher's job instead of only matching keywords.

### How To Verify

1. Identify the exact URL, template, brand workspace, connector account, or page group in scope.
2. Collect evidence from: Firecrawl, Playwright, GSC, CMS/code, OSS.
3. Record pass, fail, not_applicable, or not_checked_blocked in the audit matrix with an artifact reference.

### Evidence Sources

Firecrawl, Playwright, GSC, CMS/code, OSS

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

## Item 14

Item ID: `generic-on-page-seo.2-crawlability.80d06061`

Original checklist item: Nonvaluable facet combinations are controlled to avoid crawl traps, duplicate pages, and empty result pages.

### What It Means

Confirm whether the audited scope satisfies this requirement: "Nonvaluable facet combinations are controlled to avoid crawl traps, duplicate pages, and empty result pages." In practice, this means the reviewer needs concrete evidence, not a general impression.

### Why It Affects SEO

Intent alignment affects whether the page deserves to show for the target query. This check keeps the page focused on the searcher's job instead of only matching keywords. Search engines cannot rank what they cannot discover, render, canonicalize, or keep indexable. This check protects crawl access, index coverage, and canonical signal quality.

### How To Verify

1. Identify the exact URL, template, brand workspace, connector account, or page group in scope.
2. Collect evidence from: Firecrawl, Playwright, GSC, CMS/code, OSS.
3. Record pass, fail, not_applicable, or not_checked_blocked in the audit matrix with an artifact reference.

### Evidence Sources

Firecrawl, Playwright, GSC, CMS/code, OSS

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

## Item 15

Item ID: `generic-on-page-seo.2-crawlability.ef8cd8e9`

Original checklist item: For large, fast-changing, or heavily parameterized sites, Search Console Crawl Stats or server logs are reviewed for wasted crawl on redirects, 404 or 410, soft 404s, 5xx or 429 responses, and low-value parameter paths.

### What It Means

Confirm whether the audited scope satisfies this requirement: "For large, fast-changing, or heavily parameterized sites, Search Console Crawl Stats or server logs are reviewed for wasted crawl on redirects, 404 or 410, soft 404s, 5xx or 429 responses, and low-value parameter paths." In practice, this means the reviewer needs concrete evidence, not a general impression.

### Why It Affects SEO

Intent alignment affects whether the page deserves to show for the target query. This check keeps the page focused on the searcher's job instead of only matching keywords. Search engines cannot rank what they cannot discover, render, canonicalize, or keep indexable. This check protects crawl access, index coverage, and canonical signal quality.

### How To Verify

1. Identify the exact URL, template, brand workspace, connector account, or page group in scope.
2. Collect evidence from: Firecrawl, Playwright, GSC, CMS/code, OSS.
3. Record pass, fail, not_applicable, or not_checked_blocked in the audit matrix with an artifact reference.

### Evidence Sources

Firecrawl, Playwright, GSC, CMS/code, OSS

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

## Item 16

Item ID: `generic-on-page-seo.2-crawlability.d583a490`

Original checklist item: When logs, bot allowlists, or firewall rules are used as evidence, Googlebot is verified by reverse DNS or official IP ranges rather than user-agent strings alone.

### What It Means

Confirm whether the audited scope satisfies this requirement: "When logs, bot allowlists, or firewall rules are used as evidence, Googlebot is verified by reverse DNS or official IP ranges rather than user-agent strings alone." In practice, this means the reviewer needs concrete evidence, not a general impression.

### Why It Affects SEO

Intent alignment affects whether the page deserves to show for the target query. This check keeps the page focused on the searcher's job instead of only matching keywords. Useful, source-backed content improves relevance, user confidence, and eligibility for sensitive or competitive queries. Weak or unsupported content can suppress trust and conversions.

### How To Verify

1. Identify the exact URL, template, brand workspace, connector account, or page group in scope.
2. Collect evidence from: Firecrawl, Playwright, GSC, CMS/code, OSS.
3. Record pass, fail, not_applicable, or not_checked_blocked in the audit matrix with an artifact reference.

### Evidence Sources

Firecrawl, Playwright, GSC, CMS/code, OSS

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
