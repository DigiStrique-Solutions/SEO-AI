# Core Web Vitals & Performance — Audit Definition

**ID:** `core-web-vitals` · **Scope:** per URL · **Pairs with:** [core-web-vitals.json](core-web-vitals.json)

## What it checks
Google's page-experience signals plus the performance basics behind them.

| Section | Items | Threshold |
|---------|-------|-----------|
| Loading | LCP · TTFB | LCP ≤ 2.5s · TTFB ≤ 0.8s |
| Interactivity | INP · render-blocking resources | INP ≤ 200ms |
| Stability & Assets | CLS · image optimization | CLS ≤ 0.1 |

## Why it matters
Core Web Vitals are a confirmed ranking signal and a direct conversion lever. Field data (real users, 75th percentile) is what Google scores — lab data only explains *why*.

## Scoring
Weighted pass ratio. Severity weights: **high = 3, medium = 2, low = 1**. LCP/INP/CLS are the high-severity three.

## Output
- `audits/core-web-vitals.json` — findings rows with measured values.
- Rolled into `audits/summary.json`.

## Needs
Performance data providers (field: CrUX/PSI; lab: Lighthouse). Rows are `blocked` until a performance provider is connected.
