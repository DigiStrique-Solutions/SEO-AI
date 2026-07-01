# Ecommerce SEO Checklist

Updated: 2026-06-29

Use this checklist for ecommerce stores, marketplaces, Shopify catalogs, product detail pages, category and collection pages, faceted navigation, product feeds, merchant listings, reviews, and revenue SEO. Use it after the generic on-page checklist when the page or section has ecommerce-specific risk.

## Research Basis

Primary and reputable sources used:

- [Google ecommerce SEO best practices](https://developers.google.com/search/docs/specialty/ecommerce)
- [Google where ecommerce content can appear](https://developers.google.com/search/docs/specialty/ecommerce/where-ecommerce-data-can-appear-on-google)
- [Google share product data with Google](https://developers.google.com/search/docs/specialty/ecommerce/share-your-product-data-with-google)
- [Google ecommerce structured data guidance](https://developers.google.com/search/docs/specialty/ecommerce/include-structured-data-relevant-to-ecommerce)
- [Google Product structured data guidance](https://developers.google.com/search/docs/appearance/structured-data/product)
- [Google Merchant listing structured data guidance](https://developers.google.com/search/docs/appearance/structured-data/merchant-listing)
- [Google product variant structured data guidance](https://developers.google.com/search/docs/appearance/structured-data/product-variants)
- [Google ecommerce URL structure guidance](https://developers.google.com/search/docs/specialty/ecommerce/designing-a-url-structure-for-ecommerce-sites)
- [Google ecommerce site structure guidance](https://developers.google.com/search/docs/specialty/ecommerce/help-google-understand-your-ecommerce-site-structure)
- [Google ecommerce pagination and incremental loading guidance](https://developers.google.com/search/docs/specialty/ecommerce/pagination-and-incremental-page-loading)
- [Google high quality product review guidance](https://developers.google.com/search/docs/specialty/ecommerce/write-high-quality-reviews)
- [Google faceted navigation crawling guidance](https://developers.google.com/crawling/docs/faceted-navigation)
- [Google crawl budget guidance](https://developers.google.com/crawling/docs/crawl-budget)
- [Google canonicalization guidance](https://developers.google.com/search/docs/crawling-indexing/consolidate-duplicate-urls)
- [Google image SEO best practices](https://developers.google.com/search/docs/appearance/google-images)
- [Google Core Web Vitals guidance](https://developers.google.com/search/docs/appearance/core-web-vitals)
- [Google AI features optimization guide](https://developers.google.com/search/docs/fundamentals/ai-optimization-guide)
- [Google Merchant Center product data specification](https://support.google.com/merchants/answer/7052112)
- [Google Merchant Center supported structured data attributes](https://support.google.com/merchants/answer/6386198)
- [Google Merchant Center landing page requirements](https://support.google.com/merchants/answer/4752265)
- [Shopify theme SEO documentation](https://shopify.dev/docs/storefronts/themes/seo)
- [Baymard ecommerce category page guidance](https://baymard.com/learn/ecommerce-category-page)
- [Baymard ecommerce filter guidance](https://baymard.com/learn/ecommerce-filter-ui)
- [Baymard product page UX research](https://baymard.com/research/product-page)

2026-specific notes:

- Ecommerce SEO is not only metadata. Product page content, catalog structure, product feed quality, structured data, availability, shipping, returns, reviews, and crawl control all affect discoverability and eligibility.
- Google's ecommerce guidance centers on sharing product data and site structure clearly through crawlable pages, structured data, Merchant Center feeds, and stable URLs.
- Product page, schema, Merchant Center feed, and landing page values must agree for title, description, image, price, currency, availability, product identifiers, variants, shipping, and returns.
- Faceted navigation remains a high-risk area because filters can create large duplicate or low-value URL spaces.
- Google AI feature guidance still depends on normal SEO foundations: helpful content, crawlability, snippet eligibility, page experience, and accurate structured data. Do not create AI-only markup or hidden prompt instructions.
- Use browser-rendered checks before claiming product schema, price, availability, reviews, or links are absent.

## Evidence Source Legend

Use free, owned, or open-source sources first.

- `GMC`: Google Merchant Center product data, diagnostics, free listings, shipping, returns, feed rules, product disapprovals, and issue details.
- `GSC`: Search Console performance, indexing, sitemaps, shopping enhancements, product snippets, merchant listings, Core Web Vitals, and crawl stats.
- `GA4`: organic landing page sessions, engagement, revenue, add-to-cart, checkout, purchase, assisted conversion, and funnel events.
- `Shopify`: Shopify products, variants, collections, redirects, themes, Liquid templates, apps, feeds, markets, and metafields.
- `Firecrawl`: public crawl, rendered extraction, raw HTML, links, canonicals, schema, images, screenshots, status codes, and page groups.
- `Playwright`: rendered DOM inspection, mobile checks, screenshots, checkout and variant interactions, filter behavior, and client-side schema validation.
- `CMS/code`: platform exports, product database, templates, redirects, robots, sitemaps, logs, CDN, server rendering, schema code, and feed jobs.
- `GKP`: Google Ads Keyword Planner for directional category, product, brand, and modifier demand.
- `CrUX/LH`: Chrome UX Report and Lighthouse for field and lab performance signals.
- `OSS`: schema validators, sitemap parsers, robots parsers, link checkers, image tooling, accessibility tooling, and log analysis.
- `Manual/free SERP`: Google and Bing search results, image results, product grids, Shopping surfaces, AI answer observations, and competitor page type review.
- `Human/context`: product marketing context, merchandising strategy, margin, inventory, seasonality, legal review, support data, and customer research.

## Scoring

- `critical`: blocks crawling, indexing, merchant eligibility, purchase completion, legal trust, or accurate product representation.
- `high`: materially weakens product discovery, rich result eligibility, catalog coverage, feed health, revenue pages, trust, or conversion.
- `medium`: improves relevance, completeness, internal linking, snippet quality, template quality, or product data consistency.
- `low`: polish, maintenance, reporting, optional enhancements, or small UX improvements.
- `not_applicable`: store, page type, market, or platform does not use this item.

Issue record:

```text
Severity:
Area:
Evidence source:
Affected URL, template, feed, or product group:
Issue:
Why it matters:
Recommended fix:
Owner:
Confidence:
Source:
```

## 1. Scope And Ecommerce Context

Evidence sources: `Human/context`, `GMC`, `GSC`, `GA4`, `Shopify`, `CMS/code`.

- [ ] The audit scope is defined: full store, product template, category template, collection set, product feed, merchant listings, migration, international market, or revenue recovery.
- [ ] Store type is identified: DTC, B2B ecommerce, marketplace, dropship, retail catalog, subscription, local inventory, digital goods, or hybrid.
- [ ] Platform and constraints are known: Shopify, headless Shopify, WooCommerce, Magento, custom, marketplace, or app-based storefront.
- [ ] Primary revenue goals are captured: organic revenue, free listings, Shopping eligibility, category visibility, product discovery, assisted conversion, or retention.
- [ ] Priority product groups are identified by revenue, margin, inventory, seasonality, strategic value, and search opportunity.
- [ ] The product data source of truth is known for names, descriptions, variants, prices, availability, identifiers, images, shipping, and returns.
- [ ] Product marketing context is loaded before recommending content, category, positioning, or buyer-guide changes.
- [ ] The checklist is paired with [Generic On-Page SEO Checklist](generic-on-page-seo-checklist.md) and [Site Architecture SEO Checklist](site-architecture-seo-checklist.md) where the issue is not ecommerce-specific.

## 2. Catalog And Product Data Inventory

Evidence sources: `GMC`, `Shopify`, `CMS/code`, `Firecrawl`, `GSC`, `GA4`, `OSS`.

- [ ] A product inventory exists from the platform, feed, sitemap, crawl, GSC, and GA4 landing pages.
- [ ] Products are grouped by template, category, collection, brand, variant count, inventory status, revenue, impressions, clicks, and indexability.
- [ ] Product identifiers are present where applicable: GTIN, MPN, SKU, brand, item group ID, and variant attributes.
- [ ] Product names are stable, user-readable, and not overloaded with every variant, promo, or internal code.
- [ ] Variant data is complete for attributes users search and filter by, such as size, color, material, gender, age group, flavor, bundle size, or model.
- [ ] Product descriptions, images, pricing, availability, identifiers, and variant attributes match across page, feed, schema, and platform data.
- [ ] Out-of-stock, discontinued, draft, hidden, restricted, and unpublished products are separated from active acquisition pages.
- [ ] Product groups with missing feed attributes or Merchant Center issues are prioritized by revenue and visibility impact.

## 3. Product Detail Pages

Evidence sources: `Firecrawl`, `Playwright`, `GMC`, `GSC`, `GA4`, `Shopify`, `CMS/code`, `Manual/free SERP`.

- [ ] Each indexable product page has one clear product identity and is not a generic category, search, or variant selector page.
- [ ] The title tag, H1, product name, feed title, and structured data name describe the same product.
- [ ] The page shows price, currency, availability, primary image, variant options, shipping or delivery expectations, return information, and purchase action.
- [ ] The product description explains what the product is, who it is for, key attributes, materials, sizing, compatibility, use cases, care, and constraints where relevant.
- [ ] Product copy is unique enough to help shoppers choose and is not only manufacturer boilerplate across many retailers.
- [ ] Variant selection changes visible price, availability, image, URL, and structured data consistently where those values differ.
- [ ] Product pages include relevant trust details: reviews, ratings, warranty, guarantees, security, support, merchant identity, policies, and contact path.
- [ ] Product pages answer purchase objections such as fit, compatibility, delivery time, return cost, bundle contents, and comparisons.
- [ ] Product pages include related products, alternatives, accessories, bundles, or guides where they genuinely help purchase decisions.
- [ ] Product pages are not indexable when they are empty, duplicate, unavailable with no replacement, or inaccessible to users.

## 4. Category And Collection Pages

Evidence sources: `Firecrawl`, `Playwright`, `GSC`, `GA4`, `GKP`, `Shopify`, `CMS/code`, `Manual/free SERP`.

- [ ] Each indexable category or collection targets a real browse or search intent.
- [ ] Category names match customer language and product taxonomy, not only internal merchandising labels.
- [ ] The page includes a useful intro, subcategory links, products, filters, sorting, internal links, and next-step paths.
- [ ] Category copy helps users choose without pushing product listings below the useful first screen.
- [ ] The title, H1, intro, breadcrumb, canonical, and internal anchors agree on the category identity.
- [ ] Empty, near-empty, one-product, duplicate, or seasonal categories have an indexability policy.
- [ ] Category pages link to important child categories, buying guides, popular products, sale pages, and relevant informational content.
- [ ] Product listings expose crawlable product links with useful anchor text or product names.
- [ ] Pagination, filters, sorting, and view modes do not hide products from users or crawlers.
- [ ] Category performance is reviewed by organic revenue, product clicks, add-to-cart, conversion, query mix, and assisted revenue.

## 5. Facets, Filters, Sorting, And Internal Search

Evidence sources: `Firecrawl`, `Playwright`, `GSC`, `GA4`, `GMC`, `Shopify`, `CMS/code`, `OSS`.

- [ ] Facets are classified before recommendations: indexable value, user-only filter, duplicate variant, temporary state, sort order, internal search, or tracking parameter.
- [ ] Valuable facets have search demand, product depth, unique content, stable URLs, self-referencing canonicals, internal links, and sitemap inclusion where appropriate.
- [ ] Nonvaluable facets are controlled to prevent crawl traps and index bloat.
- [ ] Filter combinations with no results, tiny result sets, or duplicate product sets are not indexable.
- [ ] Sorting, price sliders, view modes, stock toggles, session IDs, tracking IDs, and personalization parameters are not indexable acquisition pages.
- [ ] Filter links that should be crawled use crawlable anchors, not only JavaScript events.
- [ ] Filter states that should not be crawled are controlled with platform routing, robots rules, nofollow where appropriate, canonicalization, or URL design.
- [ ] Internal search result pages are not indexable by default unless there is a deliberate public landing page strategy.
- [ ] Search logs and zero-result searches are reviewed for missing categories, synonyms, redirects, and product data gaps.
- [ ] Facet rules are documented so merchandising changes do not accidentally create thousands of indexable low-value URLs.

## 6. URLs, Variants, Pagination, And Canonicals

Evidence sources: `Firecrawl`, `Playwright`, `GSC`, `Shopify`, `CMS/code`, `OSS`.

- [ ] Product, category, collection, brand, and guide URLs use stable, readable, lowercase paths.
- [ ] URL parameters use clear key-value pairs where parameters are needed.
- [ ] Session IDs, timestamps, tracking codes, and user-specific values are not part of indexable URLs.
- [ ] Product variants have a clear URL policy: shared parent URL, unique variant URL, or parameterized variant URL.
- [ ] Variant canonicals reflect the intended indexing strategy and do not collapse genuinely distinct products.
- [ ] Variant URLs are crawlable and indexable only when they provide useful unique value or demand.
- [ ] Paginated category pages use unique crawlable URLs and do not all canonicalize to page 1 unless they are true duplicates.
- [ ] "Load more" and infinite scroll expose crawlable paginated URLs or equivalent linked pages.
- [ ] Canonicals, sitemap URLs, internal links, hreflang, and Merchant Center links point to the intended final URL.
- [ ] Redirect chains, duplicate hosts, trailing slash conflicts, and case variants are cleaned up for priority ecommerce URLs.

## 7. Merchant Center And Product Feeds

Evidence sources: `GMC`, `Shopify`, `CMS/code`, `GSC`, `GA4`, `Firecrawl`, `Human/context`.

- [ ] Merchant Center account, feeds, free listings, diagnostics, shipping, returns, tax, and target countries are reviewed where connected.
- [ ] Feed titles, descriptions, images, links, mobile links, prices, availability, condition, brand, GTIN, MPN, SKU, item group ID, and variant attributes are complete where required.
- [ ] Feed data matches the landing page visible content and structured data for product, variant, price, currency, availability, shipping, returns, and identifiers.
- [ ] Product landing page URLs lead to the specific product or primary variant, not a category, search page, homepage, or generic collection.
- [ ] Merchant Center disapprovals, limited eligibility, warnings, and issue details are grouped by root cause.
- [ ] Feed refresh cadence matches how often price, stock, product availability, and promotions change.
- [ ] Sale price, promotions, bundles, multi-item offers, subscriptions, and member pricing are represented accurately where used.
- [ ] Shipping rates, delivery regions, return windows, return costs, and policy URLs are current and consistent with the site.
- [ ] Feed rules or app-generated fields are documented so automated fixes do not hide source data quality problems.
- [ ] High-value products with missing identifiers or low-quality images are prioritized before low-revenue long-tail cleanup.

## 8. Structured Data And Search Appearance

Evidence sources: `Playwright`, `Firecrawl`, `GSC`, `GMC`, `Shopify`, `CMS/code`, `OSS`.

- [ ] Browser-rendered pages are checked before declaring schema absent or broken.
- [ ] Product, Offer, AggregateRating, Review, ProductGroup, BreadcrumbList, Organization, MerchantReturnPolicy, and OfferShippingDetails markup are used only where visible content supports them.
- [ ] Merchant listing markup is used for pages where users can buy the product from the site.
- [ ] Product snippet markup is used for editorial product review pages or non-purchasable product information pages where appropriate.
- [ ] Product schema includes required fields and useful recommended fields for price, currency, availability, image, brand, identifiers, variants, shipping, returns, and reviews where applicable.
- [ ] Product variant markup connects parent and child products correctly when variants need explicit representation.
- [ ] Review and rating markup reflects real user-visible reviews and does not invent or cherry-pick ratings.
- [ ] Shipping and return policy structured data matches visible policy pages and Merchant Center settings.
- [ ] Breadcrumb structured data matches visible breadcrumbs and the intended category path.
- [ ] Structured data values match feed and landing page values.
- [ ] JSON-LD is valid, parsable, not duplicated in conflicting ways, and not blocked from rendering.
- [ ] Rich Results Test, Schema.org validator, GSC product snippets, and GSC merchant listings reports are checked where available.

## 9. Reviews, Buying Guides, And Trust Content

Evidence sources: `Firecrawl`, `Playwright`, `GSC`, `GA4`, `Shopify`, `CMS/code`, `Human/context`, `Manual/free SERP`.

- [ ] Product reviews are authentic, visible, tied to the right product or variant, and moderated for spam or abuse.
- [ ] Review summaries, pros and cons, ratings, photos, and Q&A help shoppers decide rather than only decorate the page.
- [ ] Review collection follows platform rules, advertising law, and brand policy.
- [ ] Editorial product reviews, comparisons, and buying guides show firsthand evidence, tested criteria, tradeoffs, and who each option is for.
- [ ] Category guides explain key decision criteria, compatibility, sizing, materials, care, safety, warranty, and use cases where relevant.
- [ ] Trust pages such as shipping, returns, warranty, contact, privacy, terms, about, and support are easy to find from commercial pages.
- [ ] Claims about "best", "top", "official", "guaranteed", "eco-friendly", "medical", "safe", or "certified" are supported and reviewed where needed.
- [ ] UGC, reviews, and Q&A do not create indexable spam, hidden content, or unsupported claims.

## 10. Product Images, Video, And Media

Evidence sources: `Firecrawl`, `Playwright`, `GMC`, `Shopify`, `CMS/code`, `CrUX/LH`, `OSS`.

- [ ] Primary product images show the actual product clearly and match the product or variant.
- [ ] Product images meet feed and marketplace quality expectations for size, clarity, background, cropping, and crawlable URL access.
- [ ] Product pages include useful alternate views, scale, detail shots, lifestyle images, included contents, labels, or variant images where relevant.
- [ ] Informative images have useful alt text and decorative images use empty alt text or equivalent treatment.
- [ ] Images use responsive sizing, efficient formats, compression, width and height attributes, and reserved layout space.
- [ ] Above-the-fold product media does not delay LCP unnecessarily.
- [ ] Video helps explain fit, use, assembly, styling, comparison, or troubleshooting and includes crawlable supporting text where useful.
- [ ] Image and video URLs remain stable enough for search and feed systems to fetch them reliably.
- [ ] Media shown in schema and feeds matches visible page media.

## 11. Availability, Out-Of-Stock, Seasonal, And Discontinued Products

Evidence sources: `GMC`, `GSC`, `GA4`, `Shopify`, `CMS/code`, `Firecrawl`, `Human/context`.

- [ ] Product availability is visible to users and consistent across page, feed, schema, and inventory systems.
- [ ] Temporary out-of-stock products remain useful with restock information, notification signup, alternatives, and clear availability markup where appropriate.
- [ ] Permanently discontinued products redirect to the closest replacement, remain live with alternatives, or return 404/410 based on value and replacement availability.
- [ ] Discontinued products are not redirected to the homepage or unrelated category.
- [ ] Seasonal products have a policy for off-season visibility, stock messages, preorders, redirects, and internal links.
- [ ] Sale, clearance, limited-time, and campaign URLs have expiration and redirect plans.
- [ ] Product removals are checked against organic traffic, backlinks, revenue, and feed status before deletion.
- [ ] Soft 404 product pages are identified, especially empty, unavailable, or error-like pages returning 200.

## 12. Internal Linking And Ecommerce Discovery

Evidence sources: `Firecrawl`, `Playwright`, `GSC`, `GA4`, `Shopify`, `CMS/code`, `Manual/free SERP`.

- [ ] Important products and categories receive links from navigation, collections, related products, guides, merchandising modules, and high-traffic pages.
- [ ] Breadcrumbs link users and crawlers back to relevant parent categories.
- [ ] Product pages link to parent categories, compatible accessories, alternatives, bundles, replacement parts, and buying guides where useful.
- [ ] Category pages link to subcategories, popular filters, best sellers, new arrivals, sale pages, and relevant guides when those links help users.
- [ ] Anchor text is descriptive and not mechanically exact-match.
- [ ] Related product modules are relevant, crawlable, and not only personalized client-side widgets.
- [ ] Orphan product pages are linked, merged, noindexed, or removed.
- [ ] High-revenue pages with weak internal links are prioritized for navigation and contextual link improvements.
- [ ] Internal links point to canonical URLs and avoid redirecting product or category URLs.

## 13. Crawlability, Indexability, And Sitemaps

Evidence sources: `Firecrawl`, `Playwright`, `GSC`, `GMC`, `Shopify`, `CMS/code`, `OSS`.

- [ ] Important product, category, collection, brand, and guide pages are crawlable through normal HTML links.
- [ ] Product and category pages that should rank return successful status codes and are not blocked or noindexed.
- [ ] Cart, checkout, account, login, internal search, order status, wishlist, compare, and utility pages are not indexable unless intentionally public.
- [ ] Noindex pages are not blocked by robots.txt when crawlers need to see the noindex directive.
- [ ] XML sitemaps contain only canonical, indexable ecommerce URLs and exclude utility, noindexed, redirected, broken, duplicate, and parameter-only URLs.
- [ ] Product and category sitemap `lastmod` values reflect meaningful changes, not every build or template update.
- [ ] Large catalogs use sitemap segmentation by product, category, image, market, or update cadence where useful.
- [ ] Crawl stats or logs are reviewed for wasted crawl on filters, sort orders, internal search, redirects, 404/410, soft 404, 5xx, and 429 responses.
- [ ] Googlebot verification uses official verification methods when logs, firewalls, or bot allowlists are part of the evidence.
- [ ] Staging, preview, duplicate theme, and test domains are blocked or noindexed before launch.

## 14. Mobile, Performance, And Buying UX

Evidence sources: `Playwright`, `CrUX/LH`, `GSC`, `GA4`, `Firecrawl`, `Shopify`, `CMS/code`, `OSS`.

- [ ] Mobile and desktop show equivalent product information, links, schema, metadata, variant options, reviews, and purchase paths.
- [ ] Core Web Vitals are reviewed with field data where available: LCP, INP, and CLS.
- [ ] The likely LCP element on product and category pages is identified and optimized.
- [ ] Variant selectors, filters, sort controls, menus, product cards, review widgets, and add-to-cart controls work on mobile.
- [ ] Popups, cookie banners, app-install prompts, chat widgets, and promo bars do not block main product content or purchase actions.
- [ ] Add-to-cart, cart, checkout entry, shipping estimator, discount code, and payment options work for sample products and markets.
- [ ] Product card grids reserve image and text space to avoid layout shifts.
- [ ] Third-party scripts for reviews, personalization, analytics, ads, chat, and affiliate tracking are justified and monitored.
- [ ] Accessibility basics are checked for product options, forms, filters, error states, images, and checkout entry.

## 15. International, Markets, And Local Inventory

Use only when the store targets multiple countries, languages, currencies, pickup locations, or local inventory.

Evidence sources: `GMC`, `GSC`, `GA4`, `Shopify`, `CMS/code`, `Firecrawl`, `Playwright`, `Human/context`.

- [ ] Locale, country, currency, language, shipping, tax, legal, and availability differences are visible and accurate.
- [ ] Hreflang points to canonical, indexable locale URLs and is reciprocal.
- [ ] Locale pages do not canonicalize to a different language or market version unless intentionally consolidated.
- [ ] Auto-redirects based on IP, currency, or language do not block users or crawlers from alternate market URLs.
- [ ] Merchant Center target countries, currencies, feeds, landing pages, and shipping settings match the site market setup.
- [ ] Local inventory, pickup, store pages, and store locator pages have a crawlable and indexable policy where local SEO matters.
- [ ] Product identifiers, prices, taxes, returns, units, sizing, and legal claims fit each market.
- [ ] Translated product and category pages include translated metadata, schema, navigation, reviews policy, and support details where relevant.

## 16. AI Search And Shopping Answer Readiness

Evidence sources: `Firecrawl`, `Playwright`, `GSC`, `GMC`, `GA4`, `CMS/code`, `Manual/free SERP`, `Human/context`.

- [ ] Pages are crawlable, indexable, helpful, and eligible for normal snippets before AI search recommendations are made.
- [ ] Product and category pages use clear, extractable language for product identity, use cases, differences, shipping, returns, availability, and buyer fit.
- [ ] Product data is consistent across visible content, feed, schema, reviews, and trusted third-party profiles.
- [ ] Buying guides and comparisons include original evidence, expert judgment, decision criteria, and concrete recommendations.
- [ ] AI-visible content is not hidden, cloaked, or stuffed with instructions to ranking systems or AI assistants.
- [ ] Snippet controls such as `nosnippet`, `max-snippet`, `max-image-preview`, `max-video-preview`, and `data-nosnippet` are intentional.
- [ ] Robots policy for AI crawlers is a business decision and not assumed to improve Google AI visibility.
- [ ] Manual prompt sets, referral logs, GSC, Bing Webmaster Tools, and analytics are used as measurement inputs instead of claimed AI rankings.

## 17. Measurement And Revenue Validation

Evidence sources: `GSC`, `GA4`, `GMC`, `Shopify`, `CMS/code`, `Firecrawl`, `Playwright`, `Human/context`.

- [ ] Organic performance is reported by page type, category, product group, market, device, and query intent.
- [ ] Revenue metrics include organic sessions, product views, add-to-cart, checkout starts, purchases, revenue, conversion rate, average order value, and assisted conversions where available.
- [ ] GSC product snippets, merchant listings, indexing, sitemap, Core Web Vitals, and crawl stats reports are reviewed where available.
- [ ] Merchant Center diagnostics, free listings, disapprovals, clicks, impressions, and product issue trends are reviewed where connected.
- [ ] GA4 events and ecommerce tracking are validated before using revenue data for prioritization.
- [ ] Changes are annotated with deployment date, affected templates, product groups, expected impact, owner, and review date.
- [ ] Before and after comparisons allow enough time for crawl, feed processing, indexing, and seasonality.
- [ ] Recommendations separate SEO impact, feed eligibility impact, UX impact, and conversion impact.

## 18. Common Anti-Patterns

Evidence sources: `Firecrawl`, `Playwright`, `GSC`, `GMC`, `GA4`, `Shopify`, `CMS/code`, `Human/context`.

- [ ] Product schema says a product is in stock when the page or feed says it is out of stock.
- [ ] Merchant feed prices, schema prices, and visible prices disagree.
- [ ] All variant URLs canonicalize to one product even when variants have distinct demand and content.
- [ ] All paginated category pages canonicalize to page 1.
- [ ] Filter combinations create unlimited crawlable URLs with duplicate or empty product sets.
- [ ] Product pages use manufacturer descriptions with no unique merchant value.
- [ ] Category pages are thin product grids with no helpful browse path or internal links.
- [ ] Internal search result pages are indexed by accident.
- [ ] Out-of-stock products redirect to unrelated pages or the homepage.
- [ ] Reviews, ratings, or availability are marked up when users cannot see them.
- [ ] Product JSON-LD is generated by multiple apps with conflicting values.
- [ ] Product images are blocked, low quality, swapped by JavaScript only, or inconsistent with the feed.
- [ ] Storefront, feed, schema, and analytics owners work from different product data definitions.
- [ ] "AI SEO" work adds hidden instructions or fake facts instead of improving product clarity and data consistency.

## 19. Minimal Audit Flow

Evidence sources: `GMC`, `GSC`, `GA4`, `Shopify`, `Firecrawl`, `Playwright`, `CMS/code`, `OSS`, `Human/context`.

1. Define scope, market, platform, priority categories, and revenue goal.
2. Pull product inventory from platform, feed, crawl, sitemap, GSC, and GA4.
3. Classify product, category, collection, facet, search, utility, and guide URLs.
4. Check crawlability, indexability, canonicals, sitemap inclusion, and URL patterns.
5. Sample priority product pages across templates, variants, stock states, and markets.
6. Sample category and collection pages across pagination, filters, sort orders, and empty states.
7. Compare visible page data, schema, Merchant Center feed, and platform source data.
8. Review Merchant Center diagnostics and Search Console product enhancement reports.
9. Validate rendered schema, mobile UX, Core Web Vitals, internal links, and purchase paths.
10. Prioritize fixes by revenue, eligibility, crawl/indexing risk, user trust, and implementation effort.

## 20. Output Template

Evidence sources: cite specific tools and properties used, such as `GMC`, `GSC`, `GA4`, `Shopify`, `Firecrawl`, `Playwright`, `CMS/code`, `CrUX/LH`, `OSS`, `Manual/free SERP`, or `Human/context`.

```text
Summary:

Top findings:
1. [severity] [area]
   Evidence:
   Affected URLs, templates, feeds, or product groups:
   Impact:
   Fix:
   Owner:
   Confidence:
   Source:

Quick wins:

Larger fixes:

Feed or Merchant Center issues:

Template or engineering issues:

Needs data:

Recommended next crawl/check:

Sources used:
```
