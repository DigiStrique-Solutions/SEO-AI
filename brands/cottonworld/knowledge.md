# Cottonworld — Knowledge

Last refreshed from the live site, Firecrawl, Search Console and Lighthouse on 2026-07-27. These brand-specific rules override generic defaults.

## Positioning

- Indian natural-clothing brand founded in 1987.
- Live homepage language: “Made for everyday life”, “Rooted in simplicity”, “Natural fabrics”, “Everyday comfort”, “Made to be lived in”.
- About-page purpose: clothing should feel comfortable, last longer and become part of everyday life.
- Natural fabrics and simple design are the core story. The current homepage also claims “100% natural fabrics”, “Made in India” and “Consciously crafted”.
- Shopify storefront plus physical stores in India. Exact store count is not sourced.

## Writing and voice rules

- Use short, plain, reassuring sentences.
- **Slow living is the primary brand asset and editorial lens.** Cottonworld writes about living well, moving with intention and making room for everyday life; clothing enters the story as quiet support.
- Begin blog introductions with an observation about modern life, a daily rhythm or a real-life tension. Do not begin with fashion trends or the product.
- Keep the underlying hierarchy clear: life first, clothing second. Every article should show how clothing makes work, travel, rest, relationships or daily rituals easier without suggesting that dressing is the main event.
- Lead practical sections with the real-life situation, then explain how fabric, comfort, climate, repeated wear and usefulness help.
- Slow living does not mean inactivity or romanticised leisure. It means fewer unnecessary decisions, thoughtful choices, repeat wear, comfort and attention to what the day actually needs.
- Mention slow living naturally where it adds meaning. Do not force the exact phrase into every section or use it as empty lifestyle decoration.
- Prefer concrete everyday occasions: work, brunch, summer, travel and slow days.
- Sound like a grounded friend: calm, assured, warm, intentional, contemporary and human.
- Invite rather than push. Product links and calls to action must feel like useful paths, never urgency or pressure.
- Use heritage only as “since 1987” unless a deeper history source is cited.
- Keep calls to action simple and product-led.
- Avoid fast-fashion hype, trend obsession, fashion-industry jargon, generic “best/top” claims, inflated sustainability language, invented statistics, excessive excitement and over-poetic lifestyle language.
- Never use the four current article bodies as voice training: they contain Lorem Ipsum, empty bodies or unrelated JSW Defence copy.
- The safe voice model lives in [blogs/writing-style.md](blogs/writing-style.md).

### Cottonworld blog test

Before a blog is approved, confirm that it:

1. feels calm, warm and unhurried;
2. begins with life rather than a product or trend;
3. gives practical value beyond selling;
4. connects comfort to a real everyday activity;
5. supports slow living through simplicity, intention, repeat wear or fewer decisions;
6. integrates products only after the reader's situation is clear;
7. treats clothing as support for life, not the centre of it;
8. remains useful and readable beyond the current season.

## Visual identity

- Primary olive: `#41512A`
- Background: `#FFFFFF`
- Primary text: `#000000`
- Light button text: `#F7F6CA`
- Primary typeface observed: Nunito
- Logo: `https://cottonworld.net/cdn/shop/files/CW-Logo.png?height=35&v=1776677229`

## Merchandising taxonomy

- Gender: Men, Women
- Fabrics: Cotton, Linen, Bamboo, Modal
- Men: shirts, T-shirts, pants, shorts, jackets, kurtas
- Women: tops/blouses, T-shirts, pants, shorts, dresses/jumpsuits, skirts, leggings, culottes
- Occasions: Work, Brunch, Summer, Travel, Slow Days, Gifts
- Commercial groupings: Bestsellers, New Arrivals, Sale

## Search and measurement

- Search Console is connected for `https://cottonworld.net/` with `siteFullUser` permission.
- Final web-search totals for 2026-04-25 to 2026-07-24: 78,662 clicks, 6,065,461 impressions, 1.30% CTR and average position 9.17.
- Exact-match GSC data is saved in `keywords/universe.csv` and `logs/keywords/raw/20260727T122353Z-gsc-refresh.json`.
- Keyword Planner remains blocked because `GOOGLE_ADS_PLATFORM_ID` is unset; volume and difficulty fields are intentionally blank.
- CrUX/PageSpeed field data remains blocked because `GOOGLE_API_KEY` is unset.
- GA4 or another analytics stack is not confirmed. Do not assume GA4.

## Blog database

- Blog index: `https://cottonworld.net/blogs/blog`
- Four published posts were confirmed in the Shopify Atom feed and sitemap.
- All four are unusable as genuine articles:
  - two contain repeated Lorem Ipsum and unrelated JSW Defence copy;
  - two have no real article body and expose placeholder excerpts.
- Search Console inspection confirms the blog index and the sampled broken post are submitted and indexed.
- Treat all four as `rewrite_required`, not optimization candidates.
- Summaries and dates: [blogs/summary.md](blogs/summary.md)
- Voice model: [blogs/writing-style.md](blogs/writing-style.md)

## Current technical carry-outs

- Homepage, blog index and sampled broken post pass URL Inspection and are indexed.
- Search Console reports sitemap warnings and a suspicious 8 indexed of 1,107 submitted web URLs. Investigate the sitemap/index-coverage gap before treating the count as complete sitewide coverage.
- Lighthouse lab run on 2026-07-27: performance 0.34, SEO 0.77, accessibility 0.83, best practices 0.58.
- Lab LCP was 7.20s and total blocking time 11.59s. CLS improved to 0.001 in this single run.
- Lighthouse found non-crawlable anchors, one non-descriptive link, missing image alt attributes, unnamed buttons, contrast failures and heading-order issues.
- Field Core Web Vitals remain unverified.

## Open questions

- Exact store/customer counts
- Current complete product count
- GA4/analytics stack
- Brand-approved competitors
- Leadership names and ownership details
- Price tier by category

## Provenance

- Brand refresh: `logs/web_data/raw/20260727T122353Z-brand-refresh.json`
- GSC refresh: `logs/keywords/raw/20260727T122353Z-gsc-refresh.json`
- Blog refresh: `logs/blogs/raw/20260727T122353Z-blog-refresh.json`
- Audit snapshot: `logs/audits/raw/20260727T122353Z-refresh-checks.json`
