# Off-Page SEO Checklist

Updated: 2026-06-29

Use this checklist when auditing or planning external visibility signals: backlinks, digital PR, brand mentions, reputation, reviews, local citations, partnerships, affiliates, creator campaigns, and link spam risk. This checklist should not turn into a paid-link workflow. The goal is durable visibility and trust.

## Research Basis

Primary and reputable sources used:

- [Google Search Essentials](https://developers.google.com/search/docs/essentials)
- [Google Search spam policies](https://developers.google.com/search/docs/essentials/spam-policies)
- [Google link spam policy](https://developers.google.com/search/docs/essentials/spam-policies#link-spam)
- [Google qualify outbound links guidance](https://developers.google.com/search/docs/crawling-indexing/qualify-outbound-links)
- [Google Search Console Links report](https://support.google.com/webmasters/answer/9049606)
- [Google Manual actions report](https://support.google.com/webmasters/answer/9044175)
- [Google Disavow links guidance](https://support.google.com/webmasters/answer/2648487)
- [Google creating helpful, reliable, people-first content](https://developers.google.com/search/docs/fundamentals/creating-helpful-content)
- [Google Search Quality Rater Guidelines](https://static.googleusercontent.com/media/guidelines.raterhub.com/en//searchqualityevaluatorguidelines.pdf)
- [Google local ranking guidance](https://support.google.com/business/answer/7091)
- [Google review removal guidance](https://support.google.com/business/answer/4596773)
- [Google Business Profile guidelines](https://support.google.com/business/answer/3038177)
- [FTC endorsement guides, Federal Register](https://www.federalregister.gov/documents/2023/07/26/2023-14795/guides-concerning-the-use-of-endorsements-and-testimonials-in-advertising)
- [FTC consumer reviews and testimonials rule, Federal Register](https://www.federalregister.gov/documents/2024/08/22/2024-18519/trade-regulation-rule-on-the-use-of-consumer-reviews-and-testimonials)

## Evidence Source Legend

Use free, owned, or open-source sources first.

- `GSC`: Search Console Links report, Manual Actions, Security Issues, performance by landing page, branded queries.
- `GA4`: referral traffic, assisted conversions, landing page conversion, campaign traffic quality.
- `GBP`: Google Business Profile reviews, categories, photos, products, services, posts, Q&A, profile performance.
- `GMAPS`: Maps/Places competitors, category coverage, local results visibility, citations, review patterns.
- `BWT`: Bing Webmaster Tools backlinks, impressions, clicks, crawl and search visibility where available.
- `Firecrawl`: crawl public linking pages, partner pages, directory pages, citation pages, review pages, and brand mention pages.
- `Playwright`: render public linking pages, verify visible attribution, sponsored disclosure, link attributes, and review widgets.
- `CMS/code`: outbound link attributes, affiliate/sponsored pages, press pages, case studies, testimonials, partner pages, schema, redirect targets.
- `Manual/free SERP`: brand SERPs, search operators, Google News, normal web results, local results blocks, review surfaces, industry directories.
- `Alerts/free monitoring`: Google Alerts, Talkwalker Alerts, RSS, social search, community monitoring, referral log alerts.
- `CRM/sales`: customer logos, partner relationships, integrations, resellers, affiliates, events, awards, testimonials.
- `Human/context`: PR judgment, legal/compliance review, brand policy, partnership intent, subject-matter expert review.

## Scoring

- `critical`: manual action, hacked/spam association, fake reviews, undisclosed paid endorsement risk, or large manipulative link pattern.
- `high`: major authority gap, important brand reputation issue, harmful citation/review inconsistency, or risky link acquisition.
- `medium`: missed mention/link opportunities, weak local prominence, poor referral quality, weak partner attribution, or low-quality directories.
- `low`: cleanup, monitoring, reporting, disclosure polish, or minor citation updates.
- `not_applicable`: page, site, or business type does not use this off-page surface.

Issue record:

```text
Severity:
Area:
Evidence source:
Affected domain, URL, profile, or campaign:
Issue:
Why it matters:
Recommended fix:
Owner:
Confidence:
```

## 1. Scope And Risk Posture

Evidence sources: `Human/context`, `GSC`, `GA4`, `GBP`, `CRM/sales`, `Manual/free SERP`.

- [ ] The off-page audit scope is defined: full domain, new site, migration, local visibility, reputation cleanup, PR campaign, affiliate program, partnership program, review program, or link-risk audit.
- [ ] Business type is identified: SaaS, ecommerce, local service, marketplace, app, publisher, healthcare, finance, legal, education, nonprofit, or enterprise.
- [ ] Risk level is set before recommendations: conservative, standard, or aggressive.
- [ ] YMYL exposure is identified and requires stronger trust, reputation, and compliance review.
- [ ] Past SEO work is reviewed for paid links, link exchanges, guest post networks, expired domains, PBNs, widgets, scholarships, coupons, or mass directory submissions.
- [ ] Manual actions, security issues, and major traffic drops are checked before link building recommendations.
- [ ] The goal is clear: authority, referral traffic, local prominence, brand trust, partnerships, PR reach, review growth, or recovery.

## 2. Baseline Off-Page Inventory

Evidence sources: `GSC`, `BWT`, `GA4`, `GBP`, `GMAPS`, `Manual/free SERP`, `Alerts/free monitoring`, `Firecrawl`.

- [ ] Export external links from GSC Links report.
- [ ] Export backlink data from Bing Webmaster Tools if available.
- [ ] Pull GA4 referral traffic and conversions by source, medium, landing page, and campaign.
- [ ] Pull branded query trends from GSC.
- [ ] Pull local profile, review, and performance data from GBP where relevant.
- [ ] Capture top brand SERPs for brand, product, founder, local, and review queries.
- [ ] Capture key non-linked brand mentions from free search and alerts.
- [ ] Group external visibility by source type: editorial, directory, local citation, partner, affiliate, sponsorship, PR, review, forum/community, social, app marketplace, marketplace listing, or spam.
- [ ] Record which sources drive qualified traffic or conversions, not only links.

## 3. Backlink Quality And Relevance

Evidence sources: `GSC`, `BWT`, `GA4`, `Firecrawl`, `Playwright`, `Manual/free SERP`.

- [ ] Important backlinks come from topically relevant, trustworthy, crawlable pages.
- [ ] Linking pages have visible editorial context, not only footer, sidebar, profile, comment, or generated-list links.
- [ ] Linking pages are indexed or plausibly indexable when checked manually.
- [ ] Link placements make sense for users.
- [ ] The linked destination matches the context of the mention.
- [ ] Important links point to live, canonical, indexable URLs.
- [ ] Redirected backlink targets are reviewed after migrations or URL changes.
- [ ] High-value links are not wasted on deleted pages, campaign URLs, tracking URLs, or non-canonical variants.
- [ ] Referral traffic quality is checked before treating a link source as valuable.
- [ ] Links from irrelevant, spammy, hacked, scraped, adult, gambling, malware, or auto-generated pages are flagged for risk review.

## 4. Link Profile Pattern Review

Evidence sources: `GSC`, `BWT`, `Manual/free SERP`, `Firecrawl`, `Human/context`.

- [ ] Anchor text profile is reviewed for unnatural exact-match concentration.
- [ ] Linking domain growth is reviewed for sudden spikes that match campaigns, spam attacks, migrations, or negative SEO concerns.
- [ ] Sitewide links are reviewed separately from editorial links.
- [ ] Repeated links from the same templates or network are grouped as one pattern.
- [ ] Links from obvious paid guest post networks, PBNs, expired domain networks, or link farms are flagged.
- [ ] Foreign-language links are reviewed for relevance instead of automatically treated as bad.
- [ ] Scraper links, image hotlinks, and low-value auto-generated links are usually ignored unless they are part of a larger manipulative pattern.
- [ ] Competitor link overlap is reviewed for legitimate opportunities, not copied link spam.

## 5. Link Acquisition Compliance

Evidence sources: `Human/context`, `CRM/sales`, `CMS/code`, `Firecrawl`, `Playwright`, `Manual/free SERP`.

- [ ] Link acquisition is based on real value: useful content, original data, tools, partnerships, events, products, expertise, or news.
- [ ] Paid links do not pass PageRank.
- [ ] Sponsored links use `rel="sponsored"` or `rel="nofollow sponsored"` where appropriate.
- [ ] User-generated links use `rel="ugc"` or `rel="nofollow ugc"` where appropriate.
- [ ] Affiliate links use `rel="sponsored"` or equivalent nofollow treatment.
- [ ] Product reviews, samples, creator campaigns, and sponsorships disclose material connections.
- [ ] Guest posts are editorially justified and not mass-produced only for anchor text.
- [ ] Link exchanges are not used as a ranking manipulation tactic.
- [ ] Private blog networks, expired-domain link schemes, automated outreach spam, and paid insertion schemes are prohibited.
- [ ] Campaign briefs prohibit exact-match anchor manipulation.

## 6. Digital PR And Earned Media

Evidence sources: `Manual/free SERP`, `Alerts/free monitoring`, `GA4`, `GSC`, `Firecrawl`, `CRM/sales`, `Human/context`.

- [ ] PR angles are based on real news, original data, expert commentary, product launches, research, events, community work, or useful resources.
- [ ] Target publications match audience, geography, industry, and topical relevance.
- [ ] Outreach is personalized and useful, not bulk spam.
- [ ] Earned coverage is tracked by publication, URL, date, link status, anchor, landing page, referral traffic, conversions, and brand sentiment.
- [ ] Unlinked brand mentions are reviewed for polite attribution requests only when a link would help users.
- [ ] Press pages, newsroom pages, media kits, and expert bios make journalist verification easy.
- [ ] Coverage quality is valued over raw link count.
- [ ] PR wins are connected back to relevant on-site pages, case studies, assets, or conversion paths.

## 7. Brand Mentions And Entity Reputation

Evidence sources: `Manual/free SERP`, `Alerts/free monitoring`, `GSC`, `GA4`, `Firecrawl`, `Human/context`.

- [ ] Brand, product, founder, executive, and key expert names are monitored.
- [ ] Brand SERPs show accurate owned profiles, reviews, knowledge panels, social profiles, app listings, marketplace pages, and press results.
- [ ] Negative or inaccurate results are triaged by accuracy, risk, visibility, and owner.
- [ ] Reputable third-party descriptions of the brand are consistent with the preferred positioning.
- [ ] Important mentions use the correct brand name, product name, URL, location, and category.
- [ ] Entity signals are consistent across website, Organization schema, social profiles, Google Business Profile, directories, app stores, marketplaces, and press bios.
- [ ] Reputation for YMYL sites is checked against independent expert sources, not only company-owned content.

## 8. Local Citations And NAP Consistency

Use for local businesses, franchises, marketplaces with physical locations, healthcare, legal, home services, restaurants, retail, and multi-location brands.

Evidence sources: `GBP`, `GMAPS`, `Manual/free SERP`, `Firecrawl`, `Playwright`, `CRM/sales`, `Human/context`.

- [ ] Name, address, phone, website, hours, categories, service areas, and appointment URLs are consistent across major profiles.
- [ ] Google Business Profile primary and secondary categories match real services.
- [ ] Location pages match GBP and Maps data.
- [ ] Duplicate or outdated location listings are flagged.
- [ ] Closed, moved, merged, or rebranded locations have a cleanup plan.
- [ ] Important industry citations are present and accurate.
- [ ] Low-quality directory submissions are not recommended only to inflate citation count.
- [ ] Local landing pages, GBP, Maps, and citations agree on NAP and service details.
- [ ] Multi-location brands have a process for updating citations after moves, phone changes, hours changes, or rebrands.

## 9. Reviews And Ratings

Evidence sources: `GBP`, `GMAPS`, `Manual/free SERP`, `GA4`, `CRM/sales`, `Human/context`.

- [ ] Review strategy follows platform policies and applicable advertising law.
- [ ] Reviews are requested from real customers without incentives, pressure, gating, or scripts that distort sentiment.
- [ ] Employees, vendors, agencies, and owners do not post fake customer reviews.
- [ ] Review requests do not ask customers to mention specific employees, keywords, locations, or services in a manipulative way.
- [ ] Review response process exists for positive, neutral, negative, and policy-violating reviews.
- [ ] Policy-violating reviews are flagged through the proper platform process.
- [ ] Review themes are analyzed for product, service, local, trust, and content improvement opportunities.
- [ ] Review snippets, testimonials, and ratings shown on-site are authentic and not cherry-picked in a misleading way.
- [ ] FTC disclosure and endorsement requirements are reviewed for testimonials, influencers, affiliates, and creator campaigns.

## 10. Directories, Listings, Marketplaces, And App Stores

Evidence sources: `Manual/free SERP`, `GA4`, `GSC`, `Firecrawl`, `Playwright`, `CRM/sales`, `Human/context`.

- [ ] Listings are prioritized by audience relevance, trust, and referral value.
- [ ] Profile descriptions are accurate and not stuffed with keywords.
- [ ] Categories, industries, locations, features, screenshots, prices, and contact details are accurate.
- [ ] Marketplace and app store listings link to the best relevant website page.
- [ ] UTM usage is consistent where allowed.
- [ ] Duplicate, abandoned, or inaccurate profiles are cleaned up.
- [ ] Pay-to-play directories are evaluated for real audience value and disclosure risk.
- [ ] Review solicitation on third-party marketplaces follows each platform's rules.

## 11. Partnerships, Affiliates, Sponsorships, And Creators

Evidence sources: `CRM/sales`, `CMS/code`, `GA4`, `Firecrawl`, `Playwright`, `Human/context`.

- [ ] Partner pages and integration directories are accurate and mutually useful.
- [ ] Affiliate and creator links use appropriate sponsored or nofollow treatment where required.
- [ ] Sponsored placements disclose the relationship.
- [ ] Partner claims, logos, badges, certifications, and awards are approved and current.
- [ ] Co-marketing pages link users to useful resources, not thin landing pages.
- [ ] Sponsorships are tracked by traffic, leads, brand lift, and real audience fit, not link count.
- [ ] Expired partnerships and outdated logos are removed or updated.
- [ ] Widgets, badges, embeds, and templates do not force keyword-rich followed links.

## 12. Competitor And Market Link Intelligence

Evidence sources: `Manual/free SERP`, `GSC`, `BWT`, `Firecrawl`, `GA4`, `Human/context`.

- [ ] Search competitors are identified by query set, not only business category.
- [ ] Competitor mentions, directories, partner pages, awards, podcasts, events, and editorial coverage are reviewed manually.
- [ ] Legitimate common sources are separated from spam networks.
- [ ] Competitor backlink gaps are translated into PR, partnership, content, or listing opportunities.
- [ ] Competitor anchor manipulation is not copied.
- [ ] Market authority sources are prioritized: associations, standards bodies, trusted publications, universities, government, communities, podcasts, events, and credible directories.

## 13. Toxic Link, Manual Action, And Disavow Handling

Evidence sources: `GSC`, `BWT`, `Manual/free SERP`, `Firecrawl`, `Human/context`.

- [ ] Search Console Manual Actions report is checked before recommending disavow work.
- [ ] Suspect links are grouped by pattern, source, intent, and acquisition history.
- [ ] Disavow is treated as a last-resort tool, not routine backlink hygiene.
- [ ] Disavow is considered only when there are many spammy, artificial, or low-quality links and they caused or are likely to cause a manual action.
- [ ] Link removal outreach is attempted for links the business created or controlled where practical.
- [ ] Disavow files are reviewed by a senior owner before upload.
- [ ] Negative SEO fears are not used to justify broad disavow files without evidence.
- [ ] Recovery plans include reconsideration request preparation when a manual action exists.

## 14. Social, Community, And Demand Signals

Evidence sources: `Manual/free SERP`, `GA4`, `Alerts/free monitoring`, `CRM/sales`, `Human/context`.

- [ ] Social and community work is evaluated for audience, referral quality, brand discovery, and journalist/creator visibility.
- [ ] Community participation is helpful and disclosed when affiliated with the brand.
- [ ] Social profiles use accurate URLs, names, bios, categories, and contact details.
- [ ] Reused social bios and brand descriptions stay consistent with website positioning.
- [ ] Viral or campaign spikes are checked for branded search lift, referral traffic, links, mentions, and conversions.
- [ ] Spammy forum drops, comment spam, fake accounts, and undisclosed promotion are prohibited.

## 15. Off-Page To On-Site Alignment

Evidence sources: `GSC`, `GA4`, `Firecrawl`, `CMS/code`, `Playwright`, `Human/context`.

- [ ] High-value external links point to pages that satisfy the visitor's intent.
- [ ] Campaign landing pages are indexable only when they should rank.
- [ ] Press, partner, review, and directory traffic has relevant next steps.
- [ ] Top externally linked pages are maintained, redirected carefully, or preserved during migrations.
- [ ] Brand claims made off-site are supported on the website.
- [ ] Partner and citation URLs do not point to outdated domains, HTTP URLs, tracking-only URLs, or dead pages.
- [ ] UTM parameters do not create indexable duplicate URLs.

## 16. Monitoring And Reporting

Evidence sources: `GSC`, `GA4`, `GBP`, `GMAPS`, `BWT`, `Alerts/free monitoring`, `Manual/free SERP`.

- [ ] Track GSC external links, top linked pages, top linking sites, and top linking text.
- [ ] Track GA4 referral sessions, engaged sessions, conversions, revenue or lead value, and assisted outcomes.
- [ ] Track branded queries, non-branded queries, and local visibility where relevant.
- [ ] Track review count, rating, review velocity, response rate, and major review themes.
- [ ] Track new earned media, unlinked mentions, citations, partnerships, and directory changes.
- [ ] Track manual actions, security issues, and major spam-risk changes.
- [ ] Track campaign outcomes by quality and business impact, not raw link count.
- [ ] Create alerts for brand, product, founders, key experts, and high-risk review platforms.

## 17. Context-Specific Checks

Evidence sources: use relevant connectors plus the common sources above.

- [ ] Ecommerce: reviews, product mentions, affiliate links, creator campaigns, marketplaces, shopping publications, return policy mentions, and Merchant Center consistency are reviewed.
- [ ] Lead gen: local citations, review platforms, case studies, partner pages, comparison mentions, directory listings, and referral quality are reviewed.
- [ ] App installs: app store listings, review surfaces, product directories, integration marketplaces, launch platforms, creators, and platform badges are reviewed.
- [ ] Local: GBP, Maps, citations, local press, community sponsorships, service-area mentions, reviews, and NAP consistency are reviewed.
- [ ] SaaS: integration directories, comparison pages, partner listings, review platforms, case studies, communities, podcasts, and analyst mentions are reviewed.
- [ ] Publisher/content: author reputation, expert mentions, citations from authoritative sources, syndication, newsletters, and site reputation abuse risk are reviewed.

## 18. Anti-Patterns

- [ ] Buying followed links.
- [ ] Selling followed links.
- [ ] Private blog networks.
- [ ] Expired domain link schemes.
- [ ] Mass exact-match guest posting.
- [ ] Large-scale link exchanges.
- [ ] Scholarship, coupon, badge, widget, or embed links made only for PageRank.
- [ ] Fake reviews or incentivized reviews.
- [ ] Review gating.
- [ ] Fake awards, fake certifications, fake customers, or fake testimonials.
- [ ] Spammy directory blasts.
- [ ] Comment/forum/profile spam.
- [ ] Recommendation poisoning or attempts to manipulate AI answers.
- [ ] Third-party site reputation abuse.

## 19. Output Template

Evidence sources: cite the specific sources used, such as `GSC`, `GA4`, `GBP`, `GMAPS`, `BWT`, `Firecrawl`, `Playwright`, `CMS/code`, `Manual/free SERP`, `Alerts/free monitoring`, `CRM/sales`, or `Human/context`.

```text
Summary:

Off-page goal:

Risk posture:

Authority/reputation baseline:

Priority issues:
1. [severity] [area]
   Evidence:
   Impact:
   Fix:
   Owner:
   Confidence:

Safe opportunities:

Risk cleanup:

Review/citation actions:

PR/partnership actions:

Disavow recommendation:

Monitoring plan:

Sources used:
```

## 20. Minimal Audit Flow

1. Check GSC Manual Actions, Security Issues, GSC Links, GA4 referrals, GBP, and brand SERPs.
2. Group external signals by type: editorial, local, review, partner, affiliate, PR, directory, marketplace, community, social, and spam.
3. Review backlink quality, relevance, anchor patterns, target URLs, and referral value.
4. Review reputation, reviews, citations, listings, and brand/entity consistency.
5. Separate safe opportunities from risky manipulation.
6. Recommend only actions that improve user trust, visibility, referral quality, or legitimate authority.
7. Set monitoring for links, reviews, mentions, manual actions, branded search, and referral conversions.
