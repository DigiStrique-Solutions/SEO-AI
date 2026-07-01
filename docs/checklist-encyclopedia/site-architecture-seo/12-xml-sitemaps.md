---
title: 12. XML Sitemaps
sidebar_position: 16
---

# 12. XML Sitemaps

Checklist: `site-architecture-seo`

Source: `docs/checklists/site-architecture-seo-checklist.md`

This page explains every checklist item in this section. Each item should still be verified with evidence before it is marked `pass` or `fail`.

## Item 1

Item ID: `site-architecture-seo.12-xml-sitemaps.f6274b55`

Original checklist item: XML sitemaps contain only canonical, indexable URLs.

### What It Means

Confirm whether the audited scope satisfies this requirement: "XML sitemaps contain only canonical, indexable URLs." In practice, this means the reviewer needs concrete evidence, not a general impression.

### Why It Affects SEO

Architecture controls how users and crawlers find important pages. Good internal linking helps distribute context, priority, and crawl paths. Search engines cannot rank what they cannot discover, render, canonicalize, or keep indexable. This check protects crawl access, index coverage, and canonical signal quality.

### How To Verify

1. Identify the exact URL, template, brand workspace, connector account, or page group in scope.
2. Collect evidence from: GSC, Firecrawl, CMS/code, OSS, Playwright.
3. Record pass, fail, not_applicable, or not_checked_blocked in the audit matrix with an artifact reference.

### Evidence Sources

GSC, Firecrawl, CMS/code, OSS, Playwright

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

Item ID: `site-architecture-seo.12-xml-sitemaps.5a71232d`

Original checklist item: Utility, noindexed, redirected, broken, duplicate, and parameter-only URLs are excluded.

### What It Means

Confirm whether the audited scope satisfies this requirement: "Utility, noindexed, redirected, broken, duplicate, and parameter-only URLs are excluded." In practice, this means the reviewer needs concrete evidence, not a general impression.

### Why It Affects SEO

Architecture controls how users and crawlers find important pages. Good internal linking helps distribute context, priority, and crawl paths.

### How To Verify

1. Identify the exact URL, template, brand workspace, connector account, or page group in scope.
2. Collect evidence from: GSC, Firecrawl, CMS/code, OSS.
3. Record pass, fail, not_applicable, or not_checked_blocked in the audit matrix with an artifact reference.

### Evidence Sources

GSC, Firecrawl, CMS/code, OSS

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

Item ID: `site-architecture-seo.12-xml-sitemaps.87c7313f`

Original checklist item: Sitemaps are split by content type or section when useful.

### What It Means

Confirm whether the audited scope satisfies this requirement: "Sitemaps are split by content type or section when useful." In practice, this means the reviewer needs concrete evidence, not a general impression.

### Why It Affects SEO

Architecture controls how users and crawlers find important pages. Good internal linking helps distribute context, priority, and crawl paths.

### How To Verify

1. Identify the exact URL, template, brand workspace, connector account, or page group in scope.
2. Collect evidence from: GSC, Firecrawl, CMS/code, OSS.
3. Record pass, fail, not_applicable, or not_checked_blocked in the audit matrix with an artifact reference.

### Evidence Sources

GSC, Firecrawl, CMS/code, OSS

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

Item ID: `site-architecture-seo.12-xml-sitemaps.baa12785`

Original checklist item: Sitemaps are referenced in robots.txt.

### What It Means

Confirm whether the audited scope satisfies this requirement: "Sitemaps are referenced in robots.txt." In practice, this means the reviewer needs concrete evidence, not a general impression.

### Why It Affects SEO

Architecture controls how users and crawlers find important pages. Good internal linking helps distribute context, priority, and crawl paths. Search engines cannot rank what they cannot discover, render, canonicalize, or keep indexable. This check protects crawl access, index coverage, and canonical signal quality.

### How To Verify

1. Identify the exact URL, template, brand workspace, connector account, or page group in scope.
2. Collect evidence from: GSC, Firecrawl, CMS/code, OSS.
3. Record pass, fail, not_applicable, or not_checked_blocked in the audit matrix with an artifact reference.

### Evidence Sources

GSC, Firecrawl, CMS/code, OSS

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

Item ID: `site-architecture-seo.12-xml-sitemaps.c08f523a`

Original checklist item: Sitemaps are submitted in GSC where property access exists.

### What It Means

Confirm whether the audited scope satisfies this requirement: "Sitemaps are submitted in GSC where property access exists." In practice, this means the reviewer needs concrete evidence, not a general impression.

### Why It Affects SEO

