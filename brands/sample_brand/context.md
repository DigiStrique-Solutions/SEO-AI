# Brand Context Index — sample_brand

Read this first for any task about this brand, then load **only** the files the task needs.

## File map — what answers what

| Need to know… | Load | When |
|---------------|------|------|
| Identity — voice, audience, competitors, goals | [brand-dna.json](brand-dna.json) | almost any brand task |
| Brand-specific rules, decisions, do/don'ts | [knowledge.md](knowledge.md) | **always** for output; overrides defaults |
| Keyword targets, volumes, intent, clusters | [keywords/](keywords/) (`keywords.csv`, `clusters.json`) | keyword, content, brief, audit-intent |
| What's already published (dupes, gaps) | [blogs/summary.md](blogs/summary.md) → `blogs/references/<slug>.md` | content planning, briefs |
| Current SEO health + prioritized fixes | [audits/summary.json](audits/summary.json) + [summary.md](audits/summary.md) | audit, fix, reporting |
| What was fetched/run and when | [logs/](logs/) | provenance, trace, resume, avoid re-fetch |
| Setup progress / open items | `tasks/brand-setup.checklist.json` | resuming or verifying onboarding |

## Brand-specific carry-outs (must honor — from knowledge.md)

- **Analytics is PostHog, not GA4.** Never assume/reference GA4 for this brand.
- **GSC + Keyword Planner via Composio** — use for search/keyword evidence.
- **Voice:** direct, operator-centric, metrics over adjectives; no generic AI hype.
- **Approval gates** for high-stakes actions are a selling point, not a limitation.

## Schemas & tool map

Exact file schemas + provider/tool mapping → [.claude/skills/brand-setup/references/file-schemas.md](../../.claude/skills/brand-setup/references/file-schemas.md)
