# Logs & Failure Handling (cross-cutting)

Applies to every phase. This is how work is tracked and how failures are recorded rather than hidden.

## Logging — every external action

For any fetch / crawl / API pull / audit run, append one line to
`brands/<brand_id>/logs/<category>/activity.jsonl` and store the raw payload in
`brands/<brand_id>/logs/<category>/raw/<ts>-<slug>.json`.

Categories: `web_data` · `blogs` · `keywords` · `audits` (add more as needed).

**Event shape (one JSON object per line):**
```json
{"ts":"<ISO-8601 UTC>","run_id":"<groups a run>","action":"crawl|fetch|api_call|audit_run|generate",
 "category":"web_data","source":"<url|endpoint>","provider":"firecrawl|playwright|gsc|keyword_planner|crux|pagespeed|lighthouse|posthog|web|audit_engine",
 "input":{...raw request params...},"output_ref":"raw/<ts>-<slug>.json",
 "status":"ok|partial|error","records":<n>,"actor":"<agent>","notes":"<text>"}
```

Rules: **append, never overwrite**; raw payloads are **immutable** (re-fetch = new file, new `ts`); downstream files cite the `run_id`/`output_ref` they came from.

## The setup checklist file

Maintain `brands/<brand_id>/tasks/brand-setup.checklist.json`:
```json
{
  "schema_version": "1.0.0",
  "brand_id": "<id>",
  "started_at": "<ts>",
  "updated_at": "<ts>",
  "phases": [
    { "phase": "1-crawl-brand-dna", "status": "done|in_progress|pending|failed",
      "items": [ { "id": "p1.crawl-ok", "status": "done", "severity": "high", "note": "", "log_ref": "" } ] }
  ]
}
```
Update an item the moment it passes or fails. Phase status = `failed` if any `high` item failed; `done` when all non-failed items are resolved.

## Failure protocol (when a checklist item fails)

1. **Record** the item `status: "failed"` with a `note` (what/why) and a `log_ref` to the error event.
2. **Log** an event with `status: "error"` and the raw error/response in `raw/`.
3. **Classify by severity:**
   - `high` → **BLOCK**: stop the phase, do not start dependent phases, report to the user with the blocker and a `next_action`.
   - `medium` / `low` → **CONTINUE**: proceed, but carry the gap forward — route missing brand facts to `open_questions`, missing data to `*.blockers`, and unmet providers to audit `not_applicable` + `top_fixes`.
4. **Never** fake a pass, invent data, or silently truncate. A skipped/blocked item must be visible in the checklist AND in the phase's output (summary/notes).
5. **Retry once** for transient tool errors (timeout, 5xx) — Firecrawl↔Playwright, PageSpeed↔local Lighthouse — before marking failed.

## End-of-run report

After Phase 5, tell the user: phases completed, overall audit score, and every `failed`/`blocked` item with its `next_action`.
