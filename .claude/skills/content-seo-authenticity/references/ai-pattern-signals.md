# Reference — AI-Pattern Signals & Fixes

Signal library for `checklists/ai-pattern-review.md`. Use to name the specific pattern, then fix by adding
source-backed specificity from the authenticity log — never by adding errors or awkward phrasing.

## Research basis (why detectors are weak signals)

- OpenAI retired its public text classifier for low accuracy and said classifiers shouldn't be the primary decision tool.
- Detector robustness research: paraphrasing lowers detection; watermark-like signatures cause false accusations.
- GPT detectors show bias against non-native English writing.
- Google Search guidance weighs accuracy, quality, relevance, helpfulness, metadata, alt text, and spam policy — not whether AI helped draft the page.

Conclusion: treat any score (`ZeroGPT`, `GPTZero`, `Originality`, `Copyleaks`) as a weak editorial signal. Working target `< 20`, not proof.

## Phrase / structure signals to flag

- **Empty openers:** "in today's digital landscape", "unlock your potential", "at its core", "game changer", "when it comes to".
- **Formulaic transitions:** repeated "Furthermore", "Moreover", "Additionally", "In conclusion".
- **Contrast reframes:** "not just X, but Y", "not about X, it is about Y", "no X, no Y, just Z".
- **Uniform rhythm:** sentences/paragraphs of near-identical length and shape.
- **Repeated openings:** consecutive units starting the same way.
- **Abstract benefit-stacking:** claims with no concrete noun, number, product name, customer language, or source-backed detail.
- **Stock summaries:** generic conclusion headings that don't help a decision.

## Fix pattern (when a draft fails)

1. Keep the facts and source-backed claims.
2. Cut filler and repeated transitions.
3. Add concrete source detail from the authenticity log — Brand DNA, GSC queries, PostHog behavior evidence, crawl evidence, customer notes, product facts.
4. Vary sentence and paragraph rhythm naturally.
5. Replace abstract claims with specific mechanisms, limits, examples, owners, or next actions.
6. Re-run `verify-authenticity` until source checks pass and `ai_text_risk.score` is `< 20`.

## Do not

- Do not add errors, awkward phrasing, fake anecdotes, unsupported opinions, or unverifiable detail to beat a detector.
- Do not write separate content "for AI" — preserve useful structure for both readers and AI search.
- Do not overstate certainty; label assumptions and `[needs source]` instead.
