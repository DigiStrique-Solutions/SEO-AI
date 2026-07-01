# Context Intelligence 02: Brand DNA Expansion

## Goal

Expand Brand DNA from a branding document into the durable context store used by audits, strategy, media plans, blog briefs, analysis, and reporting.

## Brand DNA Layers

Brand DNA should have two representations:

1. Structured data for runtime resolution.
2. Markdown rendering for humans.

The structured record is the source of truth. `brand-dna.md` remains the readable view.

## Required Brand DNA Sections

### Brand Identity

- Brand name.
- Website URL.
- Canonical domain.
- Logo and favicon references.
- Entity type.
- Organization details.
- Social profiles.
- Founder or expert names where relevant.

### Business Model

- Site type: SaaS, ecommerce, local, marketplace, publisher, app, docs, lead gen, hybrid.
- Revenue model.
- Primary products or services.
- Priority product groups.
- Service areas or markets.
- Sales motion.
- Target countries and languages.

### Audience And ICP

- Primary audience.
- Secondary audiences.
- Roles.
- Industries.
- Buyer stages.
- Skill level.
- Customer objections.
- Support themes.
- Customer language.

### Goals And Conversions

- Primary business goal.
- Secondary goals.
- Primary conversion events.
- Micro conversions.
- Offline conversion definitions.
- Lead quality rules.
- Revenue or margin priority.
- Reporting cadence.

### SEO And AI Search Scope

- Priority topics.
- Priority queries.
- Priority pages.
- Priority page types.
- Target search surfaces.
- AI target platforms.
- Prompt sets.
- Competitors by query.
- Geographic and language scope.

### Content And Voice

- Tone of voice.
- Approved messaging.
- Forbidden messaging.
- Proof points.
- Case studies.
- Source requirements.
- Editorial rules.
- Human review requirements.

### Compliance, Risk, And Claims

- YMYL exposure.
- Regulated verticals.
- Legal review requirements.
- Approved claims.
- Restricted claims.
- Required disclaimers.
- Data privacy constraints.
- Platform policy constraints.

### Ecommerce Context

Use when relevant:

- Store platform.
- Catalog source of truth.
- Feed source of truth.
- Product identifiers.
- Priority product groups.
- Inventory and seasonality rules.
- Shipping and returns rules.
- Review policy.
- Merchant Center ownership.

### Local Context

Use when relevant:

- Location model.
- Service area.
- GBP ownership.
- NAP source of truth.
- Primary local conversion.
- Booking, calls, directions, and walk-in rules.
- License and credential requirements.
- Review response rules.

### Off-Page Context

- Risk posture.
- Past link work.
- PR policy.
- Partnership policy.
- Affiliate and sponsorship policy.
- Review generation policy.
- Approved directories or marketplaces.
- Reputation risks.

### Measurement And Connected Sources

- GSC property.
- GA4 property or PostHog project.
- BWT property.
- Shopify or ecommerce connector.
- GMC account.
- GBP accounts.
- CRM or call tracking source.
- Known unavailable sources.

### Open Questions

Open questions are first-class. Each should point to the field it blocks.

```json
{
  "field_id": "primary_local_conversion",
  "question_id": "primary_local_conversion",
  "blocks": ["local_seo.measurement", "local_seo.scope"],
  "created_at": "2026-07-01T09:30:00Z"
}
```

## Markdown Rendering

`brand-dna.md` should render durable fields in grouped sections and include:

- Confirmed facts.
- Inferred facts.
- Evidence sources.
- Open questions.
- Last reviewed date.

Do not paste raw connector payloads into the Markdown.

## Promotion Rules

Promote run answers into Brand DNA when:

- The answer describes durable brand reality.
- The answer is client-confirmed or connector-confirmed.
- The same answer is used by more than one workflow.

Keep answers in run context when:

- The answer applies only to one audit, one report, one campaign, or one piece of content.
- The answer is exploratory.
- The answer is a temporary priority.

## Verification

- Brand DNA includes source and confidence for every structured field.
- Open questions map to field IDs.
- Sensitive values are rejected.
- Durable answers are reusable across at least one checklist or workflow.
- Generated Markdown matches structured Brand DNA.

