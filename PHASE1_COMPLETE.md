# Phase 1 — Foundations: Complete

Built on the v2 baseline (v1 archived at `archive/els-site-v1.zip`). Git repo initialised in this folder, one clean commit.

## What's live

- **Legal/compliance pages:** Cookie Notice, Affiliate Disclosure, Terms of Use added alongside existing Disclaimer and Privacy Policy. All linked from every page footer.
- **Cookie consent banner:** sitewide, gates analytics until accepted; declines are respected via `localStorage`.
- **Analytics:** Plausible (privacy-friendly, cookieless) wired in behind consent — no account/site key needed to view the dashboard once you add the site at plausible.io, nothing for you to configure in code.
- **Technical SEO:** `robots.txt`, `sitemap.xml` (13 URLs), custom `404.html` (noindexed).
- **On-page SEO:** canonical URL, Open Graph, and Twitter card tags added to all 13 pages; Organization/WebSite JSON-LD sitewide; Article + BreadcrumbList JSON-LD on the two article pages.
- **IA additions:** `/start-here.html` router (grievance / dismissed / at tribunal), and `resources.html` restructured into a proper Templates & Tools hub shell (category cards, each marked `<!-- CONTENT: to be supplied / reviewed by Paul -->` — no product content invented).
- **Verification:** ran an internal link crawl across all pages — no broken internal links.

## What I didn't do (needs your input)

- **Email capture / ESP** — no MailerLite/ConvertKit/Buttondown key from you yet, so no signup forms wired in. That's Phase 2.
- **Real template/resource content** — the Templates & Tools cards are structural placeholders only, flagged per the guardrail.
- **GA4/Plausible account** — I used Plausible in the code since it needs no cookie banner complexity and fits the "trust" positioning, but you'll need to add the domain at plausible.io yourself (no key required for their script tag).
- **Pillar pages** (Compensation & Remedy, Evidence & Strategy, Know Your Rights, Settlement, standalone Discrimination/Grievances) — that's Phase 3 content work, deliberately not started since it needs real legal-strategy content from you.

## One flag on the working environment

Git in this sandboxed folder had trouble with file deletion (the mount blocks unlinking files once written), which broke git's own lock-file cleanup mid-session. I fixed it by requesting delete permission and reinitialising — the repo is now clean with one commit. If you move this to your own machine or a normal CI/CD setup for Cloudflare Pages, this issue won't recur; it was specific to this session's sandbox.

## Suggested next step

Phase 2 (growth plumbing): email capture + first lead magnet, on-page SEO pass refinements, FAQ structured data where relevant. Let me know when you're ready and whether you have an ESP picked.
