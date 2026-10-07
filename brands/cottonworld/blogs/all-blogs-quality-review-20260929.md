# Cottonworld blog quality review and repair plan

User-facing review: [Cottonworld blog quality review and editorial repairs](https://docs.google.com/document/d/11deSYq8vji6aYfrIoFR4fs6H_N_jRShkwSL51d1xDMQ/edit).

Reviewed 2026-09-29; updated 2026-10-07 for the three-topic editorial set. Scope: the four articles live at `/blogs/blog/` and seven article drafts in this brand workspace. Collection-page copy is excluded. Benchmark: [Semrush's SEO blog post guide](https://www.semrush.com/blog/seo-blog-post/) and Cottonworld's `writing-style.md`. Counts are approximate body words from the current draft text; they are a depth signal, not a ranking threshold.

## Verdict

The blog programme is **not yet up to publication standard**. The seven unpublished articles have useful copy and meet the user-approved 1,000-plus-word depth. Four published URLs are a critical content failure: two contain unrelated JSW Defence and Lorem Ipsum copy; two have no genuine article body. A fresh HTTP and Article JSON-LD check on 2026-10-07 confirmed all four remain in that state. Replacement drafts have been written for all four, but the live site has not been changed. The ZeroGPT API returned 403 “Not enough credits”; website UI checks on the exact three-topic set returned 86.9%, 91.0% and 87.8%, above the strict below-20% gate. All remain editorial review drafts.

## Article-by-article status

| Article | Current state | Approx. words | Finding | Repair made | Remaining gate |
|---|---|---:|---|---|---|
| Comfort Meets Style | Live placeholder | 1,329 replacement | Critical: unrelated defence copy and Lorem Ipsum | [Full replacement draft](https://docs.google.com/document/d/1qqxHCzDkc5hJyJZEZq5grMeh-GIUFCKOdXX6CGbPHjg/edit); clear day-to-outfit flow, fabric/fit checks, repeat-wear examples | Replace Shopify body; real author/date/image; ZeroGPT score |
| The Story of Natural Cotton | Live placeholder | 1,268 replacement | Critical: unrelated defence copy and Lorem Ipsum | [Full replacement draft](https://docs.google.com/document/d/1lRnaZN98Q50c-8hMzQRh1nLM_NHaF0EEoAmUmLsF5DY/edit); cotton properties, limits, garment check and care | Replace Shopify body; real author/date/image; ZeroGPT score |
| Slow Living, Everyday Style | Live empty article | 1,280 replacement | Critical: only placeholder excerpt and site furniture | [Full replacement draft](https://docs.google.com/document/d/1iaUbZVsoyOEvTz4ub_CLMvjGkSRlwWkrkUMNv1u_tEA/edit); ordinary-week audit, useful combinations, care and shopping brief | Replace Shopify body; real author/date/image; ZeroGPT score |
| Timeless Wardrobes | Live empty article | 1,337 replacement | Critical: only placeholder excerpt and site furniture; visible “cloths” typo | [Full replacement draft](https://docs.google.com/document/d/1QHzLiML98JxZs3p2aPMfwwbKb5iqNuv2DeLzYc4t4As/edit) with “clothes” in H1; existing URL retained pending redirect plan | Replace Shopify body; real author/date/image; ZeroGPT score |
| 8 Relaxed Outfit Ideas | Draft | 1,255 | Three 404 product links; several forced keyword phrases | Replaced links with verified current categories and removed unsupported SKU detail; tightened phrases | Sync current draft to publishing doc; image/byline; ZeroGPT score |
| From Commute to Office | Draft | 1,419 | Four 404 product links and a forced keyword phrase | Replaced links, removed stale product detail, tightened phrase | Sync current draft to publishing doc; image/byline; ZeroGPT score |
| Long-Weekend Packing List | Draft | 1,115 | One 404 product link; keyword-first sentence | Replaced link and stale detail; made opening route-led | Sync current draft to publishing doc; image/byline; ZeroGPT score |
| Comfortable Date Outfits | Draft | 1,211 | Three 404 product links; one weak colour paragraph | Replaced links and stale details; made colour advice useful beyond a single occasion | Sync current draft to publishing doc; image/byline; ZeroGPT score |
| A Full Wardrobe, Nothing to Wear | Draft | 1,255 | The earlier version repeated its advice and ended with a bolted-on FAQ | Rewrote as a continuous wardrobe-to-outfit-to-gap story; removed FAQ; [refined Google Doc](https://docs.google.com/document/d/1Jw4TuMCqLxueBf2KiFLPjDOEbQ6-bKDrt8PBEMowh-M/edit) | ZeroGPT UI 86.9%; image/byline |
| Warm Afternoons, Cooler Evenings | Draft | 1,339 | The earlier version felt modular and its FAQ interrupted the ending | Rewrote around a day that changes temperature; combined fit, carry and outfit guidance; [refined Google Doc](https://docs.google.com/document/d/1taPykz2elffvZWOSKw7jGNQ6lV61eJxgMSYuD_grN3o/edit) | ZeroGPT UI 91.0%; image/byline |
| One Bag, Two Climates | New draft | 1,530 | Approved third topic had no article draft | Wrote a route-led short-trip guide with a shared clothing base, conditional weather layers, clean-clothes planning and [Google Doc](https://docs.google.com/document/d/1LzSFlSeweOqN864WGQNE78jKRwvwfKxysbRrg-lUBNs/edit) | ZeroGPT UI 87.8%; image/byline |

## Benchmark findings

Semrush's January 2026 guide recommends selecting a primary keyword or prompt, matching search intent, answering directly in a clear heading structure, adding useful examples and current information, writing a distinct title tag and meta description, using relevant images and natural internal links, showing the real author, and using a clear URL. It proposes short title tags as a display tactic, not a guarantee that Google will show a precise number of characters. Its advice to add expert insights and statistics applies when real, relevant evidence exists; these lifestyle articles should not gain invented quotes or numbers to fill a checklist.

The exact-title searches for the four live article replacements primarily returned Cottonworld's own placeholder URLs and index. To obtain three comparable organic articles per topic, topical queries were run and the first three relevant accessible blog or editorial-guide results were reviewed. The captured text and headings are in `../logs/content/raw/20260929-all-blogs-serp-benchmark-captures.json`; lengths below are extracted estimates and sometimes include page furniture.

| Replacement topic | Ranking comparable and URL | Tone | Est. words | Structure and flow |
|---|---|---|---:|---|
| Comfortable everyday outfits | [Islinen](https://www.islinen.com/blogs/news/10-casual-linen-outfit-ideas-for-everyday-comfort) | Promotional listicle | 985 | Short opening, ten numbered outfit pairings, fabric benefits, FAQs |
|  | [MEC PRIMO](https://mecprimo.com/blogs/news/5-ways-to-style-your-cotton-linen-outfits-for-everyday-wear) | Breezy retail advice | 486 | Five styling ideas, little explanation; heading extraction limited |
|  | [Lush Linen Threads](https://lushlinenthreads.com/blogs/journal/linen-outfit-ideas-for-work-travel-every-wear) | Detailed, practical | 2,592 | Quick picks, fabric/shape guidance, occasion outfits, FAQ |
| Natural cotton | [ScienceInsights](https://scienceinsights.org/is-cotton-a-good-material-pros-cons-and-best-uses/) | Explanatory and balanced | 1,090 | Benefits, wet-weather limits, durability and uses |
|  | [Moda Selection](https://www.modaselection.com/articles/fabric-guide-for-everyday-clothes) | Concise editorial | 592 | Fabric-by-fabric comparison and fitting-room test |
|  | [Fabric Care Lab](https://fabriccarelab.org/fabrics/cotton/) | Direct reference guide | 760 | Quick answer, properties, care and questions |
| Slow living style | [AuthentikYou](https://authentikyou.com/blogs/fashion/dressing-for-yourself-a-slow-fashion-guide-to-everyday-style) | Personal editorial | 1,440 | Everyday-wardrobe problem, identity and practicality, buying questions |
|  | [Daniela Salazar](https://daniela-salazar.com/blogs/journal/wearing-intentions-the-deeper-meaning-of-a-slow-wardrobe-and-slow-living) | Reflective | 717 | Meaning of a slow wardrobe, quality and personal connection |
|  | [Bloguido](https://bloguido.com/the-mindful-wardrobe-how-to-dress-with-intention-instead-of-on-autopilot-6204/) | Practical how-to | 1,361 | Wardrobe scan, real-life sorting, outfit formulas, shopping list |
| Timeless wardrobe | [Lifestyle Hub Today](https://www.lifestylehubtoday.com/l/how-to-build-a-timeless-wardrobe-quality-fit-cost-per-wear/) | Measured practical guide | 2,007 | Definition, fit, construction, fabric and care checks |
|  | [Outfit Maker](https://blog.outfitmakerapp.com/en/clothing-that-never-gets-old-the-timeless-wardrobe-playbook) | Checklist-led | 1,470 | Pieces, quality, fit, colour, care, seasonal refresh |
|  | [Project Cece](https://www.projectcece.com/blog/794/how-to-build-a-seasonless-wardrobe/) | Accessible explanatory | 1,197 | Seasonless definition, mindset, process and examples |

The replacements use comparable practical depth with Cottonworld's calmer voice, Indian day-to-day occasions, specific fit and care checks, and a clear reader journey. Their section sequence and wording are original. The benchmark does not justify a universal word-count rule; each draft is long enough to answer its topic without adding unrelated statistics.

For the two 2026-10-07 rewrites, exact-title live searches and topical follow-ups identified three relevant organic blogs apiece. The five-piece comparables ranged from roughly 620 to 1,950 extracted words; the layering comparables from roughly 830 to 2,740. Both sets favoured a concrete opening, practical examples, and a progression toward a decision. The revised Cottonworld drafts use that depth and continuity while keeping their own scenarios and section order. Rankings, URLs, tone, headings, extracted lengths and access date are recorded in `../logs/content/raw/20261007-refined-blogs-serp-captures.json`.

The third title also received a mandatory live SERP check before drafting. No exact-title article appeared. The first three relevant organic India packing blogs in the topical query were Packzup (about 729 extracted words, checklist-led), G Adventures (about 1,254 words from live web extraction, lively itinerary and season sections) and Lux India Tours (about 1,069 words, regional planning and checklist). The new article takes the shared-clothes problem of a short two-stop journey as its own organising idea. Rankings, tone, lengths and heading flow are recorded in `../logs/content/raw/20261007-third-blog-serp/benchmark.json`.

## Findings and priority fixes

1. **Critical — published placeholders.** Evidence: all four live URLs returned HTTP 200 on 2026-09-29 and again on 2026-10-07. The first two Article JSON-LD bodies still include JSW Defence and Lorem Ipsum; the other two Article JSON-LD bodies are empty and have Lorem Ipsum descriptions. Fix: replace the body and excerpt at the existing URLs with the new drafts; remove the unrelated copy and check the rendered article after publishing. Owner: Cottonworld Shopify content owner. Confidence: high.
2. **High — stale internal destinations.** Evidence: 11 in-body links across four drafts pointed to eight product URLs returning 404. Fix completed in the workspace: all 63 in-body internal links across the ten drafts at the 2026-09-29 check pointed to 31 unique destinations that returned HTTP 200 with no redirects. The two rewritten drafts' internal links were checked again on 2026-10-07 and returned HTTP 200. An automated request to the external Utah State University citation disconnected once; a live web fetch on 2026-10-07 reached the page and confirmed the cited passage. Owner: SEO editor for source copy, Shopify content owner for CMS copies. Confidence: high.
3. **High — external authenticity gate failed or blocked.** Evidence: ten drafts submitted through the repository ZeroGPT harness on 2026-09-29; every API response reported 403 “Not enough credits.” The three-topic set was checked on the ZeroGPT website UI on 2026-10-07: 86.9% (five-piece), 91.0% (layering) and 87.8% (packing). All three fail the strictly-below-20% publication gate. The tool's local fallback values are not ZeroGPT percentages. Fix: keep the drafts in editorial review; revise only where source-backed, brand-specific changes improve the copy, then recheck the exact final bodies. Owner: SEO/content editor and tool owner. Confidence: high.
4. **Medium — publication presentation.** Evidence: the draft files carry no actual article imagery, verified individual author bio or visible update date. Fix: assign a real writer/editor with an accurate bio; display the publication or material update date; add one useful, rights-cleared brand image or simple visual per article with descriptive alt text and compressed dimensions. Owner: content editor and site producer. Confidence: high.
5. **Medium — keyword evidence.** Evidence: primary topics are identified, but the current keyword universe explicitly lists only “how to build a capsule wardrobe” from this ten-article set. Fix: validate remaining primary queries against Search Console and/or Keyword Planner before scheduling; use the live SERP intent comparison as a format cue, not a search-volume claim. Owner: SEO strategist. Confidence: high.
6. **Low — URL/title typo.** Evidence: the live timeless URL contains `cloths`; the article title has the same typo. Fix: use “clothes” in visible H1 and metadata now. If changing the slug later, redirect the old indexed URL to the new canonical before release. Owner: Shopify content owner and SEO. Confidence: high.

## Image briefs for production

- Comfortable everyday outfits: one real Cottonworld shirt-and-trouser or dress outfit shown in an ordinary work-to-weekend setting; alt text describes garment and setting.
- Natural cotton: close photograph of two distinct cotton garment constructions, such as knit tee and woven shirt, labelled accurately.
- Slow living: simple repeat-wear outfit grid using the same garment across two real occasions; no invented wearer testimonial.
- Timeless wardrobe: a small garment-check visual showing seam, button, label and fit details.
- Rainy day outfits: a real shorter-hem outfit and packed dry layer; avoid implying cotton is waterproof.
- Monsoon workwear: one outfit with and without an indoor layer.
- Long-weekend packing: a nine-piece flat lay whose count matches the article.
- Comfortable date outfits: one outfit each for brunch, a walk and dinner, using actual available products.
- Five-piece wardrobe: five garment flat lay plus two outfit combinations from them.
- Cotton and linen layering: the same base outfit with and without the removable layer.
- Two-climate short trip: one small bag beside a shared set of clothes and a distinct weather layer; do not imply a tested bag capacity.

## Handoff checks

Before any article is called publish-ready: verify the current exact body on ZeroGPT at strictly below 20%; check the live CMS page for the correct H1, title tag, meta description, visible date and author; verify at least three blue-underlined in-body internal links including a contextual collection, a supporting guide/category and the conclusion CTA; check image alt text and load size; confirm the live article contains no placeholder copy; inspect the mobile rendered page. No Shopify write was made in this review.

## Evidence

- `../logs/content/raw/20260929-semrush-and-live-post-captures.json`: Semrush guide and four live page captures.
- `../logs/content/raw/20260929-all-blogs-serp-benchmark-captures.json`: 12 ranking comparable captures with headings and extracted length.
- `../logs/content/raw/20260929-all-draft-internal-link-check.json`: initial 404 findings.
- `../logs/content/raw/20260929-all-draft-internal-link-final.json`: final in-body link map and HTTP checks.
- `../logs/content/raw/20260929-zero-gpt-review/`: exact draft submissions and detector responses.
- `../logs/content/raw/20261007-refined-blogs-serp-captures.json`: ranking comparables for the two named rewrites.
- `../logs/content/raw/20261007-refined-two-link-and-gate-check.json`: current in-body link checks and gate status.
- `../logs/content/raw/20261007-zero-gpt-review/`: exact rewritten body submissions and detector responses.
- `../logs/content/raw/20261007-zero-gpt-website-ui-review.json`: verified UI percentages for the three-topic set.
- `../logs/content/raw/20261007-third-blog-serp/benchmark.json`: third-topic SERP tone, depth and flow benchmark.
- `../logs/content/raw/20261007-third-blog-links/verification.json`: live third-article internal link targets and source page.
- `../logs/content/raw/20261007-third-blog-zerogpt/`: exact third draft submission and API fallback.
- `../logs/content/raw/20261007-usu-source-recheck.json`: current live citation fetch and supported passage.
- `../logs/content/raw/20261007-live-blog-recheck/`: four current HTTP captures and Article JSON-LD findings.
- `../logs/content/raw/20261007-blog-google-doc-verification.json`: native review documents and heading/link styling checks.
- `context.md`, `knowledge.md`, `blogs/writing-style.md`: brand boundaries and approved editorial standard.
