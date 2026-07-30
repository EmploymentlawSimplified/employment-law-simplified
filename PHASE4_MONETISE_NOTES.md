# Monetisation: Document Templates — What's Built

You asked to build a system to sell your own document templates. Given the site is static HTML with no backend, and per the CLAUDE.md brief (`Phase 4 — Monetise`), I built it on **Gumroad/Payhip embeds** rather than a custom Stripe + database backend — no server, no payment credentials for me to touch, and no ongoing code to maintain. Gumroad/Payhip themselves act as your "document database": they store the files, take payment, issue receipts, and email the download link.

## What's live in the code (on `resources.html`)

Five product placeholders under a new "Our Own Templates" section, matching the Phase 3 priority list from CLAUDE.md: Grievance Letter Template, SAR Template, Schedule of Loss Template, ET1 Drafting Guide, Witness Statement Template.

Each one currently shows:
- Title and one-line description
- "Price TBD" (no price invented — that's yours to set)
- A disabled "Buy Now" button and a "Coming soon" badge
- An HTML comment marking exactly where to paste your real Gumroad/Payhip product URL

A `/thank-you.html` page (noindex'd) for the post-purchase redirect, showing a confirmation message and firing a `purchase` analytics event (only if the visitor accepted analytics).

Analytics wiring: a `product_click` event fires whenever someone clicks a "Buy Now" button (tracking interest even on disabled/placeholder buttons), and `purchase` fires on the thank-you page. Both go to Plausible, gated by the existing cookie consent choice — nothing fires if the visitor declined analytics.

## What you need to do to go live with each product

1. Create a Gumroad or Payhip account if you don't have one.
2. Write or finalise the actual template content (the guardrail in CLAUDE.md means I can't draft the legal wording myself — that's flagged `<!-- CONTENT: to be supplied / reviewed by Paul -->` throughout).
3. Create the product in Gumroad/Payhip: upload the file, set your price, and set the post-purchase redirect URL to `https://employmentlawsimplified.co.uk/thank-you.html?product=grievance-letter` (swap the slug per product — this is what makes the `purchase` event tell you which product sold).
4. In `resources.html`, find the matching `<!-- PRODUCT LINK -->` comment, replace the `href="#"` with your real Gumroad product URL, delete `aria-disabled="true"`, and delete the `<span class="coming-soon-badge">` line. Also replace "Price TBD" with the real price.
5. Repeat per product, then redeploy (drag the updated `resources.html` into a new Cloudflare Pages deployment — remember the earlier `articles/` subfolder issue, so double-check the whole folder structure is included).

## Not built (deliberately)

- No custom database — Gumroad/Payhip's own dashboard is your order/customer record.
- No Stripe integration — this avoids you or me handling any payment credentials directly.
- No Product schema (structured data) yet — adding fake prices to schema markup for search engines would be misleading before real prices exist; I'll add it once real Gumroad links and prices are in place.
- No free-download email gating yet — that's tied to picking an ESP (Phase 2), still pending your choice.

If your volume or needs outgrow Gumroad/Payhip later (e.g. you want your own checkout, subscriber data, or bundled pricing), the alternative — Cloudflare D1 + R2 + a Worker + Stripe — is a bigger build, and I already have a Cloudflare connector authorized that could support it if you want to go that route down the line.
