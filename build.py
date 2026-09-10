"""
Build the portfolio site.

One shell, one content model, generated pages. Every number here is taken from
a repo's actual run output — nothing is rounded up for effect.
"""

import json
import pathlib
import shutil

import charts

ROOT = pathlib.Path(r"C:\Users\saiha\OneDrive\Desktop\Master Resume and prompt's\02_PROJECTS")
SITE = pathlib.Path(__file__).resolve().parent
GH = "https://github.com/gadesaiharika"
SITE_URL = "https://gadesaiharika.github.io"

NAV = [("#work", "Work"), ("#experience", "Experience"),
       ("#skills", "Skills"), ("#about", "About"), ("#contact", "Contact")]

# Structured data, homepage only. Recruiters google the name before they call,
# and this is what decides whether the result renders as a person or a URL.
PERSON_LD = {
    "@context": "https://schema.org",
    "@type": "Person",
    "name": "Sai Harika Gade",
    "jobTitle": "Research Data Analyst",
    "url": SITE_URL,
    "email": "mailto:gadesaiharika@gmail.com",
    "image": f"{SITE_URL}/assets/og-card.png",
    "sameAs": [GH, "https://linkedin.com/in/saiharikagade"],
    "worksFor": {"@type": "Organization", "name": "Mississippi State University"},
    "alumniOf": [
        {"@type": "CollegeOrUniversity", "name": "Mississippi State University"},
        {"@type": "CollegeOrUniversity", "name": "Malla Reddy University"},
    ],
    "address": {"@type": "PostalAddress",
                "addressLocality": "Starkville", "addressRegion": "MS",
                "addressCountry": "US"},
    "knowsAbout": ["Healthcare data analytics", "SQL", "Dimensional modeling",
                   "HL7 v2", "Epic Clarity and Caboodle data model",
                   "Revenue cycle analytics", "Data validation", "PostgreSQL",
                   "Tableau", "Python"],
}


def shell(title, desc, body, depth=0, path="", ld=None):
    """depth 0 = site root, 1 = /work/ — adjusts relative asset paths.

    `path` is the page's location under the site root, used for the canonical
    and og:url. Absolute, because a relative og:url is ignored by every
    crawler that reads it.
    """
    up = "../" * depth
    home = up + "index.html"
    nav_items = "\n".join(
        f'                    <li><a href="{home if depth else ""}{href}">{label}</a></li>'
        for href, label in NAV)
    canonical = f"{SITE_URL}/{path}".rstrip("/")
    ld_block = ("\n<script type=\"application/ld+json\">"
                + json.dumps(ld, indent=None) + "</script>") if ld else ""
    # Plain text for the card alt — og:image:alt is read aloud by screen readers
    # on some platforms and shown when the image fails to load.
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<link rel="canonical" href="{canonical}">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:type" content="website">
<meta property="og:url" content="{canonical}">
<meta property="og:site_name" content="Sai Harika Gade">
<meta property="og:image" content="{SITE_URL}/assets/og-card.png">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta property="og:image:alt" content="Sai Harika Gade, Research Data Analyst. 237 automated checks, 1,047 of 1,047 injected HL7 faults detected, 3 repositories that run from a clean clone.">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{title}">
<meta name="twitter:description" content="{desc}">
<meta name="twitter:image" content="{SITE_URL}/assets/og-card.png">
<meta name="theme-color" content="#f9f9f7" media="(prefers-color-scheme: light)">
<meta name="theme-color" content="#0d0d0d" media="(prefers-color-scheme: dark)">
<link rel="icon" href="data:image/svg+xml,<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 100 100'><rect width='100' height='100' rx='22' fill='%232a78d6'/><text y='68' x='50' text-anchor='middle' font-size='52' font-family='monospace' font-weight='700' fill='white'>SG</text></svg>">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Instrument+Serif:ital@0;1&family=Inter:wght@400;500;600&family=JetBrains+Mono:wght@400;500&display=swap" rel="stylesheet">
<link rel="stylesheet" href="{up}css/style.css">{ld_block}
<noscript><style>.reveal{{opacity:1!important;transform:none!important}}</style></noscript>
<script>
/* Apply the stored theme before first paint so the page never flashes. */
(function(){{try{{var t=localStorage.getItem("theme");if(t)document.documentElement.setAttribute("data-theme",t);}}catch(e){{}}}})();
</script>
</head>
<body>
<a class="skip-link" href="#main">Skip to content</a>

<header class="nav">
    <div class="wrap nav__inner">
        <a class="brand" href="{home}">
            <span class="brand__mark" aria-hidden="true">SG</span>
            <span>Sai Harika Gade</span>
        </a>
        <nav aria-label="Primary">
            <ul class="nav__links" id="nav-links" data-open="false">
{nav_items}
            </ul>
        </nav>
        <div class="nav__actions">
            <button class="icon-btn" data-theme-toggle type="button" aria-label="Switch theme">
                <svg class="icon-sun" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" aria-hidden="true"><circle cx="12" cy="12" r="4"/><path d="M12 2v2M12 20v2M4.9 4.9l1.4 1.4M17.7 17.7l1.4 1.4M2 12h2M20 12h2M4.9 19.1l1.4-1.4M17.7 6.3l1.4-1.4"/></svg>
                <svg class="icon-moon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M21 12.8A9 9 0 1111.2 3a7 7 0 009.8 9.8z"/></svg>
            </button>
            <button class="icon-btn nav__toggle" data-nav-toggle type="button" aria-label="Menu" aria-expanded="false" aria-controls="nav-links">
                <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" aria-hidden="true"><path d="M3 6h18M3 12h18M3 18h18"/></svg>
            </button>
            <a class="btn btn--primary btn--sm nav__cta" href="{home}#contact">Get in touch</a>
        </div>
    </div>
