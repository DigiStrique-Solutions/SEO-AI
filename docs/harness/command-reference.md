---
title: Command Reference
sidebar_position: 2
---

# Command Reference

These command sections are generated from the current CLI help. The harness file is the source of truth.

## compile-checklists

Purpose: Compile Markdown checklist items into stable JSON rows for audits.

```text
usage: seo_audit_harness.py compile-checklists [-h] [--checklist CHECKLIST]
                                               [--output OUTPUT]

optional arguments:
  -h, --help            show this help message and exit
  --checklist CHECKLIST
                        Checklist Markdown path
  --output OUTPUT       Output JSON path
```

## init-audit

Purpose: Create an audit matrix for a target URL from compiled checklists.

```text
usage: seo_audit_harness.py init-audit [-h] --compiled COMPILED --url URL
                                       [--audit-type {partial,full}]
                                       [--scope {page,site,google-visible}]
                                       [--evidence-run-id EVIDENCE_RUN_ID]
                                       [--brand-dir BRAND_DIR]
                                       [--strict-evidence] [--output OUTPUT]

optional arguments:
  -h, --help            show this help message and exit
  --compiled COMPILED   Compiled checklist JSON
  --url URL             Audited URL
  --audit-type {partial,full}
  --scope {page,site,google-visible}
  --evidence-run-id EVIDENCE_RUN_ID
  --brand-dir BRAND_DIR
  --strict-evidence
  --output OUTPUT       Output audit matrix JSON path
```

## verify-audit

Purpose: Validate audit matrix completeness, statuses, and evidence requirements.

```text
usage: seo_audit_harness.py verify-audit [-h] --compiled COMPILED --audit
                                         AUDIT [--strict-evidence]
                                         [--output OUTPUT]

optional arguments:
  -h, --help           show this help message and exit
  --compiled COMPILED
  --audit AUDIT
  --strict-evidence
  --output OUTPUT      Output verification JSON path
```

## summarize-audit

Purpose: Summarize audit coverage and unresolved findings after evidence is recorded.

```text
usage: seo_audit_harness.py summarize-audit [-h] --audit AUDIT
                                            [--output OUTPUT]

optional arguments:
  -h, --help       show this help message and exit
  --audit AUDIT
  --output OUTPUT  Output summary JSON path
```

## init-authenticity

Purpose: Create a source and claim log before publishing SEO content.

```text
usage: seo_audit_harness.py init-authenticity [-h] --target TARGET
                                              [--output OUTPUT]

optional arguments:
  -h, --help       show this help message and exit
  --target TARGET
  --output OUTPUT  Output authenticity JSON path
```

## verify-authenticity

Purpose: Check whether a rewrite has enough source evidence and claim support.

```text
usage: seo_audit_harness.py verify-authenticity [-h] --authenticity
                                                AUTHENTICITY
                                                [--rewrite-file REWRITE_FILE]
                                                [--max-ai-detector-score MAX_AI_DETECTOR_SCORE]
                                                [--output OUTPUT]

optional arguments:
  -h, --help            show this help message and exit
  --authenticity AUTHENTICITY
  --rewrite-file REWRITE_FILE
  --max-ai-detector-score MAX_AI_DETECTOR_SCORE
                        Maximum recorded detector or local AI-pattern risk
                        score allowed before verification fails.
  --output OUTPUT       Output verification JSON path
```

When `--rewrite-file` is present, output includes an `ai_text_risk` report with the local score and blocking signals.

## verify-content-batch

Purpose: Check a group of drafts for batch-level AI-pattern and specificity risk.

