---
title: 2. Content Inventory
sidebar_position: 6
---

# 2. Content Inventory

Checklist: `site-architecture-seo`

Source: `docs/checklists/site-architecture-seo-checklist.md`

This page explains every checklist item in this section. Each item should still be verified with evidence before it is marked `pass` or `fail`.

## Item 1

Item ID: `site-architecture-seo.2-content-inventory.b51c4d11`

Original checklist item: A crawl inventory exists for all discoverable public URLs.

### What It Means

Confirm whether the audited scope satisfies this requirement: "A crawl inventory exists for all discoverable public URLs." In practice, this means the reviewer needs concrete evidence, not a general impression.

### Why It Affects SEO

Architecture controls how users and crawlers find important pages. Good internal linking helps distribute context, priority, and crawl paths. Search engines cannot rank what they cannot discover, render, canonicalize, or keep indexable. This check protects crawl access, index coverage, and canonical signal quality.

### How To Verify

1. Identify the exact URL, template, brand workspace, connector account, or page group in scope.
2. Collect evidence from: Firecrawl, GSC, GA4, CMS/code, OSS, Playwright.
3. Record pass, fail, not_applicable, or not_checked_blocked in the audit matrix with an artifact reference.

### Evidence Sources

Firecrawl, GSC, GA4, CMS/code, OSS, Playwright

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

## Item 2

Item ID: `site-architecture-seo.2-content-inventory.bc59ab80`

Original checklist item: XML sitemap URLs are collected and compared against crawled URLs.

### What It Means

Confirm whether the audited scope satisfies this requirement: "XML sitemap URLs are collected and compared against crawled URLs." In practice, this means the reviewer needs concrete evidence, not a general impression.

### Why It Affects SEO

Architecture controls how users and crawlers find important pages. Good internal linking helps distribute context, priority, and crawl paths. Search engines cannot rank what they cannot discover, render, canonicalize, or keep indexable. This check protects crawl access, index coverage, and canonical signal quality.

### How To Verify

1. Identify the exact URL, template, brand workspace, connector account, or page group in scope.
2. Collect evidence from: Firecrawl, GSC, GA4, CMS/code, OSS.
3. Use Search Console data when access exists; otherwise mark the row as blocked with the missing property or permission.
4. Record pass, fail, not_applicable, or not_checked_blocked in the audit matrix with an artifact reference.

### Evidence Sources

Firecrawl, GSC, GA4, CMS/code, OSS

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

Item ID: `site-architecture-seo.2-content-inventory.e76e2d39`

Original checklist item: CMS, code routes, Shopify/Webflow/WordPress pages, or database-backed URLs are exported where available.

### What It Means

Confirm whether the audited scope satisfies this requirement: "CMS, code routes, Shopify/Webflow/WordPress pages, or database-backed URLs are exported where available." In practice, this means the reviewer needs concrete evidence, not a general impression.

### Why It Affects SEO

Architecture controls how users and crawlers find important pages. Good internal linking helps distribute context, priority, and crawl paths.

### How To Verify

1. Identify the exact URL, template, brand workspace, connector account, or page group in scope.
2. Collect evidence from: Firecrawl, GSC, GA4, CMS/code, OSS.
3. Record pass, fail, not_applicable, or not_checked_blocked in the audit matrix with an artifact reference.

### Evidence Sources

Firecrawl, GSC, GA4, CMS/code, OSS

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

Item ID: `site-architecture-seo.2-content-inventory.24865652`

Original checklist item: GSC top pages are included even if the crawler missed them.

### What It Means

Confirm whether the audited scope satisfies this requirement: "GSC top pages are included even if the crawler missed them." In practice, this means the reviewer needs concrete evidence, not a general impression.

### Why It Affects SEO

Architecture controls how users and crawlers find important pages. Good internal linking helps distribute context, priority, and crawl paths. SEO decisions need reliable measurement. This check prevents prioritization based on incomplete, unscoped, or misleading data.

### How To Verify

