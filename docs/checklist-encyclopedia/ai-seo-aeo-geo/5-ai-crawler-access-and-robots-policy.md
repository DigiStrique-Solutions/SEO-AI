---
title: 5. AI Crawler Access And Robots Policy
sidebar_position: 10
---

# 5. AI Crawler Access And Robots Policy

Checklist: `ai-seo-aeo-geo`

Source: `docs/checklists/ai-seo-aeo-geo-checklist.md`

This page explains every checklist item in this section. Each item should still be verified with evidence before it is marked `pass` or `fail`.

## Item 1

Item ID: `ai-seo-aeo-geo.5-ai-crawler-access-and-robots-policy.d05a68e9`

Original checklist item: Robots.txt is reviewed for Googlebot, Bingbot, OAI-SearchBot, GPTBot, ChatGPT-User, PerplexityBot, ClaudeBot, Claude-SearchBot, Claude-User, and other relevant agents.

### What It Means

Confirm whether the audited scope satisfies this requirement: "Robots.txt is reviewed for Googlebot, Bingbot, OAI-SearchBot, GPTBot, ChatGPT-User, PerplexityBot, ClaudeBot, Claude-SearchBot, Claude-User, and other relevant agents." In practice, this means the reviewer needs concrete evidence, not a general impression.

### Why It Affects SEO

Search engines cannot rank what they cannot discover, render, canonicalize, or keep indexable. This check protects crawl access, index coverage, and canonical signal quality. Answer engines need crawlable, clear, well-supported information they can cite or summarize. This check improves extractability, factual grounding, and mention quality.

### How To Verify

1. Identify the exact URL, template, brand workspace, connector account, or page group in scope.
2. Collect evidence from: CMS/code, Logs/CDN/WAF, Firecrawl, Playwright, OSS, Human/context, saved prompt set, manual AI SERP, GSC.
3. Record pass, fail, not_applicable, or not_checked_blocked in the audit matrix with an artifact reference.

### Evidence Sources

CMS/code, Logs/CDN/WAF, Firecrawl, Playwright, OSS, Human/context, saved prompt set, manual AI SERP, GSC

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

Item ID: `ai-seo-aeo-geo.5-ai-crawler-access-and-robots-policy.236d86f9`

Original checklist item: Crawler roles are separated where the provider supports it: search/indexing, training, and user-triggered fetches.

### What It Means

Confirm whether the audited scope satisfies this requirement: "Crawler roles are separated where the provider supports it: search/indexing, training, and user-triggered fetches." In practice, this means the reviewer needs concrete evidence, not a general impression.

### Why It Affects SEO

Answer engines need crawlable, clear, well-supported information they can cite or summarize. This check improves extractability, factual grounding, and mention quality.

### How To Verify

1. Identify the exact URL, template, brand workspace, connector account, or page group in scope.
2. Collect evidence from: CMS/code, Logs/CDN/WAF, Firecrawl, Playwright, OSS, Human/context, saved prompt set, manual AI SERP, GSC.
3. Record pass, fail, not_applicable, or not_checked_blocked in the audit matrix with an artifact reference.

### Evidence Sources

CMS/code, Logs/CDN/WAF, Firecrawl, Playwright, OSS, Human/context, saved prompt set, manual AI SERP, GSC

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

Item ID: `ai-seo-aeo-geo.5-ai-crawler-access-and-robots-policy.42d62038`

Original checklist item: The business decision to allow or block AI training crawlers is documented separately from the decision to allow AI search or citation crawlers.

### What It Means

Confirm whether the audited scope satisfies this requirement: "The business decision to allow or block AI training crawlers is documented separately from the decision to allow AI search or citation crawlers." In practice, this means the reviewer needs concrete evidence, not a general impression.

### Why It Affects SEO

External mentions, links, reviews, and citations help establish reputation and discovery beyond the site. Risky patterns can create spam or compliance exposure. Answer engines need crawlable, clear, well-supported information they can cite or summarize. This check improves extractability, factual grounding, and mention quality.

### How To Verify

1. Identify the exact URL, template, brand workspace, connector account, or page group in scope.
2. Collect evidence from: CMS/code, Logs/CDN/WAF, Firecrawl, Playwright, OSS, Human/context, GSC Links, Bing Webmaster Tools, manual SERP, saved prompt set, manual AI SERP, GSC.
3. Record prompt wording, platform, location, date, account state, cited URLs, and answer summary.
4. Record pass, fail, not_applicable, or not_checked_blocked in the audit matrix with an artifact reference.

### Evidence Sources

CMS/code, Logs/CDN/WAF, Firecrawl, Playwright, OSS, Human/context, GSC Links, Bing Webmaster Tools, manual SERP, saved prompt set, manual AI SERP, GSC

### Pass Criteria

The item is verified as true for the scoped URL, template, brand, connector account, or page group, and the audit row includes a specific evidence source and artifact reference.

### Fail Criteria

The evidence shows the requirement is missing, inconsistent, inaccurate, inaccessible, risky, or materially incomplete for the audited scope.

### Common Fix

