---
name: content-seo-authenticity
description: Use when auditing, rewriting, or producing SEO content that must be source-backed, brand-voice aligned, less likely to trigger detector concerns, and publish-ready. Trigger for content SEO, humanization, ZeroGPT or GPTZero concerns, AI plagiarism concerns, content authenticity, blog or landing page refreshes, and Strique content recommendations.
---

# Content SEO Authenticity

This is the Strique-local fork for content SEO work where the output must sound like a person wrote it, stay factual, and hold up in editorial review. It adapts the practical parts of these external skill patterns: AI-writing pattern audits, content humanization, SEO content writing, content quality auditing, content research writing, and optional detector gates such as CheckApp. Keep this as an instruction asset, not executable code.

## Non-Negotiables

- AI detector scores are weak editorial signals. They are not plagiarism proof, authorship proof, or a guarantee of publish readiness.
- Never promise a ZeroGPT, GPTZero, Originality, Copyleaks, or CheckApp result. If a score is recorded, treat less than 20 percent as the working target, not as proof the content is human.
- Do not bypass detectors by adding errors, awkward phrasing, filler, fake anecdotes, or unsupported opinions.
- Do not invent sources, proof, prices, results, rankings, customer language, reviews, expert quotes, or competitor claims.
- Publish-ready content needs concrete evidence in the authenticity log. If evidence is missing, mark the missing source or use `[needs source]`.

## Inputs To Gather

Use the smallest set that can prove the claims being made:

- Brand DNA, product marketing context, and customer language.
- Target URL crawl evidence from Firecrawl and Playwright.
- Site evidence manifest, URL inventory, and site checks from the audit harness.
- GSC queries and pages for real demand and current search language.
- Keyword universe and prioritized keyword tracker.
- PostHog behavior evidence when claiming engagement, funnels, conversion, or audience behavior.
- SERP or competitor pages when making comparison, format, or topical-gap claims.
- Human notes from sales, support, founders, merchandisers, buyers, or subject-matter experts.

## Workflow

1. Define the target page, target reader, primary keyword, secondary keywords, search intent, and desired action.
2. Create or update an authenticity log with `python3 tools/seo_audit_harness.py init-authenticity --target <target>`.
3. Add every source used to the log with `source_id`, `source_type`, `source_ref`, and extracted facts. Prefer `brand_dna`, `gsc`, `product_page`, `competitor_page`, `serp`, `customer_note`, `human_context`, and PostHog-backed notes when relevant.
4. Audit content SEO basics: intent match above the fold, title, meta description, H1, H2 structure, answer coverage, internal links, schema opportunity, cannibalization risk, freshness, and conversion path.
5. Gate claims before rewriting. Stats, rankings, "best", "top", "leading", superiority claims, customer proof, performance claims, and comparisons need source-backed claims in the authenticity log.
6. Rewrite or recommend edits using concrete observations from the sources. Preserve useful SEO structure while removing generic phrasing, repeated transitions, bloated summaries, keyword stuffing, and unsupported certainty.
7. Run a specificity and rhythm pass: vary sentence rhythm, replace abstract benefits with page-specific details, keep vocabulary natural for the brand, and read the piece aloud for mechanical cadence.
8. Run the local AI text risk gate through `verify-authenticity` or `write-content`; a score at or above 20 blocks publish-ready output.
9. Record external detector output only when a detector or review artifact is available. Put it in `detector_notes`; do not treat it as proof.
10. Save publishable content only through `python3 tools/seo_audit_harness.py write-content --draft-file <draft> --content-output <final> --authenticity <log> --max-ai-detector-score 20`. Use `verify-authenticity` for read-only checks when no file is being written.

## AI-Pattern Review

Flag issues with severity:

- P0: fabricated proof, fake citation, unsupported best/top claim, hallucinated product detail, or detector score at or above the agreed threshold.
- P1: generic opening, vague authority claim, stock conclusion, uniform paragraph rhythm, repetitive transition pattern, keyword stuffing, or claim that needs a source.
- P2: mild repetition, weak verb choice, over-polished phrasing, or scannability issue.

Common AI-pattern signals:

- Opens with broad setup instead of the specific problem or page fact.
- Uses smooth but empty phrases such as "in today's digital landscape" or "unlock your potential".
- Stacks benefits without showing what the product, page, customer, or data actually proves.
- Repeats the same paragraph shape or transition cadence.
- Adds generic summaries that do not help a reader make a decision.
- Uses "best" or "top" without criteria, tradeoffs, or evidence.

## Content SEO Checks

For each target page, return:

- Search intent: informational, commercial, navigational, transactional, or mixed.
- Primary keyword and closest matching current page.
- Title and meta recommendation when needed.
- H1 and H2 fixes when needed.
- Missing sections or answer gaps.
- Internal links to add, remove, or relabel.
- Structured data opportunity.
- Claims requiring source support.
- Rewrite recommendations or publish-ready copy only when evidence is sufficient.

## Output Shape

Use this format:

```text
Verdict: ship, fix, or block
Target URL:
Primary keyword:
Intent:
Evidence used:
Content SEO findings:
Authenticity risks:
Recommended edits:
Detector notes:
Next action:
```

Use `block` when the request asks for publish-ready content but concrete evidence is missing, required claims are unsupported, or a recorded AI detector score is at or above the agreed threshold.
