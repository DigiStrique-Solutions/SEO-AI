# Ecommerce SEO Task

Date: 2026-07-08

Target URL: https://www.strique.io/

Checklist: `docs/checklists/ecommerce-seo-checklist.md`

Status: not_applicable / blocked

## Evidence Used

- Fresh Playwright homepage render.
- Fresh Firecrawl homepage extraction.

## Coverage

Checklist items:

- Items: 169

Current-session blockers:

- Shopify, Merchant Center, product feed, product catalog, reviews, shipping, returns, cart, checkout, and inventory sources were not connected.

## Findings

### Strique Homepage Is Not An Ecommerce Storefront

The page targets ecommerce brands, but it does not itself expose a product catalog, PDPs, collection pages, cart, checkout, product prices, availability, reviews, shipping, returns, Merchant Center feed, or storefront conversion path.

### Ecommerce Rows Should Not Be Forced Onto This Homepage

Most storefront-specific rows should be marked `not_applicable` for the Strique SaaS homepage. They may become applicable for Strique customer sites or app marketplace surfaces.

## Next Task

Only use this checklist if the scope changes to a Strique customer ecommerce site, a Shopify app listing, or a real product/feed/storefront surface.
