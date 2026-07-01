---
name: ai-text-risk-gate
description: Use when checking Strique blog drafts, SEO content, landing page copy, or publish-ready customer-facing copy for AI-pattern risk, detector-score concerns, ZeroGPT/GPTZero/Originality style review, humanization, or the local harness requirement that AI-pattern risk stays under 20 percent before publishing.
---

# AI Text Risk Gate

## Purpose

Use this skill as an editorial risk gate. It is not proof of authorship. The goal is to catch copy that reads like unreviewed AI output before it ships.

## Research Basis

- OpenAI retired its public text classifier because of low accuracy and said classifiers should not be the primary decision-making tool.
- Research on detector robustness shows paraphrasing can reduce detection rates and watermark-like signatures can create false accusations.
- Research on GPT detectors found bias against non-native English writing.
- Google Search guidance focuses on accuracy, quality, relevance, helpfulness, metadata, alt text, and spam policy compliance rather than whether AI helped draft the page.

## Gate Rules

1. Run the repo harness with the draft file:

```bash
python3 tools/seo_audit_harness.py verify-authenticity \
  --authenticity <authenticity.json> \
  --rewrite-file <draft.md> \
  --max-ai-detector-score 20
```

2. Use `write-content` only when the final file should be written after all authenticity checks pass.
3. Treat the returned `ai_text_risk.score` as a local AI-pattern risk percentage.
4. Block publish-ready output when the score is `20` or higher.
5. If an external detector result is available, record it in `detector_notes`, but do not treat it as proof.
6. Never lower the score by adding errors, awkward phrasing, fake anecdotes, unsupported opinions, or unverifiable details.

## Review Signals

Look for:

- Generic phrases such as "in today's digital landscape", "unlock your potential", "at its core", and "game changer".
- Formulaic transitions such as repeated "Furthermore", "Moreover", "Additionally", or "In conclusion".
- Repeated contrastive reframes such as "not just X, but Y", "not about X, it is about Y", or "no X, no Y, just Z".
- Uniform sentence and paragraph rhythm.
- Repeated sentence or paragraph openings.
- Abstract marketing language without concrete nouns, evidence, numbers, product names, customer language, or source-backed detail.
- Generic conclusion headings or stock summaries.

## Fix Pattern

When a draft fails:

1. Keep the facts and source-backed claims.
2. Cut filler and repeated transitions.
3. Add concrete source detail from the authenticity log, especially Brand DNA, GSC queries, PostHog behavior evidence, crawl evidence, customer notes, and product facts.
4. Vary sentence and paragraph rhythm naturally.
5. Replace abstract claims with specific mechanisms, limits, examples, owners, or next actions.
6. Re-run the harness until source checks pass and `ai_text_risk.score` is below `20`.

## Output

Report:

```text
Verdict: pass or fix
AI-pattern risk score:
Blocking signals:
Concrete fixes:
Harness command:
```
