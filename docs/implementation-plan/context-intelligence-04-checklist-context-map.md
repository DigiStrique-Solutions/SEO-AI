# Context Intelligence 04: Checklist Context Map

## Goal

Map each checklist item to the context fields and evidence sources needed to evaluate it.

This is the center of the system. The resolver, HITL intake, Brand DNA storage, and reporting all depend on this map.

## Map Shape

```json
{
  "checklist_id": "local_seo",
  "section_id": "scope-and-business-model",
  "item_id": "primary-local-conversion-known",
  "item_text": "The primary local conversion is known: calls, directions, bookings, walk-ins, form leads, quotes, appointments, orders, reservations, purchases, app installs, or support visits.",
  "requires": ["primary_local_conversion"],
  "evidence_sources": ["human_context", "ga4", "gbp_performance", "crm_calls"],
  "preferred_source_order": ["brand_dna", "human_context", "ga4", "gbp_performance", "crm_calls"],
  "can_infer": false,
  "on_missing": "ask",
  "blocked_status": "not_checked_blocked",
  "used_for": ["audit", "strategy", "reporting"]
}
```

## Required Checklist Coverage

The map must cover all source checklists:

- Generic On-Page SEO.
- Content SEO.
- Ecommerce SEO.
- Local SEO.
- Site Architecture SEO.
- AI SEO, AEO, and GEO.
- Off-Page SEO.

## Context Categories By Checklist

### Generic On-Page SEO

Required durable fields:

- Page type.
- Primary search intent.
- Business goal.
- Target audience.
- Site type.
- Priority pages.
- YMYL exposure.
- Target locale.
- Conversion path.

Required evidence:

- Firecrawl.
- Playwright.
- GSC.
- GA4 or PostHog.
- Lighthouse, PageSpeed, CrUX.
- CMS/code when available.
- Human context where copy, compliance, or business role matters.

### Content SEO

Required durable fields:

- Page purpose.
- Audience and buyer stage.
- Primary query theme.
- Brand voice.
- Source requirements.
- Approved and restricted claims.
- Expert review requirement.
- Conversion path.

Required evidence:

- Crawl/rendered page.
- GSC queries.
- GA4 or PostHog engagement/conversions.
- Manual SERP.
- Human context.

### Ecommerce SEO

Required durable fields:

- Store type.
- Platform.
- Revenue goal.
- Priority product groups.
- Catalog source of truth.
- Feed source of truth.
- Product data owners.
- Shipping, returns, reviews, pricing, availability rules.

Required evidence:

- Shopify or ecommerce platform.
- GMC.
- GSC.
- GA4 or PostHog.
- Firecrawl.
- Playwright.
- CMS/code.

### Local SEO

Required durable fields:

- Location model.
- Business model.
- Primary local conversion.
- Target geography.
- Service area.
- GBP ownership.
- NAP source of truth.
- Review policy.
- Vertical restrictions.

Required evidence:

- GBP.
- Google Maps.
- GSC.
- GA4 or PostHog.
- CRM/call tracking.
- Manual local SERP.
- Firecrawl.
- Playwright.

### Site Architecture SEO

Required durable fields:

- Audit scope.
- Site type.
- Primary business goals.
- Primary audiences and user tasks.
- Current pain.
- CMS and engineering constraints.
- Priority page model.

Required evidence:

- Crawl inventory.
- Sitemap.
- GSC pages.
- GA4 or PostHog landing pages.
- CMS/code routes.
- Firecrawl.
- Playwright.

### AI SEO, AEO, And GEO

Required durable fields:

- Target AI platforms.
- AI business goal.
- Priority prompt set.
- Query groups.
- Competitors cited.
- Site type.
- YMYL exposure.
- AI crawler policy.
- Monitoring cadence.

Required evidence:

- Prompt captures.
- Manual AI SERP.
- GSC.
- BWT.
- GA4 or PostHog.
- Firecrawl.
- Playwright.
- Logs/CDN/WAF where available.

### Off-Page SEO

Required durable fields:

- Off-page scope.
- Business type.
- Risk posture.
- YMYL exposure.
- Past SEO or link work.
- PR, partnership, affiliate, review policies.
- Reputation concerns.

Required evidence:

- GSC links/manual actions/security issues.
- GA4 or PostHog referral quality.
- GBP and Maps when local.
- Manual/free SERP.
- Firecrawl.
- Alerts/free monitoring.
- CRM/sales context.

## Output Status Rules

The context map controls status behavior:

- `pass`: evidence proves the item is satisfied.
- `fail`: evidence proves the item is not satisfied.
- `not_applicable`: the field or source proves the item does not apply.
- `not_checked_blocked`: required evidence or context is missing.

No checklist item can be marked pass because the agent feels confident. It needs evidence or a recorded confirmed context answer.

## Verification

- Every checklist item has a map entry.
- Every map entry has at least one evidence source.
- Human-only items have a registered question or a clear blocked state.
- Inferred fields specify allowed inference rules.
- Coverage reports include counts by checklist, source, status, and blocker.

