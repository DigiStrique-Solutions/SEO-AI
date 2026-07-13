# SEO content v2 evaluation corpus

`cases.json` is the versioned 40-case release corpus:

- 10 reference articles awaiting or carrying explicit human approval evidence
- 10 current weak generated drafts
- 10 source-rich ecommerce generation scenarios
- 10 deterministic failure and adversarial-source cases

Detector values are intentionally `null` until a person records the ZeroGPT result. A missing score never counts as a pass. Likewise, reference copy is not labelled human-approved unless approval evidence exists. Run `python3 evals/seo-content-v2/release_gate.py` for deterministic coverage and release status.

The release gate requires all 40 manual detector results, at least 32 scores below 20, 100 percent detector-failure routing, no fabricated-claim or process-leak regression, and completed human rubrics. Detector performance cannot override factual blockers.
