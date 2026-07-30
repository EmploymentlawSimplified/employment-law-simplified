#!/usr/bin/env python3
"""
Phase 1 foundations build script for Employment Law Simplified.
Idempotent-ish: designed to run once against the v2 baseline. Re-running will
duplicate injected blocks, so this file is kept in the repo for reference/audit
rather than for repeated execution.
"""
import re, os

ROOT = os.path.dirname(os.path.abspath(__file__))
DOMAIN = "https://employmentlawsimplified.co.uk"
ORG_NAME = "Employment Law Simplified"

PAGES = [
    # (relpath, url_path, title, description, kind)
    ("index.html", "/", "Employment Law Simplified — UK Employment Rights Made Simple",
     "Strategic employment rights guidance for UK workers. Practical guides on tribunals, discrimination, grievances and more — written from the employee's perspective.", "website"),
    ("about.html", "/about.html", "About — Employment Law Simplified",
     "Why Employment Law Simplified exists — strategic employment rights guidance built from real tribunal experience.", "website"),
    ("contact.html", "/contact.html", "Contact — Employment Law Simplified",
     "Get in touch with Employment Law Simplified.", "website"),
    ("disclaimer.html", "/disclaimer.html", "Legal Disclaimer — Employment Law Simplified",
     "Legal disclaimer for Employment Law Simplified. This site provides information and strategic guidance, not legal advice.", "website"),
    ("privacy.html", "/privacy.html", "Privacy Policy — Employment Law Simplified",
     "How Employment Law Simplified collects, uses and protects your data.", "website"),
    ("resources.html", "/resources.html", "Templates & Tools — Employment Law Simplified",
     "Recommended books, templates, tools, and legal insurance for UK employees navigating workplace disputes.", "website"),
    ("start-here.html", "/start-here.html", "Start Here — Employment Law Simplified",
     "Not sure where to begin? Answer one question and we'll point you to the right guide for your situation.", "website"),
    ("cookie-notice.html", "/cookie-notice.html", "Cookie Notice — Employment Law Simplified",
     "How Employment Law Simplified uses cookies and similar technologies.", "website"),
    ("affiliate-disclosure.html", "/affiliate-disclosure.html", "Affiliate Disclosure — Employment Law Simplified",
     "Employment Law Simplified's affiliate relationships and how they affect our recommendations.", "website"),
    ("terms.html", "/terms.html", "Terms of Use — Employment Law Simplified",
     "Terms of use for Employment Law Simplified (employmentlawsimplified.co.uk).", "website"),
    ("thank-you.html", "/thank-you.html", "Thank You — Employment Law Simplified",
     "Order confirmation for Employment Law Simplified template purchases.", "website"),
    ("articles/index.html", "/articles/", "Articles — Employment Law Simplified",
     "Practical guides on employment tribunals, discrimination, grievances, and workplace rights for UK employees.", "website"),
    ("articles/tribunal-guide.html", "/articles/tribunal-guide.html", "The Complete Employment Tribunal Guide — Employment Law Simplified",
     "A complete step-by-step guide to the UK employment tribunal process for self-represented claimants. From ACAS conciliation to the final hearing.", "article"),
    ("articles/signs-employer-building-case.html", "/articles/signs-employer-building-case.html", "Signs Your Employer Is Building a Case to Dismiss You — Employment Law Simplified",
     "The warning signs most employees miss when their employer is building a case against them — and what to do the moment you spot them.", "article"),
]

ORG_JSONLD = '''<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Organization",
  "name": "%s",
  "url": "%s",
  "description": "Free, plain-English strategic guidance for UK employees navigating workplace disputes."
}
</script>
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "WebSite",
  "name": "%s",
  "url": "%s"
}
</script>''' % (ORG_NAME, DOMAIN, ORG_NAME, DOMAIN)

CONSENT_BANNER = '''<!-- Cookie consent banner -->
<div id="cookieConsent" class="cookie-consent" role="dialog" aria-label="Cookie consent" hidden>
  <div class="cookie-consent-inner">
    <p>We use privacy-friendly analytics (Plausible, which does not use cookies) to understand how visitors use this site. Affiliate links may set cookies on partner sites when clicked. See our <a href="/cookie-notice.html">Cookie Notice</a>.</p>
    <div class="cookie-consent-actions">
      <button type="button" id="cookieDecline" class="cookie-btn cookie-btn-secondary">Decline analytics</button>
      <button type="button" id="cookieAccept" class="cookie-btn cookie-btn-primary">Accept</button>
    </div>
  </div>
</div>
<script>
(function () {
  function loadAnalytics() {
    if (document.getElementById('plausible-script')) return;
    var s = document.createElement('script');
    s.id = 'plausible-script';
    s.defer = true;
    s.setAttribute('data-domain', 'employmentlawsimplified.co.uk');
    s.src = 'https://plausible.io/js/script.js';
    document.head.appendChild(s);
  }
  var choice = localStorage.getItem('els-cookie-consent');
  if (choice === 'accepted') {
    loadAnalytics();
  } else if (choice !== 'declined') {
    var banner = document.getElementById('cookieConsent');
    if (banner) banner.hidden = false;
  }
  var acceptBtn = document.getElementById('cookieAccept');
  var declineBtn = document.getElementById('cookieDecline');
  if (acceptBtn) acceptBtn.addEventListener('click', function () {
    localStorage.setItem('els-cookie-consent', 'accepted');
    document.getElementById('cookieConsent').hidden = true;
    loadAnalytics();
  });
  if (declineBtn) declineBtn.addEventListener('click', function () {
    localStorage.setItem('els-cookie-consent', 'declined');
    document.getElementById('cookieConsent').hidden = true;
  });
})();
</script>'''

