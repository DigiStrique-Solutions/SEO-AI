# Brand Context Index — Winn Foods

Read this first for any Winn Foods task, then load only the files required for that work.

## File map

| Need | Load | When |
|---|---|---|
| Identity, audience, voice, product scope, competitors | [brand-dna.json](brand-dna.json) | Almost any brand task |
| Brand rules, writing patterns, claims guardrails | [knowledge.md](knowledge.md) | Always before creating output |
| Keyword targets and demand | [keywords/](keywords/) | Keyword research, briefs, planning |
| Published recipes/blogs and writing examples | [blogs/summary.md](blogs/summary.md), then `blogs/references/<slug>.md` | Content planning and writing |
| SEO health and fixes | [audits/summary.json](audits/summary.json) and [audits/summary.md](audits/summary.md) | Audit and implementation |
| Fetch/run provenance | [logs/](logs/) | Verification and refresh decisions |
| Setup progress and blockers | `tasks/brand-setup.checklist.json` | Resume or QA onboarding |

## Brand-specific carry-outs

- Voice is playful, sensory, high-energy, and convenience-forward; use dish-specific language and selective wordplay.
- Shopify, GSC (`sc-domain:winn-foods.com`), and Winn Foods GA4 (`properties/533748438`) are confirmed; read `knowledge.md` for contamination and interpretation cautions.
- Ingredient, nutrition, health, and clean-label claims require exact product-level evidence.
- Re-check promotions, prices, coupons, and shipping thresholds before publishing.
- Existing recipes are the primary style reference and must be checked for content duplication.

## Provenance

- Foundational setup run: `winn-foods-setup-20260727`.
- Crawl record: `logs/web_data/raw/20260727T072346Z-brand-dna-crawl.json`.
- Branding record: `logs/web_data/raw/20260727T072449Z-homepage-branding.json`.