</header>

<main id="main">
{body}
</main>

<footer class="footer">
    <div class="wrap footer__inner">
        <p>&copy; <span data-year>2026</span> Sai Harika Gade &middot; Starkville, MS</p>
        <div class="footer__links">
            <a href="{GH}" target="_blank" rel="noopener">GitHub</a>
            <a href="https://linkedin.com/in/saiharikagade" target="_blank" rel="noopener">LinkedIn</a>
            <a href="mailto:gadesaiharika@gmail.com">Email</a>
        </div>
    </div>
</footer>

<script src="{up}js/script.js"></script>
</body>
</html>
"""


# ==========================================================================
# Projects — the single source for both the cards and the case studies
# ==========================================================================
PROJECTS = [
    {
        "slug": "hl7-interface-monitor",
        "repo": "hl7-interface-monitor",
        "name": "HL7 v2 Interface Monitor",
        "sub": "Parses live-shaped HL7 v2 traffic, validates it against 21 rules, and proves the "
               "validator itself works by injecting faults and reconciling every one back.",
        "chips": [("HL7 v2", True), ("Python", False), ("ADT / ORM / ORU", False),
                  ("Zero dependencies", False)],
        "metrics": [("1,047 / 1,047", "injected faults detected"),
                    ("21", "validation rules"),
                    ("173", "self-test checks")],
        "img": "interface_health.png",
        "caption": "Interface health: message volume, error rate by interface, and the failure "
                   "reasons behind it.",
        "chart_caption": "Rejected share of 20,000 messages, by interface. Radiology results reject "
                         "more than six times as often as pharmacy orders &mdash; the split a single "
                         "engine-wide error rate hides.",
        "tagline": "When a lab result never posts, someone has to find out why. This is that tool.",
        "sections": [
            ("The problem", """
<p>An EMR support analyst spends real time on interface failures: an order that never filed,
a result that never posted, an admission the downstream system never saw. The message is
usually malformed in a specific, boring way &mdash; a missing segment, a datetime the receiver
cannot parse, a code that is not in the value set.</p>
<p>I wanted hands-on familiarity with that failure surface, so I built the thing that watches it.</p>"""),
            ("How it works", """
<p>Three parts, each independently useful:</p>
<ul>
<li><strong>Parser</strong> &mdash; HL7 v2 in the standard library only. Segments, fields,
components, repetitions, and the encoding characters declared in <code>MSH-1</code>/<code>MSH-2</code>
rather than assumed.</li>
<li><strong>Generator</strong> &mdash; realistic <code>ADT^A01</code>, <code>ADT^A03</code>,
<code>ADT^A08</code>, <code>ORM^O01</code>, and <code>ORU^R01</code> traffic, with faults
deliberately injected at a controlled rate.</li>
<li><strong>Validator</strong> &mdash; 21 rules over message structure, the MSH header, patient and
visit segments, and order and result segments.</li>
</ul>"""),
            ("Severity is about consequence, not tidiness", """
<p>The rules do not grade messages on neatness. Each severity maps to what actually happens to the
message downstream:</p>
<div class="table-scroll"><table>
<thead><tr><th>Severity</th><th>What it means</th><th>Example</th></tr></thead>
<tbody>
<tr><td><strong>Rejected</strong></td><td>The receiver cannot file this at all</td>
<td>Missing <code>MSH</code>, unparseable message type, no patient identifier</td></tr>
<tr><td><strong>Accepted with defect</strong></td><td>It files, but something inside it is wrong</td>
<td>Unknown order code, out-of-range observation, malformed datetime in a non-key field</td></tr>
<tr><td><strong>Informational</strong></td><td>Worth surfacing, not worth paging anyone</td>
<td>Optional segment absent, non-standard but tolerated formatting</td></tr>
</tbody></table></div>
<p>The second row is the one that matters. A rejected message announces itself. A message that files
with a defect inside it is the one someone discovers three weeks later in a report that has been
quietly wrong the whole time.</p>"""),
            ("Proving the validator works", """
<div class="callout"><p><strong>A validator nobody tested is a validator that quietly passes
everything.</strong> So there are two independent checks, and the build fails if either does.</p></div>
<p><strong>Self-test &mdash; 173 checks.</strong> Every fault the generator can produce is applied to a
message that would otherwise be clean, and the suite asserts that the specific expected rule fires
&mdash; not merely that <em>something</em> fired.</p>
<p><strong>Reconciliation &mdash; 1,047 of 1,047.</strong> The generator records every fault it injects
across 20,000 messages. The validator runs blind. The two ledgers are then compared: every injected
fault must be detected, and detections must not exceed injections. Both directions matter &mdash; a
validator that flags everything would pass the first check and fail the second.</p>
<pre><code>[1/5] Validator self-test          173 passed, 0 failed
[2/5] Generating 20,000 messages   1,047 faults injected
[3/5] Validating
      reconciliation: 1,047/1,047 injected faults detected (100.0%)  [OK]</code></pre>"""),
            ("Honest scope", """
