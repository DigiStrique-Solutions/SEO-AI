---
title: 4A. Technical Infrastructure And Production Health
sidebar_position: 10
---

# 4A. Technical Infrastructure And Production Health

Checklist: `generic-on-page-seo`

Source: `docs/checklists/generic-on-page-seo-checklist.md`

This page explains every checklist item in this section. Each item should still be verified with evidence before it is marked `pass` or `fail`.

## Item 1

Item ID: `generic-on-page-seo.4a-technical-infrastructure-and-production-health.fa4c59b5`

Original checklist item: HTTPS is enabled for all public canonical pages.

### What It Means

Confirm whether the audited scope satisfies this requirement: "HTTPS is enabled for all public canonical pages." In practice, this means the reviewer needs concrete evidence, not a general impression.

### Why It Affects SEO

Intent alignment affects whether the page deserves to show for the target query. This check keeps the page focused on the searcher's job instead of only matching keywords. Search engines cannot rank what they cannot discover, render, canonicalize, or keep indexable. This check protects crawl access, index coverage, and canonical signal quality.

### How To Verify

1. Identify the exact URL, template, brand workspace, connector account, or page group in scope.
2. Collect evidence from: GSC, Firecrawl, Playwright, LH, CMS/code, OSS, Monitoring, Human/context.
3. Record pass, fail, not_applicable, or not_checked_blocked in the audit matrix with an artifact reference.

### Evidence Sources

GSC, Firecrawl, Playwright, LH, CMS/code, OSS, Monitoring, Human/context

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

Item ID: `generic-on-page-seo.4a-technical-infrastructure-and-production-health.2a6c35c0`

Original checklist item: TLS certificate is valid, trusted, covers the right hostnames, and is monitored before expiry.

### What It Means

Confirm whether the audited scope satisfies this requirement: "TLS certificate is valid, trusted, covers the right hostnames, and is monitored before expiry." In practice, this means the reviewer needs concrete evidence, not a general impression.

### Why It Affects SEO

Intent alignment affects whether the page deserves to show for the target query. This check keeps the page focused on the searcher's job instead of only matching keywords.

### How To Verify

1. Identify the exact URL, template, brand workspace, connector account, or page group in scope.
2. Collect evidence from: GSC, Firecrawl, Playwright, LH, CMS/code, OSS, Monitoring, Human/context.
3. Record pass, fail, not_applicable, or not_checked_blocked in the audit matrix with an artifact reference.

### Evidence Sources

GSC, Firecrawl, Playwright, LH, CMS/code, OSS, Monitoring, Human/context

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

Item ID: `generic-on-page-seo.4a-technical-infrastructure-and-production-health.0dc2a8fa`

Original checklist item: HTTP redirects to HTTPS with the intended redirect status.

### What It Means

Confirm whether the audited scope satisfies this requirement: "HTTP redirects to HTTPS with the intended redirect status." In practice, this means the reviewer needs concrete evidence, not a general impression.

### Why It Affects SEO

Intent alignment affects whether the page deserves to show for the target query. This check keeps the page focused on the searcher's job instead of only matching keywords. Search engines cannot rank what they cannot discover, render, canonicalize, or keep indexable. This check protects crawl access, index coverage, and canonical signal quality.

### How To Verify

1. Identify the exact URL, template, brand workspace, connector account, or page group in scope.
2. Collect evidence from: GSC, Firecrawl, Playwright, LH, CMS/code, OSS, Monitoring, Human/context.
3. Record pass, fail, not_applicable, or not_checked_blocked in the audit matrix with an artifact reference.

### Evidence Sources

GSC, Firecrawl, Playwright, LH, CMS/code, OSS, Monitoring, Human/context

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

## Item 4

Item ID: `generic-on-page-seo.4a-technical-infrastructure-and-production-health.a993a6dc`

Original checklist item: Mixed content is not present on rendered pages.

### What It Means

Confirm whether the audited scope satisfies this requirement: "Mixed content is not present on rendered pages." In practice, this means the reviewer needs concrete evidence, not a general impression.

### Why It Affects SEO