1. Identify the exact URL, template, brand workspace, connector account, or page group in scope.
2. Collect evidence from: Firecrawl, GSC, GA4, CMS/code, OSS.
3. Use Search Console data when access exists; otherwise mark the row as blocked with the missing property or permission.
4. Record pass, fail, not_applicable, or not_checked_blocked in the audit matrix with an artifact reference.

### Evidence Sources

Firecrawl, GSC, GA4, CMS/code, OSS

### Pass Criteria

The item is verified as true for the scoped URL, template, brand, connector account, or page group, and the audit row includes a specific evidence source and artifact reference.

### Fail Criteria

The evidence shows the requirement is missing, inconsistent, inaccurate, inaccessible, risky, or materially incomplete for the audited scope.

### Common Fix

Fix the data source, property scoping, export, tagging, or report definition before using the metric for decisions.

### Owner

analytics

### Notes

If the required connector, browser rendering, platform export, or human context is unavailable, mark the audit row as `not_checked_blocked` and name the missing access or artifact.

## Item 5

Item ID: `site-architecture-seo.2-content-inventory.daf8ca4a`

Original checklist item: GA4 landing pages are included even if they are missing from sitemaps.

### What It Means

Confirm whether the audited scope satisfies this requirement: "GA4 landing pages are included even if they are missing from sitemaps." In practice, this means the reviewer needs concrete evidence, not a general impression.

### Why It Affects SEO

Architecture controls how users and crawlers find important pages. Good internal linking helps distribute context, priority, and crawl paths. SEO decisions need reliable measurement. This check prevents prioritization based on incomplete, unscoped, or misleading data.

### How To Verify

1. Identify the exact URL, template, brand workspace, connector account, or page group in scope.
2. Collect evidence from: Firecrawl, GSC, GA4, CMS/code, OSS.
3. Use analytics data only when the property, date range, and conversion definitions are known.
4. Record pass, fail, not_applicable, or not_checked_blocked in the audit matrix with an artifact reference.

### Evidence Sources

Firecrawl, GSC, GA4, CMS/code, OSS

### Pass Criteria

The item is verified as true for the scoped URL, template, brand, connector account, or page group, and the audit row includes a specific evidence source and artifact reference.

### Fail Criteria

The evidence shows the requirement is missing, inconsistent, inaccurate, inaccessible, risky, or materially incomplete for the audited scope.

### Common Fix

Fix the data source, property scoping, export, tagging, or report definition before using the metric for decisions.

### Owner

analytics

### Notes

If the required connector, browser rendering, platform export, or human context is unavailable, mark the audit row as `not_checked_blocked` and name the missing access or artifact.

## Item 6

Item ID: `site-architecture-seo.2-content-inventory.fd7bd202`

Original checklist item: URLs are grouped by page type, section, template, indexability, status code, canonical target, traffic, and conversion value.

### What It Means

Confirm whether the audited scope satisfies this requirement: "URLs are grouped by page type, section, template, indexability, status code, canonical target, traffic, and conversion value." In practice, this means the reviewer needs concrete evidence, not a general impression.

### Why It Affects SEO

Architecture controls how users and crawlers find important pages. Good internal linking helps distribute context, priority, and crawl paths. Search engines cannot rank what they cannot discover, render, canonicalize, or keep indexable. This check protects crawl access, index coverage, and canonical signal quality.

### How To Verify

1. Identify the exact URL, template, brand workspace, connector account, or page group in scope.
2. Collect evidence from: Firecrawl, GSC, GA4, CMS/code, OSS, Playwright, GA4 or PostHog.
3. Use analytics data only when the property, date range, and conversion definitions are known.
4. Record pass, fail, not_applicable, or not_checked_blocked in the audit matrix with an artifact reference.

### Evidence Sources

Firecrawl, GSC, GA4, CMS/code, OSS, Playwright, GA4 or PostHog

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

## Item 7

Item ID: `site-architecture-seo.2-content-inventory.a8bffae3`

Original checklist item: Orphan pages are identified by comparing sitemap, crawl, GSC, GA4, and CMS/code sources.

### What It Means