<ul>
<li>Synthetic messages. No PHI, and nothing derived from a real feed.</li>
<li>Not an integration engine. It parses, validates, and reports &mdash; it does not route, transform,
or acknowledge.</li>
<li>The rule set is a working subset, not the full HL7 v2 conformance surface.</li>
<li>I have not worked on a production interface engine. This is how I got hands on the message
structure and the failure modes.</li>
</ul>"""),
        ],
    },
    {
        "slug": "hrrp-readmission-analytics",
        "repo": "hrrp-readmission-analytics",
        "live": "https://public.tableau.com/app/profile/sai.harika.gade/viz/HRRPReadmissionDashboard/Dashboard2",
        "name": "30-Day Readmission Analytics",
        "sub": "A Caboodle-style star schema over 11,920 synthetic inpatient encounters, with CMS "
               "HRRP cohort logic, Type 2 history, and 25 checks that guard the definition.",
        "chips": [("PostgreSQL", True), ("SQL", False), ("Python", False),
                  ("Tableau", False), ("SCD Type 2", False)],
        "metrics": [("2.7s", "cold build, empty server"),
                    ("25", "validation checks"),
                    ("11,920", "encounters modelled")],
        "img": "readmission_by_cohort.png",
        "caption": "30-day readmission rate per HRRP cohort against the CMS national benchmark. "
                   "Heart failure worst, elective joint replacement best &mdash; the published pattern.",
        "chart_caption": "Observed 30-day rate against the CMS national benchmark. The connector is "
                         "the exposure: heart failure runs 5.9 points over, COPD 2.8 points under.",
        "tagline": "Hospitals lose up to 3% of Medicare payments to readmission penalties. This "
                   "finds where.",
        "sections": [
            ("The problem", """
<p>Under the CMS Hospital Readmissions Reduction Program, hospitals are penalised up to <strong>3% of
base Medicare DRG payments</strong> when 30-day all-cause readmission rates for six target conditions
exceed risk-adjusted national benchmarks. Knowing the overall rate is useless on its own. What a
quality director needs is which cohort, which service line, which payer mix, and which providers are
genuinely outliers rather than simply carrying sicker patients.</p>"""),
            ("The model", """
<div class="table-scroll"><table>
<thead><tr><th>Layer</th><th>Contents</th></tr></thead>
<tbody>
<tr><td><strong>Staging</strong></td><td>Synthea-format CSVs &mdash; patients, encounters, conditions,
procedures, payers, providers, organizations</td></tr>
<tr><td><strong>Dimensions</strong></td><td><code>DimPatient</code> (Type 2), <code>DimDate</code>,
<code>DimDiagnosis</code> with ICD-10 chapter rollups, <code>DimProvider</code>,
<code>DimPayer</code>, <code>DimFacility</code>, <code>DimHrrpCohort</code></td></tr>
<tr><td><strong>Facts</strong></td><td><code>FactEncounter</code> (per encounter) &middot;
<code>FactReadmission</code> (per index admission)</td></tr>
<tr><td><strong>Views</strong></td><td>Six reporting views &mdash; cohort summary, monthly trend,
payer mix, service-line heatmap, provider outliers, row-level detail</td></tr>
</tbody></table></div>
<p>The 30-day logic is two window functions over one partition:</p>
<pre><code>WINDOW w AS (PARTITION BY patient_key ORDER BY admit_datetime)

LAG(discharge_datetime)  OVER w   -- was THIS admission a readmission?
LEAD(admit_datetime)     OVER w   -- was it followed by one?  &lt;- HRRP numerator</code></pre>"""),
            ("A bug the checks caught", """
<p>The reported day count and the flag derived from it were computed from two different expressions:</p>
<pre><code>-- reported number: rounded
ROUND(EXTRACT(EPOCH FROM (next_admit - discharge)) / 86400.0)::INT

-- flag: raw, unrounded
EXTRACT(EPOCH FROM (next_admit - discharge)) / 86400.0 BETWEEN 0 AND 30</code></pre>
<p>A gap of 30.4 days reported as <strong>30 days</strong> while the readmission flag read
<strong>false</strong>. Filtering a dashboard on <code>days_to_next_admission &lt;= 30</code> therefore
returned a different population than the headline rate &mdash; the kind of discrepancy that surfaces
as "these two numbers don't match" and is miserable to trace after the fact.</p>
<p>Both now derive from one calendar-day delta, which also matches the CMS definition: the 30th
calendar day counts regardless of what hour either event happened at.</p>"""),
            ("A bug the checks missed", """
<p>All 25 checks passed while half of COPD was being filed as &ldquo;All other inpatient.&rdquo; The
classifier matched <code>'%chronic bronchitis%'</code>; the diagnosis text read &ldquo;Chronic
<em>obstructive</em> bronchitis,&rdquo; and the word in the middle broke the match. COPD reported 89
admissions at 16.9%, below its benchmark, when the true figure was 176 at 25.0%, above it.</p>
<p>The Tableau heatmap exposed it: 87 &ldquo;All other&rdquo; admissions sitting in Pulmonology at 33.3%,
a combination the data should not produce. A range check on cohort share had passed at 55.7%, and the
check meant to guard classification could never fail &mdash; the column is <code>NOT NULL</code> and the
ETL defaults to <code>OTHER</code>. It is replaced by a check that fails with exactly those 87 rows
against the old build and passes against the fixed one.</p>"""),
            ("Why Type 2 history", """
