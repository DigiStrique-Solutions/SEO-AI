# Brand Context Index — inc5shop (Inc.5)

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

- **Market is India, currency INR.** Scope keywords, demand, competitors, and seasonality to India.
- **Occasion-led merchandising** (EOSS, festive, wedding, Navratri, Raksha Bandhan) drives the calendar — plan content around it.
- **Women's footwear is the lead category**; men's (Privo) and handbags/wallets are secondary.
- **GSC + Keyword Planner via Composio** are the evidence sources; **analytics platform is unconfirmed — do NOT assume GA4.**
- **Index-hygiene risk:** 150+ collections incl. many dated/"dark" ones — a known audit focus.

## Schemas & tool map

Exact file schemas + provider/tool mapping → [.claude/skills/brand-setup/references/file-schemas.md](../../.claude/skills/brand-setup/references/file-schemas.md)
