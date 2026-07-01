# Site Architecture SEO Checklist

Updated: 2026-06-29

Use this checklist when auditing or planning site structure, navigation, page hierarchy, URL patterns, taxonomy, hub pages, breadcrumbs, internal linking, or sitemap alignment. This is a site-wide checklist, not a single-page on-page audit.

## Research Basis

Primary and reputable sources used:

- [Google link best practices](https://developers.google.com/search/docs/crawling-indexing/links-crawlable)
- [Google sitemap overview](https://developers.google.com/search/docs/crawling-indexing/sitemaps/overview)
- [Google build and submit sitemap guidance](https://developers.google.com/search/docs/crawling-indexing/sitemaps/build-sitemap)
- [Google BreadcrumbList structured data guidance](https://developers.google.com/search/docs/appearance/structured-data/breadcrumb)
- [Google canonicalization guidance](https://developers.google.com/search/docs/crawling-indexing/consolidate-duplicate-urls)
- [Google redirects guidance](https://developers.google.com/search/docs/crawling-indexing/301-redirects)
- [Google pagination and incremental page loading guidance](https://developers.google.com/search/docs/specialty/ecommerce/pagination-and-incremental-page-loading)
- [Google ecommerce site structure guidance](https://developers.google.com/search/docs/specialty/ecommerce/help-google-understand-your-ecommerce-site-structure)
- [Google ecommerce URL structure guidance](https://developers.google.com/search/docs/specialty/ecommerce/designing-a-url-structure-for-ecommerce-sites)
- [Google faceted navigation guidance](https://developers.google.com/crawling/docs/faceted-navigation)
- [Google JavaScript SEO basics](https://developers.google.com/search/docs/crawling-indexing/javascript/javascript-seo-basics)
- [Google robots.txt guide](https://developers.google.com/search/docs/crawling-indexing/robots/intro)
- [Google robots meta and X-Robots-Tag guidance](https://developers.google.com/search/docs/crawling-indexing/robots-meta-tag)
- [Google crawl budget guidance](https://developers.google.com/crawling/docs/crawl-budget)
- [Google Search Console Performance report guidance](https://support.google.com/webmasters/answer/7576553)
- [Google Search Console Crawl Stats report guidance](https://support.google.com/webmasters/answer/9679690)
- [NN/g information architecture study guide](https://www.nngroup.com/articles/ia-study-guide/)
- [NN/g information architecture vs sitemaps](https://www.nngroup.com/articles/information-architecture-sitemaps/)
- [NN/g flat vs deep website hierarchies](https://www.nngroup.com/articles/flat-vs-deep-hierarchy/)
- [NN/g menu design checklist](https://www.nngroup.com/articles/menu-design/)
- [NN/g card sorting](https://www.nngroup.com/articles/card-sorting-definition/)
- [NN/g breadcrumb design guidelines](https://www.nngroup.com/articles/breadcrumbs/)
- [Baymard ecommerce category navigation research](https://baymard.com/research/homepage-and-category-usability)
- [Baymard ecommerce category page guidance](https://baymard.com/learn/ecommerce-category-page)
- [Baymard ecommerce filter guidance](https://baymard.com/learn/ecommerce-filter-ui)
- [Baymard information architecture UX guidance](https://baymard.com/learn/information-architecture-ux)
- [Baymard findability and discoverability guidance](https://baymard.com/learn/findability-vs-discoverability-ux)

## Evidence Source Legend

Use free, owned, or open-source sources first.

Google-visible scope: judge pass/fail from public rendered evidence, HTTP responses, robots/sitemaps, GSC outcome data, and lab/field performance evidence. CMS/code, GA4/PostHog, governance, ownership, logs, and editorial workflow are optional implementation or prioritization evidence, not blockers for what Google can see.

- `Firecrawl`: crawl URLs, links, headings, titles, canonicals, status codes, rendered content, screenshots, sitemap discovery.
- `Playwright`: precision DOM inspection, mobile and desktop navigation checks, screenshots, interactive menu testing, rendered JavaScript state.
- `GSC`: Search Console performance, indexed pages, sitemaps, search appearance, URL Inspection, Crawl Stats.
- `GA4`: landing page traffic, engagement, conversion, revenue or lead value.
- `GKP`: Google Ads Keyword Planner for directional demand and keyword variants.
- `Lighthouse`: free Lighthouse runner for mobile rendering, SEO, accessibility, link, and page quality checks.
- `GBP`: Google Business Profile for local location/profile context.
- `GMAPS`: Google Maps Places for local competitor, category, and place data.
- `GMC`: Google Merchant Center for ecommerce product/feed/category context.
- `CMS/code`: CMS exports, Shopify/Webflow/WordPress data, GitHub/codebase routes, redirects, templates, logs, robots, sitemaps.
- `OSS`: open-source/free tools such as sitemap parser, robots parser, link checker, graph tooling, schema validator, axe-core.
- `Manual/free SERP`: manual SERP review, user-provided screenshots, GSC search appearance, free search surfaces.
- `Human/context`: product marketing context, customer input, editorial judgment, UX research, card sorting, tree testing, stakeholder review.

## Scoring

- `critical`: important pages cannot be found, crawled, indexed, or reached by users.
- `high`: architecture causes crawl waste, duplicate/index-bloat risk, orphan priority pages, poor navigation, or conversion path failure.
- `medium`: architecture weakens relevance, discoverability, internal-link flow, or UX but does not block discovery.
- `low`: naming, grouping, sitemap, breadcrumb, or navigation polish.
- `not_applicable`: site type or page set does not use this architecture pattern.

For each issue record:

```text
Severity:
Area:
Evidence source:
Affected URLs or section:
Issue:
Why it matters:
Recommended fix:
Owner:
Confidence:
```

## 1. Scope And Site Type

Evidence sources: `Human/context`, `GSC`, `GA4`, `GKP`, `Firecrawl`, `CMS/code`.

- [ ] The audit scope is defined: full site, section, migration, navigation redesign, taxonomy cleanup, ecommerce category tree, docs IA, blog/content hub, or local/service architecture.
- [ ] Site type is classified: SaaS marketing, content/blog, ecommerce, documentation, marketplace, local service, app install, hybrid, or support portal.
- [ ] Primary business goals are captured: traffic, leads, signups, purchase, app install, support deflection, brand trust, retention, or partner/referral traffic.
- [ ] Primary audiences and user tasks are captured.
- [ ] Current pain is captured: poor indexing, low organic traffic, cannibalization, poor conversion, users cannot find pages, crawl waste, migration risk, or messy CMS growth.
- [ ] Constraints are known: CMS limits, engineering ownership, legacy URLs, legal pages, international structure, ecommerce platform, or app routing model.

## 2. Content Inventory

Evidence sources: `Firecrawl`, `GSC`, `GA4`, `CMS/code`, `OSS`.

- [ ] A crawl inventory exists for all discoverable public URLs.
- [ ] XML sitemap URLs are collected and compared against crawled URLs.
- [ ] CMS, code routes, Shopify/Webflow/WordPress pages, or database-backed URLs are exported where available.
- [ ] GSC top pages are included even if the crawler missed them.
- [ ] GA4 landing pages are included even if they are missing from sitemaps.
- [ ] URLs are grouped by page type, section, template, indexability, status code, canonical target, traffic, and conversion value.
- [ ] Orphan pages are identified by comparing sitemap, crawl, GSC, GA4, and CMS/code sources.
- [ ] Duplicate or near-duplicate page sets are identified.
- [ ] Thin, stale, empty, utility, account, search result, and parameter pages are flagged separately from acquisition pages.
- [ ] Non-HTML assets such as PDFs, docs, images, feeds, and downloadable files are inventoried when they receive traffic or are linked internally.

## 3. Priority Page Model

Evidence sources: `GSC`, `GA4`, `GKP`, `Human/context`, `Manual/free SERP`.

- [ ] Priority pages are ranked by business value, not only traffic.
- [ ] Pages with high impressions and low CTR are marked as snippet/title opportunities.
- [ ] Pages with organic sessions but poor conversion are marked as UX or intent mismatch opportunities.
- [ ] Pages with conversions but weak organic visibility are marked as internal-link and content expansion opportunities.
- [ ] Pages with strategic importance but low links, low crawl depth, or no hub support are flagged.
- [ ] Pages with declining clicks or impressions are marked for freshness, cannibalization, and internal-link review.
- [ ] Priority pages have an intended search intent and one primary role in the architecture.

## 4. Hierarchy And Depth

Evidence sources: `Firecrawl`, `Playwright`, `GSC`, `GA4`, `CMS/code`, `Human/context`, `OSS`.

- [ ] The hierarchy can be represented as an ASCII tree or visual sitemap.
- [ ] The homepage links to the main sections users and crawlers need.
- [ ] Primary sections map to recognizable user tasks and business areas.
- [ ] Important pages are reachable from the homepage or a relevant hub within a shallow click depth.
- [ ] Deep pages have a clear parent, hub, category, or section.
- [ ] The architecture is not flat in a way that overwhelms navigation with too many sibling pages.
- [ ] The architecture is not deep in a way that hides important content.
- [ ] Pages are grouped by intent and entity relationships, not only by internal department names.
- [ ] Large sites use hubs, categories, or section indexes to expose depth.
- [ ] Support, legal, account, utility, and acquisition sections are separated where possible.

## 5. Navigation System

Evidence sources: `Playwright`, `Firecrawl`, `GA4`, `Human/context`, `OSS`.

- [ ] Header navigation exposes the most important sections.
- [ ] Navigation labels use customer language, not internal jargon.
- [ ] Navigation labels are specific enough to predict the destination.
- [ ] Primary navigation does not contain unnecessary or low-value links.
- [ ] Dropdowns or mega menus are used only when they help users scan meaningful groups.
- [ ] Large menus group links by clear categories.
- [ ] Menus are visible, keyboard accessible, mobile usable, and not hidden behind unclear controls.
- [ ] Footer navigation supports secondary discovery, legal links, trust pages, and long-tail discovery without becoming a link dump.
- [ ] Sidebar navigation is used for docs, blogs, categories, or deep sections where section context matters.
- [ ] Mobile navigation includes the same important destinations as desktop.
- [ ] Navigation clicks and exits are reviewed in GA4 when available.

## 6. URL Structure

Evidence sources: `Firecrawl`, `CMS/code`, `GSC`, `OSS`.

- [ ] URL paths are readable and descriptive.
- [ ] URL paths are stable enough to keep through normal content updates.
- [ ] URL paths use lowercase and hyphens consistently.
- [ ] URL paths avoid unnecessary IDs, dates, session IDs, tracking parameters, and internal implementation details.
- [ ] URL paths reflect the site structure where that helps users and maintainers.
- [ ] Trailing slash, host, protocol, and casing policy is consistent.
- [ ] Old URL patterns have redirect rules before a restructuring launches.
- [ ] URL patterns are consistent by page type.
- [ ] Content pages use path URLs rather than query parameters when they should rank.
- [ ] Parameter URLs are controlled by canonicalization, robots policy, internal linking, or platform settings.

## 7. Breadcrumbs

Evidence sources: `Firecrawl`, `Playwright`, `GSC`, `CMS/code`, `OSS`.

- [ ] Breadcrumbs exist when pages sit below top-level sections or when hierarchy helps orientation.
- [ ] Breadcrumb trails mirror the intended hierarchy.
- [ ] Breadcrumb labels match user-facing navigation labels.
- [ ] Breadcrumb links are crawlable anchor links.
- [ ] Current page is not linked as a normal breadcrumb destination unless the design intentionally requires it.
- [ ] Breadcrumb structured data matches visible breadcrumbs.
- [ ] Multiple valid breadcrumb trails are handled only when the page truly belongs in multiple paths.
- [ ] Breadcrumbs do not contradict canonical URLs, hreflang, or sitemap URLs.

## 8. Hub Pages And Topic Clusters

Evidence sources: `GSC`, `GKP`, `Firecrawl`, `GA4`, `Human/context`, `Manual/free SERP`.

- [ ] Major topics, product categories, services, docs sections, and resource areas have hub pages where multiple child pages exist.
- [ ] Hub pages explain the topic or section, not only list links.
- [ ] Hub pages link to important child pages.
- [ ] Child pages link back to relevant hubs.
- [ ] Hubs group pages by intent, audience, product/category, lifecycle stage, or task.
- [ ] Hubs avoid becoming thin tag pages or auto-generated archives.
- [ ] Topic clusters have clear coverage of parent and child questions.
- [ ] Hubs have a conversion or next-step path where appropriate.
- [ ] GSC query data is used to identify missing child pages or cluster gaps.

## 9. Internal Linking

Evidence sources: `Firecrawl`, `Playwright`, `GSC`, `GA4`, `CMS/code`, `OSS`.

- [ ] Priority pages receive internal links from relevant high-traffic or high-authority pages.
- [ ] Contextual links connect related topics, products, categories, docs, and conversion pages.
- [ ] Internal anchors are descriptive and natural.
- [ ] Internal anchors are not mechanically exact-match across the site.
- [ ] New pages link to relevant existing pages.
- [ ] Existing pages are backfilled to link to new priority pages.
- [ ] Related content modules are useful and not random.
- [ ] Broken internal links are fixed.
- [ ] Redirecting internal links are updated to final URLs.
- [ ] Internal links align with canonical URLs.
- [ ] Orphan priority pages are linked from hubs or relevant sections.
- [ ] Internal links support conversion paths, not only crawl paths.

## 10. Taxonomy, Categories, Tags, And Filters

Evidence sources: `Firecrawl`, `GSC`, `GA4`, `GKP`, `GMC`, `CMS/code`, `Human/context`, `OSS`.

- [ ] Taxonomy names match user language and search behavior.
- [ ] Categories are mutually understandable and not confusingly overlapping.
- [ ] Tags are governed and do not create thousands of thin archive pages.
- [ ] Category pages have unique purpose, copy, internal links, and metadata.
- [ ] Category and tag pages are indexable only when they provide search or user value.
- [ ] Empty, single-item, low-value, or duplicate taxonomy pages are noindexed, consolidated, or removed from crawl paths.
- [ ] Ecommerce filters are separated into valuable indexable facets and nonvaluable crawl-controlled facets.
- [ ] Indexable facets have stable URL patterns, useful content, and meaningful demand.
- [ ] Non-indexable facets avoid crawl traps and infinite URL combinations.
- [ ] Filter combinations with no results return useful UX and are not indexable.

## 11. Pagination And Infinite Scroll

Evidence sources: `Firecrawl`, `Playwright`, `GSC`, `CMS/code`, `OSS`.

- [ ] Paginated series use unique crawlable URLs.
- [ ] Page 2 and later pages do not canonicalize to page 1 unless they are truly duplicates.
- [ ] Pagination links are crawlable anchor links.
- [ ] Infinite scroll has crawlable paginated URLs or equivalent linked pages.
- [ ] "Load more" experiences expose discoverable URLs or accessible fallback paths.
- [ ] Important products/posts/items are not discoverable only after many client-side interactions.
- [ ] Pagination, sorting, and filtering URL states are controlled to avoid duplicate crawl paths.

## 12. XML Sitemaps

Evidence sources: `GSC`, `Firecrawl`, `CMS/code`, `OSS`.

- [ ] XML sitemaps contain only canonical, indexable URLs.
- [ ] Utility, noindexed, redirected, broken, duplicate, and parameter-only URLs are excluded.
- [ ] Sitemaps are split by content type or section when useful.
- [ ] Sitemaps are referenced in robots.txt.
- [ ] Sitemaps are submitted in GSC where property access exists.
- [ ] Sitemap coverage is compared to crawl, GSC, GA4, and CMS inventory.
- [ ] `lastmod` is present only when accurate and reflects meaningful page changes.
- [ ] Sitemap errors and discovered/indexed deltas are reviewed.
- [ ] Image, video, or news sitemaps are used only when the content type benefits from them.

## 13. Robots, Noindex, Canonicals, And Utility Areas

Evidence sources: `Firecrawl`, `Playwright`, `GSC`, `CMS/code`, `OSS`.

- [ ] Important acquisition pages are not blocked by robots.txt.
- [ ] Utility pages such as thank-you, checkout success, form success, unsubscribe, login, password reset, account, cart, and internal search results are reviewed for indexability.
- [ ] Utility pages that should not rank use `noindex`, not only robots.txt blocking.
- [ ] Sensitive pages require authentication or authorization. Robots.txt is not used as privacy control.
- [ ] Canonicals align with internal links and sitemaps.
- [ ] Duplicate template variants canonicalize to the preferred URL.
- [ ] Canonicals do not collapse distinct locale, category, product, or paginated pages incorrectly.
- [ ] Robots, noindex, canonical, redirects, and sitemap signals do not contradict each other.

## 14. Redirects And Migration Architecture

Evidence sources: `CMS/code`, `Firecrawl`, `GSC`, `GA4`, `OSS`.

- [ ] Old URLs are mapped to the closest relevant new URLs.
- [ ] Redirects use permanent or temporary status according to intent.
- [ ] Redirect chains and loops are removed.
- [ ] Internal links point directly to final URLs.
- [ ] Canonicals and sitemaps point directly to final URLs.
- [ ] High-value backlinks or historically strong URLs are preserved through relevant redirects.
- [ ] Deleted pages with no replacement return 404 or 410 rather than redirecting to the homepage.
- [ ] Migration launch includes crawl, GSC, GA4, and log checks.
- [ ] Redirect rules are tested before launch.

## 15. Template-Level Architecture

Evidence sources: `CMS/code`, `Firecrawl`, `Playwright`, `GSC`, `GA4`.

- [ ] Every page template supports unique title, meta description, H1, intro, canonical, schema, and internal-link modules.
- [ ] Template defaults do not create duplicate titles or boilerplate copy across many URLs.
- [ ] Templates expose crawlable links to related pages, parent hubs, and conversion paths.
- [ ] Templates support breadcrumbs where hierarchy exists.
- [ ] Templates do not hide main content or links behind client-only rendering.
- [ ] Templates handle empty states, out-of-stock states, removed content, and unpublished content correctly.
- [ ] Templates prevent indexable thin pages from being generated by default.

## 16. Mobile Architecture

Evidence sources: `Playwright`, `Firecrawl`, `Lighthouse`, `GSC`, `Human/context`, `OSS`.

- [ ] Mobile navigation exposes important sections and conversion paths.
- [ ] Mobile menus are discoverable and usable.
- [ ] Mobile and desktop have equivalent primary links and content.
- [ ] Breadcrumbs, footer links, related links, and hub links remain useful on mobile.
- [ ] Important links are not removed from mobile for design convenience.
- [ ] Mobile interstitials do not block architecture discovery.

## 17. Site Search And Discovery Surfaces

Use when the site has internal search, faceted search, resource search, docs search, store locator search, or app/help search.

Evidence sources: `Firecrawl`, `Playwright`, `GSC`, `GA4`, `CMS/code`, `OSS`, `Human/context`.

- [ ] Internal search result pages are not indexable by default unless there is a deliberate, high-value public search landing page strategy.
- [ ] Search result pages are excluded from XML sitemaps.
- [ ] Search result URLs with query parameters are controlled to avoid crawl traps.
- [ ] Zero-result search pages are not indexable.
- [ ] Search UI helps users recover with suggestions, categories, popular pages, or alternative queries.
- [ ] Search logs or GA4 search events are reviewed for missing navigation labels, missing pages, and taxonomy gaps.
- [ ] Store locator or location search pages have crawlable location detail pages where local SEO matters.
- [ ] Docs/help search does not replace crawlable sidebar navigation, section indexes, and related links.

## 18. Local Architecture

Use when the site has physical locations, service areas, or local intent.

Evidence sources: `GBP`, `GMAPS`, `GSC`, `GA4`, `Firecrawl`, `Playwright`, `Human/context`.

- [ ] Location pages map to real locations or service areas.
- [ ] Each location page has unique local value and not just swapped city names.
- [ ] Location pages are linked from a store locator, locations hub, service area hub, footer, or relevant service pages.
- [ ] Location URLs follow a consistent pattern.
- [ ] NAP details match Google Business Profile and Maps data.
- [ ] LocalBusiness structured data matches visible location details.
- [ ] Multi-location navigation helps users find nearby locations without generating useless thin pages.

## 19. Ecommerce Architecture

Use for ecommerce, marketplaces, and large product catalogs.

Evidence sources: `GMC`, `Firecrawl`, `Playwright`, `GSC`, `GA4`, `CMS/code`, `Human/context`.

- [ ] Product, category, subcategory, collection, brand, and guide pages each have a clear role.
- [ ] Category taxonomy matches how users browse and search.
- [ ] Product pages link to parent categories, related products, alternatives, guides, and conversion paths.
- [ ] Category pages include useful content, filters, sorting, internal links, and merchant trust signals.
- [ ] Valuable facets are intentionally indexable and supported with useful content.
- [ ] Nonvaluable facets are controlled to prevent crawl traps.
- [ ] Out-of-stock, discontinued, seasonal, and variant URLs have clear index/redirect/keep policies.
- [ ] Product feed and Merchant Center categories align with website categories where possible.
- [ ] Reviews, shipping, returns, price, availability, and variant data are consistent across page, schema, and Merchant Center.

## 20. Lead Generation And Service Architecture

Use for B2B, SaaS, agencies, consultants, marketplaces, local services, healthcare, legal, education, and other lead-driven sites.

Evidence sources: `GSC`, `GA4`, `GKP`, `Firecrawl`, `Playwright`, `CMS/code`, `Human/context`, `Manual/free SERP`.

- [ ] Service pages, solution pages, industry pages, use-case pages, comparison pages, and location pages each have a clear role.
- [ ] Lead intent pages are reachable from informational pages and navigation paths.
- [ ] Informational pages link to relevant service, solution, demo, pricing, contact, or lead magnet pages.
- [ ] Conversion pages are not isolated from the organic content architecture.
- [ ] Lead magnets have indexable public landing pages when organic acquisition matters.
- [ ] Thank-you and form success pages are not indexable and are not included in sitemaps.
- [ ] Case studies, testimonials, and proof assets link to relevant service, solution, and conversion pages.
- [ ] Location/service-area pages avoid thin city-name swaps and provide real local value.
- [ ] Competitor, alternative, and comparison pages are grouped under a clear comparison hub where this strategy is used.

## 21. App Install And Product-Led Architecture

Use for mobile apps, browser extensions, SaaS onboarding, PLG products, and app install campaigns.

Evidence sources: `GSC`, `GA4`, `GKP`, `Firecrawl`, `Playwright`, `CMS/code`, `Human/context`, `Manual/free SERP`.

- [ ] App install pages clearly separate web SEO intent from app-store listing intent.
- [ ] Platform pages exist where useful: iOS, Android, Chrome extension, Shopify app, Slack app, or other platform surfaces.
- [ ] Feature, use-case, integration, pricing, docs, changelog, and support paths are connected.
- [ ] App-store badges and outbound app links do not replace crawlable product explanation pages.
- [ ] Deep links, app links, universal links, and web fallback URLs are documented where relevant.
- [ ] Onboarding, login, account, invite, and in-app utility pages are not indexable unless intentionally public.
- [ ] Public docs, changelog, and integration pages link back to acquisition and conversion pages.

## 22. International And Multilingual Architecture

Use when the site targets multiple countries, languages, regions, currencies, or locale-specific catalogs.

Evidence sources: `GSC`, `Firecrawl`, `Playwright`, `CMS/code`, `Human/context`, `OSS`.

- [ ] The international structure is explicit: ccTLD, subdomain, subdirectory, or parameter-based.
- [ ] Locale URLs are stable and crawlable.
- [ ] Each localized page has a clear equivalent or intentional gap.
- [ ] Hreflang annotations are reciprocal and point to canonical URLs.
- [ ] `x-default` is used where a global selector or fallback page exists.
- [ ] Navigation, breadcrumbs, sitemaps, canonicals, and hreflang agree on locale URLs.
- [ ] Auto-redirects based on IP or language do not block users or crawlers from accessing alternate locales.
- [ ] Currency, availability, shipping, legal, and local content differences are reflected in page content where relevant.

## 23. Documentation And Support Architecture

Use for docs, help centers, knowledge bases, and API references.

Evidence sources: `Firecrawl`, `Playwright`, `GSC`, `GA4`, `CMS/code`, `Human/context`.

- [ ] Docs have a clear hierarchy: overview, getting started, guides, reference, troubleshooting, API, changelog.
- [ ] Sidebar navigation exposes section context.
- [ ] Docs pages link to prerequisites, next steps, related concepts, and reference pages.
- [ ] Outdated docs are marked, redirected, archived, or updated.
- [ ] Versioned docs have a clear indexing policy.
- [ ] Internal search pages are not indexable by default.
- [ ] Support content has clear task completion paths.
- [ ] API reference pages are crawlable where public visibility matters.

## 24. Competitive And SERP Architecture Benchmark

Evidence sources: `Manual/free SERP`, `GKP`, `GSC`, `Firecrawl`, `Human/context`.

- [ ] Top organic competitors are identified by query set, not only by known business competitors.
- [ ] Competitor navigation, category structure, hubs, URL patterns, and internal linking patterns are reviewed for repeated market conventions.
- [ ] SERP page types are mapped: product pages, category pages, guides, tools, comparison pages, local pages, videos, forums, and documentation.
- [ ] Search features are noted where they influence architecture: local result blocks, product grids, image result blocks, video, discussions, featured snippets, sitelinks, and AI summaries.
- [ ] Missing page types or hubs are identified from SERP evidence.
- [ ] Competitor patterns are used as input, not copied blindly.

## 25. Architecture Governance

Evidence sources: `CMS/code`, `Human/context`, `GSC`, `GA4`, `Firecrawl`.

- [ ] New page creation has rules for parent section, URL pattern, template, canonical, indexability, sitemap inclusion, and internal links.
- [ ] New categories, tags, filters, and collections require approval or documented criteria before becoming indexable.
- [ ] Redirect rules are owned and reviewed before URL changes launch.
- [ ] Navigation changes have an owner and a before/after validation plan.
- [ ] Page deletion has a decision path: update, consolidate, redirect, noindex, 404, or 410.
- [ ] Architecture changes are tracked with date, owner, rationale, affected URLs, and expected impact.
- [ ] GSC and GA4 annotations or equivalent release notes are kept for major architecture changes.

## 26. Measurement And Validation

Evidence sources: `GSC`, `GA4`, `Firecrawl`, `Playwright`, `CMS/code`, `OSS`.

- [ ] Crawl before and after architecture changes.
- [ ] Track number of indexable pages by section and template.
- [ ] Track orphan pages and click depth.
- [ ] Track internal links to priority pages.
- [ ] Track GSC impressions, clicks, CTR, and position by page group.
- [ ] Track GA4 organic landing page engagement and conversion by section.
- [ ] Track sitemap submitted, discovered, indexed, and excluded counts.
- [ ] Track crawl errors, redirect chains, soft 404s, and server errors.
- [ ] Validate navigation and key paths on desktop and mobile.
- [ ] Validate a sample of templates, not just one page.

## 27. Output Template

Evidence sources: cite the specific tools used, such as `Firecrawl`, `Playwright`, `GSC`, `GA4`, `GKP`, `GMC`, `GBP`, `GMAPS`, `CMS/code`, `OSS`, `Manual/free SERP`, or `Human/context`.

```text
Summary:

Architecture map:

Priority issues:
1. [severity] [area]
   Evidence:
   Affected URLs/sections:
   Impact:
   Fix:
   Owner:
   Confidence:

Quick wins:

Structural fixes:

Migration or engineering risks:

Needs data:

Recommended next crawl/check:

Sources used:
```

## 28. Minimal Audit Flow

1. Gather crawl, sitemap, GSC, GA4, and CMS/code inventory.
2. Classify pages by type, section, template, status, indexability, traffic, and value.
3. Build an ASCII tree or visual sitemap of the current structure.
4. Identify priority pages and their desired parent/hub paths.
5. Check navigation, URL paths, breadcrumbs, and internal links for alignment.
6. Check taxonomy, categories, tags, facets, pagination, and utility pages.
7. Compare sitemap and indexability signals with the intended public surface.
8. Review mobile navigation and important templates.
9. Produce prioritized architecture fixes with evidence and owner.