<p><code>DimPatient</code> versions on address change, so an encounter from 2023 stays joined to where
that patient lived in 2023. Without it, last quarter's regional numbers silently restate every time
someone moves.</p>
<div class="table-scroll"><table>
<thead><tr><th>patient</th><th>city</th><th>effective start</th><th>effective end</th><th>current</th></tr></thead>
<tbody>
<tr><td><code>00e463c7&hellip;</code></td><td>Tupelo</td><td>1976-09-02</td><td>2026-08-25</td><td>false</td></tr>
<tr><td><code>00e463c7&hellip;</code></td><td>Starkville</td><td>2026-08-26</td><td>&mdash;</td><td>true</td></tr>
</tbody></table></div>
<p>Ranges abut without overlapping &mdash; the invariant the validation suite enforces. A second
patient extract in which roughly 8% have moved runs on every build, so the merge is exercised against
real changed data rather than asserted in a comment.</p>"""),
            ("What it found", """
<ul>
<li><strong>Heart failure is the dominant exposure</strong> &mdash; 27.4% against a 21.5% benchmark,
and the largest denominator among the named cohorts, so intervention pays back most there.</li>
<li><strong>COPD is the second exposure, and it was hiding</strong> &mdash; 25.0% on 176 admissions
against a 19.6% benchmark. An earlier build showed it at 16.9% and below benchmark, because the
classifier was missing half its admissions.</li>
<li><strong>Medicare readmits at 18.5% against 14.4% commercial</strong> &mdash; a 4.2-point gap in
precisely the population HRRP measures.</li>
<li><strong>Case-mix adjustment reorders the provider list.</strong> Ranking on raw rate just finds
whoever carries the most heart failure; the provider view weights each provider's own cohort mix by
the national rates and compares against that.</li>
</ul>"""),
            ("Honest scope", """
<ul>
<li>Synthetic data, calibrated to the published CMS bands. The rates are properties of the generator.</li>
<li>Every inpatient stay is treated as an index admission. Real HRRP applies planned-readmission
exclusions, transfer merging, and an eligibility threshold.</li>
<li>No risk standardisation. The excess-cost figure is a linear approximation for executive framing,
not the CMS payment-adjustment formula.</li>
<li>Modelled on Epic's publicly documented Clarity/Caboodle patterns. No Epic software or production
environment is involved.</li>
</ul>"""),
        ],
    },
    {
        "slug": "revenue-cycle-denials",
        "repo": "revenue-cycle-denials",
        "name": "Revenue Cycle Denials &amp; AR",
        "sub": "A three-grain billing warehouse over 85,000 claims and 480,000 remittance postings, "
               "with a CARC taxonomy that keeps the denial rate honest.",
        "chips": [("PostgreSQL", True), ("SQL", False), ("Python", False),
                  ("CARC / RARC", False), ("KPI modelling", False)],
        "metrics": [("39", "validation checks"),
                    ("480k", "remittance postings"),
                    ("to the cent", "financial identity asserted")],
        "img": "denial_pareto.png",
        "caption": "Denied dollars by reason code with the cumulative Pareto line. Red bars are "
                   "denials a front-end or coding process could have prevented.",
        "chart_caption": "Denied dollars by CARC code, with cumulative share. Prior authorisation "
                         "alone is half of all denied dollars &mdash; and it is preventable.",
        "tagline": "Most denial dashboards report a rate above 90%. That number is wrong, and this "
                   "explains why.",
        "sections": [
            ("The definition that decides everything", """
<div class="callout"><p><strong>A remittance carries an adjustment code for every dollar not paid
&mdash; and most of those are not denials.</strong></p></div>
<p><code>CO-45</code> is the contractual write-down: the charge exceeded the contracted fee schedule.
It appears on essentially every commercial and Medicare claim. <code>PR-1</code>, <code>PR-2</code>,
and <code>PR-3</code> are deductible, coinsurance, and copay &mdash; the balance moved to the patient.
In all four cases the claim adjudicated <em>correctly</em>.</p>
<p>Count them as denials and the rate lands above 90%, which is how the metric stops meaning anything.
<code>DimDenialReason.is_true_denial</code> carries the distinction, every KPI view respects it, and a
validation check fails the build if a <code>CO-45</code> or <code>PR-*</code> claim is ever counted as
denied.</p>
<div class="table-scroll"><table>
<thead><tr><th>Counted as</th><th>Codes</th><th class="num">Reported denial rate</th></tr></thead>
<tbody>
<tr><td>Every adjustment code</td><td>all CARCs</td><td class="num">&gt; 90%</td></tr>
<tr><td>True denials only</td><td>CO-16, CO-197, CO-50, &hellip;</td><td class="num"><strong>11.08%</strong></td></tr>
</tbody></table></div>"""),
            ("Three grains, deliberately", """
<div class="table-scroll"><table>
<thead><tr><th>Fact</th><th>Grain</th><th>The question only it can answer</th></tr></thead>
<tbody>
<tr><td><code>FactClaim</code></td><td>one row per claim</td><td>What is our denial rate?</td></tr>
<tr><td><code>FactClaimLine</code></td><td>one row per charge line</td><td>Which CPT codes deny?</td></tr>
<tr><td><code>FactClaimTransaction</code></td><td>one row per posting</td><td>What did AR look like on a given date?</td></tr>
</tbody></table></div>
<p>The third one is not redundancy. A balance is a running total of postings, not a column &mdash; a
claim-grain table cannot express point-in-time AR at all.</p>"""),
            ("Making the money foot", """