Intent alignment affects whether the page deserves to show for the target query. This check keeps the page focused on the searcher's job instead of only matching keywords.

### How To Verify

1. Identify the exact URL, template, brand workspace, connector account, or page group in scope.
2. Collect evidence from: GSC, Firecrawl, Playwright, LH, CMS/code, OSS, Monitoring, Human/context.
3. Record pass, fail, not_applicable, or not_checked_blocked in the audit matrix with an artifact reference.

### Evidence Sources

GSC, Firecrawl, Playwright, LH, CMS/code, OSS, Monitoring, Human/context

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

## Item 5

Item ID: `generic-on-page-seo.4a-technical-infrastructure-and-production-health.31347dac`

Original checklist item: HSTS is reviewed for production sites where forced HTTPS is safe for the domain and subdomains.

### What It Means

Confirm whether the audited scope satisfies this requirement: "HSTS is reviewed for production sites where forced HTTPS is safe for the domain and subdomains." In practice, this means the reviewer needs concrete evidence, not a general impression.

### Why It Affects SEO

Intent alignment affects whether the page deserves to show for the target query. This check keeps the page focused on the searcher's job instead of only matching keywords.

### How To Verify

1. Identify the exact URL, template, brand workspace, connector account, or page group in scope.
2. Collect evidence from: GSC, Firecrawl, Playwright, LH, CMS/code, OSS, Monitoring, Human/context.
3. Record pass, fail, not_applicable, or not_checked_blocked in the audit matrix with an artifact reference.

### Evidence Sources

GSC, Firecrawl, Playwright, LH, CMS/code, OSS, Monitoring, Human/context

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

## Item 6

Item ID: `generic-on-page-seo.4a-technical-infrastructure-and-production-health.94dc1121`

Original checklist item: CDN, firewall, WAF, bot protection, rate limits, and geo rules do not block important users, Googlebot, GSC fetchers, AdsBot, Merchant Center, or other required crawlers.

### What It Means

Confirm whether the audited scope satisfies this requirement: "CDN, firewall, WAF, bot protection, rate limits, and geo rules do not block important users, Googlebot, GSC fetchers, AdsBot, Merchant Center, or other required crawlers." In practice, this means the reviewer needs concrete evidence, not a general impression.

### Why It Affects SEO

Intent alignment affects whether the page deserves to show for the target query. This check keeps the page focused on the searcher's job instead of only matching keywords. Product visibility depends on consistent page, schema, and feed data. Gaps can reduce merchant listing eligibility, product rich results, and purchase confidence.

### How To Verify

1. Identify the exact URL, template, brand workspace, connector account, or page group in scope.
2. Collect evidence from: GSC, Firecrawl, Playwright, LH, CMS/code, OSS, Monitoring, Human/context, Shopify or CMS, GMC.
3. Use Search Console data when access exists; otherwise mark the row as blocked with the missing property or permission.
4. Compare visible page content, structured data, and feed or platform values for consistency.
5. Record pass, fail, not_applicable, or not_checked_blocked in the audit matrix with an artifact reference.

### Evidence Sources

GSC, Firecrawl, Playwright, LH, CMS/code, OSS, Monitoring, Human/context, Shopify or CMS, GMC

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

Item ID: `generic-on-page-seo.4a-technical-infrastructure-and-production-health.35495f6d`

Original checklist item: Googlebot handling is verified with reverse DNS or official Google IP ranges, not only user-agent strings.

### What It Means

Confirm whether the audited scope satisfies this requirement: "Googlebot handling is verified with reverse DNS or official Google IP ranges, not only user-agent strings." In practice, this means the reviewer needs concrete evidence, not a general impression.

### Why It Affects SEO

Intent alignment affects whether the page deserves to show for the target query. This check keeps the page focused on the searcher's job instead of only matching keywords.

### How To Verify

1. Identify the exact URL, template, brand workspace, connector account, or page group in scope.
2. Collect evidence from: GSC, Firecrawl, Playwright, LH, CMS/code, OSS, Monitoring, Human/context.
3. Record pass, fail, not_applicable, or not_checked_blocked in the audit matrix with an artifact reference.

