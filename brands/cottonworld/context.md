# Brand Context Index — cottonworld

Read this first for any task about this brand, then load **only** the files the task needs.
Full workspace built via `brand-setup` on 2026-07-13.

## What Cottonworld is

Indian D2C apparel brand ("The Natural Clothing Co. \| Est. 1987") selling natural **cotton, linen & bamboo**
clothing for men & women, omnichannel (Shopify store + physical stores across India). `cottonworld.net`
(Cloudflare, en-IN). 892 products / 157 collections / 101 pages. Full identity → [brand-dna.json](brand-dna.json).

## File map — what answers what

| Need to know… | Load | When |
|---------------|------|------|
| Identity — voice, audience, competitors, goals | [brand-dna.json](brand-dna.json) | almost any brand task |
| Brand-specific rules, do/don'ts, carry-outs | [knowledge.md](knowledge.md) | **always** for output; overrides defaults |
| Keyword targets, intent, clusters | [keywords/](keywords/) (`keywords.csv`, `clusters.json`) | keyword, content, brief, audit-intent |
| What's already published (all currently broken) | [blogs/summary.md](blogs/summary.md) → `blogs/references/<slug>.md` | content planning |
| Current SEO health + prioritized fixes | [audits/summary.md](audits/summary.md) + [audits/summary.json](audits/summary.json) | audit, fix, reporting |
| What was fetched/run and when | [logs/](logs/) | provenance, trace, resume |
| Setup progress / open items | [tasks/brand-setup.checklist.json](tasks/brand-setup.checklist.json) | verifying onboarding |

## Carry-outs from this audit (2026-07-13)

- **Overall SEO score 0.59 (PARTIAL).** Strong technical base; broken blog content is the top risk.
- **4 audit items are blocked** pending **Google Search Console** (indexation, field CWV) and manual AI-mention testing. Connect GSC via Composio to complete the audit.
- **Keyword-demand validation pending** — `GOOGLE_ADS_PLATFORM_ID` unset; fall back to GSC for demand.
- Do **not** invent brand facts (heritage, materials, competitors) for content until `brand-dna.json` exists.