<p>In a financial warehouse the checks that matter most are the ones that make the money balance. A
denial rate computed over a fact table that silently duplicated rows in a join is still a number,
still plausible, and completely wrong.</p>
<p>Every claim satisfies this identity, asserted <strong>to the cent</strong>:</p>
<pre><code>charge = contractual_adjustment + insurance_payment + patient_payment
       + patient_bad_debt + denial_writeoff + open_balance</code></pre>
<p>That single check caught a real bug during the build. When a patient payment fell after the
reporting date, the code zeroed the payment but carried only the <em>uncollected remainder</em> to open
balance &mdash; losing the collected portion and breaking the identity on 2,574 claims. It failed
loudly, which is the entire point.</p>"""),
            ("KPIs, and the definitions behind them", """
<div class="table-scroll"><table>
<thead><tr><th>Metric</th><th class="num">Result</th><th>Definition used</th></tr></thead>
<tbody>
<tr><td>Denial rate</td><td class="num">11.08%</td><td>True-denial claims / adjudicated claims</td></tr>
<tr><td>First-pass yield</td><td class="num">88.92%</td><td>Paid on first submission / adjudicated</td></tr>
<tr><td>Net collection rate</td><td class="num">87.64%</td><td>Payments / allowed, over adjudicated claims only</td></tr>
<tr><td>Days in AR</td><td class="num">43.8</td><td>Open AR / average daily net revenue</td></tr>
</tbody></table></div>
<p>Two definitional choices are load-bearing. <strong>Net collection includes what the patient pays</strong>
&mdash; modelling only the insurer understates it by the entire patient-responsibility share. And it is
measured <strong>over adjudicated claims only</strong>; leaving in-flight claims in the denominator counts
revenue that has not had a chance to be collected yet, and understates the rate every single month.</p>
<p>87.64% against a 95% best-practice benchmark is not a bug in the model. It is the finding:
<strong>$50.5M of gap</strong> across the book, decomposing into denial write-offs, bad debt, and
open AR.</p>"""),
            ("What it found", """
<ul>
<li><strong>Claims filed late are denied 3.5&times; as often.</strong> Claims submitted 90+ days after
service deny at 36.3% against a baseline near 10% &mdash; and charge lag is a process problem, not a
payer problem.</li>
<li><strong>A blended denial rate hides the spread.</strong> One payer denies at more than twice
Medicare's 8.3% and collects 82.6% against Medicare's 90.8%. The blended number describes no
individual payer.</li>
<li><strong>The work queue should rank by recoverable dollars, not claim count.</strong> The
highest-volume denial reason is rarely the highest-value one; <code>vw_recovery_opportunity</code>
weights unworked denials by each reason's historical overturn rate.</li>
</ul>"""),
            ("Honest scope", """
