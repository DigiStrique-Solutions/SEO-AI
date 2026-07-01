# AI SEO, AEO, And GEO Checklist

Updated: 2026-06-29

Use this checklist when auditing or planning visibility in AI search and answer experiences, including Google AI Overviews and AI Mode, ChatGPT Search, Perplexity, Claude search/browsing, Gemini, Microsoft Copilot, and other answer engines. Treat AI SEO, AEO, and GEO as an extension of SEO, content quality, entity trust, and off-page reputation. Do not create AI-only pages that are worse for users.

## Research Basis

Primary and reputable sources used:

- [Google AI optimization guide](https://developers.google.com/search/docs/fundamentals/ai-optimization-guide)
- [Google AI features and your website](https://developers.google.com/search/docs/appearance/ai-features)
- [Google Search Essentials](https://developers.google.com/search/docs/essentials)
- [Google helpful, reliable, people-first content guidance](https://developers.google.com/search/docs/fundamentals/creating-helpful-content)
- [Google spam policies](https://developers.google.com/search/docs/essentials/spam-policies)
- [Google robots meta and X-Robots-Tag guidance](https://developers.google.com/search/docs/crawling-indexing/robots-meta-tag)
- [Google snippet controls guidance](https://developers.google.com/search/docs/appearance/snippet)
- [Google structured data introduction](https://developers.google.com/search/docs/appearance/structured-data/intro-structured-data)
- [Google JavaScript SEO basics](https://developers.google.com/search/docs/crawling-indexing/javascript/javascript-seo-basics)
- [Google common crawlers and Google-Extended guidance](https://developers.google.com/crawling/docs/crawlers-fetchers/google-common-crawlers)
- [Google crawler verification guidance](https://developers.google.com/crawling/docs/crawlers-fetchers/verify-google-requests)
- [OpenAI crawler documentation](https://developers.openai.com/api/docs/bots)
- [Perplexity crawler documentation](https://docs.perplexity.ai/docs/resources/perplexity-crawlers)
- [Anthropic crawler documentation](https://support.claude.com/en/articles/8896518-does-anthropic-crawl-data-from-the-web-and-how-can-site-owners-block-the-crawler)
- [Microsoft Copilot Studio public website grounding guidance](https://learn.microsoft.com/en-us/microsoft-copilot-studio/guidance/generative-ai-public-websites)
- [Bing Webmaster Tools AI Performance announcement](https://blogs.bing.com/webmaster/February-2026/Introducing-AI-Performance-in-Bing-Webmaster-Tools-Public-Preview)
- [GEO: Generative Engine Optimization, arXiv](https://arxiv.org/abs/2311.09735)
- [Google Search Quality Rater Guidelines](https://static.googleusercontent.com/media/guidelines.raterhub.com/en//searchqualityevaluatorguidelines.pdf)

## Source Notes

- Google says normal SEO best practices still apply to generative AI features in Google Search.
- Google says no special AI markup, AI text file, Markdown file, or `llms.txt` file is required for Google AI Overviews or AI Mode.
- Google AI features use normal Search preview controls such as `nosnippet`, `max-snippet`, `max-image-preview`, `max-video-preview`, and `data-nosnippet`.
- `Google-Extended` is not a control for Google AI Overviews or AI Mode.
- OpenAI, Perplexity, Anthropic, Bing, and other AI/search systems have separate crawler, search, user-fetch, and training behavior. Do not assume one robots rule controls all AI surfaces.
- The GEO paper supports tactics such as citations, quotations, statistics, clarity, and fluency, but it is not a universal ranking formula. Treat it as research evidence, not a magic checklist.

## Evidence Source Legend

Use free, owned, or open-source sources first.

Google-visible scope: judge pass/fail from public rendered content, crawlability, preview controls, robots/sitemaps, GSC outcome data, and performance evidence. CMS/code, GA4/PostHog, logs, governance, and editorial workflow are optional unless the item is explicitly about external visibility, AI answer captures, crawler access logs, or off-page reputation.

- `Manual AI SERP`: manual checks in Google AI Overviews/AI Mode, ChatGPT, Perplexity, Claude, Gemini, Copilot, and other answer engines.
- `Prompt set`: saved prompts, query variants, location, date, platform, account state, and captured answers/citations.
- `GSC`: Google Search Console performance, indexing, sitemaps, URL Inspection, search appearance, Crawl Stats.
- `BWT`: Bing Webmaster Tools performance, AI Performance, backlinks, crawl and index data.
- `GA4`: referral traffic, conversion quality, landing page engagement, AI referral sources where visible.
- `Firecrawl`: rendered extraction, markdown extraction, page text, metadata, links, schema, screenshots, crawl samples.
- `Playwright`: precise rendered DOM checks, screenshots, mobile rendering, accessibility tree, interactive flows, hidden content.
- `CMS/code`: templates, structured data, robots.txt, headers, content fields, feeds, docs, pricing, product data, changelogs.
- `Logs/CDN/WAF`: crawler access, blocked requests, status codes, bot verification, rate limits, cache and firewall events.
- `GBP`: Google Business Profile for local entity data, categories, services, reviews, photos, Q&A.
- `GMC`: Google Merchant Center for products, prices, availability, shipping, returns, and merchant listing context.
- `Off-page`: reviews, PR, citations, directories, app stores, marketplaces, social profiles, Wikipedia/Wikidata where legitimate.
- `OSS`: schema validators, link checkers, HTML validators, accessibility tooling, robots parsers, markdown linters.
- `Human/context`: product facts, expert review, legal/compliance, customer research, sales objections, editorial judgment.

## Scoring

- `critical`: AI systems cannot access important public content, content is misleading or unsafe, spam/manual-action risk exists, or prompt injection/recommendation poisoning is present.
- `high`: content is indexable but not answerable, lacks evidence, has weak entity trust, is absent from key third-party sources, or is blocked by crawler/WAF policy.
- `medium`: content is useful but hard to extract, stale, under-cited, weakly structured, or poorly measured.
- `low`: formatting, monitoring, attribution, disclosure, or minor clarity improvements.
- `not_applicable`: platform or page type does not apply.

Issue record:

```text
Severity:
Area:
Evidence source:
Affected prompt, query, URL, crawler, or profile:
Issue:
Why it matters:
Recommended fix:
Owner:
Confidence:
```

## 1. Scope And Platform Targets

Evidence sources: `Human/context`, `Manual AI SERP`, `Prompt set`, `GSC`, `BWT`, `GA4`.

- [ ] The target experience is defined: Google AI Overviews, Google AI Mode, ChatGPT Search, Perplexity, Claude, Gemini, Copilot, vertical AI search, or agentic browsing.
- [ ] The business goal is defined: citations, brand mentions, product recommendations, local visibility, referral traffic, lead quality, ecommerce sales, support deflection, or reputation.
- [ ] Priority query set is defined by topic, buyer stage, platform, location, and language.
- [ ] Query types are grouped: definition, how-to, comparison, best-of, troubleshooting, local, product, pricing, review, alternative, and branded.
- [ ] Competitors currently cited or recommended by AI systems are recorded.
- [ ] The site type and business model are identified: ecommerce, lead gen, app installs, local, SaaS, publisher, docs, marketplace, or hybrid.
- [ ] YMYL exposure is identified before recommendations are made.

## 2. Baseline AI Visibility Measurement

Evidence sources: `Manual AI SERP`, `Prompt set`, `BWT`, `GSC`, `GA4`, `Off-page`.

- [ ] A repeatable prompt set exists for priority topics and buyer stages.
- [ ] Each prompt run records platform, date, location, language, account state, device, prompt wording, answer summary, cited URLs, mentioned brands, and sentiment.
- [ ] The audit records whether the brand is cited, mentioned without citation, omitted, or described inaccurately.
- [ ] Competitor citation frequency and cited source types are tracked.
- [ ] Cited page types are classified: brand page, third-party review, directory, documentation, news, forum, video, marketplace, app store, local profile, or research source.
- [ ] Google AI results are compared with normal Google organic visibility.
- [ ] Bing Webmaster Tools AI Performance is checked where available.
- [ ] GA4 referral traffic from AI/search assistants is monitored where identifiable.
- [ ] Logs are reviewed for AI/search crawler activity when crawler access matters.

## 3. Foundational SEO Readiness

Evidence sources: `GSC`, `BWT`, `Firecrawl`, `Playwright`, `CMS/code`, `Logs/CDN/WAF`, `OSS`.

- [ ] Priority pages are crawlable, indexable, canonical, and included in relevant sitemaps.
- [ ] Important content renders in HTML and is visible without fragile client-only behavior.
- [ ] Pages return stable 200 responses and do not intermittently fail with 4xx, 5xx, 429, timeout, DNS, TLS, or WAF errors.
- [ ] Mobile and desktop render equivalent primary content.
- [ ] Titles, meta descriptions, headings, canonicals, robots directives, hreflang, and structured data are available after rendering.
- [ ] Page experience problems do not block users or agents from consuming the content.
- [ ] Content satisfies Search Essentials and helpful content guidance before any AI-specific optimization.

## 4. AI Feature Controls And Preview Policy

Evidence sources: `GSC`, `Firecrawl`, `Playwright`, `CMS/code`, `OSS`, `Human/context`.

- [ ] `nosnippet`, `max-snippet`, `max-image-preview`, `max-video-preview`, and `data-nosnippet` settings are intentional.
- [ ] Snippet controls are reviewed for their impact on normal Google snippets and Google AI features.
- [ ] `Google-Extended` is not treated as an opt-out for Google AI Overviews or AI Mode.
- [ ] Sensitive content that should not appear in search snippets is handled with preview controls, access control, or publishing policy.
- [ ] Content that should not be indexed uses `noindex` or access control rather than relying on AI crawler blocks alone.
- [ ] Paywalled, gated, or member content has an explicit policy for what is public, indexable, and citable.

## 5. AI Crawler Access And Robots Policy

Evidence sources: `CMS/code`, `Logs/CDN/WAF`, `Firecrawl`, `Playwright`, `OSS`, `Human/context`.

- [ ] Robots.txt is reviewed for Googlebot, Bingbot, OAI-SearchBot, GPTBot, ChatGPT-User, PerplexityBot, ClaudeBot, Claude-SearchBot, Claude-User, and other relevant agents.
- [ ] Crawler roles are separated where the provider supports it: search/indexing, training, and user-triggered fetches.
- [ ] The business decision to allow or block AI training crawlers is documented separately from the decision to allow AI search or citation crawlers.
- [ ] WAF, CDN, bot protection, rate limits, geo blocks, and JavaScript challenges do not accidentally block required search or AI crawlers.
- [ ] Crawler verification uses official IP ranges, reverse DNS, provider docs, or verified bot tooling where available.
- [ ] Logs are sampled for blocked, throttled, redirected, or challenged AI/search crawler requests.
- [ ] Blocking a crawler is documented with expected visibility tradeoffs.

## 6. Answerability And Extractable Content

Evidence sources: `Firecrawl`, `Playwright`, `Manual AI SERP`, `Prompt set`, `Human/context`.

- [ ] Each priority page gives a direct answer to its main question early.
- [ ] Definitions, steps, comparisons, recommendations, constraints, and examples are self-contained enough to quote accurately.
- [ ] Important sections start with the answer, then provide context and proof.
- [ ] Headings match real user questions and tasks without becoming keyword spam.
- [ ] Comparison content uses tables or clearly labeled criteria where useful.
- [ ] Procedural content uses ordered steps where useful.
- [ ] Product or service pages expose concrete facts: use cases, pricing, limits, integrations, requirements, availability, support, and alternatives where relevant.
- [ ] Pages avoid vague marketing copy that cannot be cited or summarized.
- [ ] Content is not chopped into unnatural AI-bait fragments.

## 7. Evidence, Citations, And Originality

Evidence sources: `Firecrawl`, `Playwright`, `Manual AI SERP`, `Human/context`, `CMS/code`, `Off-page`.

- [ ] Important claims are supported by primary sources, product data, screenshots, examples, customer evidence, research, or expert review.
- [ ] Statistics include source, date, unit, and context.
- [ ] Original research, benchmarks, surveys, public data analysis, product data, or methodology are included where the brand can add real information gain.
- [ ] Expert quotes include name, role, organization, and relevant credentials.
- [ ] Recommendations explain tradeoffs, not only conclusions.
- [ ] Content distinguishes facts, assumptions, opinions, and product claims.
- [ ] Pages avoid unsupported superlatives such as "best", "number one", and "guaranteed".
- [ ] AI-assisted drafts are fact checked and edited by a human with topical knowledge.

## 8. Entity, Brand, And Knowledge Graph Consistency

Evidence sources: `GSC`, `Manual AI SERP`, `Off-page`, `CMS/code`, `GBP`, `GMC`, `Human/context`.

- [ ] Brand name, product names, organization details, founders, authors, locations, categories, and social profiles are consistent.
- [ ] Organization, WebSite, Person, Product, LocalBusiness, Article, BreadcrumbList, and other relevant structured data match visible content.
- [ ] `sameAs` and profile links point to real, maintained official profiles.
- [ ] Brand and product descriptions are consistent across website, GBP, app stores, marketplaces, review sites, directories, social profiles, and press bios.
- [ ] Author and expert entities have credible bios and external corroboration where topical trust matters.
- [ ] Local entities align across website, GBP, Maps, reviews, citations, and local pages.
- [ ] Product entities align across website, Product schema, Merchant Center, marketplaces, reviews, and comparison pages.

## 9. Topical Coverage And Query Fan-Out

Evidence sources: `GSC`, `BWT`, `GKP`, `Manual AI SERP`, `Prompt set`, `Firecrawl`, `Human/context`.

- [ ] Priority topics are mapped to parent questions, follow-up questions, comparisons, objections, constraints, and adjacent tasks.
- [ ] Query fan-out variants are covered by the page or by linked supporting pages.
- [ ] Topic clusters connect definitions, how-to content, comparisons, product pages, case studies, reviews, docs, and conversion pages.
- [ ] Content gaps are identified from AI answers that cite competitors but omit the brand.
- [ ] Searcher intent is not split across too many thin pages.
- [ ] The site avoids creating many near-duplicate pages for tiny prompt variants.
- [ ] Important answers are reachable through internal links, hubs, navigation, and sitemaps.

## 10. Third-Party Presence And Corroboration

Evidence sources: `Manual AI SERP`, `Off-page`, `GA4`, `GSC`, `GBP`, `GMAPS`, `Human/context`.

- [ ] AI systems cite or mention the brand from credible third-party sources where relevant.
- [ ] Review platforms, marketplaces, app stores, directories, partner pages, industry publications, podcasts, communities, and local citations are accurate.
- [ ] Third-party descriptions match the brand's actual category, use cases, pricing, locations, and audience.
- [ ] Review and rating strategies follow platform policies and advertising law.
- [ ] Reddit, Wikipedia, Quora, forums, and communities are not spammed or manipulated for AI visibility.
- [ ] Digital PR and earned media target sources AI systems are likely to trust and users are likely to value.
- [ ] Unlinked brand mentions are reviewed for accuracy and possible attribution only when useful.

## 11. Structured Data, Feeds, And Machine-Readable Context

Evidence sources: `CMS/code`, `Firecrawl`, `Playwright`, `GSC`, `GMC`, `GBP`, `OSS`.

- [ ] Structured data is valid, accurate, and visible-content aligned.
- [ ] Standard schema is used where appropriate: Organization, WebSite, Person, Article, Product, Offer, Review, LocalBusiness, FAQPage, HowTo, VideoObject, SoftwareApplication, BreadcrumbList.
- [ ] Schema does not invent facts, ratings, reviews, prices, FAQs, authors, or business details.
- [ ] Merchant Center feeds are current for ecommerce products.
- [ ] Google Business Profile data is current for local businesses.
- [ ] App store, marketplace, integration, and product directory data are current where those surfaces matter.
- [ ] Optional files such as `llms.txt`, `pricing.md`, `products.md`, docs indexes, or changelog feeds are treated as experimental convenience for non-Google systems and agents, not a Google requirement.
- [ ] Optional machine-readable files are public, accurate, maintained, linked from relevant pages, and consistent with visible page content.

## 12. Agentic Browsing And Accessibility Readiness

Evidence sources: `Playwright`, `Firecrawl`, `CMS/code`, `OSS`, `Human/context`.

- [ ] Important pages work for a browser agent that renders, clicks, reads the DOM, and uses the accessibility tree.
- [ ] Semantic HTML is used for landmarks, headings, buttons, links, lists, tables, forms, and navigation.
- [ ] Interactive controls have accessible names and predictable behavior.
- [ ] Pricing, contact, product specs, shipping, returns, limits, requirements, and support details are visible when needed for evaluation.
- [ ] Key information is not locked behind login, popups, heavy JavaScript, broken accordions, images of text, or PDFs only.
- [ ] Tables use real table markup for comparisons and specs.
- [ ] Forms and conversion flows are usable by keyboard and screen-reader style navigation.
- [ ] Agent-facing shortcuts do not replace normal user-facing usability.

## 13. Platform-Specific Checks

Evidence sources: `Manual AI SERP`, `Prompt set`, `GSC`, `BWT`, `GA4`, `Logs/CDN/WAF`, provider crawler docs.

- [ ] Google AI: page follows normal SEO, helpful content, crawlability, preview controls, structured data, and spam policies.
- [ ] Google AI: no special AI markup or `llms.txt` is required or treated as a ranking shortcut.
- [ ] ChatGPT/OpenAI: OAI-SearchBot and GPTBot access policy is intentional; ChatGPT-User behavior is understood as user-triggered fetching.
- [ ] Perplexity: PerplexityBot access policy is intentional if Perplexity visibility matters.
- [ ] Anthropic/Claude: ClaudeBot, Claude-SearchBot, and Claude-User policies are reviewed separately where relevant.
- [ ] Microsoft Copilot/Bing: Bing indexability and Bing Webmaster Tools AI Performance are checked where available.
- [ ] Gemini: Google Search and entity data quality are treated as the foundation.
- [ ] Vertical assistants or marketplaces: platform profile, feed, review, and product data requirements are checked.

## 14. Measurement And Monitoring

Evidence sources: `Prompt set`, `Manual AI SERP`, `BWT`, `GSC`, `GA4`, `Logs/CDN/WAF`, `Alerts/free monitoring`, `Human/context`.

- [ ] Prompt checks are repeated on a defined cadence.
- [ ] Results capture citations, mentions, sentiment, source URLs, answer accuracy, and competitor visibility.
- [ ] Bing Webmaster Tools AI Performance is monitored where available.
- [ ] GSC is used for Google Search performance, with the understanding that Google does not provide a separate AI Overview report in GSC.
- [ ] GA4 tracks identifiable AI referral sources and assisted conversions where possible.
- [ ] Logs monitor AI/search crawler access and blocked requests.
- [ ] Brand, product, founder, expert, and key topic alerts are configured.
- [ ] AI visibility metrics are tied to business outcomes, not only citation counts.
- [ ] Screenshots or saved answer exports are kept for volatile AI results.

## 15. Risk, Spam, And Safety Checks

Evidence sources: `GSC`, `Manual AI SERP`, `Firecrawl`, `Playwright`, `CMS/code`, `Human/context`, `Off-page`.

- [ ] No scaled AI-generated content exists without real review, usefulness, and differentiation.
- [ ] No prompt injection, hidden instructions, cloaked AI text, or recommendation poisoning is present.
- [ ] No fake citations, fake experts, fake reviews, fake awards, or fabricated statistics are used.
- [ ] No content is created only to manipulate AI answers while harming users.
- [ ] User-generated content is moderated where it can affect brand trust or safety.
- [ ] YMYL topics have stronger expert review, source quality, safety language, and accountability.
- [ ] AI answers that misstate the brand are documented and corrected through source updates, third-party corrections, and better on-site clarity.
- [ ] Legal, privacy, copyright, and platform policy risks are reviewed for crawler access, AI reuse, endorsements, reviews, and claims.

## 16. Context-Specific Checks

Evidence sources: use relevant connectors plus common sources above.

- [ ] Ecommerce: product pages, Merchant Center, reviews, pricing, availability, shipping, returns, variants, comparison content, and marketplace profiles are consistent and extractable.
- [ ] Lead gen: service pages, comparison pages, case studies, testimonials, review sites, local/service citations, and lead magnets answer buyer objections clearly.
- [ ] App installs: app store listings, app schema, screenshots, permissions, privacy, pricing, platform pages, reviews, docs, and onboarding details are accurate.
- [ ] Local: GBP, Maps, reviews, NAP, services, locations, hours, directions, photos, local citations, and local pages are aligned.
- [ ] SaaS: pricing, integrations, security, docs, changelog, case studies, alternatives, reviews, and partner directories are accessible and current.
- [ ] Docs/support: troubleshooting, prerequisites, versioning, examples, API references, changelogs, and support paths are direct and extractable.

## 17. Anti-Patterns

- [ ] Writing separate worse content "for AI".
- [ ] Creating thin prompt-variant pages.
- [ ] Treating `llms.txt` as required for Google AI features.
- [ ] Treating `Google-Extended` as an AI Overviews opt-out.
- [ ] Blocking all AI/search crawlers without understanding visibility tradeoffs.
- [ ] Hiding the answer behind vague marketing copy.
- [ ] Gating all useful evidence.
- [ ] Using unsupported statistics or fake citations.
- [ ] Spamming Reddit, Wikipedia, Quora, review sites, or forums.
- [ ] Stuffing schema with invisible or false content.
- [ ] Measuring only rankings when AI answers absorb the click.
- [ ] Optimizing for citation while ignoring conversion quality.

## 18. Output Template

Evidence sources: cite the specific sources used, such as `Manual AI SERP`, `Prompt set`, `GSC`, `BWT`, `GA4`, `Firecrawl`, `Playwright`, `CMS/code`, `Logs/CDN/WAF`, `GBP`, `GMC`, `Off-page`, `OSS`, or `Human/context`.

```text
Summary:

Target platforms:

Priority prompts:

Current AI visibility:

Competitors cited:

Priority issues:
1. [severity] [area]
   Evidence:
   Impact:
   Fix:
   Owner:
   Confidence:

Crawler and robots decisions:

Content improvements:

Entity and third-party improvements:

Measurement plan:

Risks:

Sources used:
```

## 19. Minimal Audit Flow

1. Define target platforms, query set, business goal, and site type.
2. Run prompt checks and capture cited sources, competitors, answer accuracy, and sentiment.
3. Verify crawlability, indexability, rendering, robots policy, preview controls, and crawler access.
4. Audit answerability, evidence, originality, structure, schema, and entity consistency.
5. Check third-party corroboration, reviews, profiles, citations, feeds, and marketplaces.
6. Separate Google requirements from non-Google AI/search engine tactics.
7. Prioritize fixes by visibility impact, trust risk, and business value.
8. Set monitoring cadence for prompts, crawler access, referrals, BWT AI Performance, GSC, and conversions.
