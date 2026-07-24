# Reference — Brand Voice Contract

How to turn a brand's files into a **voice contract**: a short, concrete spec you write *before* drafting and review against *after*.

Every brand carries rich voice data in `brand-dna.json` (`brand_voice`, `voice_patterns`, `brand_aesthetic`, `target_audience`) plus rules in `knowledge.md`. Historically none of it reached the page — `brand_dna` was wired in only as a *fact provider* for the authenticity log, never as a style guide. So every brand's copy converged on the same neutral register. The contract is the fix: it makes voice an explicit input to writing, not an afterthought at review.

## Build it (10 minutes, before drafting)

**1. Read the sources** — in `context.md` order: `knowledge.md` (rules win) → `brand-dna.json` (voice fields) → `blogs/references/*.md` + their `voice_notes` (how the brand actually sounds when it writes).

**2. Write the contract** — keep it in the working notes and in the `Voice contract:` output line:

```text
Register:        # from brand_voice.description, in your own words
Patterns to use: # from voice_patterns — the specific framings and community language
Proof points:    # what this brand argues with (heritage, tech names, price, sizing)
Vocabulary:      # words this brand uses / real product + tech names, spelled correctly
Prohibitions:    # from knowledge.md — what this brand must NOT sound like
Reader:          # from target_audience — who is on the other side
Positioning:     # the axis the brand competes on, and what it positions against
Source:          # the files, so a reviewer can check
```

**3. Sanity-test it** — could a competitor publish this draft after find-and-replacing the brand name? If yes, the contract isn't on the page.

## Worked example — OFFLIMITS

Reading `brands/offlimits/knowledge.md` + `brand-dna.json`:

```text
Register:        Motivational, gutsy, inclusive, value-conscious. Athlete-first, never luxury-aspirational.
Patterns to use: "Push limits, not excuses" / "beyond limits" framing; "OFF LIMITS Tribe" community language;
                 performance and affordability argued together; made-in-India, built-for-Indian-conditions pride;
                 inclusivity cues (plus-size / big & tall, sizes 12-14).
Proof points:    Real tech names — Advance Memory Foam, Athlite®, Flexinit®, Glovefit®, Wiktech®.
                 Manufacturing scale and export credibility. Value at international standards.
Vocabulary:      Canonical brand name is unresolved (Offlimits / OFF LIMITS / Off Limits) — open question; standardize before publishing.
Prohibitions:    No generic hype. No unattributed "quick-dry"/"breathable" claims when a named tech covers it.
                 Keyword volumes are estimated — never presented as measured.
Reader:          Value-seeking Indian fitness enthusiasts and everyday athletes; students, recreational
                 runners and gym-goers; plus-size shoppers; streetwear buyers.
Positioning:     "Accessible high performance". Positions AGAINST Nike/Adidas/Puma as aspirational alternatives on price.
Source:          brands/offlimits/knowledge.md, brands/offlimits/brand-dna.json
```

**Read what that contract prevents.** A monsoon activewear draft hedging about unverified "quick-dry fabric" is violating this contract three ways: it ignores `Wiktech®` ("faster moisture evaporation") which is *already sanctioned*; it breaks "cite real tech names"; and hedging is the opposite of gutsy. The brand had the answer, in its own vocabulary, on disk.

It also shows where **the contract must beat the request**. A reviewer asking for a more "aspirational" voice conflicts with a DNA that positions *against* aspiration. `CLAUDE.md` is explicit — the brand file wins, and you surface the discrepancy. Read that feedback for what it's really reporting (the copy is lifeless) and fix it with the brand's own energy: gutsy, motivational, Tribe. Don't quietly rewrite the brand into a luxury label. If the DNA is genuinely wrong, that's an `open_question` for the brand team, not a silent edit.

## Using it while writing

- Draft **from** the contract, don't retrofit to it. Retrofitting produces slogans dropped into neutral prose — which reads worse than no voice at all.
- `voice_patterns` are **framings, not catchphrases**. "Push limits, not excuses" is a way of arguing; it is not a sentence to paste into every intro.
- Prohibitions bind hardest. "Avoid generic hype" outranks any instinct to sound exciting.
- When the contract and a generic best-practice disagree, **the contract wins** — it's the brand's file.

## Voice corpus: the brand's own posts

`blogs/references/<slug>.md` stores metadata and a summary per published post, never the body (no republishing prose). Their `voice_notes` field carries the observable style signal — cadence, person, opening move, sentence length, how products get introduced. Read them as evidence of how this brand *actually* writes, which is often more specific than `brand_voice.description`.

If `voice_notes` are missing, note the gap; brand-setup Phase 3 (`brand-setup/references/03-blogs.md`) captures them.