Architecture controls how users and crawlers find important pages. Good internal linking helps distribute context, priority, and crawl paths. SEO decisions need reliable measurement. This check prevents prioritization based on incomplete, unscoped, or misleading data.

### How To Verify

1. Identify the exact URL, template, brand workspace, connector account, or page group in scope.
2. Collect evidence from: GSC, Firecrawl, CMS/code, OSS.
3. Use Search Console data when access exists; otherwise mark the row as blocked with the missing property or permission.
4. Record pass, fail, not_applicable, or not_checked_blocked in the audit matrix with an artifact reference.

### Evidence Sources

GSC, Firecrawl, CMS/code, OSS

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

Item ID: `site-architecture-seo.12-xml-sitemaps.99a01349`

Original checklist item: Sitemap coverage is compared to crawl, GSC, GA4, and CMS inventory.

### What It Means

Confirm whether the audited scope satisfies this requirement: "Sitemap coverage is compared to crawl, GSC, GA4, and CMS inventory." In practice, this means the reviewer needs concrete evidence, not a general impression.

### Why It Affects SEO

Architecture controls how users and crawlers find important pages. Good internal linking helps distribute context, priority, and crawl paths. Search engines cannot rank what they cannot discover, render, canonicalize, or keep indexable. This check protects crawl access, index coverage, and canonical signal quality.

### How To Verify

1. Identify the exact URL, template, brand workspace, connector account, or page group in scope.
2. Collect evidence from: GSC, Firecrawl, CMS/code, OSS, Playwright.
3. Use Search Console data when access exists; otherwise mark the row as blocked with the missing property or permission.
4. Use analytics data only when the property, date range, and conversion definitions are known.
5. Record pass, fail, not_applicable, or not_checked_blocked in the audit matrix with an artifact reference.

### Evidence Sources

GSC, Firecrawl, CMS/code, OSS, Playwright

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

Item ID: `site-architecture-seo.12-xml-sitemaps.b722331a`

Original checklist item: `lastmod` is present only when accurate and reflects meaningful page changes.

### What It Means

Confirm whether the audited scope satisfies this requirement: "`lastmod` is present only when accurate and reflects meaningful page changes." In practice, this means the reviewer needs concrete evidence, not a general impression.

### Why It Affects SEO

Architecture controls how users and crawlers find important pages. Good internal linking helps distribute context, priority, and crawl paths.

### How To Verify

1. Identify the exact URL, template, brand workspace, connector account, or page group in scope.
2. Collect evidence from: GSC, Firecrawl, CMS/code, OSS.
3. Record pass, fail, not_applicable, or not_checked_blocked in the audit matrix with an artifact reference.

### Evidence Sources

GSC, Firecrawl, CMS/code, OSS

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

Item ID: `site-architecture-seo.12-xml-sitemaps.b44952a6`

Original checklist item: Sitemap errors and discovered/indexed deltas are reviewed.

### What It Means

Confirm whether the audited scope satisfies this requirement: "Sitemap errors and discovered/indexed deltas are reviewed." In practice, this means the reviewer needs concrete evidence, not a general impression.

### Why It Affects SEO

Architecture controls how users and crawlers find important pages. Good internal linking helps distribute context, priority, and crawl paths. Search engines cannot rank what they cannot discover, render, canonicalize, or keep indexable. This check protects crawl access, index coverage, and canonical signal quality.

### How To Verify

1. Identify the exact URL, template, brand workspace, connector account, or page group in scope.
2. Collect evidence from: GSC, Firecrawl, CMS/code, OSS.
3. Use Search Console data when access exists; otherwise mark the row as blocked with the missing property or permission.
4. Record pass, fail, not_applicable, or not_checked_blocked in the audit matrix with an artifact reference.

### Evidence Sources

GSC, Firecrawl, CMS/code, OSS

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

Item ID: `site-architecture-seo.12-xml-sitemaps.12bc8103`

Original checklist item: Image, video, or news sitemaps are used only when the content type benefits from them.

### What It Means

Confirm whether the audited scope satisfies this requirement: "Image, video, or news sitemaps are used only when the content type benefits from them." In practice, this means the reviewer needs concrete evidence, not a general impression.

### Why It Affects SEO

Architecture controls how users and crawlers find important pages. Good internal linking helps distribute context, priority, and crawl paths.

### How To Verify

1. Identify the exact URL, template, brand workspace, connector account, or page group in scope.
2. Collect evidence from: GSC, Firecrawl, CMS/code, OSS, Playwright.
3. Use browser-rendered evidence before claiming the item is absent or broken.
4. Record pass, fail, not_applicable, or not_checked_blocked in the audit matrix with an artifact reference.

### Evidence Sources

GSC, Firecrawl, CMS/code, OSS, Playwright

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
