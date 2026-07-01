# Context Intelligence 01: Data Model And File Layout

## Goal

Define the durable objects and files that let Strique resolve context across all SEO checklists and downstream work products.

## Production Objects

### Context Field

A reusable fact or decision the system can resolve.

```json
{
  "field_id": "primary_business_goal",
  "label": "Primary business goal",
  "description": "The main business outcome Strique should optimize toward.",
  "scope": "brand",
  "data_type": "enum_multi_or_custom",
  "durability": "stable",
  "allowed_sources": ["brand_dna", "human_context", "ga4", "crm"],
  "safe_to_infer": false,
  "used_by": ["generic_on_page", "content_seo", "site_architecture", "ai_seo", "off_page"],
  "sensitive": false
}
```

### Context Answer

The resolved value for a field.

```json
{
  "field_id": "primary_business_goal",
  "value": ["increase qualified leads"],
  "source_type": "client_confirmed",
  "source_ref": "hitl:2026-07-01T09:30:00Z",
  "confidence": "high",
  "scope": "brand",
  "brand_id": "strique",
  "expires_at": null,
  "updated_at": "2026-07-01T09:30:00Z",
  "updated_by": "user"
}
```

### Question

A reusable HITL prompt tied to one or more context fields.

```json
{
  "question_id": "primary_business_goal",
  "field_ids": ["primary_business_goal"],
  "question": "What is the primary business goal Strique should optimize for?",
  "recommended_option": "Increase qualified leads",
  "options": [
    "Increase qualified leads",
    "Increase ecommerce sales",
    "Increase brand visibility"
  ],
  "allow_custom": true,
  "store_scope": "brand",
  "blocking_level": "blocks_prioritization"
}
```

### Checklist Context Requirement

The contract between a checklist item and the context resolver.

```json
{
  "checklist_id": "content_seo",
  "section_id": "page-purpose-and-audience",
  "item_id": "audience-is-explicit",
  "requires": ["target_audience", "buyer_stage"],
  "preferred_sources": ["brand_dna", "human_context", "gsc", "ga4"],
  "on_missing": "ask",
  "blocked_status": "not_checked_blocked"
}
```

### Run Context

Task-specific context that should not become durable Brand DNA unless promoted.

```json
{
  "run_id": "20260701T093000Z",
  "brand_id": "strique",
  "work_type": "content_audit",
  "target_urls": ["https://www.strique.io/product"],
  "answers": {},
  "assumptions": {},
  "evidence_refs": []
}
```

## Required File Layout

Production Strique should use database tables or equivalent persisted records. The local SEO module can mirror the shape with JSON and CSV files.

```text
registry/
  context-fields.json
  question-registry.json
  checklist-context-map.json
  assumption-rules.json
  source-priority.json

schemas/
  context-field.schema.json
  context-answer.schema.json
  question.schema.json
  checklist-context-map.schema.json
  audit-run-context.schema.json

prompts/
  context-resolver.md
  hitl-question-batcher.md
  answer-normalizer.md
  checklist-evaluator.md
  strategy-synthesizer.md
  reporting-synthesizer.md

brands/<brand>/
  brand-dna.md
  context/
    brand-dna.json
    answers.json
    assumptions.json
    open-questions.json
  prompt-sets/
    ai-visibility-prompts.csv
    serp-prompts.csv
  runs/<run-id>/
    run-context.json
    hitl-questions.json
    checklist-results.json
    report-context.json
```

## Field Scopes

- `global`: shared definitions and policies.
- `org`: org-level defaults, permissions, and connector availability.
- `brand`: durable brand facts.
- `property`: website, app, store, or location-specific facts.
- `run`: one audit, strategy, brief, media plan, analysis, or report.
- `page`: URL-level context.
- `campaign`: campaign-specific goals, budget, markets, and creative rules.

## Required Metadata

Every stored answer must have:

- `field_id`
- `value`
- `source_type`
- `source_ref`
- `confidence`
- `scope`
- `updated_at`
- `updated_by`

When inferred, also store:

- `reason`
- `evidence_refs`
- `can_user_override`

## Verification

- Validate registry files against schemas.
- Reject answers with no source and no confidence.
- Reject durable Brand DNA fields created from raw connector payloads without summarization.
- Reject cross-org references.
- Reject secret-looking values in Brand DNA and prompt artifacts.

