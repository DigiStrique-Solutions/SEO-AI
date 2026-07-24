# Voice Contract — Relivo · blog "Publish the task, not the work"

Built from `context.md` order: `knowledge.md` (rules win) → `brand-dna.json` (voice fields). Written 2026-07-21.

```text
Register:        Precise, technical, understated. Written for engineers who already know MCP, Go, HTTP.
                 Lead with what the system does and the design decision behind it. Show code/config, do not sell.
Patterns to use: Capability-first framing (the task crossing a boundary, not the vendor); architecture stated
                 as a property the reader gets (decoupling, durability, owner-scope, async fan-out) each anchored
                 to a real Relivo mechanism; the real event log (topic + offsets) as the hero exhibit, the way
                 the landing page uses mcp.json; terse invariant lines ("Just publish the task.", "Nothing is cached.").
Proof points:    Five namespaces on one endpoint; event = Kafka on Confluent Cloud; publish returns partition+offset;
                 consume is owner-scoped by X-API-Key (x-mcp-owner header); durable per-caller consumer group;
                 self-registering mux (cmd/server/main.go never changes); skills = live SKILL.md from GitHub, nothing cached.
Vocabulary:      namespace, topic, partition, offset, consumer group, owner-scope, X-API-Key, producer, consumer,
                 Streamable HTTP, pgvector, MCP client. Product name: Relivo. Repo: go-mcp-server.
Prohibitions:    No hype words (revolutionary/seamless/powerful/supercharge/unlock/game-changing). No invented numbers
                 (no latency figures, no adoption/star counts, no benchmarks). No en/em dashes anywhere. Do not define
                 MCP or Kafka from scratch. Do not imply a paid tier, SLA, or production domain (there is none yet).
Reader:          Engineers building AI agents / MCP clients, and Go/infra engineers who self-host and extend.
Positioning:     An agent that PUBLISHES tasks vs. an agent that DOES every task. The event namespace is the verb;
                 the other namespaces are the vocabulary. Against synchronous single-worker agents and bespoke per-API wiring.
Source:          brands/relivo/knowledge.md, brands/relivo/brand-dna.json, brands/relivo/logs/web_data/raw/20260721T145007Z-brand-dna-crawl.json
```

**First-party run facts** (topic `go-mcp-events`, the three events at offsets 0/1/2, skill names `frontend-design` / `awesome-design-skills`, the `information.md` Product Hunt task) come from the author's own session. Logged as `human_note` sources. Keep exactly as given, do not embellish or add infra specifics not provided.

**Competitor test:** if the draft would read the same for any generic "message queue for agents" post after find-and-replace, Relivo is not on the page. Non-negotiable specifics that must show: five-namespaces-one-endpoint, event-as-verb / namespaces-as-vocabulary, X-API-Key owner-scoping on consume, and the self-registering mux as why adding a capability costs the producer nothing.
```
