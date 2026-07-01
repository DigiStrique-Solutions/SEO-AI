# Context Intelligence 03: Question Registry

## Goal

Create a reusable question registry so Strique asks consistent questions, stores answers correctly, and avoids repeating client intake across workflows.

## Question Shape

Every question should have:

- Stable `question_id`.
- One or more `field_ids`.
- User-facing question.
- Recommended option.
- Two alternate options.
- Custom answer allowed.
- Store scope.
- Blocking level.
- Used-by workflows.
- Answer normalization rules.

Example:

```json
{
  "question_id": "site_type",
  "field_ids": ["site_type", "business_model"],
  "question": "Which best describes this website?",
  "recommended_option": "Lead generation or service website",
  "options": [
    "Lead generation or service website",
    "Ecommerce store",
    "SaaS, app, or documentation site"
  ],
  "allow_custom": true,
  "store_scope": "brand",
  "blocking_level": "blocks_scope",
  "used_by": ["generic_on_page", "content_seo", "site_architecture", "ai_seo", "local_seo", "ecommerce_seo", "off_page_seo"]
}
```

## Required Question Groups

### Brand And Business

- Website type.
- Business model.
- Revenue model.
- Products and services.
- Primary business goal.
- Secondary business goals.
- Target countries.
- Target languages.

### Audience And Positioning

- Primary audience.
- Buyer stage.
- ICP.
- Customer objections.
- Approved positioning.
- Differentiators.
- Competitors.

### SEO Scope

- Audit scope.
- Priority URLs.
- Priority page types.
- Priority queries.
- Target topics.
- Search intent.
- Existing problem or pain.

### Conversion And Measurement

- Primary conversion.
- Secondary conversion.
- Lead quality signal.
- Revenue or margin priority.
- Reporting cadence.
- Attribution source.
- Offline conversion source.

### Content

- Page purpose.
- Content type.
- Brand voice.
- Source requirements.
- Expert review requirement.
- Freshness requirement.
- Approved claims.
- Restricted claims.

### Ecommerce

- Store platform.
- Catalog source of truth.
- Feed source of truth.
- Priority product groups.
- Inventory or seasonality constraints.
- Shipping and returns policy.
- Reviews policy.
- Merchant Center ownership.

### Local

- Location model.
- Service area.
- Primary local conversion.
- GBP owner.
- NAP source of truth.
- Eligibility and policy risks.
- Vertical-specific restrictions.

### Off-Page

- Off-page goal.
- Risk posture.
- Past SEO or link work.
- PR policy.
- Partnership policy.
- Review policy.
- Reputation concerns.

### AI Search

- Target AI platforms.
- Prompt set.
- AI visibility goal.
- Crawler policy.
- Competitor citations.
- Monitoring cadence.

## Question Selection Rules

Ask a question only when:

- A selected checklist item requires the field.
- The resolver cannot find a high-confidence answer.
- The field cannot be safely inferred.
- The missing field affects prioritization, compliance, scope, or output quality.

Batching rules:

- Ask highest-impact blockers first.
- Group questions by concept.
- Do not ask the same durable question twice for the same brand.
- Show why the question matters when the user opens details, not in the main prompt.

## Runtime-Generated Questions

Agents may generate a runtime question when:

- No registered question covers the missing field.
- The field blocks the current work.
- The generated question is saved with checklist, section, item, and reason.

Promotion rule:

```text
If a runtime question is reused across three brands or three checklist runs, promote it into the registry.
```

## Answer Normalization

User answers should normalize into structured values.

Example:

```text
User answer: "Mostly Shopify, but some landing pages are custom Next.js."
```

Normalized:

```json
{
  "ecommerce_platform": ["shopify"],
  "platform_constraints": ["custom next.js landing pages"],
  "business_model": ["ecommerce", "hybrid"]
}
```

## Verification

- Every question maps to at least one field.
- Every question has a recommended option and custom path.
- Every option is mutually understandable to a non-SEO user.
- Every answer can be stored as durable or run-scoped data.
- Runtime questions are reviewed for promotion.

