# Logs

Provenance and activity trail for the brand. Every external fetch, API pull, and run is recorded here
with its **raw input/output**, so anything produced elsewhere in the brand (brand-dna, keywords, blogs,
audits) can be traced back to the exact source and moment it came from.

## Layout

```
logs/
├── web_data/     # raw site crawls / page fetches (brand-dna extraction, audit crawls)
├── blogs/        # blog discovery + fetches from the brand's site
├── keywords/     # keyword-demand + Search Console pulls
├── audits/       # audit-run inputs (site checks, evidence manifests)
└── <category>/   # add more as new data sources appear
```

Each category folder holds:
- **`activity.jsonl`** — append-only event log, one JSON object per line (newest appended at the end).
- **`raw/`** — the raw payloads referenced by each event's `output_ref`.

## Event schema (`activity.jsonl`)

| Field | Meaning |
|-------|---------|
| `ts` | ISO-8601 UTC timestamp of the event |
| `run_id` | groups events that belong to the same run |
| `action` | `fetch` \| `crawl` \| `api_call` \| `audit_run` \| `generate` |
| `category` | matches the folder (`web_data`, `blogs`, …) |
| `source` | URL or endpoint the data came from |
| `provider` | `web` \| `firecrawl` \| `gsc` \| `keyword_planner` \| `audit_engine` |
| `input` | the raw request params / query used |
| `output_ref` | path to the stored raw payload under `raw/` |
| `status` | `ok` \| `partial` \| `error` |
| `records` | count of items returned |
| `actor` | who/what triggered it |
| `notes` | free text |

## Rules
- **Append, never overwrite** — logs are history.
- Raw payloads are immutable; if a source is re-fetched, write a new `raw/` file with a new `ts`.
- Downstream files should cite the `run_id` or `output_ref` they were derived from.
