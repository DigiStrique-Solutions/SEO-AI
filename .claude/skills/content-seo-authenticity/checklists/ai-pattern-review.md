# Checklist — AI-Pattern Review

Load this when the task is to review copy for **AI-pattern risk / humanization** (before or after the harness gate).
Signal library and fix moves are in `references/ai-pattern-signals.md` — read that alongside this checklist.

AI-detector scores are weak signals. This review is editorial: catch copy that reads like unreviewed AI output.
Flag each finding with a severity, then fix by adding specificity — not by adding errors.

**Scope.** This checklist covers *AI-pattern tells* only. Claims are gated in `authenticity-gate.md`; voice, spine, section differentiation, hook and payload are in `editorial-craft.md`. Run all three — none substitutes for another.

**This checklist is all prohibitions, and that is its limit.** Removing every tell below produces copy that is not *detectably* machine-written. It does not produce copy anyone wants to read — nothing here rewards a draft for being good. Clearing this list is necessary and nowhere near sufficient; `editorial-craft.md` is where the draft actually earns publication. Never fix an item here by subtracting until the prose has nothing left: stripping every connective to clear "repetitive transitions" leaves disconnected assertions, which reviewers read as flat and robotic — trading one tell for a worse one.

## P0 — blocks publish

- [ ] Recorded AI-pattern / detector score is **below 20**.

(Fabricated proof and unsupported superlatives are gated in `authenticity-gate.md` — not repeated here.)

## P1 — fix before shipping

- [ ] **No generic opening** — leads with the specific problem or page fact, not "in today's digital landscape".
- [ ] **No vague authority** — expertise is shown with concrete detail, not asserted.
- [ ] **No stock conclusion** — ending helps the reader decide, not a generic summary.
- [ ] **Varied rhythm** — sentence/paragraph length and shape genuinely vary. **Note both failure modes:** uniform mid-length cadence *and* uniform staccato. Chopping everything to eight words is not variety, and padding robotic prose with two long sentences is not either — the harness measures median dispersion precisely so neither reads as human.
- [ ] **No repetitive transitions** — not stacked "Furthermore / Moreover / Additionally / In conclusion". Replace them with connective prose; don't just delete them.
- [ ] **No repeated openings** — consecutive sentences/paragraphs don't start the same way.
- [ ] **No forced contrast reframes** — "not just X but Y", "not about X, it's about Y", "no X, no Y, just Z" used sparingly, if at all.
- [ ] **No keyword stuffing** — keywords read naturally.
- [ ] **Concrete nouns present** — product names, numbers, customer language, source-backed detail — not abstract benefit-stacking. **Specificity means knowing things, not counting digits:** the score reads *distinct* numbers and names, so studding prose with figures buys nothing. If a number isn't doing work for the reader, cut it.

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
