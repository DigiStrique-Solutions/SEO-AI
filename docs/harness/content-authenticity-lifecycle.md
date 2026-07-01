---
title: Content Authenticity Lifecycle
sidebar_position: 4
---

# Content Authenticity Lifecycle

Use this flow before publishing customer-facing SEO content.

## 1. Initialize The Source Log

```bash
python3 tools/seo_audit_harness.py init-authenticity --target brands/inc5/blogs/drafts/example.md --output brands/inc5/references/example-authenticity.json
```

## 2. Add Concrete Sources

Useful source types include:

- product pages
- brand DNA
- GSC
- GA4
- Shopify
- Merchant Center
- reviews
- customer notes
- merchandiser notes
- SERP observations
- competitor pages
- human context

## 3. Gate Sensitive Claims

Claims such as `best`, `top`, `leading`, superiority, customer proof, performance claims, and comparisons need source evidence.

## 4. Verify Or Write

```bash
python3 tools/seo_audit_harness.py verify-authenticity --authenticity brands/inc5/references/example-authenticity.json --rewrite-file brands/inc5/blogs/drafts/example.md
```

Use `write-content` when the output file should be written only after the gate passes.

## AI Text Risk Gate

When `--rewrite-file` or `write-content` provides draft text, the harness computes a local `ai_text_risk` report. The score is an AI-pattern risk percentage, not proof of authorship. Verification fails when the score is `20` or higher.

The local gate checks generic phrases, formulaic transitions, repeated openings, uniform rhythm, abstract marketing language, weak specificity, and stock conclusion patterns. Fix failures by adding source-backed detail, cutting filler, and varying sentence rhythm naturally.

## Detector Notes

Record external AI detector output only as weak editorial signal in `detector_notes`. Do not treat it as plagiarism proof or authorship proof.
