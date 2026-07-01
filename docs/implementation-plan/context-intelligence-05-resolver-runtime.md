# Context Intelligence 05: Context Resolver Runtime

## Goal

Implement the runtime service that resolves fields before the SEO agent evaluates checklists or creates strategy, media plans, content briefs, analysis, or reports.

## Resolver Order

The resolver should check sources in this order:

1. Run context answers.
2. Brand DNA structured fields.
3. Prior accepted answers for the same brand.
4. Connected platform data.
5. Public crawl and rendered evidence.
6. Prompt captures or SERP captures.
7. Safe inference rules.
8. HITL question.
9. Blocked state.

## Resolver Contract

Input:

```json
{
  "brand_id": "strique",
  "work_type": "ai_seo_audit",
  "checklist_ids": ["ai_seo_aeo_geo", "content_seo"],
  "target_urls": ["https://www.strique.io/product"],
  "run_id": "20260701T093000Z"
}
```

Output:

```json
{
  "resolved": {
    "business_model": {
      "value": ["saas", "hybrid"],
      "source_type": "brand_dna",
      "confidence": "high"
    }
  },
  "questions": [],
  "blocked": [],
  "assumptions": []
}
```

## Safe Inference

Inference is allowed only when:

- The field definition marks `safe_to_infer: true`.
- The inference rule has explicit evidence requirements.
- The inference records reason, source refs, and confidence.
- The user can override it.

Example:

```json
{
  "field_id": "ymyl_exposure",
  "value": true,
  "source_type": "system_inferred",
  "confidence": "high",
  "reason": "Healthcare service keywords and GBP category detected.",
  "can_user_override": true
}
```

Fields that should usually not be inferred:

- Primary business goal.
- Risk posture.
- Approved claims.
- Restricted claims.
- Legal/compliance rules.
- Lead quality definition.
- Past link-building work.
- AI crawler policy.

## Connector Use

The resolver does not pass raw connector payloads into Brand DNA.

It extracts normalized facts:

- GSC: query/page performance, indexing, sitemaps, search appearance.
- GA4 or PostHog: traffic quality, conversions, events, funnels, lead quality.
- Shopify/GMC: product/feed facts, availability, pricing, issues.
- GBP: location details, categories, services, reviews, actions.
- BWT: Bing search and AI Performance where available.
- CRM/calls: lead quality and offline conversion context.

## Runtime Flow

```text
build_required_fields()
load_existing_context()
normalize_connector_facts()
apply_safe_inference()
build_question_batch()
wait_for_hitl_if_needed()
store_answers()
return_resolved_context_to_agent()
```

## Blocked State

If a field cannot be resolved and the user cannot answer during the run, return:

```json
{
  "field_id": "primary_local_conversion",
  "status": "not_checked_blocked",
  "blocker": "Primary local conversion is missing.",
  "next_action": "Ask the client which local conversion matters most.",
  "candidate_sources": ["human_context", "ga4", "crm_calls"]
}
```

## Agent Boundary

The SEO agent receives resolved context, question metadata, and evidence references. It does not receive raw credentials, cross-org context, or raw private system prompts.

## Verification

- Unit test source priority.
- Unit test blocked state creation.
- Unit test safe inference with source refs.
- Unit test that high-risk fields are not inferred.
- Unit test that durable answers are not stored from raw payloads.
- Integration test one checklist run with questions and one without questions.