### Evidence Sources

GSC, Firecrawl, Playwright, LH, CMS/code, OSS, Monitoring, Human/context

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

Item ID: `generic-on-page-seo.4a-technical-infrastructure-and-production-health.e8ab48c8`

Original checklist item: Important pages do not return unexpected 4xx, 5xx, 429, timeout, DNS, TLS, or connection errors.

### What It Means

Confirm whether the audited scope satisfies this requirement: "Important pages do not return unexpected 4xx, 5xx, 429, timeout, DNS, TLS, or connection errors." In practice, this means the reviewer needs concrete evidence, not a general impression.

### Why It Affects SEO

Intent alignment affects whether the page deserves to show for the target query. This check keeps the page focused on the searcher's job instead of only matching keywords. Product visibility depends on consistent page, schema, and feed data. Gaps can reduce merchant listing eligibility, product rich results, and purchase confidence.

### How To Verify

1. Identify the exact URL, template, brand workspace, connector account, or page group in scope.
2. Collect evidence from: GSC, Firecrawl, Playwright, LH, CMS/code, OSS, Monitoring, Human/context, Shopify or CMS, GMC.
3. Compare visible page content, structured data, and feed or platform values for consistency.
4. Record pass, fail, not_applicable, or not_checked_blocked in the audit matrix with an artifact reference.

### Evidence Sources

GSC, Firecrawl, Playwright, LH, CMS/code, OSS, Monitoring, Human/context, Shopify or CMS, GMC

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

## Item 9

Item ID: `generic-on-page-seo.4a-technical-infrastructure-and-production-health.37a80e25`

Original checklist item: Uptime, server response, and error-rate monitoring exist for templates and sections that matter to organic traffic.

### What It Means

Confirm whether the audited scope satisfies this requirement: "Uptime, server response, and error-rate monitoring exist for templates and sections that matter to organic traffic." In practice, this means the reviewer needs concrete evidence, not a general impression.

### Why It Affects SEO

Intent alignment affects whether the page deserves to show for the target query. This check keeps the page focused on the searcher's job instead of only matching keywords. SEO decisions need reliable measurement. This check prevents prioritization based on incomplete, unscoped, or misleading data.

### How To Verify

1. Identify the exact URL, template, brand workspace, connector account, or page group in scope.
2. Collect evidence from: GSC, Firecrawl, Playwright, LH, CMS/code, OSS, Monitoring, Human/context.
3. Record pass, fail, not_applicable, or not_checked_blocked in the audit matrix with an artifact reference.

### Evidence Sources

GSC, Firecrawl, Playwright, LH, CMS/code, OSS, Monitoring, Human/context

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

Item ID: `generic-on-page-seo.4a-technical-infrastructure-and-production-health.a7955152`

Original checklist item: GSC Crawl Stats or server/CDN logs are reviewed for large, fast-changing, or heavily parameterized sites.

### What It Means

Confirm whether the audited scope satisfies this requirement: "GSC Crawl Stats or server/CDN logs are reviewed for large, fast-changing, or heavily parameterized sites." In practice, this means the reviewer needs concrete evidence, not a general impression.

### Why It Affects SEO

Intent alignment affects whether the page deserves to show for the target query. This check keeps the page focused on the searcher's job instead of only matching keywords. Search engines cannot rank what they cannot discover, render, canonicalize, or keep indexable. This check protects crawl access, index coverage, and canonical signal quality.

### How To Verify

1. Identify the exact URL, template, brand workspace, connector account, or page group in scope.
2. Collect evidence from: GSC, Firecrawl, Playwright, LH, CMS/code, OSS, Monitoring, Human/context.
3. Use Search Console data when access exists; otherwise mark the row as blocked with the missing property or permission.
4. Record pass, fail, not_applicable, or not_checked_blocked in the audit matrix with an artifact reference.

### Evidence Sources

GSC, Firecrawl, Playwright, LH, CMS/code, OSS, Monitoring, Human/context

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

## Item 11

Item ID: `generic-on-page-seo.4a-technical-infrastructure-and-production-health.130fa5cb`

