# Relivo — Brand Knowledge (living memory)

> Brand-specific rules that override generic defaults. Seeded 2026-07-21 from a Firecrawl crawl of the live site + the GitHub README. Provenance: `logs/web_data/activity.jsonl` (run `relivo-setup-20260721`).

## What Relivo is (one line)

An **open-source, MIT-licensed, multi-namespace MCP server in Go** — five independent MCP servers (memory, skills, gsc, producthunt, event) mounted on one HTTP endpoint over Streamable HTTP. **42 tools, 5 namespaces, 1 endpoint, Go 1.26+.**

## Canonical facts (do not drift)

- **Name:** Relivo (also "Relivo MCP Server"). Repo is `go-mcp-server`; the product brand is **Relivo**.
- **Surfaces:** marketing/docs site `go-mcp-server.vercel.app` · hosted API `go-mcp-server-latest.onrender.com/<namespace>/mcp` · beta app `relivo-fe.vercel.app` · source `github.com/Hitesh-s0lanki/go-mcp-server`.
- **No `relivo.*` production domain yet.** Early stage. Do not imply a stable brand domain in copy.
- **The five namespaces (memorize the tool counts):**
  - `memory` (6 tools) — per-user long-term memory, hybrid RAG (semantic + keyword) over **Postgres + pgvector**; survives across sessions; per-key row scoping.
  - `skills` (2 tools) — find + download **Agent Skills live from GitHub**; nothing cached.
  - `gsc` (17 tools) — Google Search Console: properties, search-analytics, URL inspection, sitemaps; mutations gated behind `GSC_ALLOW_DESTRUCTIVE`.
  - `producthunt` (11 tools) — Product Hunt v2 GraphQL: posts, topics, collections, users + raw GraphQL escape hatch; read-only.
  - `event` (6 tools) — Kafka over MCP on **Confluent Cloud**: publish/consume with durable per-caller consumer groups; topic admin gated behind `KAFKA_ALLOW_TOPIC_ADMIN`.
- **Architecture invariants** (these are the brand's proof points — use them, verbatim in spirit):
  - Self-registering namespaces via `mcpx.Register` in `init()`; **`cmd/server/main.go` never changes** when you add one.
  - **Keyed by default** — every namespace requires `X-API-Key` before dispatch (401 otherwise); `/healthz` is the only exempt route.
  - Isolation — "a domain never reaches across another except through `internal/mcpx`."
  - Built on the **official MCP Go SDK's Streamable HTTP transport**, stdlib `net/http`, structured `slog` logging.
- **Tech stack:** Go 1.26+, official `modelcontextprotocol/go-sdk`, `net/http`, `log/slog`, Postgres + pgvector, Confluent Cloud Kafka; frontend is Next.js + Tailwind + shadcn/ui.
- **Run it:** `cp .env.example .env && make run` → listens on `:8080`.

## Voice contract (write like this)

- **Audience is engineers.** Assume they know MCP, Go, HTTP. Do NOT over-explain basics or sell benefits with adjectives.
- **Show, don't sell.** Lead with what it does and the design decision behind it. Code/config snippets (`mcp.json`, `register.go`) carry the argument.
- **Exact nouns over hype:** namespace, mux, transport, `init()`, pgvector, slog, consumer group. Never "revolutionary", "seamless", "powerful", "game-changing".
- **Terse, confident, invariant-style claims:** "Keyed by default." "Nothing is cached." "That's it."
- **Monochrome, minimal, infra-doc register** (Vercel/Linear/shadcn lineage). Match that restraint in copy too.
- Full voice contract for content: write it to `.claude/skills/content-seo-authenticity/references/brand-voice-contract.md` before drafting.

## Do / Don't

- **DO** anchor every claim in the namespace list, tool counts, architecture invariants, or README facts above.
- **DO** exploit the meta-angle honestly: a dev-tools brand that itself ships a GSC namespace and Agent-Skills tooling. Good content territory (MCP, agent memory, RAG, dogfooding SEO tools).
- **DON'T** invent tool counts, benchmarks, adoption/star numbers, users, or a pricing model — **none are published.** → `open_questions`.
- **DON'T** imply enterprise readiness, SLAs, or a paid tier. State is "open source + free hosted endpoint + beta app."
- **DON'T** reference a `relivo.com`/`relivo.io` domain — those are unrelated brands (supplement, AI-events). This Relivo is the MCP server only.
- **DON'T** use en/em dashes in any customer-facing copy (house rule).

## Measurement / tooling (brand-specific)

- **No GSC or GA4 connection for Relivo's own site right now** (confirmed by user). Do **not** claim search or analytics evidence for this brand until a property is verified.
- **Keyword demand is blocked** — no GSC, and Google Ads Keyword Planner `platform-id` is unset (see memory `keyword-planner-platform-id-blocked`). Keyword research falls back to seed/manual and must be labelled `not_checked_blocked`, never a silent pass.
- Once Relivo verifies its own domain in Search Console, it can **dogfood its own `gsc` namespace** for measurement — flag this as the natural next step, not a current capability.

## Key pages

- `/` — landing (hero, namespace cards, feature pillars, `mcp.json`).
- `/doc/overview` — docs entry; per-namespace docs at `/doc/{memory,skills,gsc,producthunt,event}`, plus `/doc/architecture`, `/doc/quickstart`.
- `github.com/Hitesh-s0lanki/go-mcp-server` — source, README, layout, Makefile targets.

## Open questions

See `brand-dna.json → open_questions`. Biggest for content: (1) monetization/model, (2) canonical domain, (3) lead ICP (tool-consumers vs. self-hosters), (4) whether a `/blog` content surface exists yet.
