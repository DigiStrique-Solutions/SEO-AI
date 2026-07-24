# Brand Context Index — relivo

Read this first for any task about Relivo, then load **only** the files the task needs.

## What Relivo is (30-second version)

Open-source (MIT) **multi-namespace MCP server in Go**. Five independent MCP servers — memory, skills, gsc, producthunt, event — on one HTTP endpoint over Streamable HTTP. 42 tools, Go 1.26+. Site: go-mcp-server.vercel.app · repo: github.com/Hitesh-s0lanki/go-mcp-server. **Early stage, no production domain yet.**

## File map — what answers what

| Need to know… | Load | When |
|---------------|------|------|
| Identity — voice, audience, competitors, goals, namespaces | [brand-dna.json](brand-dna.json) | almost any brand task |
| Brand-specific rules, canonical facts, do/don'ts, voice | [knowledge.md](knowledge.md) | **always** for output; overrides defaults |
| Keyword targets, volumes, intent, clusters | [keywords/](keywords/) | keyword/content/brief work — **currently empty/blocked** |
| What's already published (dupes, gaps) | [blogs/summary.md](blogs/summary.md) | content planning — **none yet** |
| Current SEO health + fixes | [audits/summary.json](audits/summary.json) | audit/reporting — **not run yet** |
| What was fetched/run and when | [logs/](logs/) | provenance, trace, resume |
| Setup progress / open items | [tasks/brand-setup.checklist.json](tasks/brand-setup.checklist.json) | resuming or verifying onboarding |

## Brand-specific carry-outs (must honor — from knowledge.md)

- **Audience is engineers.** Voice is precise, technical, understated; show code/config, don't sell with adjectives. No "seamless/powerful/revolutionary".
- **No GSC/GA4 for Relivo's own site right now** — no search/analytics evidence claims until a property is verified. Keyword demand is **blocked** (no GSC; Keyword Planner platform-id unset).
- **Never invent** tool counts beyond the recorded 42/5, adoption/star numbers, users, benchmarks, or a pricing model — none are published.
- **"Relivo" is the MCP server only** — not the unrelated supplement/AI-events/footwear brands. Don't reference a `relivo.*` domain.
- **No en/em dashes** in customer-facing copy.

## Setup status (2026-07-21)

- **Phase 0 (init)** — done.
- **Phase 1 (crawl + brand DNA)** — done. `brand-dna.json` + `knowledge.md` written from live site + README.
- **Phase 2 (keywords)** — `not_checked_blocked` (no GSC; Keyword Planner platform-id unset).
- **Phase 3 (existing blogs)** — none found on the site; nothing to import.
- **Phase 4 (audits)** — not run yet (Lighthouse/PageSpeed available on request).

## Schemas & tool map

Exact file schemas + provider/tool mapping → [.claude/skills/brand-setup/references/file-schemas.md](../../.claude/skills/brand-setup/references/file-schemas.md)
