# Brand Knowledge — Inc.5 (inc5shop)

> Free-form, living memory for anything brand-specific that doesn't fit the structured `brand-dna.json`.
> Add a dated entry whenever you learn something worth reusing anywhere, anytime. Newest first.
> `brand-dna.json` = the canonical, structured facts. This file = context, nuances, decisions, and one-offs.

---

## How to use this file

- One entry per fact/decision. Prefix with a date `(YYYY-MM-DD)` so history is traceable.
- Keep entries short and reusable — write what a future run would need to act correctly.
- If an entry hardens into a stable, structured fact, promote it into `brand-dna.json` and note it here.
- Never delete history; strike through or add a correcting entry instead.

---

## Product & Positioning

- Indian fashion-footwear + accessories brand, **established 1998**, started at a 100 sq. ft. store in Mumbai's Heera Panna.
- Legacy + omnichannel: **90+ stores, 50+ cities, 20+ states**; also sold at **Lifestyle, Centro, Shoppers Stop**. inc5shop.com is the D2C online storefront.
- Positioning promise: **comfort + craftsmanship + contemporary design**. Women's footwear is the lead category; men's (incl. **Privo**) and **handbags/wallets** are secondary. **Inc.6** is a sub-label collection.
- Core taxonomy — Women: Heels, Transparent Heels, Sandals, Mules, Flats, Ethnic, Boots, Wedges, Platform, Pumps, Comfort. Men: Driving Shoes, Formal Shoes, Sandals, Slip-Ons, Boots, Large Size ("Prime Fit"). Bags: Sling, Clutch, Shoulder, Wallets, Backpacks.

## Market & Commercial context

- **Market = India, currency = INR (₹).** Everything (keywords, demand, competitors, seasonality) should be scoped to India.
- Seasonality/occasions are central to merchandising: **EOSS (End of Season Sale), festive, wedding, Navratri, Raksha Bandhan, Haldi/Mehendi, party**. Plan content/keywords around Indian occasion calendar.
- Heavy sale/discount framing ("Flat 50% Off", "Hot Stepper Sale"). Value + urgency is a core lever.
- **Club5** loyalty program: 1 point = 1 rupee, checked by mobile number.

## Messaging Do / Don't

- **Do:** occasion- and edit-led framing (festive/wedding/party/ethnic/comfort), comfort + "true to size" reassurance, legacy/trust ("since 1998"), real customer-review social proof.
- **Don't:** invent product specs, materials, prices, or store counts beyond what the site states; don't use generic Western fashion framing that ignores the Indian occasion context.

## Measurement & Tooling (important for SEO work)

- **Google Search Console** — site shows `google-site-verification` meta (verified). Connect via **Composio** for search performance, indexing, and page/query evidence. This is the priority evidence source.
- **Google Ads Keyword Planner** via **Composio** → keyword demand research; scope to **India**.
- **Analytics platform is NOT confirmed** (GA4 vs other) — do NOT assume GA4. Confirm the connected analytics before citing behavioral/conversion numbers. → open question.
- Third-party stack observed (do not treat as SEO analytics): Shopify (platform), **GoKwik** (checkout), **ClickPost** (order tracking + returns, on `inc5shop.clickpost.in`), **Judge.me** (reviews, ~1,758 reviews), **LimeChat / Shiprocket Engage** (WhatsApp chat).

## Technical / SEO notes (to verify in audits)

- Platform: **Shopify** (`/cdn/shop/` assets, `shopify-digital-wallet` meta, shop id 56488263854).
- **Crawl/index hygiene risk:** the URL map surfaced **150+ collections**, many dated/operational "dark" collections (e.g. `full-fresh-aug-2023`, `creative-31-10-2023`, `zero-stock-25-09`, `testnew`, `put-in-draft-...`). These likely shouldn't be indexable — flag for audit (index bloat, thin/duplicate collections, crawl budget).
- Blog lives at `/blogs/blog`.
- Order tracking, returns, and some support flows live off-domain (`inc5shop.clickpost.in`) — exclude from on-domain SEO scope but note internal links.
- Legacy domain **inc5shoes.co.in** referenced in policy pages — confirm redirect/canonical relationship to inc5shop.com.
- GST notice on site (Gazette Notification No. 09/2025-Central Tax dated 17 Sep 2025) — pricing/MRP compliance context, not SEO.

## Proof & Customers

- **~1,758 Judge.me reviews**; dominant sentiment: comfort, "true to size", value. Reviews are a strong on-page trust asset (schema opportunity).
- Repeat-buyer signal: reviewers mention buying offline then finding size online.

## Contact & Social (evidence sources)

- Email `customercare@inc5shoes.com`; Call/WhatsApp **+91 9152646417**.
- Social: Facebook `inc5shoesofficial`, Instagram `inc5official`, Pinterest `inc5shoes`, YouTube `@Inc.5ShoesOfficial`, LinkedIn `inc.5-shoes-private-limited`.

## Key Pages (evidence sources)

- `/` — hero edits, category tiles, shoppable video, reviews, full nav taxonomy, palette.
- `/pages/about-us` — origin story, store/city/state counts, retail partners.
- `/pages/contactus` — support channels.
- `/blogs/blog` — content/blog (Phase 3 source).
- `/collections/*` — category & occasion collections (keyword + audit targets).
- `/pages/frequently-asked-questions`, `/pages/refund-policy`, `/pages/payment-delivery-policy`, `/pages/store-locator` — support/trust pages.

## Open Questions / To Confirm

- Exact brand hex values, typography, canonical vector logo.
- Connected analytics platform (GA4 or other).
- Approved competitor set & primary positioning.
- Priority growth category for SEO (women's vs men's/Privo vs handbags).
- Index hygiene decision on dated/dark collections.
- Canonical relationship between inc5shop.com and inc5shoes.co.in.

## Change Log

- **2026-07-13** — File created. Seeded from Phase 1 crawl of homepage, about-us, contact (Firecrawl, run `inc5shop-phase1-20260713`).