```text
usage: seo_audit_harness.py verify-content-batch [-h]
                                                 --authenticity AUTHENTICITY
                                                 --draft-file DRAFT_FILE
                                                 [--max-ai-detector-score MAX_AI_DETECTOR_SCORE]
                                                 [--max-template-similarity-score MAX_TEMPLATE_SIMILARITY_SCORE]
                                                 [--min-brand-specificity-score MIN_BRAND_SPECIFICITY_SCORE]
                                                 [--output OUTPUT]

options:
  -h, --help            show this help message and exit
  --authenticity AUTHENTICITY
  --draft-file DRAFT_FILE
                        Draft Markdown file to verify. Repeat for multiple
                        files.
  --max-ai-detector-score MAX_AI_DETECTOR_SCORE
                        Maximum recorded detector or local AI-pattern risk
                        score allowed before verification fails.
  --max-template-similarity-score MAX_TEMPLATE_SIMILARITY_SCORE
                        Maximum batch outline similarity score allowed before
                        verification fails.
  --min-brand-specificity-score MIN_BRAND_SPECIFICITY_SCORE
                        Minimum product or brand specificity score required
                        for each draft.
  --output OUTPUT       Output batch verification JSON path
```

## write-content

Purpose: Write publishable content only when the authenticity gate passes.

```text
usage: seo_audit_harness.py write-content [-h] --draft-file DRAFT_FILE
                                          --content-output CONTENT_OUTPUT
                                          --authenticity AUTHENTICITY
                                          [--max-ai-detector-score MAX_AI_DETECTOR_SCORE]
                                          [--output OUTPUT]

optional arguments:
  -h, --help            show this help message and exit
  --draft-file DRAFT_FILE
  --content-output CONTENT_OUTPUT
  --authenticity AUTHENTICITY
  --max-ai-detector-score MAX_AI_DETECTOR_SCORE
                        Maximum recorded detector or local AI-pattern risk
                        score allowed before writing content.
  --output OUTPUT       Output write report JSON path
```

## record-authenticity-source

Purpose: Add a concrete source and optional claim to an authenticity log.

```text
usage: seo_audit_harness.py record-authenticity-source [-h] --authenticity
                                                       AUTHENTICITY --source-id
                                                       SOURCE_ID --source-type
                                                       SOURCE_TYPE --source-ref
                                                       SOURCE_REF
                                                       --extracted-facts
                                                       EXTRACTED_FACTS
                                                       [--claim CLAIM]
                                                       [--claim-type CLAIM_TYPE]
                                                       [--source-id-for-claim SOURCE_ID_FOR_CLAIM]
                                                       [--output OUTPUT]

optional arguments:
  -h, --help            show this help message and exit
  --authenticity AUTHENTICITY
  --source-id SOURCE_ID
  --source-type SOURCE_TYPE
  --source-ref SOURCE_REF
  --extracted-facts EXTRACTED_FACTS
  --claim CLAIM
  --claim-type CLAIM_TYPE
  --source-id-for-claim SOURCE_ID_FOR_CLAIM
  --output OUTPUT       Output recording JSON path
```

## write-blog

Purpose: Write a blog only after blog structure and authenticity gates pass.

```text
usage: seo_audit_harness.py write-blog [-h] --brand-dir BRAND_DIR --keyword
                                       KEYWORD --draft-file DRAFT_FILE
                                       --content-output CONTENT_OUTPUT
                                       --authenticity AUTHENTICITY
                                       [--run-id RUN_ID]
                                       [--brief-file BRIEF_FILE]
                                       [--max-ai-detector-score MAX_AI_DETECTOR_SCORE]
                                       [--output OUTPUT]

optional arguments:
  -h, --help            show this help message and exit
  --brand-dir BRAND_DIR
  --keyword KEYWORD
  --draft-file DRAFT_FILE
  --content-output CONTENT_OUTPUT
  --authenticity AUTHENTICITY
  --run-id RUN_ID
  --brief-file BRIEF_FILE
  --max-ai-detector-score MAX_AI_DETECTOR_SCORE
                        Maximum recorded detector or local AI-pattern risk
                        score allowed before writing content.
  --output OUTPUT       Output blog write report JSON path
```

## ingest-content-source

