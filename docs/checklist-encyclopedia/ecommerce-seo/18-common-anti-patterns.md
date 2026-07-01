---
title: 18. Common Anti-Patterns
sidebar_position: 22
---

# 18. Common Anti-Patterns

Checklist: `ecommerce-seo`

Source: `docs/checklists/ecommerce-seo-checklist.md`

This page explains every checklist item in this section. Each item should still be verified with evidence before it is marked `pass` or `fail`.

## Item 1

Item ID: `ecommerce-seo.18-common-anti-patterns.f4fe7382`

Original checklist item: Product schema says a product is in stock when the page or feed says it is out of stock.

### What It Means

Confirm whether the audited scope satisfies this requirement: "Product schema says a product is in stock when the page or feed says it is out of stock." In practice, this means the reviewer needs concrete evidence, not a general impression.

### Why It Affects SEO

Metadata, headings, and structured data help search systems understand the page and shape how it can appear in results, snippets, rich results, and AI summaries. Product visibility depends on consistent page, schema, and feed data. Gaps can reduce merchant listing eligibility, product rich results, and purchase confidence.

### How To Verify

1. Identify the exact URL, template, brand workspace, connector account, or page group in scope.
2. Collect evidence from: Firecrawl, Playwright, GSC, GMC, GA4, Shopify, CMS/code, Human/context, Shopify or CMS.
3. Use browser-rendered evidence before claiming the item is absent or broken.
4. Compare visible page content, structured data, and feed or platform values for consistency.
5. Record pass, fail, not_applicable, or not_checked_blocked in the audit matrix with an artifact reference.

### Evidence Sources

Firecrawl, Playwright, GSC, GMC, GA4, Shopify, CMS/code, Human/context, Shopify or CMS

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

Item ID: `ecommerce-seo.18-common-anti-patterns.69f65fe3`

Original checklist item: Merchant feed prices, schema prices, and visible prices disagree.

### What It Means

Confirm whether the audited scope satisfies this requirement: "Merchant feed prices, schema prices, and visible prices disagree." In practice, this means the reviewer needs concrete evidence, not a general impression.

### Why It Affects SEO

Metadata, headings, and structured data help search systems understand the page and shape how it can appear in results, snippets, rich results, and AI summaries. Product visibility depends on consistent page, schema, and feed data. Gaps can reduce merchant listing eligibility, product rich results, and purchase confidence.

### How To Verify

1. Identify the exact URL, template, brand workspace, connector account, or page group in scope.
2. Collect evidence from: Firecrawl, Playwright, GSC, GMC, GA4, Shopify, CMS/code, Human/context, Shopify or CMS.
3. Use browser-rendered evidence before claiming the item is absent or broken.
4. Compare visible page content, structured data, and feed or platform values for consistency.
5. Record pass, fail, not_applicable, or not_checked_blocked in the audit matrix with an artifact reference.

### Evidence Sources

Firecrawl, Playwright, GSC, GMC, GA4, Shopify, CMS/code, Human/context, Shopify or CMS

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

## Item 3

Item ID: `ecommerce-seo.18-common-anti-patterns.17660f47`

Original checklist item: All variant URLs canonicalize to one product even when variants have distinct demand and content.

### What It Means

Confirm whether the audited scope satisfies this requirement: "All variant URLs canonicalize to one product even when variants have distinct demand and content." In practice, this means the reviewer needs concrete evidence, not a general impression.

### Why It Affects SEO

Product visibility depends on consistent page, schema, and feed data. Gaps can reduce merchant listing eligibility, product rich results, and purchase confidence.

### How To Verify

1. Identify the exact URL, template, brand workspace, connector account, or page group in scope.
2. Collect evidence from: Firecrawl, Playwright, GSC, GMC, GA4, Shopify, CMS/code, Human/context, Shopify or CMS.
3. Compare visible page content, structured data, and feed or platform values for consistency.
4. Record pass, fail, not_applicable, or not_checked_blocked in the audit matrix with an artifact reference.

### Evidence Sources

Firecrawl, Playwright, GSC, GMC, GA4, Shopify, CMS/code, Human/context, Shopify or CMS

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

## Item 4

Item ID: `ecommerce-seo.18-common-anti-patterns.799328da`

Original checklist item: All paginated category pages canonicalize to page 1.

### What It Means

Confirm whether the audited scope satisfies this requirement: "All paginated category pages canonicalize to page 1." In practice, this means the reviewer needs concrete evidence, not a general impression.

### Why It Affects SEO

Product visibility depends on consistent page, schema, and feed data. Gaps can reduce merchant listing eligibility, product rich results, and purchase confidence. Local SEO depends on accurate entity, location, category, review, and profile data. Inconsistency can weaken relevance, prominence, and customer trust.

### How To Verify

