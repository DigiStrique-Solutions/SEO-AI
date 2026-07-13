# SEO content pipeline v2

## Runtime split

`strique-ai-server` owns production state, stage transitions, evidence gates, exact Markdown export, publication registration, and ranking schedules. This repository owns offline fixtures, schema compatibility, deterministic evaluation, Promptfoo plans, and legacy CLI compatibility.

Production blog runs do not load writing, SEO, humanization, or detector skills. They use one bounded `ContentPacketV2`, one accepted outline, one Markdown draft, and one separate claim map. The local skills remain documentation and manual aids only.

## New CLI behavior

`write-blog` uses schema version 2 by default. Supply `--content-packet`, `--outline`, and `--claim-map`. It runs both single-draft gates and similarity checks against `--batch-file` values or the five most recently modified articles in the same brand workspace.

Use `--legacy-compatibility` to retain the original skill-backed article anatomy and authenticity log behavior. Legacy outputs retain their historical `ai_text_risk` key. Version-two outputs use `style_pattern_risk`, which is an editorial heuristic and not an authorship probability.

## Release evaluation

The 40 cases live in `evals/seo-content-v2/cases.json`. Missing human reviews or ZeroGPT results fail closed. The current 23-draft local baseline is in `baseline-current-23.json`; its ZeroGPT values remain pending because no approved stable API is available.

Run:

```bash
python3 -m unittest tests.test_seo_audit_harness
pytest tests/test_seo_content_pipeline_v2.py
python3 evals/seo-content-v2/release_gate.py
```

The final command is expected to fail until all 40 manual scores and human rubrics are complete. Enabling production export before it passes is not an accepted rollout state.

## Production rollout

The production flag is `SEO_CONTENT_PIPELINE_ENABLED`. Repository and Kubernetes defaults are `false`. The intended sequence is internal development shadow generation, 40-case comparison, export enablement after acceptance, then ranking monitoring after the first verified human-published URL. CMS publication remains manual.

The production migration is `scripts/sql/seo_content_pipeline_v2.sql` in `strique-ai-server`. It must be applied manually because startup `create_all` cannot alter an existing database.