Purpose: Convert an approved content source into source-backed evidence for content briefs.

```text
usage: seo_audit_harness.py ingest-content-source [-h] --brand-dir BRAND_DIR
                                                  --source {youtube} --url URL
                                                  --run-id RUN_ID
                                                  [--learnings-root LEARNINGS_ROOT]
                                                  [--allow-whisper]
                                                  [--output OUTPUT]

optional arguments:
  -h, --help            show this help message and exit
  --brand-dir BRAND_DIR
  --source {youtube}
  --url URL
  --run-id RUN_ID
  --learnings-root LEARNINGS_ROOT
                        Path to the learnings-from-youtube repo.
  --allow-whisper
  --output OUTPUT       Output ingestion JSON path
```

## build-content-brief

Purpose: Build a content brief from approved intake sources and update the authenticity log.

```text
usage: seo_audit_harness.py build-content-brief [-h] --brand-dir BRAND_DIR
                                                --run-id RUN_ID --keyword KEYWORD
                                                --target TARGET --authenticity
                                                AUTHENTICITY --output OUTPUT
                                                [--report-output REPORT_OUTPUT]

optional arguments:
  -h, --help            show this help message and exit
  --brand-dir BRAND_DIR
  --run-id RUN_ID
  --keyword KEYWORD
  --target TARGET
  --authenticity AUTHENTICITY
  --output OUTPUT       Output brief Markdown path
  --report-output REPORT_OUTPUT
                        Output command report JSON path
```

## firecrawl-scrape

Purpose: Collect public page evidence through Firecrawl when configured.

```text
usage: seo_audit_harness.py firecrawl-scrape [-h] --url URL [--format FORMAT]
                                             [--full-content]
                                             [--wait-for WAIT_FOR] [--mobile]
                                             [--timeout TIMEOUT]
                                             [--output OUTPUT]

optional arguments:
  -h, --help           show this help message and exit
  --url URL
  --format FORMAT      Firecrawl output format. Repeat for multiple formats.
  --full-content
  --wait-for WAIT_FOR
  --mobile
  --timeout TIMEOUT
  --output OUTPUT      Output scrape JSON path
```

## generate-keywords

Purpose: Build or update keyword tracker rows from available demand evidence.

```text
usage: seo_audit_harness.py generate-keywords [-h] --brand-dir BRAND_DIR
                                              --google-ads-customer-id
                                              GOOGLE_ADS_CUSTOMER_ID
                                              [--country COUNTRY]
                                              [--language LANGUAGE]
                                              [--max-prioritized MAX_PRIORITIZED]
                                              [--raw-limit RAW_LIMIT]
                                              [--output OUTPUT]

optional arguments:
  -h, --help            show this help message and exit
  --brand-dir BRAND_DIR
  --google-ads-customer-id GOOGLE_ADS_CUSTOMER_ID
  --country COUNTRY     Target country override. If omitted, GSC and Brand DNA
                        are used.
  --language LANGUAGE   Google Ads language constant.
  --max-prioritized MAX_PRIORITIZED
  --raw-limit RAW_LIMIT
  --output OUTPUT       Output generation JSON path
```

## verify-keywords

Purpose: Validate keyword tracker and keyword universe quality.

```text
usage: seo_audit_harness.py verify-keywords [-h] --brand-dir BRAND_DIR
                                            [--min-prioritized MIN_PRIORITIZED]
                                            [--max-prioritized MAX_PRIORITIZED]
                                            [--min-universe MIN_UNIVERSE]
                                            [--allow-large] [--output OUTPUT]

optional arguments:
  -h, --help            show this help message and exit
  --brand-dir BRAND_DIR
  --min-prioritized MIN_PRIORITIZED
  --max-prioritized MAX_PRIORITIZED
  --min-universe MIN_UNIVERSE
  --allow-large
  --output OUTPUT       Output verification JSON path
```

## collect-evidence

