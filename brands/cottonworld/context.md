# Brand Context Index — cottonworld

> ⚠️ **Audit-only workspace.** This brand was created to hold the results of an on-demand SEO audit of
> https://cottonworld.net. It is **not fully onboarded** — `brand-dna.json`, `knowledge.md`, and
> `keywords/` are not yet built. Run the **`brand-setup`** skill to complete onboarding before content work.

## What Cottonworld is (from the audit, unverified brand facts)

Indian D2C apparel brand ("The Natural Clothing Co. \| Est. 1987") selling natural cotton & linen clothing
for men & women. Shopify storefront on `cottonworld.net` (Cloudflare, en-IN). ~892 products / 157 collections.
*Any brand fact used for content must be verified via `brand-setup`, not assumed from here.*

## File map — what answers what

| Need to know… | Load | When |
|---------------|------|------|
| Current SEO health + prioritized fixes | [audits/summary.md](audits/summary.md) + [audits/summary.json](audits/summary.json) | audit, fix, reporting |
| Per-audit item detail + evidence | `audits/<audit_id>.json` | drilling into a finding |
| Raw crawl payloads, screenshot, run log | [logs/audits/](logs/audits/) | provenance, re-check |
| Identity, voice, keywords, blogs | *not built yet* | run `brand-setup` |

## Carry-outs from this audit (2026-07-13)

- **Overall SEO score 0.59 (PARTIAL).** Strong technical base; broken blog content is the top risk.
- **4 audit items are blocked** pending **Google Search Console** (indexation, field CWV) and manual AI-mention testing. Connect GSC via Composio to complete the audit.
- **Keyword-demand validation pending** — `GOOGLE_ADS_PLATFORM_ID` unset; fall back to GSC for demand.
- Do **not** invent brand facts (heritage, materials, competitors) for content until `brand-dna.json` exists.
