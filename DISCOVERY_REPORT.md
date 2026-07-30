# Employment Law Simplified — Phase 1 Discovery Report

## Findings

**Stack:** Plain static HTML + CSS. No framework (no React/Next/Astro/Hugo/Jekyll), no package manager, no `package.json`, no build step, no JS bundler. One shared `style.css` (644 lines, custom properties, Inter/Lora via Google Fonts). A few inline `onclick` handlers for the mobile nav toggle — no other JS.

**Hosting:** You said Cloudflare. There's no `wrangler.toml`, `_headers`, `_redirects`, or Pages Functions in the project files, so this reads as a static site deployed to Cloudflare Pages by pointing at a folder/repo, with no Cloudflare-specific config committed yet.

**Version control:** No `.git` directory in what you gave me — so either it isn't initialised yet, or the working copy I received is a plain export/zip rather than a git checkout.

**Content model:** No CMS, no Markdown/MDX — every page is hand-written HTML with the nav/footer duplicated in each file. Two versions exist: `els-site.zip` (4 files — an earlier, thinner draft) and `els-site-v2.zip` (11 files — current, more developed). **v2 is clearly the one to build on**; v1 looks superseded.

**Existing routes (v2):**
- `/` (home)
- `/about.html`
- `/contact.html`
- `/disclaimer.html`
- `/privacy.html`
- `/resources.html`
- `/articles/index.html`
- `/articles/tribunal-guide.html`
- `/articles/signs-employer-building-case.html`

**What's already in decent shape:** nav + footer (consistent across pages), a legal disclaimer page, a privacy policy, home page copy and IA hints (six topic cards matching most of §3's pillar list), meta title/description on most pages.

**Gaps against the brief:**
- No pillar pages yet (cards link to `/articles/` generically, not to dedicated pillar URLs) for Compensation & Remedy, Evidence & Strategy, Know Your Rights, Settlement, Grievances as standalone pages, Discrimination as standalone.
- No "Start Here" router page.
- No Templates & Tools *hub* (resources.html is a "coming soon" stub, not a resource content type).
- No cookie consent banner / cookie notice page, no Affiliate Disclosure page, no Terms page.
- No `sitemap.xml`, `robots.txt`, custom 404.
- No structured data (Article/FAQPage/BreadcrumbList/Organization) anywhere.
- No analytics (GA4/Plausible) wired in.
- No email capture / ESP integration.
- No canonical tags / OG / Twitter card tags.
- Two articles are placeholder "coming soon" stubs (tribunal guide, employer-building-case) — consistent with your instruction not to fabricate legal content; these need real content from you or a flagged placeholder treatment.
- No `.env.example` (not needed yet since nothing consumes secrets, but will be once ESP/analytics keys are added).

## Proposed Phase 1 plan (Foundations)

1. Confirm v2 is the base (delete/archive v1 from the working set — flagging here rather than silently discarding, per guardrails).
2. Add sitewide technical scaffolding: `robots.txt`, `sitemap.xml`, custom `404.html`.
3. Add missing legal pages: Cookie Notice, Affiliate Disclosure, Terms — plus a cookie consent banner component that gates analytics.
4. Add a lightweight analytics snippet (GA4 or Plausible — your call) wrapped so it only fires after consent.
5. Add per-page `<link rel="canonical">`, Open Graph, and Twitter card tags to all existing pages.
6. Add Organization/WebSite structured data sitewide, plus BreadcrumbList on article pages.
7. Build the "Start Here" router page and wire it into nav.
8. Turn `resources.html` into a real Templates & Tools hub shell (structure only — no products yet, that's Phase 4).

I haven't touched any files yet. Before I start:

- Which analytics do you want — GA4 or Plausible?
- OK to init a git repo in this folder so changes are tracked as small commits (per guardrail), or is version control handled elsewhere?
- Confirm I should proceed through steps 1–8 above as Phase 1, and stop for your review before Phase 2 (email capture/lead magnet/SEO pass) and Phase 3 (pillar content).