Purpose: Collect page-level evidence for a brand URL.

```text
usage: seo_audit_harness.py collect-evidence [-h] --brand-dir BRAND_DIR --url
                                             URL
                                             [--google-ads-customer-id GOOGLE_ADS_CUSTOMER_ID]
                                             [--run-id RUN_ID]
                                             [--output OUTPUT]

optional arguments:
  -h, --help            show this help message and exit
  --brand-dir BRAND_DIR
  --url URL
  --google-ads-customer-id GOOGLE_ADS_CUSTOMER_ID
  --run-id RUN_ID
  --output OUTPUT       Output collection JSON path
```

## crawl-site

Purpose: Crawl public site URLs into a brand workspace.

```text
usage: seo_audit_harness.py crawl-site [-h] --brand-dir BRAND_DIR --url URL
                                       [--run-id RUN_ID]
                                       [--max-pages MAX_PAGES]
                                       [--output OUTPUT]

optional arguments:
  -h, --help            show this help message and exit
  --brand-dir BRAND_DIR
  --url URL
  --run-id RUN_ID
  --max-pages MAX_PAGES
  --output OUTPUT       Output crawl JSON path
```

## collect-site-evidence

Purpose: Collect evidence across site inventory rows.

```text
usage: seo_audit_harness.py collect-site-evidence [-h] --brand-dir BRAND_DIR
                                                  --url URL
                                                  [--google-ads-customer-id GOOGLE_ADS_CUSTOMER_ID]
                                                  [--run-id RUN_ID]
                                                  [--max-pages MAX_PAGES]
                                                  [--output OUTPUT]

optional arguments:
  -h, --help            show this help message and exit
  --brand-dir BRAND_DIR
  --url URL
  --google-ads-customer-id GOOGLE_ADS_CUSTOMER_ID
  --run-id RUN_ID
  --max-pages MAX_PAGES
  --output OUTPUT       Output collection JSON path
```

## run-site-checks

Purpose: Create site-level checks from crawl and evidence artifacts.

```text
usage: seo_audit_harness.py run-site-checks [-h] --brand-dir BRAND_DIR
                                            --run-id RUN_ID [--output OUTPUT]

optional arguments:
  -h, --help            show this help message and exit
  --brand-dir BRAND_DIR
  --run-id RUN_ID
  --output OUTPUT       Output site checks JSON path
```

## resolve-google-visible-audit

Purpose: Resolve audit rows that can be checked through Google-visible evidence.

```text
usage: seo_audit_harness.py resolve-google-visible-audit [-h] --brand-dir
                                                         BRAND_DIR --run-id
                                                         RUN_ID --audit AUDIT
                                                         [--output-audit OUTPUT_AUDIT]
                                                         [--output OUTPUT]

optional arguments:
  -h, --help            show this help message and exit
  --brand-dir BRAND_DIR
  --run-id RUN_ID
  --audit AUDIT
  --output-audit OUTPUT_AUDIT
  --output OUTPUT       Output resolver JSON path
```

## resolve-google-visible-audits

Purpose: Resolve Google-visible rows across multiple audit files.

```text
usage: seo_audit_harness.py resolve-google-visible-audits [-h] --brand-dir
                                                          BRAND_DIR --run-id
                                                          RUN_ID
                                                          [--audit AUDIT]
                                                          [--output OUTPUT]

optional arguments:
  -h, --help            show this help message and exit
  --brand-dir BRAND_DIR
  --run-id RUN_ID
  --audit AUDIT
  --output OUTPUT       Output resolver JSON path
```

## route-evidence

Purpose: Map checklist items to required logical and concrete evidence sources.

```text
usage: seo_audit_harness.py route-evidence [-h] --brand-dir BRAND_DIR --audit
                                           AUDIT [--output-audit OUTPUT_AUDIT]
                                           [--output OUTPUT]

optional arguments:
  -h, --help            show this help message and exit
  --brand-dir BRAND_DIR
  --audit AUDIT
  --output-audit OUTPUT_AUDIT
  --output OUTPUT       Output routing JSON path
```

