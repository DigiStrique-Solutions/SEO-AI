# Cottonworld — Knowledge (living memory)

Seeded from the public crawl on 2026-07-13. Brand-specific rules here **override generic defaults**.

## Positioning

- Indian natural-clothing brand, **Est. 1987**. Tagline: *"The Natural Clothing Co."* / *"Made with care. Worn for years."*
- Core promise: comfortable, breathable, climate-appropriate, **long-lasting** clothing in **natural fabrics — cotton, linen, bamboo**.
- Sustainability framing ("Go Green"), heritage, and comfort — **not** discount-first or fast-fashion trend churn.
- Omnichannel: online (Shopify) **plus physical stores across India**.

## Merchandising taxonomy (use these for keyword/page mapping)

- **Gender:** Men, Women.
- **Fabric:** Cotton, Linen, Bamboo.
- **Top wear:** T-Shirts, Shirts, Kurtas, Jackets, Tops, Vests.
- **Bottom wear:** Pants, Shorts, Skirts, Leggings, Culottes.
- **Other:** Dresses/Jumpsuits, Lounge Wear, Sleep Wear, Co-ords.
- **Collections (occasion):** Work, Travel, Brunch, Summer, Bestsellers, New Arrivals.

## Voice do / don't

- **Do:** lead with comfort, fabric, care, and longevity; use warm, plain, reassuring lines; cite heritage (1987) and natural materials.
- **Don't:** hype, generic "best/top" claims without evidence, discount-only messaging, invented stats. The store/customer counts on the homepage are **animated counters that render 0 in raw HTML — do not quote them as facts** until real numbers are sourced.

## Measurement / tooling notes

- Platform: **Shopify** (Cloudflare, edge Mumbai, `content-language en-IN`). Shopify web-pixel analytics cookies present.
- **GSC is NOT connected** — indexation and field Core Web Vitals could not be verified in the audit. Connect via Composio to unblock.
- **Keyword demand is blocked**: `GOOGLE_ADS_PLATFORM_ID` is unset, so Keyword Planner can't be called; fall back to GSC once connected. Keyword volumes in `keywords/` are therefore **unmeasured** this run.
- GA4 status unconfirmed — do not assume GA4; verify the actual analytics stack.

## Proof / assets

- Socials (use as Organization `sameAs`): `https://www.facebook.com/cottonworld`, `https://www.instagram.com/cottonworldlive/`.
- Policy pages live: privacy, shipping, refund, terms, store-locator. **Missing (404): `/pages/contact`, `/pages/track-order`** — confirm correct URLs.

## Key pages

- Home `/` · Collections `/collections/<fabric|category>` (157) · Products `/products/<handle>` (892) · Blog `/blogs/blog` (5 URLs) · About `/pages/about-us`.

## Carry-outs from the SEO audit (2026-07-13) — see `audits/summary.md`

- Overall **0.59 (PARTIAL)**. Strong technical base; **the blog is the top liability**.
- 🔴 **Blog posts render placeholder lorem-ipsum + wrong "JSW Defence" copy, 0 H1, missing/wrong metas** — unpublish or rewrite before any content work.
- Content/page templates emit **0 H1**; collection titles are **keyword-stuffed (~130 chars)**.
- **CLS 0.155**, **0/340 images in WebP/AVIF** (~4.7MB payload).
- Homepage has **no WebSite schema and no `sameAs`** — add the two socials above.
- No product reviews/aggregateRating; no BreadcrumbList; no AEO/FAQ content.

## Open questions

See `brand-dna.json.open_questions` — store/customer counts, named competitors, analytics stack, contact/track-order URLs, logo asset, price tier.