Original checklist item: Crawl budget issues are investigated only when the site scale or crawl behavior justifies it.

### What It Means

Confirm whether the audited scope satisfies this requirement: "Crawl budget issues are investigated only when the site scale or crawl behavior justifies it." In practice, this means the reviewer needs concrete evidence, not a general impression.

### Why It Affects SEO

Intent alignment affects whether the page deserves to show for the target query. This check keeps the page focused on the searcher's job instead of only matching keywords. Search engines cannot rank what they cannot discover, render, canonicalize, or keep indexable. This check protects crawl access, index coverage, and canonical signal quality.

### How To Verify

1. Identify the exact URL, template, brand workspace, connector account, or page group in scope.
2. Collect evidence from: GSC, Firecrawl, Playwright, LH, CMS/code, OSS, Monitoring, Human/context.
3. Record pass, fail, not_applicable, or not_checked_blocked in the audit matrix with an artifact reference.

### Evidence Sources

GSC, Firecrawl, Playwright, LH, CMS/code, OSS, Monitoring, Human/context

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

Item ID: `generic-on-page-seo.4a-technical-infrastructure-and-production-health.7e65ae08`

Original checklist item: Staging, preview, QA, dev, and test environments are blocked by authentication or network controls, not only robots.txt.

### What It Means

Confirm whether the audited scope satisfies this requirement: "Staging, preview, QA, dev, and test environments are blocked by authentication or network controls, not only robots.txt." In practice, this means the reviewer needs concrete evidence, not a general impression.

### Why It Affects SEO

Intent alignment affects whether the page deserves to show for the target query. This check keeps the page focused on the searcher's job instead of only matching keywords. Search engines cannot rank what they cannot discover, render, canonicalize, or keep indexable. This check protects crawl access, index coverage, and canonical signal quality.

### How To Verify

1. Identify the exact URL, template, brand workspace, connector account, or page group in scope.
2. Collect evidence from: GSC, Firecrawl, Playwright, LH, CMS/code, OSS, Monitoring, Human/context.
3. Record pass, fail, not_applicable, or not_checked_blocked in the audit matrix with an artifact reference.

### Evidence Sources

GSC, Firecrawl, Playwright, LH, CMS/code, OSS, Monitoring, Human/context

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

Item ID: `generic-on-page-seo.4a-technical-infrastructure-and-production-health.80766ce0`

Original checklist item: Staging or preview pages are not accidentally canonicalized from production pages.

### What It Means

Confirm whether the audited scope satisfies this requirement: "Staging or preview pages are not accidentally canonicalized from production pages." In practice, this means the reviewer needs concrete evidence, not a general impression.

### Why It Affects SEO

Intent alignment affects whether the page deserves to show for the target query. This check keeps the page focused on the searcher's job instead of only matching keywords.

### How To Verify

1. Identify the exact URL, template, brand workspace, connector account, or page group in scope.
2. Collect evidence from: GSC, Firecrawl, Playwright, LH, CMS/code, OSS, Monitoring, Human/context.
3. Record pass, fail, not_applicable, or not_checked_blocked in the audit matrix with an artifact reference.

### Evidence Sources

GSC, Firecrawl, Playwright, LH, CMS/code, OSS, Monitoring, Human/context

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

Item ID: `generic-on-page-seo.4a-technical-infrastructure-and-production-health.448d6270`

Original checklist item: Accidental indexation of non-production URLs is checked in GSC, logs, and manual search where relevant.

### What It Means

Confirm whether the audited scope satisfies this requirement: "Accidental indexation of non-production URLs is checked in GSC, logs, and manual search where relevant." In practice, this means the reviewer needs concrete evidence, not a general impression.

### Why It Affects SEO

Intent alignment affects whether the page deserves to show for the target query. This check keeps the page focused on the searcher's job instead of only matching keywords. SEO decisions need reliable measurement. This check prevents prioritization based on incomplete, unscoped, or misleading data.

### How To Verify

