# Brand Context Index — offlimits

Read this first for any task about this brand, then load **only** the files the task needs.

> **Status: partial workspace.** Seeded by the 2026-07-13 in-depth audit, not a full `brand-setup` run. `keywords/`, `blogs/`, and a fully-researched `brand-dna.json` are not yet built — run the **brand-setup** skill to complete onboarding.

## File map — what answers what

| Need to know… | Load | When |
|---------------|------|------|
| Identity, product lines, socials, policies (observed) | [brand-dna.json](brand-dna.json) | any brand task (note `open_questions`) |
| Brand-specific rules & do/don'ts | [knowledge.md](knowledge.md) | **always** for output; overrides defaults |
| Current SEO health + prioritized fixes | [audits/summary.md](audits/summary.md) · [audits/summary.json](audits/summary.json) | audit, fix, reporting |
| Per-audit findings + evidence | [audits/](audits/) (6 audit JSONs) | drilling into a specific area |
| What was crawled/checked and when | [logs/](logs/) | provenance, trace, avoid re-fetch |

## Brand-specific carry-outs (must honor — from knowledge.md)

- **Shopify · India (INR).** Fixes must fit Shopify; targeting is India-scoped.
- **No GSC/GA4 connected** — indexation, field CWV, and query data are `not_checked_blocked`, never assumed.
- **Keyword demand unverified** — Keyword Planner platform-id unset; no GSC fallback.
- **Standardize the brand name** (OFF LIMITS / Offlimits / Off Limits) before customer-facing copy or schema.

## Schemas & tool map

Exact file schemas + provider/tool mapping → [.claude/skills/brand-setup/references/file-schemas.md](../../.claude/skills/brand-setup/references/file-schemas.md)