1. Identify the exact URL, template, brand workspace, connector account, or page group in scope.
2. Collect evidence from: Firecrawl, Playwright, GSC, GMC, GA4, Shopify, CMS/code, Human/context, Shopify or CMS.
3. Record pass, fail, not_applicable, or not_checked_blocked in the audit matrix with an artifact reference.

### Evidence Sources

Firecrawl, Playwright, GSC, GMC, GA4, Shopify, CMS/code, Human/context, Shopify or CMS

### Pass Criteria

The item is verified as true for the scoped URL, template, brand, connector account, or page group, and the audit row includes a specific evidence source and artifact reference.

### Fail Criteria

The evidence shows the requirement is missing, inconsistent, inaccurate, inaccessible, risky, or materially incomplete for the audited scope.

### Common Fix

Have merchandising, marketing, or engineering make the smallest change that satisfies the evidence requirement, then rerun the check.

### Owner

merchandising, marketing, or engineering

### Notes

If the required connector, browser rendering, platform export, or human context is unavailable, mark the audit row as `not_checked_blocked` and name the missing access or artifact.

## Item 5

Item ID: `ecommerce-seo.18-common-anti-patterns.41f9aa5a`

Original checklist item: Filter combinations create unlimited crawlable URLs with duplicate or empty product sets.

### What It Means

Confirm whether the audited scope satisfies this requirement: "Filter combinations create unlimited crawlable URLs with duplicate or empty product sets." In practice, this means the reviewer needs concrete evidence, not a general impression.

### Why It Affects SEO

Product visibility depends on consistent page, schema, and feed data. Gaps can reduce merchant listing eligibility, product rich results, and purchase confidence.

### How To Verify

1. Identify the exact URL, template, brand workspace, connector account, or page group in scope.
2. Collect evidence from: Firecrawl, Playwright, GSC, GMC, GA4, Shopify, CMS/code, Human/context, Shopify or CMS.
3. Compare visible page content, structured data, and feed or platform values for consistency.
4. Record pass, fail, not_applicable, or not_checked_blocked in the audit matrix with an artifact reference.

### Evidence Sources

Firecrawl, Playwright, GSC, GMC, GA4, Shopify, CMS/code, Human/context, Shopify or CMS

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

## Item 6

Item ID: `ecommerce-seo.18-common-anti-patterns.cceabdd3`

Original checklist item: Product pages use manufacturer descriptions with no unique merchant value.

### What It Means

Confirm whether the audited scope satisfies this requirement: "Product pages use manufacturer descriptions with no unique merchant value." In practice, this means the reviewer needs concrete evidence, not a general impression.

### Why It Affects SEO

Product visibility depends on consistent page, schema, and feed data. Gaps can reduce merchant listing eligibility, product rich results, and purchase confidence.

### How To Verify

1. Identify the exact URL, template, brand workspace, connector account, or page group in scope.
2. Collect evidence from: Firecrawl, Playwright, GSC, GMC, GA4, Shopify, CMS/code, Human/context, Shopify or CMS.
3. Compare visible page content, structured data, and feed or platform values for consistency.
4. Record pass, fail, not_applicable, or not_checked_blocked in the audit matrix with an artifact reference.

### Evidence Sources

Firecrawl, Playwright, GSC, GMC, GA4, Shopify, CMS/code, Human/context, Shopify or CMS

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

## Item 7

Item ID: `ecommerce-seo.18-common-anti-patterns.0cbb6422`

Original checklist item: Category pages are thin product grids with no helpful browse path or internal links.

### What It Means

Confirm whether the audited scope satisfies this requirement: "Category pages are thin product grids with no helpful browse path or internal links." In practice, this means the reviewer needs concrete evidence, not a general impression.

### Why It Affects SEO

Useful, source-backed content improves relevance, user confidence, and eligibility for sensitive or competitive queries. Weak or unsupported content can suppress trust and conversions. Architecture controls how users and crawlers find important pages. Good internal linking helps distribute context, priority, and crawl paths.

### How To Verify

1. Identify the exact URL, template, brand workspace, connector account, or page group in scope.
2. Collect evidence from: Firecrawl, Playwright, GSC, GMC, GA4, Shopify, CMS/code, Human/context, Shopify or CMS.
3. Use browser-rendered evidence before claiming the item is absent or broken.
4. Compare visible page content, structured data, and feed or platform values for consistency.
5. Record pass, fail, not_applicable, or not_checked_blocked in the audit matrix with an artifact reference.

### Evidence Sources

Firecrawl, Playwright, GSC, GMC, GA4, Shopify, CMS/code, Human/context, Shopify or CMS

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

## Item 8

Item ID: `ecommerce-seo.18-common-anti-patterns.cb606a5d`

Original checklist item: Internal search result pages are indexed by accident.

### What It Means

