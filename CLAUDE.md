# Employment Law Simplified — Website Build Brief (for Claude Code)

> Hand this to Claude Code as the project brief, or place it in the repo root as `CLAUDE.md` so it is read as standing instructions.
>
> **Rule: work in phases, confirm the stack first, and treat every acceptance checkbox as a gate before moving on.**

## Kick-off prompt to paste first

> You are Claude Code working on the Employment Law Simplified website (a UK employment-law content site). Read this entire brief before acting. Begin with **Phase 1: discovery** — detect the tech stack, hosting, and content model, then report your findings plus a proposed plan. Do NOT make large changes or invent legal content until I approve the plan. Follow all guardrails in section 2.

## 0. Context & goal
- **Site:** employmentlawsimplified.co.uk — free, plain-English strategic guidance for UK employees in workplace disputes; monetised via templates, a self-rep course, affiliates and paid support.
- **Goal:** a fast, SEO-optimised, mobile-first content site with email capture, a gated template/download system, legal/compliance pages, and analytics — ready to publish guides and sell products.
- **Audience:** stressed UK employees, on mobile, mid-crisis. Prioritise clarity, speed and trust.

## 1. Phase 1 — Discovery (do this before changing anything)
- Detect the framework, hosting, package manager and build/deploy commands; read README and config files.
- Map existing routes, the content model (Markdown/MDX/CMS), components and styling system.
- Produce a short written report of findings **and a proposed plan** before any large change. Work within the existing framework — do not rewrite it.
- If the stack or intent is ambiguous, **stop and ask** rather than guessing.

## 2. Guardrails (must follow at all times)
- **Do not fabricate legal content or present anything as legal advice.** Where a guide or template needs substantive legal drafting, insert a clearly-marked placeholder `<!-- CONTENT: to be supplied / reviewed by Paul -->` instead of inventing law.
- Keep a sitewide **“information & strategy, not legal advice” disclaimer** component on every page.
- **Never commit secrets or API keys.** Use environment variables and provide a `.env.example`.
- Preserve existing content; do not delete pages without flagging first.
- Make **small, reviewable commits** with clear messages; never force-push.
- Meet **WCAG 2.1 AA** accessibility and use semantic HTML.

## 3. Information architecture
- **Pillar page per SEO category:** Grievances · Tribunals (process) · Compensation & Remedy · Discrimination · Evidence & Strategy · Know Your Rights · Settlement.
- **Supporting guides** under each pillar, interlinked to the pillar and to sibling guides.
- Global nav + footer; **breadcrumb** on every guide.
- A **“Start Here” router** page that segments visitors by situation (raising a grievance / just dismissed / already at tribunal).
- A **Templates & Tools hub** listing every download.
- An **About / Your Story** page for trust.

## 4. On-page SEO (apply to every page)
- Unique `<title>` (~55–60 chars) and meta description (~150 chars) containing the target keyword.
- One `<h1>`; logical `<h2>`/`<h3>` structure.
- Canonical URL; Open Graph + Twitter card tags.
- **Structured data:** Article/BlogPosting, FAQPage (where FAQs exist), BreadcrumbList, and Organization/WebSite.
- Internal links within the cluster with descriptive anchor text.
- Image `alt` text and descriptive filenames; table of contents on long guides.

## 5. Email capture & lead magnets
- Integrate an ESP (MailerLite / ConvertKit / Buttondown) via an env-configured key or embed.
- Inline signup forms + a light exit-intent prompt + a dedicated lead-magnet landing page.
- Deliver the lead-magnet PDF on confirmed signup; use **double opt-in**.
- GDPR: explicit consent checkbox (not pre-ticked), link to the privacy policy.

## 6. Template / download system
- A reusable “resource” content type: title, description, category, free/paid flag, file.
- **Free** downloads gated behind email; **paid** via Gumroad/Payhip embed (phase 4) or Stripe.
- Every template links to/from its matching guide page (the SEO content).
- Store files via the platform’s asset handling; keep large binaries out of git.

## 7. Legal & compliance
- Pages: **Privacy Policy, Cookie notice + consent banner, Affiliate Disclosure, Terms**, and the sitewide **not-legal-advice** disclaimer.
- Cookie consent must gate non-essential analytics.

## 8. Technical SEO & performance
- Auto-generated `sitemap.xml`, `robots.txt`, canonical tags, clean URLs, a custom 404, and redirects for any changed URLs.
- Core Web Vitals: responsive next-gen images, lazy loading, minimise JS/CSS, caching headers.
- **Lighthouse targets (mobile):** Performance >= 90, SEO 100, Accessibility >= 95, Best Practices >= 95.

## 9. Analytics
- GA4 or Plausible (privacy-friendly). Track pageviews plus events: `email_signup`, `template_download`, `product_click`/`purchase`.
- Connect Google Search Console and submit the sitemap.

## 10. Acceptance criteria (verify before declaring any phase “done”)
- [ ] Build passes; no console errors; linter clean
- [ ] All navigation links resolve; no broken internal links
- [ ] Every page has a unique title/meta/H1; structured data validates
- [ ] Sitemap and robots.txt present and correct
- [ ] Email signup works end-to-end (a test signup receives the lead magnet)
- [ ] Mobile Lighthouse meets the section 8 targets
- [ ] Disclaimer + privacy/cookie/affiliate/terms pages live and linked
- [ ] No secrets in the repo; `.env.example` present
- [ ] Placeholders clearly marked wherever human legal content is required

## 11. Suggested work order (phased — report + pass acceptance before advancing)
1. **Phase 1 — Foundations:** discovery, IA, nav/footer, disclaimer, legal pages, analytics, sitemap/robots.
2. **Phase 2 — Growth plumbing:** email capture + first lead magnet, Templates & Tools hub, on-page SEO pass, structured data.
3. **Phase 3 — Content:** build the pillar pages + priority guides (grievance letter, SAR, Schedule of Loss, ET1 guide, witness statement), each with a matching template download (legal body left as a marked placeholder).
4. **Phase 4 — Monetise:** Gumroad/Payhip products for templates + a course landing page.

## 12. What Paul will supply
- Real legal/template content (or ask him to generate it separately for review).
- ESP, analytics and payment account keys (via env vars — never in chat or git).
- Brand assets and the “your story” copy.

---

**Reminder for Claude:** the value of this site is trust and accuracy. When in doubt about anything legal, insert a placeholder and flag it — do not improvise the law.
