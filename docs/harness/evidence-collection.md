---
title: Evidence Collection
sidebar_position: 5
---

# Evidence Collection

Evidence should be specific enough to support an audit row.

## Public Crawl Evidence

- Firecrawl markdown, HTML, raw HTML, links, images, and screenshots.
- Public HTTP status, canonical, robots, sitemap, and headers.

## Rendered Browser Evidence

- Playwright DOM checks.
- Desktop and mobile screenshots.
- JavaScript-rendered content.
- Hidden content and interactive states.
- Accessibility tree when relevant.

## Performance Evidence

- Lighthouse lab data.
- PageSpeed Insights.
- CrUX field data when available.

## Connected Platform Evidence

- GSC for queries, pages, indexing, sitemaps, search appearance, and links.
- GA4 or PostHog for traffic, engagement, conversions, funnels, and revenue.
- Shopify or CMS for product, page, template, and source-of-truth data.
- GMC for product feed, shipping, returns, availability, and merchant listing diagnostics.
- GBP and Maps for local profile, reviews, photos, categories, services, and hours.

If access is missing, mark the exact item as `not_checked_blocked`.