Confirm whether the audited scope satisfies this requirement: "Internal search result pages are indexed by accident." In practice, this means the reviewer needs concrete evidence, not a general impression.

### Why It Affects SEO

Product visibility depends on consistent page, schema, and feed data. Gaps can reduce merchant listing eligibility, product rich results, and purchase confidence.

### How To Verify

1. Identify the exact URL, template, brand workspace, connector account, or page group in scope.
2. Collect evidence from: Firecrawl, Playwright, GSC, GMC, GA4, Shopify, CMS/code, Human/context, Shopify or CMS.
3. Record pass, fail, not_applicable, or not_checked_blocked in the audit matrix with an artifact reference.

### Evidence Sources

Firecrawl, Playwright, GSC, GMC, GA4, Shopify, CMS/code, Human/context, Shopify or CMS

### Pass Criteria

The item is verified as true for the scoped URL, template, brand, connector account, or page group, and the audit row includes a specific evidence source and artifact reference.

### Fail Criteria

The evidence shows the requirement is missing, inconsistent, inaccurate, inaccessible, risky, or materially incomplete for the audited scope.

### Common Fix

Have merchandising, marketing, or engineering make the smallest change that satisfies the evidence requirement, then rerun the check.

### Owner

merchandising, marketing, or engineering

### Notes

If the required connector, browser rendering, platform export, or human context is unavailable, mark the audit row as `not_checked_blocked` and name the missing access or artifact.

## Item 9

Item ID: `ecommerce-seo.18-common-anti-patterns.e4b2cde6`

Original checklist item: Out-of-stock products redirect to unrelated pages or the homepage.

### What It Means

Confirm whether the audited scope satisfies this requirement: "Out-of-stock products redirect to unrelated pages or the homepage." In practice, this means the reviewer needs concrete evidence, not a general impression.

### Why It Affects SEO

Product visibility depends on consistent page, schema, and feed data. Gaps can reduce merchant listing eligibility, product rich results, and purchase confidence. Search engines cannot rank what they cannot discover, render, canonicalize, or keep indexable. This check protects crawl access, index coverage, and canonical signal quality.

### How To Verify

1. Identify the exact URL, template, brand workspace, connector account, or page group in scope.
2. Collect evidence from: Firecrawl, Playwright, GSC, GMC, GA4, Shopify, CMS/code, Human/context, Shopify or CMS.
3. Record pass, fail, not_applicable, or not_checked_blocked in the audit matrix with an artifact reference.

### Evidence Sources

Firecrawl, Playwright, GSC, GMC, GA4, Shopify, CMS/code, Human/context, Shopify or CMS

### Pass Criteria

The item is verified as true for the scoped URL, template, brand, connector account, or page group, and the audit row includes a specific evidence source and artifact reference.

### Fail Criteria

The evidence shows the requirement is missing, inconsistent, inaccurate, inaccessible, risky, or materially incomplete for the audited scope.

### Common Fix

Update the template, metadata, server response, robots policy, sitemap, or structured data source, then rerun rendered and crawl checks.

### Owner

merchandising, marketing, or engineering

### Notes

If the required connector, browser rendering, platform export, or human context is unavailable, mark the audit row as `not_checked_blocked` and name the missing access or artifact.

## Item 10

Item ID: `ecommerce-seo.18-common-anti-patterns.44c2b8f2`

Original checklist item: Reviews, ratings, or availability are marked up when users cannot see them.

### What It Means

Confirm whether the audited scope satisfies this requirement: "Reviews, ratings, or availability are marked up when users cannot see them." In practice, this means the reviewer needs concrete evidence, not a general impression.

### Why It Affects SEO

Product visibility depends on consistent page, schema, and feed data. Gaps can reduce merchant listing eligibility, product rich results, and purchase confidence.

### How To Verify

1. Identify the exact URL, template, brand workspace, connector account, or page group in scope.
2. Collect evidence from: Firecrawl, Playwright, GSC, GMC, GA4, Shopify, CMS/code, Human/context, Shopify or CMS, GBP, Google Maps, GSC Links, Bing Webmaster Tools, manual SERP.
3. Compare visible page content, structured data, and feed or platform values for consistency.
4. Record pass, fail, not_applicable, or not_checked_blocked in the audit matrix with an artifact reference.

### Evidence Sources

Firecrawl, Playwright, GSC, GMC, GA4, Shopify, CMS/code, Human/context, Shopify or CMS, GBP, Google Maps, GSC Links, Bing Webmaster Tools, manual SERP

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

## Item 11

Item ID: `ecommerce-seo.18-common-anti-patterns.d131b007`

Original checklist item: Product JSON-LD is generated by multiple apps with conflicting values.

### What It Means

Confirm whether the audited scope satisfies this requirement: "Product JSON-LD is generated by multiple apps with conflicting values." In practice, this means the reviewer needs concrete evidence, not a general impression.

