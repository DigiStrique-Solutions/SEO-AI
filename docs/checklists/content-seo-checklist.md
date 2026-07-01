# Content SEO Checklist

Updated: 2026-06-29

Use this checklist when auditing, briefing, writing, refreshing, or scoring content for organic search and AI search visibility. This is the deep content checklist. Keep the generic on-page checklist as the quick page audit.

## Research Basis

Primary and reputable sources used:

- [Google creating helpful, reliable, people-first content](https://developers.google.com/search/docs/fundamentals/creating-helpful-content)
- [Google SEO Starter Guide](https://developers.google.com/search/docs/fundamentals/seo-starter-guide)
- [Google guidance on generative AI content](https://developers.google.com/search/docs/fundamentals/using-gen-ai-content)
- [Google Search spam policies](https://developers.google.com/search/docs/essentials/spam-policies)
- [Google title link guidance](https://developers.google.com/search/docs/appearance/title-link)
- [Google snippet guidance](https://developers.google.com/search/docs/appearance/snippet)
- [Google image SEO best practices](https://developers.google.com/search/docs/appearance/google-images)
- [Google video SEO best practices](https://developers.google.com/search/docs/appearance/video)
- [Google structured data introduction](https://developers.google.com/search/docs/appearance/structured-data/intro-structured-data)
- [Google article structured data guidance](https://developers.google.com/search/docs/appearance/structured-data/article)
- [Google product structured data guidance](https://developers.google.com/search/docs/appearance/structured-data/product)
- [Google review snippet structured data guidance](https://developers.google.com/search/docs/appearance/structured-data/review-snippet)
- [Google FAQ structured data guidance](https://developers.google.com/search/docs/appearance/structured-data/faqpage)
- [Google AI features optimization guide](https://developers.google.com/search/docs/fundamentals/ai-optimization-guide)
- [Google AI features and Search controls](https://developers.google.com/search/docs/appearance/ai-features)
- [Google Search Quality Rater Guidelines](https://static.googleusercontent.com/media/guidelines.raterhub.com/en//searchqualityevaluatorguidelines.pdf)
- [NN/g how users read on the web](https://www.nngroup.com/articles/how-users-read-on-the-web/)
- [NN/g writing for the web topic guide](https://www.nngroup.com/topic/writing-web/)
- [NN/g F-shaped pattern of reading](https://www.nngroup.com/articles/f-shaped-pattern-reading-web-content/)
- [W3C informative image guidance](https://www.w3.org/WAI/tutorials/images/informative/)
- [W3C decorative image guidance](https://www.w3.org/WAI/tutorials/images/decorative/)

## Evidence Source Legend

Use free, owned, or open-source sources first.

Google-visible scope: judge pass/fail from public rendered content, metadata, links, schema, media, GSC outcome data, keyword demand, and lab/field performance evidence. CMS/code, GA4/PostHog, governance, ownership, and editorial workflow are optional implementation or prioritization evidence, not blockers for what Google can see.

- `Firecrawl`: rendered page extraction, headings, text, metadata, links, images, schema, screenshots, crawl samples.
- `Playwright`: precise rendered DOM inspection, screenshots, mobile checks, hidden content, interactive elements, author/date visibility.
- `GSC`: queries, pages, impressions, clicks, CTR, positions, Discover when available, search appearance, index status.
- `GA4`: landing page engagement, conversions, revenue or lead value, scroll events, internal search, traffic by channel.
- `GKP`: Google Ads Keyword Planner for directional query demand and variants.
- `GMC`: Merchant Center product/feed context for ecommerce content.
- `GBP`: Google Business Profile for local business, service, location, review, and category context.
- `GMAPS`: Maps and Places data for local competitors, categories, locations, and attributes.
- `CMS/code`: CMS fields, templates, author data, publish/update dates, product data, docs routes, content owners, schema code.
- `OSS`: open-source/free checks such as schema validators, markdown linters, link checkers, readability libraries, spell checkers, axe-core.
- `Manual/free SERP`: manual SERP review, People Also Ask, competing result formats, visible search features, AI answer observations.
- `Human/context`: customer calls, support tickets, sales objections, expert review, product facts, editorial judgment.

## Scoring

- `critical`: content is misleading, unsafe, policy-risky, unindexable when it should rank, or fails a YMYL trust threshold.
- `high`: content misses intent, lacks originality, has major factual gaps, cannibalizes another page, or cannot convert its target audience.
- `medium`: content is useful but incomplete, poorly structured, stale, weakly linked, or missing proof.
- `low`: polish issues such as examples, formatting, media, minor citation gaps, or CTA alignment.
- `not_applicable`: section does not fit the page type.

Issue record:

```text
Severity:
Area:
Evidence source:
Affected URL:
Issue:
Why it matters:
Recommended fix:
Owner:
Confidence:
```

## 1. Page Purpose And Audience

Evidence sources: `Human/context`, `GSC`, `GA4`, `GKP`, `Manual/free SERP`.

- [ ] The page has one primary purpose: educate, compare, help decide, sell, support, onboard, build trust, or retain.
- [ ] The audience is explicit: persona, role, industry, skill level, buyer stage, location, or platform.
- [ ] The page explains who it is for within the first screen or opening section.
- [ ] The page solves a real user problem, not only a keyword target.
- [ ] The page has a clear next step for users who want more detail.
- [ ] The page has a clear next step for users ready to act.
- [ ] The content type matches the job: guide, tutorial, checklist, comparison, product page, category page, case study, docs page, local page, FAQ, template, tool, or landing page.

## 2. Search Intent Match

Evidence sources: `GSC`, `GKP`, `Manual/free SERP`, `Firecrawl`, `GA4`.

- [ ] Search intent is classified: informational, commercial, transactional, navigational, local, support, or mixed.
- [ ] The page format matches the SERP expectation: guide, short answer, list, video, product, category, comparison, local results block, image-heavy result, tool, or documentation.
- [ ] The opening section answers the main query quickly enough for impatient readers.
- [ ] The page also supports deeper readers with examples, steps, proof, and related questions.
- [ ] The page does not bury the answer below brand fluff, generic intros, or unrelated copy.
- [ ] The page does not target several unrelated intents at once.
- [ ] Mixed-intent pages clearly separate learning, evaluation, and action paths.

## 3. Keyword, Query, And Entity Coverage

Evidence sources: `GSC`, `GKP`, `Manual/free SERP`, `Firecrawl`, `Human/context`.

- [ ] One primary query theme is mapped to the page.
- [ ] The page does not compete with a stronger page for the same primary intent.
- [ ] Important synonyms, modifiers, entities, and user-language variants appear naturally.
- [ ] Exact-match keywords are not repeated mechanically.
- [ ] Product names, categories, people, organizations, locations, standards, tools, prices, attributes, and constraints are unambiguous.
- [ ] The page covers necessary subtopics without becoming a generic encyclopedia page.
- [ ] Entity gaps from top competing results are reviewed, then accepted or filled based on user value.

## 4. Information Gain And Originality

Evidence sources: `Human/context`, `CMS/code`, `Manual/free SERP`, `Firecrawl`, `GA4`.

- [ ] The page adds something competitors do not: firsthand experience, original data, screenshots, examples, templates, benchmarks, expert review, product knowledge, or decision criteria.
- [ ] Generic definitions are kept short unless the query requires a beginner explanation.
- [ ] The page avoids rewriting the same obvious points found in every ranking result.
- [ ] Claims are backed by examples, data, citations, product evidence, or expert explanation.
- [ ] The page includes practical details a real practitioner would know.
- [ ] Opinions and recommendations are labeled as opinions or recommendations.
- [ ] If AI assisted the draft, a human added facts, judgment, verification, and distinctive value.
- [ ] AI-assisted drafts are edited to remove generic filler, repetitive phrasing, fake certainty, vague summaries, and templated transitions.
- [ ] The article has a human editorial voice that fits the brand and audience instead of sounding like an unreviewed model output.

## 5. Content Depth And Completeness

Evidence sources: `Firecrawl`, `Playwright`, `GSC`, `GKP`, `Manual/free SERP`, `Human/context`.

- [ ] The page fully satisfies the main task or question.
- [ ] The page covers definitions, steps, examples, tradeoffs, mistakes, prerequisites, risks, alternatives, and next actions where relevant.
- [ ] The page answers likely follow-up questions without turning every subtopic into filler.
- [ ] The page links to deeper supporting pages when a subtopic deserves its own URL.
- [ ] Content length is not judged by a fixed word count.
- [ ] Short content is accepted when it fully satisfies intent.
- [ ] Long content is flagged when it repeats points, pads introductions, or includes irrelevant sections.
- [ ] Blog posts, guides, and paragraphs are as long as needed and as short as possible.

## 6. Structure, Headings, And Scannability

Evidence sources: `Firecrawl`, `Playwright`, `OSS`, `Human/context`.

- [ ] The H1 names the page topic clearly.
- [ ] H2s and H3s form a logical outline.
- [ ] Headings are useful to readers, not just keyword containers.
- [ ] The introduction confirms the page's promise quickly.
- [ ] Paragraphs are focused on one idea.
- [ ] Dense passages are broken with headings, bullets, tables, examples, callouts, images, or summaries where useful.
- [ ] Lists are used for lists, tables for tabular comparison, and prose for explanation.
- [ ] The page avoids walls of text on mobile.
- [ ] In-page navigation or section anchors exist for long reference content.
- [ ] Important content is not hidden behind unclear accordions, tabs, carousels, or client-only rendering.

## 7. Titles, Meta Descriptions, And SERP Promise

Evidence sources: `Firecrawl`, `GSC`, `Manual/free SERP`, `CMS/code`.

- [ ] The title tag is unique and describes the page accurately.
- [ ] The title is usually concise enough to display well, roughly 50 to 60 characters when possible.
- [ ] The title puts the main topic early without keyword stuffing.
- [ ] The H1 and title can differ, but they do not make conflicting promises.
- [ ] The meta description is unique, honest, and useful.
- [ ] The meta description usually fits roughly 120 to 160 characters when possible.
- [ ] The SERP promise matches the actual page content.
- [ ] Pages with high impressions and low CTR are reviewed for title, snippet, intent, and SERP mismatch.
- [ ] Dates, prices, ratings, availability, and other snippet-relevant details are accurate when visible.

## 8. Evidence, Citations, And Source Quality

Evidence sources: `Firecrawl`, `Playwright`, `Manual/free SERP`, `Human/context`, `CMS/code`.

- [ ] Factual claims that matter are supported by reputable sources, screenshots, product data, customer evidence, or expert review.
- [ ] External citations point to primary sources when possible.
- [ ] Statistics include source, date, and context.
- [ ] Exact numbers, benchmarks, pricing claims, competitor claims, platform policy claims, and strategic estimates have source adjacency or are clearly labeled as estimates.
- [ ] Legal, health, finance, safety, and other YMYL claims use stronger sourcing and expert review.
- [ ] Quotes are accurate and not overused.
- [ ] Affiliate, sponsored, or partner relationships are disclosed where relevant.
- [ ] The page does not cite low-quality sources to create fake authority.
- [ ] Broken or outdated citations are fixed.

## 9. E-E-A-T And Trust Signals

Evidence sources: `Firecrawl`, `Playwright`, `CMS/code`, `Human/context`, `Manual/free SERP`.

- [ ] The publisher, brand, or organization is clear.
- [ ] Author, reviewer, or editor details are visible when trust requires them.
- [ ] Credentials and practical experience are shown for expert topics.
- [ ] YMYL pages have appropriate review, accountability, consensus alignment, and safety caution.
- [ ] Contact, support, privacy, refund, shipping, terms, or business details are findable where relevant.
- [ ] Reviews, testimonials, case studies, awards, certifications, and customer logos are specific and verifiable.
- [ ] The page avoids fake authorship, fake freshness, fake reviews, and unsupported claims.
- [ ] User-generated content is moderated when quality, safety, or trust matter.

## 10. Freshness And Maintenance

Evidence sources: `GSC`, `GA4`, `Firecrawl`, `CMS/code`, `Human/context`.

- [ ] Time-sensitive content is current: pricing, screenshots, product UI, laws, stats, policies, rankings, tools, and examples.
- [ ] Publish and update dates reflect meaningful content changes.
- [ ] Date-only refreshes are not treated as content improvements.
- [ ] Content has an owner and review cadence where freshness matters.
- [ ] Decaying pages are identified through GSC clicks, impressions, CTR, and query drift.
- [ ] Old content is updated, consolidated, redirected, noindexed, or removed based on value.
- [ ] Refreshes include new facts, examples, queries, internal links, media, schema, and conversion paths where useful.

## 11. Readability And Accessibility

Evidence sources: `Playwright`, `Firecrawl`, `OSS`, `Human/context`.

- [ ] Language matches the audience's knowledge level.
- [ ] Sentences are direct and avoid unnecessary jargon.
- [ ] Terms of art are defined when the audience may not know them.
- [ ] Copy is checked for AI-style punctuation and formatting artifacts, including unnecessary em dashes, en dashes, excessive colons, repeated sentence patterns, and over-polished transitions.
- [ ] Body copy is readable on mobile and desktop.
- [ ] Text is not embedded only in images.
- [ ] Informative images have useful alt text.
- [ ] Decorative images use empty alt text or are hidden from assistive tech.
- [ ] Tables, lists, headings, and links are semantic.
- [ ] Link text is descriptive.
- [ ] Content remains understandable at common zoom levels and text spacing settings.

## 11A. Editorial Voice And Anti-Slop Cleanup

Evidence sources: `Playwright`, `Firecrawl`, `CMS/code`, `Human/context`.

- [ ] Final copy does not expose internal process language such as tool use, prompt names, model names, routing, agents, or workflow narration.
- [ ] Copy does not open with generic praise, filler, or throat-clearing phrases such as "great question", "absolutely", "it is worth noting", "when it comes to", or "at its core".
- [ ] Copy does not use formulaic consultant labels such as "key insight", "critical design principle", "the full blueprint", or similar boilerplate unless quoting a source.
- [ ] Copy does not force a fixed hook, meat, data, action structure when the page needs a normal explanation.
- [ ] Copy does not end with generic engagement-menu language such as "want me to go deeper" or "let me know if you want".
- [ ] Copy avoids binary contrast formulas such as "not X but Y" unless the contrast is genuinely useful.
- [ ] Lists are not forced into three items when the real answer has a different count.
- [ ] Sentence rhythm varies naturally and avoids chains of same-length short sentences.
- [ ] Passive voice is reviewed when it hides the actor, source, or responsibility.
- [ ] Abstract business jargon is replaced with concrete nouns, verbs, mechanisms, entities, dates, or user consequences.
- [ ] Brand voice is based on real user examples, brand profile, audience, positioning, or customer language instead of invented personality.
- [ ] The final edit asks: could any AI have written this for any company? If yes, add specificity or cut the passage.

## 12. Media, Examples, And Supporting Assets

Evidence sources: `Firecrawl`, `Playwright`, `CMS/code`, `Human/context`, `OSS`.

- [ ] Images, videos, screenshots, tables, charts, templates, calculators, or code examples help the user complete the task.
- [ ] Media is original or properly licensed.
- [ ] Screenshots are current and readable.
- [ ] Video pages include useful titles, descriptions, transcripts, thumbnails, and structured data where appropriate.
- [ ] Image-heavy pages use descriptive filenames, alt text, captions, surrounding context, and crawlable image URLs.
- [ ] Tables compare decision criteria users actually care about.
- [ ] Examples are concrete enough to copy, adapt, or verify.

## 13. Internal Links And Content Clusters

Evidence sources: `Firecrawl`, `GSC`, `GA4`, `CMS/code`, `Human/context`.

- [ ] The page links to relevant parent, child, sibling, and conversion pages.
- [ ] The page receives links from relevant hubs, navigation, related content, or high-value pages.
- [ ] Anchor text is descriptive and natural.
- [ ] Internal links help users continue the journey, not only distribute crawl signals.
- [ ] Hub pages and spokes link both ways where useful.
- [ ] New content is backfilled into older relevant pages.
- [ ] Broken or redirected internal links are fixed.
- [ ] Orphan content is linked, consolidated, or removed.

## 14. External Links And References

Evidence sources: `Firecrawl`, `Playwright`, `OSS`, `Human/context`.

- [ ] External links support claims, definitions, standards, research, or tools.
- [ ] External links open to trustworthy and relevant sources.
- [ ] Outbound links are not excessive or distracting.
- [ ] Sponsored, affiliate, or user-generated links use appropriate link attributes.
- [ ] Broken external links are fixed or removed.
- [ ] Competitor links are intentional and useful, not accidental leakage from copied outlines.

## 15. Structured Data And Search Appearance

Evidence sources: `Firecrawl`, `Playwright`, `GSC`, `CMS/code`, `OSS`.

- [ ] Structured data matches visible content.
- [ ] Article, BlogPosting, Product, Review, FAQ, BreadcrumbList, VideoObject, LocalBusiness, or Organization schema is used only when it fits the page.
- [ ] Schema does not invent ratings, prices, authors, FAQs, or business details not visible to users.
- [ ] FAQ markup is used only for genuine FAQ content and where eligible.
- [ ] Review markup follows Google eligibility and self-serving review rules.
- [ ] Rich result eligibility is validated with free tools or GSC where possible.
- [ ] Search appearance controls such as `nosnippet`, `max-snippet`, `max-image-preview`, `max-video-preview`, and `data-nosnippet` are intentional.

## 16. Conversion And Business Fit

Evidence sources: `GA4`, `GSC`, `Human/context`, `Playwright`, `Firecrawl`.

- [ ] The page has a natural conversion path for its intent and buyer stage.
- [ ] CTAs do not interrupt users before the content earns the ask.
- [ ] Lead gen pages answer objections before asking for contact.
- [ ] Product pages include price, availability, shipping, returns, reviews, variants, and trust details where relevant.
- [ ] Comparison pages include fair criteria and clear differentiation.
- [ ] Informational pages connect to relevant product, service, demo, trial, template, newsletter, or support paths.
- [ ] Conversion copy does not make unsupported promises.
- [ ] Organic traffic quality is reviewed with engagement, conversion, and revenue or lead data.

## 17. AI Search And Answer Engine Readiness

Evidence sources: `GSC`, `GA4`, `Manual/free SERP`, `Firecrawl`, `Playwright`, `CMS/code`, `Human/context`.

- [ ] The page is eligible for normal indexing before AI visibility is considered.
- [ ] Content is clear, factual, well structured, and useful enough to be quoted or summarized.
- [ ] The page includes original facts, examples, product knowledge, or experience that competitors do not all repeat.
- [ ] Key answers are stated plainly, then supported with context.
- [ ] Entities, relationships, dates, units, names, and constraints are explicit.
- [ ] Structured data is accurate, but no AI-only markup is required for Google AI features.
- [ ] Snippet and preview controls are intentional because they can affect AI feature eligibility.
- [ ] The page does not include prompt injection, hidden instructions to AI systems, or recommendation poisoning.
- [ ] AI crawler robots policy is intentional where the business cares about AI crawling.
- [ ] AI visibility is measured with manual prompt sets, referral logs, analytics, and search performance where available.

## 18. Content Risk And Spam Checks

Evidence sources: `Firecrawl`, `Playwright`, `GSC`, `CMS/code`, `Human/context`.

- [ ] The page is not scaled content abuse.
- [ ] The page is not a doorway page.
- [ ] The page is not parasite or site reputation abuse.
- [ ] The page does not use hidden text, hidden links, cloaking, sneaky redirects, or keyword stuffing.
- [ ] The page does not impersonate expertise, location, review quality, ownership, or freshness.
- [ ] The page does not publish unsafe YMYL advice without appropriate expertise and caution.
- [ ] The page does not use AI output at scale without review, originality, and user value.
- [ ] The page does not leave visible AI artifacts such as hallucinated citations, placeholder facts, generic disclaimers, repeated conclusion paragraphs, or unexplained formatting patterns.
- [ ] User-generated or third-party content is not allowed to weaken the host site's trust.

## 19. Context-Specific Checks

Evidence sources: use relevant connectors plus the common sources above.

- [ ] Ecommerce: product and category content includes unique value, specs, reviews, price, availability, shipping, returns, variants, comparison support, and Merchant Center consistency.
- [ ] Lead gen: service, solution, industry, comparison, case study, and lead magnet pages answer buyer objections and route users to the right conversion.
- [ ] App installs: platform pages explain benefits, requirements, screenshots, privacy, permissions, app store paths, web fallback, and onboarding.
- [ ] Local: location and service-area pages include real local value, NAP consistency, service details, reviews, directions, hours, and GBP alignment.
- [ ] Documentation: docs pages answer task intent quickly, include prerequisites, steps, examples, troubleshooting, versioning, and related docs.
- [ ] Blog/content: articles have a clear topic role, useful intro, original angle, supporting examples, cluster links, and update plan.

## 20. Content Refresh Workflow

Evidence sources: `GSC`, `GA4`, `Firecrawl`, `CMS/code`, `Human/context`, `Manual/free SERP`.

- [ ] Pull current queries and top pages from GSC.
- [ ] Pull organic landing page engagement and conversions from GA4.
- [ ] Crawl the page for current title, headings, copy, links, schema, media, and indexability.
- [ ] Compare the page against current SERP intent and result formats.
- [ ] Identify content gaps, factual issues, stale assets, weak links, and conversion gaps.
- [ ] Update only what improves usefulness, trust, or business fit.
- [ ] Validate rendered content, schema, links, and metadata after publishing.
- [ ] Monitor GSC and GA4 after the refresh.

## 21. Output Template

Evidence sources: cite the specific tools used, such as `Firecrawl`, `Playwright`, `GSC`, `GA4`, `GKP`, `GMC`, `GBP`, `GMAPS`, `CMS/code`, `OSS`, `Manual/free SERP`, or `Human/context`.

```text
Summary:

Primary intent:

Audience and buyer stage:

Content score:

Priority issues:
1. [severity] [area]
   Evidence:
   Impact:
   Fix:
   Owner:
   Confidence:

Quick edits:

Substantive rewrite needs:

Internal link opportunities:

Source/citation needs:

Schema/search appearance needs:

Conversion improvements:

Refresh date and next review:

Sources used:
```

## 22. Minimal Audit Flow

1. Confirm page purpose, audience, and primary intent.
2. Pull GSC queries, GA4 performance, and keyword variants.
3. Crawl and render the page.
4. Compare the page to the current SERP and competitor formats.
5. Check usefulness, originality, evidence, structure, trust, media, links, schema, and conversion fit.
6. Score issues by severity.
7. Recommend the smallest edit that fixes the real gap.
8. Validate the published page and monitor results.