Confirm whether the audited scope satisfies this requirement: "Orphan pages are identified by comparing sitemap, crawl, GSC, GA4, and CMS/code sources." In practice, this means the reviewer needs concrete evidence, not a general impression.

### Why It Affects SEO

Search engines cannot rank what they cannot discover, render, canonicalize, or keep indexable. This check protects crawl access, index coverage, and canonical signal quality. Architecture controls how users and crawlers find important pages. Good internal linking helps distribute context, priority, and crawl paths.

### How To Verify

1. Identify the exact URL, template, brand workspace, connector account, or page group in scope.
2. Collect evidence from: Firecrawl, GSC, GA4, CMS/code, OSS, Playwright.
3. Use Search Console data when access exists; otherwise mark the row as blocked with the missing property or permission.
4. Use analytics data only when the property, date range, and conversion definitions are known.
5. Record pass, fail, not_applicable, or not_checked_blocked in the audit matrix with an artifact reference.

### Evidence Sources

Firecrawl, GSC, GA4, CMS/code, OSS, Playwright

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

Item ID: `site-architecture-seo.2-content-inventory.112d3891`

Original checklist item: Duplicate or near-duplicate page sets are identified.

### What It Means

Confirm whether the audited scope satisfies this requirement: "Duplicate or near-duplicate page sets are identified." In practice, this means the reviewer needs concrete evidence, not a general impression.

### Why It Affects SEO

Architecture controls how users and crawlers find important pages. Good internal linking helps distribute context, priority, and crawl paths.

### How To Verify

1. Identify the exact URL, template, brand workspace, connector account, or page group in scope.
2. Collect evidence from: Firecrawl, GSC, GA4, CMS/code, OSS.
3. Record pass, fail, not_applicable, or not_checked_blocked in the audit matrix with an artifact reference.

### Evidence Sources

Firecrawl, GSC, GA4, CMS/code, OSS

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

Item ID: `site-architecture-seo.2-content-inventory.7ff7c395`

Original checklist item: Thin, stale, empty, utility, account, search result, and parameter pages are flagged separately from acquisition pages.

### What It Means

Confirm whether the audited scope satisfies this requirement: "Thin, stale, empty, utility, account, search result, and parameter pages are flagged separately from acquisition pages." In practice, this means the reviewer needs concrete evidence, not a general impression.

### Why It Affects SEO

Architecture controls how users and crawlers find important pages. Good internal linking helps distribute context, priority, and crawl paths.

### How To Verify

1. Identify the exact URL, template, brand workspace, connector account, or page group in scope.
2. Collect evidence from: Firecrawl, GSC, GA4, CMS/code, OSS.
3. Record pass, fail, not_applicable, or not_checked_blocked in the audit matrix with an artifact reference.

### Evidence Sources

Firecrawl, GSC, GA4, CMS/code, OSS

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

## Item 10

Item ID: `site-architecture-seo.2-content-inventory.a7c9f939`

Original checklist item: Non-HTML assets such as PDFs, docs, images, feeds, and downloadable files are inventoried when they receive traffic or are linked internally.

### What It Means

Confirm whether the audited scope satisfies this requirement: "Non-HTML assets such as PDFs, docs, images, feeds, and downloadable files are inventoried when they receive traffic or are linked internally." In practice, this means the reviewer needs concrete evidence, not a general impression.

### Why It Affects SEO

Architecture controls how users and crawlers find important pages. Good internal linking helps distribute context, priority, and crawl paths. SEO decisions need reliable measurement. This check prevents prioritization based on incomplete, unscoped, or misleading data.

### How To Verify

1. Identify the exact URL, template, brand workspace, connector account, or page group in scope.
2. Collect evidence from: Firecrawl, GSC, GA4, CMS/code, OSS, Playwright.
3. Use browser-rendered evidence before claiming the item is absent or broken.
4. Record pass, fail, not_applicable, or not_checked_blocked in the audit matrix with an artifact reference.

### Evidence Sources

Firecrawl, GSC, GA4, CMS/code, OSS, Playwright

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