### Why It Affects SEO

Product visibility depends on consistent page, schema, and feed data. Gaps can reduce merchant listing eligibility, product rich results, and purchase confidence.

### How To Verify

1. Identify the exact URL, template, brand workspace, connector account, or page group in scope.
2. Collect evidence from: Firecrawl, Playwright, GSC, GMC, GA4, Shopify, CMS/code, Human/context, Shopify or CMS.
3. Compare visible page content, structured data, and feed or platform values for consistency.
4. Record pass, fail, not_applicable, or not_checked_blocked in the audit matrix with an artifact reference.

### Evidence Sources

Firecrawl, Playwright, GSC, GMC, GA4, Shopify, CMS/code, Human/context, Shopify or CMS

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

## Item 12

Item ID: `ecommerce-seo.18-common-anti-patterns.bb04a94e`

Original checklist item: Product images are blocked, low quality, swapped by JavaScript only, or inconsistent with the feed.

### What It Means

Confirm whether the audited scope satisfies this requirement: "Product images are blocked, low quality, swapped by JavaScript only, or inconsistent with the feed." In practice, this means the reviewer needs concrete evidence, not a general impression.

### Why It Affects SEO

Product visibility depends on consistent page, schema, and feed data. Gaps can reduce merchant listing eligibility, product rich results, and purchase confidence.

### How To Verify

1. Identify the exact URL, template, brand workspace, connector account, or page group in scope.
2. Collect evidence from: Firecrawl, Playwright, GSC, GMC, GA4, Shopify, CMS/code, Human/context, Shopify or CMS.
3. Use browser-rendered evidence before claiming the item is absent or broken.
4. Compare visible page content, structured data, and feed or platform values for consistency.
5. Record pass, fail, not_applicable, or not_checked_blocked in the audit matrix with an artifact reference.

### Evidence Sources

Firecrawl, Playwright, GSC, GMC, GA4, Shopify, CMS/code, Human/context, Shopify or CMS

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

## Item 13

Item ID: `ecommerce-seo.18-common-anti-patterns.aa19debb`

Original checklist item: Storefront, feed, schema, and analytics owners work from different product data definitions.

### What It Means

Confirm whether the audited scope satisfies this requirement: "Storefront, feed, schema, and analytics owners work from different product data definitions." In practice, this means the reviewer needs concrete evidence, not a general impression.

### Why It Affects SEO

Metadata, headings, and structured data help search systems understand the page and shape how it can appear in results, snippets, rich results, and AI summaries. Product visibility depends on consistent page, schema, and feed data. Gaps can reduce merchant listing eligibility, product rich results, and purchase confidence.

### How To Verify

1. Identify the exact URL, template, brand workspace, connector account, or page group in scope.
2. Collect evidence from: Firecrawl, Playwright, GSC, GMC, GA4, Shopify, CMS/code, Human/context, Shopify or CMS.
3. Use browser-rendered evidence before claiming the item is absent or broken.
4. Compare visible page content, structured data, and feed or platform values for consistency.
5. Record pass, fail, not_applicable, or not_checked_blocked in the audit matrix with an artifact reference.

### Evidence Sources

Firecrawl, Playwright, GSC, GMC, GA4, Shopify, CMS/code, Human/context, Shopify or CMS

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

Item ID: `ecommerce-seo.18-common-anti-patterns.1e7e18e4`

Original checklist item: "AI SEO" work adds hidden instructions or fake facts instead of improving product clarity and data consistency.

### What It Means

Confirm whether the audited scope satisfies this requirement: ""AI SEO" work adds hidden instructions or fake facts instead of improving product clarity and data consistency." In practice, this means the reviewer needs concrete evidence, not a general impression.

### Why It Affects SEO

Product visibility depends on consistent page, schema, and feed data. Gaps can reduce merchant listing eligibility, product rich results, and purchase confidence. Answer engines need crawlable, clear, well-supported information they can cite or summarize. This check improves extractability, factual grounding, and mention quality.

### How To Verify

1. Identify the exact URL, template, brand workspace, connector account, or page group in scope.
2. Collect evidence from: Firecrawl, Playwright, GSC, GMC, GA4, Shopify, CMS/code, Human/context, Shopify or CMS, saved prompt set, manual AI SERP.
3. Use browser-rendered evidence before claiming the item is absent or broken.
4. Compare visible page content, structured data, and feed or platform values for consistency.
5. Record prompt wording, platform, location, date, account state, cited URLs, and answer summary.
6. Record pass, fail, not_applicable, or not_checked_blocked in the audit matrix with an artifact reference.

### Evidence Sources

Firecrawl, Playwright, GSC, GMC, GA4, Shopify, CMS/code, Human/context, Shopify or CMS, saved prompt set, manual AI SERP

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