def depth_prefix(url_path):
    # articles pages need no prefix since site uses root-relative links already
    return ""

def build_head_extra(url_path, title, description, kind):
    canonical = DOMAIN + url_path
    extra = []
    extra.append('<link rel="canonical" href="%s">' % canonical)
    extra.append('<meta property="og:title" content="%s">' % title)
    extra.append('<meta property="og:description" content="%s">' % description)
    extra.append('<meta property="og:url" content="%s">' % canonical)
    extra.append('<meta property="og:type" content="%s">' % ("article" if kind == "article" else "website"))
    extra.append('<meta property="og:site_name" content="%s">' % ORG_NAME)
    extra.append('<meta name="twitter:card" content="summary_large_image">')
    extra.append('<meta name="twitter:title" content="%s">' % title)
    extra.append('<meta name="twitter:description" content="%s">' % description)
    extra.append(ORG_JSONLD)
    if kind == "article":
        extra.append('''<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "%s",
  "description": "%s",
  "url": "%s",
  "publisher": {"@type": "Organization", "name": "%s"}
}
</script>''' % (title.split(" — ")[0], description, canonical, ORG_NAME))
        crumb_name = title.split(" — ")[0]
        extra.append('''<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "BreadcrumbList",
  "itemListElement": [
    {"@type": "ListItem", "position": 1, "name": "Home", "item": "%s/"},
    {"@type": "ListItem", "position": 2, "name": "Articles", "item": "%s/articles/"},
    {"@type": "ListItem", "position": 3, "name": "%s", "item": "%s"}
  ]
}
</script>''' % (DOMAIN, DOMAIN, crumb_name, canonical))
    return "\n".join(extra)

NAV_HOME_VARIANTS = [
    '<li><a href="/">Home</a></li>',
    '<li><a href="/" class="active">Home</a></li>',
]
START_HERE_LINK = '<li><a href="/start-here.html">Start Here</a></li>'

def inject_start_here(html):
    for variant in NAV_HOME_VARIANTS:
        if variant in html and START_HERE_LINK not in html:
            html = html.replace(variant, variant + START_HERE_LINK, 1)
            break
    return html

FOOTER_LEGAL_OLD = '<div class="footer-legal">\n        <a href="/disclaimer.html">This site does not provide legal advice</a>\n      </div>'
FOOTER_LEGAL_OLD_MIN = '<div class="footer-legal"><a href="/disclaimer.html">This site does not provide legal advice</a></div>'
FOOTER_LEGAL_NEW = ('<div class="footer-legal"><a href="/disclaimer.html">Disclaimer</a>'
                     ' &middot; <a href="/privacy.html">Privacy</a>'
                     ' &middot; <a href="/cookie-notice.html">Cookies</a>'
                     ' &middot; <a href="/affiliate-disclosure.html">Affiliate Disclosure</a>'
                     ' &middot; <a href="/terms.html">Terms</a></div>')

def inject_footer_links(html):
    if FOOTER_LEGAL_OLD in html:
        html = html.replace(FOOTER_LEGAL_OLD, FOOTER_LEGAL_NEW)
    elif FOOTER_LEGAL_OLD_MIN in html:
        html = html.replace(FOOTER_LEGAL_OLD_MIN, FOOTER_LEGAL_NEW)
    return html

FOOTER_SITE_LIST_MARK = '<li><a href="/contact.html">Contact</a></li>'
FOOTER_SITE_EXTRA = ('<li><a href="/cookie-notice.html">Cookie Notice</a></li>'
                     '<li><a href="/affiliate-disclosure.html">Affiliate Disclosure</a></li>'
                     '<li><a href="/terms.html">Terms of Use</a></li>')

def inject_footer_grid_links(html):
    if FOOTER_SITE_LIST_MARK in html and FOOTER_SITE_EXTRA not in html:
        html = html.replace(FOOTER_SITE_LIST_MARK, FOOTER_SITE_LIST_MARK + FOOTER_SITE_EXTRA, 1)
    return html

def process(relpath, url_path, title, description, kind):
    path = os.path.join(ROOT, relpath)
    with open(path, "r", encoding="utf-8") as f:
        html = f.read()

    if 'rel="canonical"' not in html:
        head_extra = build_head_extra(url_path, title, description, kind)
        html = html.replace("</head>", head_extra + "\n</head>", 1)

    html = inject_start_here(html)
    html = inject_footer_links(html)
    html = inject_footer_grid_links(html)

    if 'id="cookieConsent"' not in html:
        html = html.replace("</body>", CONSENT_BANNER + "\n</body>", 1)

    with open(path, "w", encoding="utf-8") as f:
        f.write(html)
    print("processed", relpath)

if __name__ == "__main__":
    for relpath, url_path, title, description, kind in PAGES:
        full = os.path.join(ROOT, relpath)
        if os.path.exists(full):
            process(relpath, url_path, title, description, kind)
        else:
            print("SKIP (create first):", relpath)
