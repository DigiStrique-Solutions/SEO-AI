# Checklist — AI-Pattern Review

Load this when the task is to review copy for **AI-pattern risk / humanization** (before or after the harness gate).
Signal library and fix moves are in `references/ai-pattern-signals.md` — read that alongside this checklist.

AI-detector scores are weak signals. This review is editorial: catch copy that reads like unreviewed AI output.
Flag each finding with a severity, then fix by adding specificity — not by adding errors.

## P0 — blocks publish (same weight as a failed authenticity gate)

- [ ] No fabricated proof, fake citation, or hallucinated product detail (→ also fails `authenticity-gate.md`).
- [ ] No unsupported "best" / "top" claim without criteria.
- [ ] Recorded AI-pattern / detector score is **below 20**.

## P1 — fix before shipping

- [ ] **No generic opening** — leads with the specific problem or page fact, not "in today's digital landscape".
- [ ] **No vague authority** — expertise is shown with concrete detail, not asserted.
- [ ] **No stock conclusion** — ending helps the reader decide, not a generic summary.
- [ ] **Varied rhythm** — sentence/paragraph length and shape vary; no uniform cadence.
- [ ] **No repetitive transitions** — not stacked "Furthermore / Moreover / Additionally / In conclusion".
- [ ] **No repeated openings** — consecutive sentences/paragraphs don't start the same way.
- [ ] **No forced contrast reframes** — "not just X but Y", "not about X, it's about Y", "no X, no Y, just Z" used sparingly, if at all.
- [ ] **No keyword stuffing** — keywords read naturally.
- [ ] **Concrete nouns present** — product names, numbers, customer language, source-backed detail — not abstract benefit-stacking.

## P2 — polish

- [ ] No mild repetition or weak verb choice.
- [ ] No over-polished / filler phrasing.
- [ ] Scannable structure preserved for SEO and AI search (but not written "for AI" separately).

## Output for this review

```text
Verdict: pass | fix
AI-pattern risk score:
Blocking signals:        # P0/P1 items that failed
Concrete fixes:          # specificity-based, from references/ai-pattern-signals.md
Harness command:         # the verify-authenticity / write-content line used
```