1. Identify the exact URL, template, brand workspace, connector account, or page group in scope.
2. Collect evidence from: GSC, Firecrawl, Playwright, LH, CMS/code, OSS, Monitoring, Human/context.
3. Use Search Console data when access exists; otherwise mark the row as blocked with the missing property or permission.
4. Record pass, fail, not_applicable, or not_checked_blocked in the audit matrix with an artifact reference.

### Evidence Sources

GSC, Firecrawl, Playwright, LH, CMS/code, OSS, Monitoring, Human/context

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

## Item 15

Item ID: `generic-on-page-seo.4a-technical-infrastructure-and-production-health.48e95618`

Original checklist item: Search Console Manual Actions and Security Issues are checked before major SEO recommendations.

### What It Means

Confirm whether the audited scope satisfies this requirement: "Search Console Manual Actions and Security Issues are checked before major SEO recommendations." In practice, this means the reviewer needs concrete evidence, not a general impression.

### Why It Affects SEO

Intent alignment affects whether the page deserves to show for the target query. This check keeps the page focused on the searcher's job instead of only matching keywords. Policy, spam, and compliance issues can block visibility or create legal and reputation risk. This check catches issues before optimization work amplifies them.

### How To Verify

1. Identify the exact URL, template, brand workspace, connector account, or page group in scope.
2. Collect evidence from: GSC, Firecrawl, Playwright, LH, CMS/code, OSS, Monitoring, Human/context.
3. Record pass, fail, not_applicable, or not_checked_blocked in the audit matrix with an artifact reference.

### Evidence Sources

GSC, Firecrawl, Playwright, LH, CMS/code, OSS, Monitoring, Human/context

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

Item ID: `generic-on-page-seo.4a-technical-infrastructure-and-production-health.28d374be`

Original checklist item: Hacked content, malware, phishing, injected spam, and suspicious outbound links are escalated as security issues, not normal SEO tickets.

### What It Means

Confirm whether the audited scope satisfies this requirement: "Hacked content, malware, phishing, injected spam, and suspicious outbound links are escalated as security issues, not normal SEO tickets." In practice, this means the reviewer needs concrete evidence, not a general impression.

### Why It Affects SEO

Intent alignment affects whether the page deserves to show for the target query. This check keeps the page focused on the searcher's job instead of only matching keywords. Policy, spam, and compliance issues can block visibility or create legal and reputation risk. This check catches issues before optimization work amplifies them.

### How To Verify

1. Identify the exact URL, template, brand workspace, connector account, or page group in scope.
2. Collect evidence from: GSC, Firecrawl, Playwright, LH, CMS/code, OSS, Monitoring, Human/context.
3. Use browser-rendered evidence before claiming the item is absent or broken.
4. Record pass, fail, not_applicable, or not_checked_blocked in the audit matrix with an artifact reference.

### Evidence Sources

GSC, Firecrawl, Playwright, LH, CMS/code, OSS, Monitoring, Human/context

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

## Item 17

Item ID: `generic-on-page-seo.4a-technical-infrastructure-and-production-health.5f2215c8`

Original checklist item: Migration launches include pre-launch crawl, redirect map, canonical and sitemap checks, robots/noindex cleanup, GSC validation, analytics annotation, and post-launch crawl.

### What It Means

Confirm whether the audited scope satisfies this requirement: "Migration launches include pre-launch crawl, redirect map, canonical and sitemap checks, robots/noindex cleanup, GSC validation, analytics annotation, and post-launch crawl." In practice, this means the reviewer needs concrete evidence, not a general impression.

### Why It Affects SEO

Intent alignment affects whether the page deserves to show for the target query. This check keeps the page focused on the searcher's job instead of only matching keywords. Search engines cannot rank what they cannot discover, render, canonicalize, or keep indexable. This check protects crawl access, index coverage, and canonical signal quality.

### How To Verify

1. Identify the exact URL, template, brand workspace, connector account, or page group in scope.
2. Collect evidence from: GSC, Firecrawl, Playwright, LH, CMS/code, OSS, Monitoring, Human/context.
3. Use Search Console data when access exists; otherwise mark the row as blocked with the missing property or permission.
4. Record pass, fail, not_applicable, or not_checked_blocked in the audit matrix with an artifact reference.

