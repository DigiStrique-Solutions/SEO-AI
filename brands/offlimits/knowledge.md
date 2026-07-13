# knowledge.md — OFFLIMITS (brand-specific rules)

> Seeded during the 2026-07-13 audit. This is a **partial** workspace — run the `brand-setup` skill for full onboarding (brand-dna, keywords, blogs, competitors).

## Must honor

- **Platform is Shopify.** SEO fixes must fit Shopify/theme + app constraints (title-tag templates, metafields, schema via theme/liquid or apps).
- **Market is India.** Currency INR; targeting/queries are India-scoped (e.g. "…in India", ₹ price points).
- **No GSC/GA4 connected yet.** Do not claim indexation, field CWV, or query/click data until GSC is connected via Composio. Mark such items `not_checked_blocked`, never `pass`.
- **Keyword demand is unverified** — `GOOGLE_ADS_PLATFORM_ID` is unset (Keyword Planner blocked) and there's no GSC fallback. Don't present volumes as verified.
- **Brand name is inconsistent** across the site (OFF LIMITS / Offlimits / Off Limits). Pick one canonical form before writing customer-facing copy or schema.
- **Analytics is partially broken** — GoKwik analytics script fails DNS. Don't assume tracking data is complete.

## Carry-outs from the first audit (see audits/summary.md)

- Strengths to preserve: strong technical/canonical hygiene, rich schema (Product/FAQ/Article/Breadcrumb/OnlineStore), and unusually good AI/AEO readiness (llms.txt, agentic-discovery sitemap, FAQ schema).
- Biggest levers: performance (app/JS bloat), product title tags at scale, image alt text, product review-star schema.