## record-source-evidence

Purpose: Record a source-level evidence note against an audit item.

```text
usage: seo_audit_harness.py record-source-evidence [-h] --brand-dir BRAND_DIR
                                                   --run-id RUN_ID --source
                                                   SOURCE --input INPUT
                                                   --summary SUMMARY
                                                   [--output OUTPUT]

optional arguments:
  -h, --help            show this help message and exit
  --brand-dir BRAND_DIR
  --run-id RUN_ID
  --source SOURCE
  --input INPUT
  --summary SUMMARY
  --output OUTPUT       Output recording JSON path
```

## record-evidence

Purpose: Record status, result, artifact, and next action for an audit item.

```text
usage: seo_audit_harness.py record-evidence [-h] --audit AUDIT --item-id
                                            ITEM_ID --status
                                            {fail,not_applicable,not_checked_blocked,pass}
                                            --evidence-source EVIDENCE_SOURCE
                                            --artifact-ref ARTIFACT_REF
                                            --result RESULT
                                            [--next-action NEXT_ACTION]
                                            [--blocker BLOCKER]
                                            [--evidence-run-id EVIDENCE_RUN_ID]
                                            [--output-audit OUTPUT_AUDIT]
                                            [--output OUTPUT]

optional arguments:
  -h, --help            show this help message and exit
  --audit AUDIT
  --item-id ITEM_ID
  --status {fail,not_applicable,not_checked_blocked,pass}
  --evidence-source EVIDENCE_SOURCE
  --artifact-ref ARTIFACT_REF
  --result RESULT
  --next-action NEXT_ACTION
  --blocker BLOCKER
  --evidence-run-id EVIDENCE_RUN_ID
  --output-audit OUTPUT_AUDIT
  --output OUTPUT       Output recording JSON path
```

## generate-context-map

Purpose: Generate `registry/checklist-context-map.json` from checklist Markdown and the context registries.

```text
usage: seo_audit_harness.py generate-context-map [-h]
                                                 [--registry-dir REGISTRY_DIR]
                                                 [--checklist CHECKLIST]
                                                 [--output OUTPUT]
```

## validate-context-system

Purpose: Validate context fields, questions, and checklist context map coverage.

```text
usage: seo_audit_harness.py validate-context-system [-h]
                                                   [--registry-dir REGISTRY_DIR]
                                                   [--checklist CHECKLIST]
                                                   [--output OUTPUT]
```

## init-brand-context

Purpose: Initialize `context/brand-dna.json`, `context/answers.json`, and `context/open-questions.json` from a brand workspace.

```text
usage: seo_audit_harness.py init-brand-context [-h] --brand-dir BRAND_DIR
                                               [--output OUTPUT]
```

## resolve-context

Purpose: Resolve checklist context for a brand, create HITL questions, and optionally write run artifacts.

```text
usage: seo_audit_harness.py resolve-context [-h] --brand-dir BRAND_DIR
                                            [--registry-dir REGISTRY_DIR]
                                            [--checklist-id CHECKLIST_ID]
                                            [--run-id RUN_ID]
                                            [--work-type WORK_TYPE]
                                            [--target-url TARGET_URL]
                                            [--write-run]
                                            [--output OUTPUT]
```

## record-context-answer

Purpose: Record a client-confirmed answer into Brand DNA or a run context.

```text
usage: seo_audit_harness.py record-context-answer [-h] --brand-dir BRAND_DIR
                                                  --field-id FIELD_ID
                                                  --value VALUE
                                                  [--question-id QUESTION_ID]
                                                  [--run-id RUN_ID]
                                                  [--scope {brand,run}]
                                                  [--confidence CONFIDENCE]
                                                  [--output OUTPUT]
```