### Evidence Sources

GSC, Firecrawl, Playwright, LH, CMS/code, OSS, Monitoring, Human/context

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

## Item 18

Item ID: `generic-on-page-seo.4a-technical-infrastructure-and-production-health.24488867`

Original checklist item: Post-migration monitoring checks redirects, 404 or 410, soft 404s, 5xx, 429, sitemap coverage, indexation, traffic, and conversion impact.

### What It Means

Confirm whether the audited scope satisfies this requirement: "Post-migration monitoring checks redirects, 404 or 410, soft 404s, 5xx, 429, sitemap coverage, indexation, traffic, and conversion impact." In practice, this means the reviewer needs concrete evidence, not a general impression.

### Why It Affects SEO

Intent alignment affects whether the page deserves to show for the target query. This check keeps the page focused on the searcher's job instead of only matching keywords. Search engines cannot rank what they cannot discover, render, canonicalize, or keep indexable. This check protects crawl access, index coverage, and canonical signal quality.

### How To Verify

1. Identify the exact URL, template, brand workspace, connector account, or page group in scope.
2. Collect evidence from: GSC, Firecrawl, Playwright, LH, CMS/code, OSS, Monitoring, Human/context, GA4 or PostHog.
3. Use Search Console data when access exists; otherwise mark the row as blocked with the missing property or permission.
4. Use analytics data only when the property, date range, and conversion definitions are known.
5. Record pass, fail, not_applicable, or not_checked_blocked in the audit matrix with an artifact reference.

### Evidence Sources

GSC, Firecrawl, Playwright, LH, CMS/code, OSS, Monitoring, Human/context, GA4 or PostHog

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

Item ID: `generic-on-page-seo.4a-technical-infrastructure-and-production-health.a0663e70`

Original checklist item: Template-level deploy checks validate rendered title, meta description, canonical, robots, hreflang, schema, headings, internal links, status code, and primary content.

### What It Means

Confirm whether the audited scope satisfies this requirement: "Template-level deploy checks validate rendered title, meta description, canonical, robots, hreflang, schema, headings, internal links, status code, and primary content." In practice, this means the reviewer needs concrete evidence, not a general impression.

### Why It Affects SEO

Intent alignment affects whether the page deserves to show for the target query. This check keeps the page focused on the searcher's job instead of only matching keywords. Search engines cannot rank what they cannot discover, render, canonicalize, or keep indexable. This check protects crawl access, index coverage, and canonical signal quality.

### How To Verify

1. Identify the exact URL, template, brand workspace, connector account, or page group in scope.
2. Collect evidence from: GSC, Firecrawl, Playwright, LH, CMS/code, OSS, Monitoring, Human/context.
3. Use browser-rendered evidence before claiming the item is absent or broken.
4. Record pass, fail, not_applicable, or not_checked_blocked in the audit matrix with an artifact reference.

### Evidence Sources

GSC, Firecrawl, Playwright, LH, CMS/code, OSS, Monitoring, Human/context

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

## Item 20

Item ID: `generic-on-page-seo.4a-technical-infrastructure-and-production-health.5b19ed8c`

Original checklist item: Deploy regressions are sampled across important templates, not only the homepage.

### What It Means

Confirm whether the audited scope satisfies this requirement: "Deploy regressions are sampled across important templates, not only the homepage." In practice, this means the reviewer needs concrete evidence, not a general impression.

### Why It Affects SEO

Intent alignment affects whether the page deserves to show for the target query. This check keeps the page focused on the searcher's job instead of only matching keywords.

### How To Verify

1. Identify the exact URL, template, brand workspace, connector account, or page group in scope.
2. Collect evidence from: GSC, Firecrawl, Playwright, LH, CMS/code, OSS, Monitoring, Human/context.
3. Record pass, fail, not_applicable, or not_checked_blocked in the audit matrix with an artifact reference.

### Evidence Sources

GSC, Firecrawl, Playwright, LH, CMS/code, OSS, Monitoring, Human/context

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