<ul>
<li>Synthetic claims. No PHI, and nothing derived from a real remittance file.</li>
<li>A simplified adjudication model &mdash; no coordination of benefits, secondary billing, or
capitation.</li>
<li>CARC and RARC codes are real and used correctly; the fee schedules and payer behaviour are modelled.</li>
<li>I have not worked in a production revenue cycle. This is built against the published code sets.</li>
</ul>"""),
        ],
    },
]


# ==========================================================================
# Home page
# ==========================================================================
STATS = [
    ("237", "automated checks across three repositories"),
    ("1,047<em>/1,047</em>", "injected HL7 faults detected"),
    ("32 GB <em>&rarr;</em> &lt;1 GB", "memory cut on a production research pipeline"),
    ("3", "repositories that run from a clean clone"),
]

EXPERIENCE = [
    ("Research Data Analyst, Poultry Science", "Mississippi State University &mdash; Dr. Li's Lab",
     "Aug 2026 &ndash; Present", True, [
        "Re-architected a genomics analysis pipeline from a SLURM/HPC cluster to standard local "
        "workstations, cutting environment setup from a multi-day process to a single documented install.",
        "Quality-controlled 2M+ sequencing reads across 19 samples, reconciling per-species counts "
        "against filtered totals to confirm zero read loss.",
        "Validated output against an independent reference implementation to within 0.01 percentage "
        "points across all species- and genus-level estimates.",
        "Root-caused an intermittent failure discarding results after an hour of compute &mdash; "
        "host/guest clock drift, not the reported cause &mdash; and shipped a documented fix.",
        "Cut a taxonomy lookup's memory footprint from 32&nbsp;GB to under 1&nbsp;GB with a streaming "
        "filter, removed a 9&nbsp;GB external dependency, and merged 6 pull requests."]),
    ("Graduate Teaching Assistant, Data Science", "Mississippi State University",
     "Jan 2025 &ndash; May 2026", False, [
        "First-line technical support for 60+ students across Data Wrangling and Data Visualization, "
        "triaging SQL, Python, and Tableau issues and escalating unresolved cases to faculty.",
        "Reviewed and debugged 100+ student analytics projects, writing feedback on query correctness, "
        "data validation, and reproducibility.",
        "Taught joins, aggregations, dimensional modeling, and statistical inference to non-technical "
        "learners through plain-language walkthroughs and live code review."]),
    ("Graduate Research Analyst, Healthcare Data Analytics", "Mississippi State University",
     "Aug 2024 &ndash; Dec 2024", False, [
        "Analyzed public-health surveillance and clinical records with SQL and Python to identify "
        "disease transmission drivers, reporting findings to principal investigators.",
        "Automated ETL and data-transfer pipelines in Python, SQL, and Selenium between source systems "
        "and research databases.",
        "Implemented QA/QC validation and standardization protocols to keep records audit-ready under "
        "Good Clinical Practice (GCP)."]),
    ("Data Science &amp; Machine Learning Intern", "InfraBIM Techno Solutions &mdash; Hyderabad, India",
     "Jan 2023 &ndash; May 2023", False, [
        "Integrated distributor, point-of-sale, and operations data from SQL Server and Excel into "
        "unified, analysis-ready datasets for inventory and assortment planning.",
        "Automated data preparation and validation in Python (Pandas, NumPy), cutting manual processing "
        "effort roughly 60% and shortening daily refresh cycles.",
        "Built K-Means store segmentation and baseline demand forecasts to flag slow-moving inventory."]),
    ("Marketing Data Analyst Intern", "Viral Fission &mdash; Hyderabad, India",
     "May 2022 &ndash; Aug 2022", False, [
        "Consolidated cross-channel campaign data from Instagram, YouTube, and Google Analytics into "
        "structured datasets covering reach, engagement, and conversion.",
        "Built recurring Excel and Google Data Studio KPI dashboards, reducing manual reporting effort."]),
]

SKILLS = [
    ("SQL &amp; data modeling", "Where most of the work actually happens.",
     ["PostgreSQL", "SQL Server", "T-SQL", "CTEs", "Window functions", "Query tuning", "Indexing",
      "Kimball dimensional modeling", "Star &amp; snowflake schemas", "Grain definition",
      "SCD Type 1 &amp; 2"]),
    ("Healthcare data &amp; standards", "Learned from the published specifications and built against.",
     ["Epic Clarity / Caboodle model", "ICD-10-CM/PCS", "CPT / HCPCS", "DRG", "CARC / RARC",
      "HL7 v2 (ADT, ORM, ORU)", "FHIR", "HIPAA Safe Harbor", "HRRP", "HEDIS", "MIPS"]),
    ("Python", "For pipelines, validation, and anything that has to run twice the same way.",
     ["Pandas", "NumPy", "SQLAlchemy", "psycopg2", "scikit-learn", "matplotlib", "Selenium"]),
    ("BI &amp; reporting", "Definitions live in version-controlled SQL, not in the workbook.",
     ["Tableau", "Power BI", "Excel (pivot tables, Power Query)", "KPI design", "Executive summaries"]),
    ("Data integrity", "The part that decides whether a number can be trusted.",
     ["Validation suites", "Reconciliation", "Referential integrity", "Root-cause analysis",
      "Regression testing", "Data dictionaries"]),
    ("Ways of working", "How the work gets shipped and explained.",
     ["Git &amp; pull-request review", "Technical documentation", "First-line support &amp; triage",
      "SDLC fundamentals", "Stakeholder communication"]),
]

# No phone number here on purpose. A phone number on a crawled page is scraped
# within days and ends up on spam-call lists; recruiters who actually want to
# make contact use email or LinkedIn. It stays on the resume, which goes to
# named recipients rather than to a crawler.
CONTACT = [
    ("Email", "gadesaiharika@gmail.com", "mailto:gadesaiharika@gmail.com"),
    ("LinkedIn", "in/saiharikagade", "https://linkedin.com/in/saiharikagade"),
    ("GitHub", "gadesaiharika", GH),
]


def live_btn(p):
    """A "Live dashboard" button, only for projects that have a published viz."""
    if not p.get("live"):
        return ""
    return (f'<a class="btn btn--ghost btn--sm" href="{p["live"]}" target="_blank" '
            f'rel="noopener">Live dashboard</a>')


def home():
    stats = "\n".join(f"""            <div class="stat">
                <div class="stat__value">{v}</div>
                <div class="stat__label">{l}</div>
            </div>""" for v, l in STATS)

    cards = []
    for i, p in enumerate(PROJECTS, 1):
        chips = "\n".join(
            f'                        <span class="chip{" chip--key" if key else ""}">{c}</span>'
            for c, key in p["chips"])
        metrics = "\n".join(f"""                        <div class="metric">
                            <div class="metric__value">{v}</div>
                            <div class="metric__label">{l}</div>
                        </div>""" for v, l in p["metrics"])
        cards.append(f"""            <article class="case reveal">
                <div class="case__body">
                    <p class="case__kicker"><span class="case__num">0{i}</span>{p['tagline']}</p>
                    <h3>{p['name']}</h3>
                    <p class="case__sub">{p['sub']}</p>
                    <div class="chips">
{chips}
                    </div>
                    <div class="metrics">
{metrics}
                    </div>
                    <div class="case__links">
                        <a class="btn btn--primary btn--sm" href="work/{p['slug']}.html">Read the case study</a>
                        {live_btn(p)}
                        <a class="btn btn--ghost btn--sm" href="{GH}/{p['repo']}" target="_blank" rel="noopener">
                            Source
                            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M7 17L17 7M9 7h8v8"/></svg>
                        </a>
                    </div>
                </div>
                <figure class="case__figure case__figure--chart">
                    {charts.CHARTS[p['repo']]()}
                    <figcaption>{p['chart_caption']}</figcaption>
                </figure>
            </article>""")

    tl = "\n".join(f"""                <div class="tl__item{' tl__item--now' if now else ''} reveal">
                    <div class="tl__head">
                        <h3>{title}</h3>
                        <span class="tl__when">{when}</span>
                    </div>
                    <p class="tl__org">{org}</p>
                    <ul>
{chr(10).join(f"                        <li>{b}</li>" for b in bullets)}
                    </ul>
                </div>""" for title, org, when, now, bullets in EXPERIENCE)

    # h3 and blurb share the fixed label column, so they are wrapped together —
    # otherwise the grid would drop the blurb into the tag column.
    skills = "\n".join(f"""            <div class="skillset reveal">
                <div class="skillset__label">
                    <h3>{name}</h3>
                    <p>{blurb}</p>
                </div>
                <div class="chips">
{chr(10).join(f'                    <span class="chip">{t}</span>' for t in tags)}
                </div>
            </div>""" for name, blurb, tags in SKILLS)

    contacts = "\n".join(f"""            <a class="contact-card reveal" href="{href}"{' target="_blank" rel="noopener"' if href.startswith('http') else ''}>
                <span class="contact-card__label">{label}</span>
                <span class="contact-card__value">{value}</span>
            </a>""" for label, value, href in CONTACT)

    spark, lo, hi, days = charts.hl7_sparkline()
    f = charts.hl7_facts()

    body = f"""    <section class="hero">
        <div class="wrap">
            <div class="hero__grid">
                <div class="hero__intro">
                    <p class="hero__status">Open to healthcare IT &amp; data analyst roles</p>
                    <h1>Sai&nbsp;Harika<br>Gade</h1>
                    <p class="hero__role">Research Data Analyst</p>
                    <p class="hero__lede">
                        I build healthcare data pipelines and the validation suites that decide
                        whether their numbers can be trusted. Three projects below; each one runs end
                        to end from a clean clone, and each one found a real bug while I was
                        building it.
                    </p>
                    <div class="hero__cta">
                        <a class="btn btn--primary" href="#work">See the work</a>
                        <a class="btn btn--ghost" href="{GH}" target="_blank" rel="noopener">GitHub</a>
                        <a class="btn btn--ghost" href="#contact">Contact</a>
                    </div>
                </div>

                <aside class="readout reveal" aria-label="Live figures from the HL7 interface monitor">
                    <div class="readout__head">
                        <span class="readout__title">hl7-interface-monitor</span>
                        <span class="readout__live">last run</span>
                    </div>
                    <div class="readout__spark">{spark}</div>
                    <div class="readout__scale">
                        <span>{lo:.1f}%</span>
                        <span>{days}-day rejection rate</span>
                        <span>{hi:.1f}%</span>
                    </div>
                    <div class="readout__row">
                        <span class="readout__key">messages parsed</span>
                        <span class="readout__value">{f['messages']:,}</span>
                    </div>
                    <div class="readout__row">
                        <span class="readout__key">rejected</span>
                        <span class="readout__value">{f['rejected']:,} &middot; {f['rejection_pct']:.2f}%</span>
                    </div>
                    <div class="readout__row">
                        <span class="readout__key">faults reconciled</span>
                        <span class="readout__value"><b>1,047 / 1,047</b></span>
                    </div>
                    <div class="readout__foot">
                        Read from <code>data/exports/</code> when this page was built &mdash; not
                        typed in.
                    </div>
                </aside>
            </div>

            <div class="stats reveal">
{stats}
            </div>
        </div>
    </section>

    <section id="work" class="band band--feature">
        <div class="wrap">
            <header class="section-head reveal">
                <p class="eyebrow">Selected work</p>
                <h2>Three projects, built to be run</h2>
                <p class="lede">
                    Not screenshots of dashboards. Each repository generates its own data, builds a
                    warehouse, validates itself, and fails the build if a check does not pass.
                </p>
            </header>
            <div class="work">
{chr(10).join(cards)}
            </div>
        </div>
    </section>

    <section id="experience">
        <div class="wrap">
            <header class="section-head reveal">
                <p class="eyebrow">Experience</p>
                <h2>Where I have worked</h2>
            </header>
            <div class="tl">
{tl}
            </div>
        </div>
    </section>

    <hr class="rule">

    <section id="skills">
        <div class="wrap">
            <header class="section-head reveal">
                <p class="eyebrow">Capabilities</p>
                <h2>What I work with</h2>
            </header>
            <div class="skills">
{skills}
            </div>
            <p class="note" style="margin-top:1.6rem;max-width:66ch">
                I have studied Epic's publicly documented data model and built against it with
                synthetic data. I have not worked in a production Epic environment, and nothing in this
                portfolio uses real patient data.
            </p>
        </div>
    </section>

    <hr class="rule">

    <section id="about">
        <div class="wrap">
            <header class="section-head reveal">
                <p class="eyebrow">About</p>
                <h2>Making data trustworthy</h2>
            </header>
            <div class="about">
                <div class="about__text reveal">
                    <p>
                        I am a Research Data Analyst at Mississippi State University, working on genomics
                        data pipelines in Dr.&nbsp;Li's lab. I hold an <strong>M.S. in Computer Science
                        with a 4.0 GPA</strong>, with a focus on healthcare data analytics, dimensional
                        modeling, and BI reporting.
                    </p>
                    <p>
                        Most of what I do comes down to one thing. I re-architected a pipeline off an HPC
                        cluster so it runs on a workstation, cut a step's memory footprint from 32&nbsp;GB
                        to under 1&nbsp;GB, and root-caused an intermittent failure that had been quietly
                        discarding an hour of compute per run &mdash; it turned out to be
                        <strong>host/guest clock drift, not the cause that had been reported</strong>.
                    </p>
                    <p>
                        My portfolio follows the same principle. A metric computed over a fact table that
                        silently duplicated rows in a join is still a number, still plausible, and
                        completely wrong. So every project ships with a validation suite, and the build
                        fails when a check does. All three of them caught something real.
                    </p>
                </div>
                <div>
                    <div class="panel reveal">
                        <h3>Education</h3>
                        <p><strong>M.S. Computer Science</strong> &mdash; Mississippi State University,
                        Starkville, MS &middot; 2024&ndash;2026 &middot; GPA 4.0</p>
                        <p style="margin-top:.6rem"><strong>B.Tech Computer Science</strong> &mdash;
                        Malla Reddy University, Hyderabad, India &middot; 2020&ndash;2024</p>
                    </div>
                    <div class="panel reveal">
                        <h3>Publication</h3>
                        <p>Computational Tools for Modeling Respiratory Disease Spread &mdash;
                        <em>under review</em>. Co-authored the predictive data-modeling and
                        computational-parallelization sections.</p>
                        <cite>Li Zhang, Michael E. Navicky, Saikanth Ratnavale, Pavan Dharma Adapa,
                        Sai Harika Gade</cite>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <hr class="rule">

    <section id="contact">
        <div class="wrap">
            <header class="section-head reveal">
                <p class="eyebrow">Contact</p>
                <h2>Get in touch</h2>
                <p class="lede">
                    I am open to roles in healthcare IT, EMR and clinical application support, and
                    healthcare data analytics.
                </p>
            </header>
            <div class="contact-grid">
{contacts}
            </div>
        </div>
    </section>"""

    return shell("Sai Harika Gade &middot; Research Data Analyst",
                 "Research Data Analyst building healthcare data pipelines and the validation "
                 "suites that make their numbers trustworthy. SQL, dimensional modeling, HL7 v2.",
                 body, depth=0, path="", ld=PERSON_LD)


def case_study(p):
    sections = "\n".join(f"<h2>{h}</h2>\n{b.strip()}" for h, b in p["sections"])
    metrics = "\n".join(f"""            <div class="stat">
                <div class="stat__value">{v}</div>
                <div class="stat__label">{l}</div>
            </div>""" for v, l in p["metrics"])

    body = f"""    <section class="study-hero">
        <div class="wrap--narrow">
            <a class="back-link" href="../index.html#work">
                <svg viewBox="0 0 24 24" width="14" height="14" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M19 12H5M12 19l-7-7 7-7"/></svg>
                All work
            </a>
            <p class="eyebrow">Case study</p>
            <h1>{p['name']}</h1>
            <p class="lede" style="font-size:var(--step-1)">{p['sub']}</p>
            <div class="case__links" style="margin-top:1.8rem">
                <a class="btn btn--primary btn--sm" href="{GH}/{p['repo']}" target="_blank" rel="noopener">
                    View source
                    <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M7 17L17 7M9 7h8v8"/></svg>
                </a>
                {live_btn(p)}
            </div>
        </div>
    </section>

    <div class="wrap--narrow">
        <div class="stats">
{metrics}
        </div>
    </div>

    <section style="padding-top:clamp(2.5rem,5vw,4rem)">
        <div class="wrap--narrow">
            <figure>
                <img src="../assets/{p['img']}" alt="{p['caption']}" width="1400" height="700">
                <figcaption>{p['caption']}</figcaption>
            </figure>
            <div class="prose">
{sections}
            </div>

            <hr class="rule" style="margin:3rem 0 2rem">
            <div class="case__links">
                <a class="btn btn--primary btn--sm" href="{GH}/{p['repo']}" target="_blank" rel="noopener">View source</a>
                {live_btn(p)}
                <a class="btn btn--ghost btn--sm" href="../index.html#work">Other projects</a>
            </div>
        </div>
    </section>"""

    return shell(f"{p['name'].replace('&amp;', '&')} &middot; Sai Harika Gade",
                 p["sub"].replace('"', "'"), body, depth=1,
                 path=f"work/{p['slug']}.html")


# ==========================================================================
if __name__ == "__main__":
    (SITE / "work").mkdir(exist_ok=True)
    assets = SITE / "assets"
    assets.mkdir(exist_ok=True)

    # The PNG dashboards still back the case-study pages. The homepage cards
    # draw their own SVG from the exports instead.
    for p in PROJECTS:
        src = ROOT / p["repo"] / "docs" / p["img"]
        shutil.copy2(src, assets / p["img"])
        print(f"asset  {p['img']:<30} {src.stat().st_size // 1024:>5} KB")

    import make_og
    card = make_og.build()
    print(f"asset  {card.name:<30} {card.stat().st_size // 1024:>5} KB")

    (SITE / "index.html").write_text(home(), encoding="utf-8")
    print("page   index.html")

    for p in PROJECTS:
        (SITE / "work" / f"{p['slug']}.html").write_text(case_study(p), encoding="utf-8")
        print(f"page   work/{p['slug']}.html")

    # The old flat pages are replaced by the single-page layout plus case studies.
    for stale in ("about.html", "experience.html", "projects.html", "skills.html", "contact.html"):
        f = SITE / stale
        if f.exists():
            f.unlink()
            print(f"remove {stale}")
