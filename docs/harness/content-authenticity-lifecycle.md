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
- approved YouTube video evidence

## 3. Gate Sensitive Claims

Claims such as `best`, `top`, `leading`, superiority, customer proof, performance claims, and comparisons need source evidence.

## 4. Verify Or Write

```bash
python3 tools/seo_audit_harness.py verify-authenticity --authenticity brands/inc5/references/example-authenticity.json --rewrite-file brands/inc5/blogs/drafts/example.md
```

For batches, verify every draft together before publishing:

```bash
python3 tools/seo_audit_harness.py verify-content-batch --authenticity brands/inc5/references/example-authenticity.json --draft-file brands/inc5/blogs/drafts/one.md --draft-file brands/inc5/blogs/drafts/two.md
```

Use `write-content` when the output file should be written only after the gate passes.

For blogs, use `write-blog` so the draft also passes the blog structure gate:

```bash
python3 tools/seo_audit_harness.py write-blog --brand-dir brands/inc5 --keyword "comfortable heels for women" --draft-file brands/inc5/blogs/drafts/comfortable-heels-for-women.md --content-output brands/inc5/blogs/published/comfortable-heels-for-women.md --authenticity brands/inc5/references/comfortable-heels-authenticity.json --brief-file brands/inc5/blogs/briefs/comfortable-heels-for-women.md
```

Add source evidence without editing JSON by hand:

```bash
python3 tools/seo_audit_harness.py record-authenticity-source --authenticity brands/inc5/references/example-authenticity.json --source-id brand-dna --source-type brand_dna --source-ref brands/inc5/brand-dna.md --extracted-facts "Brand positioning and product context used for the draft."
```

## YouTube Assisted Evidence

Use approved YouTube URLs as an intake source before drafting. The harness reuses the local `learnings-from-youtube` repo and records timestamp-backed evidence under `references/content-intake/`.

```bash
python3 tools/seo_audit_harness.py ingest-content-source --brand-dir brands/inc5 --source youtube --url "https://www.youtube.com/watch?v=VIDEO_ID" --run-id inc5-content-run
```

If captions are missing, the command stops with a blocker. Rerun with `--allow-whisper` only when local transcription is acceptable.

Build a brief from approved intake sources and update the authenticity log:

```bash
python3 tools/seo_audit_harness.py build-content-brief --brand-dir brands/inc5 --run-id inc5-content-run --keyword "comfortable heels for women" --target brands/inc5/blogs/drafts/comfortable-heels-for-women.md --authenticity brands/inc5/references/comfortable-heels-authenticity.json --output brands/inc5/blogs/briefs/comfortable-heels-for-women.md
```

The brief command writes `references/content-intake/<run-id>/brief-input.json` and appends usable `youtube_video` sources to the authenticity log. It does not write a blog draft.

## Batch AI Pattern Gate

`verify-content-batch` checks each draft with the single-draft authenticity gate, then adds batch checks for repeated H2 outlines, template similarity, unsupported sensitive product claims, and collection-only specificity. Use it for multi-blog runs because repeated headings and thin product evidence are often invisible when each draft is scored alone.

## AI Text Risk Gate

When `--rewrite-file` or `write-content` provides draft text, the harness computes a local `ai_text_risk` report. The score is an AI-pattern risk percentage, not proof of authorship. Verification fails when the score is `20` or higher.

The local gate checks generic phrases, formulaic transitions, repeated openings, uniform rhythm, abstract marketing language, weak specificity, and stock conclusion patterns. Fix failures by adding source-backed detail, cutting filler, and varying sentence rhythm naturally.

## Detector Notes

Record external AI detector output only as weak editorial signal in `detector_notes`. Do not treat it as plagiarism proof or authorship proof.