Prioritize legitimate relationship, PR, citation, or partner updates and avoid manipulative link tactics.

### Owner

marketing or partnerships

### Notes

If the required connector, browser rendering, platform export, or human context is unavailable, mark the audit row as `not_checked_blocked` and name the missing access or artifact.

## Item 4

Item ID: `ai-seo-aeo-geo.5-ai-crawler-access-and-robots-policy.bf9053d2`

Original checklist item: WAF, CDN, bot protection, rate limits, geo blocks, and JavaScript challenges do not accidentally block required search or AI crawlers.

### What It Means

Confirm whether the audited scope satisfies this requirement: "WAF, CDN, bot protection, rate limits, geo blocks, and JavaScript challenges do not accidentally block required search or AI crawlers." In practice, this means the reviewer needs concrete evidence, not a general impression.

### Why It Affects SEO

Answer engines need crawlable, clear, well-supported information they can cite or summarize. This check improves extractability, factual grounding, and mention quality.

### How To Verify

1. Identify the exact URL, template, brand workspace, connector account, or page group in scope.
2. Collect evidence from: CMS/code, Logs/CDN/WAF, Firecrawl, Playwright, OSS, Human/context, saved prompt set, manual AI SERP, GSC.
3. Use browser-rendered evidence before claiming the item is absent or broken.
4. Record prompt wording, platform, location, date, account state, cited URLs, and answer summary.
5. Record pass, fail, not_applicable, or not_checked_blocked in the audit matrix with an artifact reference.

### Evidence Sources

CMS/code, Logs/CDN/WAF, Firecrawl, Playwright, OSS, Human/context, saved prompt set, manual AI SERP, GSC

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

Item ID: `ai-seo-aeo-geo.5-ai-crawler-access-and-robots-policy.68ff5415`

Original checklist item: Crawler verification uses official IP ranges, reverse DNS, provider docs, or verified bot tooling where available.

### What It Means

Confirm whether the audited scope satisfies this requirement: "Crawler verification uses official IP ranges, reverse DNS, provider docs, or verified bot tooling where available." In practice, this means the reviewer needs concrete evidence, not a general impression.

### Why It Affects SEO

Answer engines need crawlable, clear, well-supported information they can cite or summarize. This check improves extractability, factual grounding, and mention quality.

### How To Verify

1. Identify the exact URL, template, brand workspace, connector account, or page group in scope.
2. Collect evidence from: CMS/code, Logs/CDN/WAF, Firecrawl, Playwright, OSS, Human/context, saved prompt set, manual AI SERP, GSC.
3. Record pass, fail, not_applicable, or not_checked_blocked in the audit matrix with an artifact reference.

### Evidence Sources

CMS/code, Logs/CDN/WAF, Firecrawl, Playwright, OSS, Human/context, saved prompt set, manual AI SERP, GSC

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

Item ID: `ai-seo-aeo-geo.5-ai-crawler-access-and-robots-policy.a0343984`

Original checklist item: Logs are sampled for blocked, throttled, redirected, or challenged AI/search crawler requests.

### What It Means

Confirm whether the audited scope satisfies this requirement: "Logs are sampled for blocked, throttled, redirected, or challenged AI/search crawler requests." In practice, this means the reviewer needs concrete evidence, not a general impression.

### Why It Affects SEO

Answer engines need crawlable, clear, well-supported information they can cite or summarize. This check improves extractability, factual grounding, and mention quality.

### How To Verify

1. Identify the exact URL, template, brand workspace, connector account, or page group in scope.
2. Collect evidence from: CMS/code, Logs/CDN/WAF, Firecrawl, Playwright, OSS, Human/context, saved prompt set, manual AI SERP, GSC.
3. Record prompt wording, platform, location, date, account state, cited URLs, and answer summary.
4. Record pass, fail, not_applicable, or not_checked_blocked in the audit matrix with an artifact reference.

### Evidence Sources

CMS/code, Logs/CDN/WAF, Firecrawl, Playwright, OSS, Human/context, saved prompt set, manual AI SERP, GSC

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

Item ID: `ai-seo-aeo-geo.5-ai-crawler-access-and-robots-policy.6e7f812f`

Original checklist item: Blocking a crawler is documented with expected visibility tradeoffs.

### What It Means

Confirm whether the audited scope satisfies this requirement: "Blocking a crawler is documented with expected visibility tradeoffs." In practice, this means the reviewer needs concrete evidence, not a general impression.

### Why It Affects SEO

Answer engines need crawlable, clear, well-supported information they can cite or summarize. This check improves extractability, factual grounding, and mention quality.

### How To Verify

1. Identify the exact URL, template, brand workspace, connector account, or page group in scope.
2. Collect evidence from: CMS/code, Logs/CDN/WAF, Firecrawl, Playwright, OSS, Human/context, saved prompt set, manual AI SERP, GSC.
3. Record pass, fail, not_applicable, or not_checked_blocked in the audit matrix with an artifact reference.

### Evidence Sources

CMS/code, Logs/CDN/WAF, Firecrawl, Playwright, OSS, Human/context, saved prompt set, manual AI SERP, GSC

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
