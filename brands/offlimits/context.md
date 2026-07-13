# Brand Context Index — offlimits

Read this first for any task about this brand, then load **only** the files the task needs.

**OFFLIMITS** — Indian D2C sports & athleisure brand (Shopify, `offlimits.co.in`) by Gurukirpa Lifestyle Company. Value-for-money performance footwear + apparel, made in India. Workspace built via `brand-setup` on 2026-07-13.

## File map — what answers what

| Need to know… | Load | When |
|---------------|------|------|
| Identity — story, tech, audience, competitors, goals | [brand-dna.json](brand-dna.json) | almost any brand task |
| Brand-specific rules & do/don'ts | [knowledge.md](knowledge.md) | **always** for output; overrides defaults |
| Keyword targets, clusters, intent | [keywords/](keywords/) (`keywords.csv`, `clusters.json`, `research-summary.json`) | keyword, content, brief, audit-intent |
| What's already published (dupes, gaps) | [blogs/summary.md](blogs/summary.md) → `blogs/references/<slug>.md` | content planning, briefs |
| Current SEO health + prioritized fixes | [audits/summary.md](audits/summary.md) · [audits/summary.json](audits/summary.json) | audit, fix, reporting |
| Per-audit findings + evidence | [audits/](audits/) (6 audit JSONs) | drilling into a specific area |
| What was crawled/run and when | [logs/](logs/) | provenance, trace, avoid re-fetch |
| Setup progress / open items | [tasks/brand-setup.checklist.json](tasks/brand-setup.checklist.json) | resuming/verifying onboarding |

## Brand-specific carry-outs (must honor — from knowledge.md)

- **Shopify · India (INR).** Fixes must fit Shopify; targeting is India-scoped.
- **Standardize the brand name** — site mixes `OFF LIMITS` / `Offlimits` / `Off Limits`.
- **No GSC/GA4 in our workspace** — indexation, field CWV, query data are `not_checked_blocked`, never assumed (the brand runs its own GSC; it's just not connected here).
- **Keyword demand is estimated/blocked** — Keyword Planner platform-id unset; volumes in `keywords/` are blank by design.
- **Analytics partially broken** — GoKwik analytics script fails DNS; tracking may be incomplete.
- **Voice:** motivational, gutsy, inclusive, value-conscious ("OFF LIMITS Tribe"); pair performance with affordability + made-in-India; cite real tech (Athlite®, Flexinit®, Glovefit®, Wiktech®, memory foam).

## Known blockers to unblock later

Connect **GSC** + a **PageSpeed/CrUX key** via Composio, and set **`GOOGLE_ADS_PLATFORM_ID`**, to close: field Core Web Vitals, indexation coverage, AI-mention testing, and real keyword volumes.

## Schemas & tool map

Exact file schemas + provider/tool mapping → [.claude/skills/brand-setup/references/file-schemas.md](../../.claude/skills/brand-setup/references/file-schemas.md)
