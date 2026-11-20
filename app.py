from html import escape

import pandas as pd
import streamlit as st

st.set_page_config(
    page_title="AIOS Hiring Plan | Senior Media Buyer | Adam Baig",
    page_icon="✦",
    layout="wide",
)

NAVY = "#0B1F4F"
BLUE = "#1F5FE0"
LIGHT = "#8DB0F2"
MINT = "#5BE38E"
PALE = "#EEF4FE"

st.markdown("""
    <style>
    :root { color-scheme: light; }
    .stApp, [data-testid="stAppViewContainer"], [data-testid="stMain"] { background:#EEF4FE!important; color:#0B1F4F!important; }
    [data-testid="stHeader"] { background:transparent!important; }
    .block-container { max-width:1240px; padding:2.5rem 2.5rem 4rem; }
    .stApp { font-family:Inter,Arial,sans-serif; }
    .stApp p,.stApp li,.stApp label,.stApp [data-testid="stCaptionContainer"] { color:#34476A; line-height:1.75; }
    .stApp h1,.stApp h2,.stApp h3,.stApp h4 { color:#0B1F4F; letter-spacing:-.035em; }
    .stApp h2 { font-size:1.85rem; padding-top:.5rem; }
    .stApp h3 { font-size:1.2rem; margin-top:1rem; }
    .stApp a { color:#1F5FE0; text-underline-offset:4px; }
    .banner { position:relative; overflow:hidden; background:linear-gradient(115deg,#0B1F4F 15%,#123875 70%,#1F5FE0); border-radius:24px; padding:3rem 3.2rem 2.6rem; margin-bottom:1.4rem; box-shadow:0 16px 40px #0B1F4F14; border:1px solid #ffffff28; }
    .banner:after { content:""; position:absolute; width:350px; height:350px; border:1px solid #8DB0F230; border-radius:50%; right:-160px; top:-110px; box-shadow:0 0 0 60px #8DB0F20a,0 0 0 120px #8DB0F208; pointer-events:none; }
    .stApp .banner h1 { position:relative; z-index:1; color:#FFFFFF!important; -webkit-text-fill-color:#FFFFFF!important; font-size:clamp(2rem,3.7vw,3.25rem); line-height:1.12; max-width:850px; margin:.95rem 0 1.1rem; padding:0; font-weight:750; letter-spacing:-.045em; }
    .stApp .banner .sub { color:#DDE9FF!important; font-size:1.06rem; max-width:720px; line-height:1.6; }
    .stApp .banner .tag { display:inline-block; color:#5BE38E!important; background:#5BE38E12; border:1px solid #5BE38E55; font-size:.68rem; text-transform:uppercase; letter-spacing:.15em; font-weight:700; padding:.45rem .75rem; border-radius:6px; }
    .stApp .banner .by,.stApp .banner .by b { color:#FFFFFF!important; font-size:.88rem; line-height:1.8; }
    .stApp .banner .by { border-top:1px solid #ffffff25; padding-top:1.3rem; margin-top:1.8rem; margin-bottom:0; }
    .stApp .banner a { color:#5BE38E!important; text-decoration:none; font-weight:600; }
    .banner a:hover { text-decoration:underline; }
    .kpis { display:grid; grid-template-columns:repeat(4,minmax(0,1fr)); gap:14px; margin-bottom:1.8rem; }
    .kpi { background:#FFFFFF; border:1px solid #DCE6F7; border-radius:14px; padding:1.3rem 1.4rem; position:relative; }
    .kpi:before { content:""; display:block; width:25px; height:4px; border-radius:4px; background:#5BE38E; margin-bottom:.75rem; }
    .kpi .v { color:#0B1F4F; font-weight:750; font-size:1.95rem; letter-spacing:-.045em; line-height:1.15; }
    .kpi .l { color:#53688B; font-size:.78rem; margin-top:.5rem; }
    .stTabs [data-baseweb="tab-list"] { gap:5px; flex-wrap:wrap; height:auto; background:transparent; padding:0 0 1.1rem; }
    .stTabs [data-baseweb="tab"] { background:#FFFFFF; border:1px solid #DCE6F7; border-radius:8px; padding:.6rem .85rem; height:auto; min-height:42px; white-space:normal; }
    .stTabs [data-baseweb="tab"] p { color:#435779!important; font-size:.77rem; font-weight:600; line-height:1.4; }
    .stTabs [data-baseweb="tab"][aria-selected="true"] { background:#0B1F4F!important; border-color:#0B1F4F; }
    .stTabs [data-baseweb="tab"][aria-selected="true"] p { color:#FFFFFF!important; }
    .stTabs [data-baseweb="tab"]:focus-visible { outline:3px solid #1F5FE0; outline-offset:3px; }
    .stTabs [data-baseweb="tab-highlight"],.stTabs [data-baseweb="tab-border"] { display:none; }
    .stTabs [data-baseweb="tab-panel"] { background:#FFFFFF; border:1px solid #DCE6F7; border-radius:18px; padding:1.7rem 2rem 2rem; box-shadow:0 8px 24px #0B1F4F04; }
    .lead { font-size:1.08rem; max-width:950px; }
    .card { background:#F5F8FF; border:1px solid #DCE6F7; border-radius:12px; padding:1.3rem; height:100%; color:#34476A; font-size:.93rem; line-height:1.7; }
    .card h4 { color:#0B1F4F!important; font-size:1rem; margin:0 0 .65rem; padding:0; letter-spacing:-.02em; }
    .note,.good,.quote { border-radius:10px; padding:1.1rem 1.3rem; margin:1rem 0; line-height:1.75; color:#0B1F4F; background:#EEF4FE; border-left:3px solid #1F5FE0; }
    .good { background:#EDFBF2; border-color:#5BE38E; }
    .quote { background:#F4F8FF; border-color:#5BE38E; font-size:1.02rem; }
    .table-scroll { overflow-x:auto; width:100%; margin:.75rem 0 1.2rem; border:1px solid #DCE6F7; border-radius:12px; }
    table.t { width:100%; border-collapse:collapse; font-size:.87rem; background:#FFFFFF; color:#34476A; }
    table.t th { background:#0B1F4F; color:#FFFFFF!important; text-align:left; font-size:.74rem; letter-spacing:.03em; padding:1rem; font-weight:600; }
    table.t td { border-bottom:1px solid #E5ECF8; padding:1rem; vertical-align:top; line-height:1.65; min-width:110px; }
    table.t td:first-child { color:#0B1F4F; font-weight:650; }
    table.t tr:nth-child(even) td { background:#F6F9FF; }
    table.t tr:last-child td { border-bottom:0; }
    .stApp [data-testid="stCode"],.stApp pre { background:#EEF4FE!important; border:1px solid #DCE6F7; border-radius:12px; }
    .stApp pre,.stApp code,.stApp pre span { color:#0B1F4F!important; }
    .footer { color:#53688B; font-size:.78rem; text-align:center; padding:1.8rem 0 .5rem; }
    @media(min-width:1600px) { .block-container { padding-top:3rem; } }
    @media(max-width:850px) { .block-container { padding:1.2rem 1rem 3rem; } .banner { padding:2rem 1.6rem; } .kpis { grid-template-columns:repeat(2,minmax(0,1fr)); } .stTabs [data-baseweb="tab-panel"] { padding:1.2rem; } }
    @media(max-width:480px) { .kpi { padding:1rem; } .kpi .v { font-size:1.6rem; } .banner h1 { font-size:2rem!important; } }
    @media(prefers-reduced-motion:reduce) { * { scroll-behavior:auto!important; } }
    </style>
""", unsafe_allow_html=True)


def table(df):
    head = "".join(f"<th>{escape(str(c))}</th>" for c in df.columns)
    rows = "".join("<tr>" + "".join(f"<td>{escape(str(v))}</td>" for v in r) + "</tr>" for r in df.values.tolist())
    st.markdown(f'<div class="table-scroll"><table class="t"><thead><tr>{head}</tr></thead><tbody>{rows}</tbody></table></div>', unsafe_allow_html=True)


def note(text, kind="note"):
    st.markdown(f'<div class="{kind}">{text}</div>', unsafe_allow_html=True)


def card(title, body):
    st.markdown(f'<div class="card"><h4>{title}</h4><div>{body}</div></div>', unsafe_allow_html=True)


# ---------------------------------------------------------------- banner
st.markdown(
    """
    <div class="banner">
      <span class="tag">Prepared for the AIOS Talent Team</span>
      <h1>Hiring a Senior Media Buyer for AIOS's European Blitzscale</h1>
      <p class="sub">A 30-day search plan built on AIOS's hiring bars, and how I would run it alongside three other live searches</p>
      <p class="by"><b>Adam Baig</b> · Talent Lead, Full-Cycle Recruiter &amp; Outbound Headhunter ·
        <a href="https://www.linkedin.com/in/adambaiguk" target="_blank" rel="noopener noreferrer">LinkedIn</a> ·
        <a href="https://github.com/SkynetAI-Labs" target="_blank" rel="noopener noreferrer">GitHub</a> ·
        <a href="https://gitlab.com/SkynetAI-Labs" target="_blank" rel="noopener noreferrer">GitLab</a></p>
    </div>
    <div class="kpis">
      <div class="kpi"><div class="v">30 days</div><div class="l">Target time-to-fill</div></div>
      <div class="kpi"><div class="v">&ge; 70%</div><div class="l">Outbound share of pipeline</div></div>
      <div class="kpi"><div class="v">&ge; 90%</div><div class="l">Offer-accept rate</div></div>
      <div class="kpi"><div class="v">Same day</div><div class="l">Ashby pipeline hygiene</div></div>
    </div>
    """,
    unsafe_allow_html=True,
)

SECTIONS = ['Why it matters', 'Scorecard', 'Target companies', 'Sourcing', 'Outreach', 'Screening', 'Closing', 'KPIs & Europe', 'Four searches at once']
st.markdown(
    '<div class="nav">' + "".join(
        f'<a href="#s{i+1}">{i+1:02d} · {name}</a>' for i, name in enumerate(SECTIONS)
    ) + "</div>",
    unsafe_allow_html=True,
)


class _Sections:
    def __getitem__(self, i):
        st.markdown(
            f'<div class="sec" id="s{i+1}"><span>SECTION {i+1:02d}</span></div>',
            unsafe_allow_html=True,
        )
        return st.container()


tabs = _Sections()

# ---------------------------------------------------------------- 1
with tabs[0]:
    st.header("Why this hire matters")
    st.markdown(
        '<p class="lead">A great Senior Media Buyer is the hire that turns each European launch into patients quickly. '
        "A missing one means a market goes live with no one owning paid acquisition. This plan shows how I would fill "
        "the role in 30 days, mostly through outbound, and then repeat the search market by market.</p>",
        unsafe_allow_html=True,
    )
    a, b = st.columns(2)
    with a:
        card("Step 1 → $1B ARR by end of 2026", "AIOS's stated plan: UK growth from 3k to 200k active GLP-1 patients needs paid acquisition that scales without wasting spend.")
    with b:
        card("Step 2 → $10B ARR by end of 2028", "AIOS's stated ambition: blitzscaling Europe means opening new markets one after another, and each one needs local media buying expertise from day one.")
    st.write("")
    st.markdown(
        '<div class="quote">The goal, in AIOS\'s own words: make sure <b>"a lack of key hires never blocks growth"</b>.</div>',
        unsafe_allow_html=True,
    )
    st.caption(
        "Senior Media Buyer is one of AIOS's recent searches, so I have used it as the worked example. "
        "The same method applies to Performance Marketing, AI and engineering, and clinical searches."
    )

# ---------------------------------------------------------------- 2
with tabs[1]:
    st.header("The scorecard")
    st.write(
        "I would agree this scorecard with the hiring manager before any sourcing starts. "
        "It uses AIOS's four hiring bars, so every candidate is judged the same way."
    )
    scorecard = pd.DataFrame(
        [
            ["Seniority",
             "Has personally owned a paid budget of meaningful scale across Meta, Google and TikTok, and made the spend decisions, not only executed them",
             "Walk through their largest budget: the split by channel, what they cut and why"],
            ["Industry fit",
             "Direct-to-consumer subscription growth, ideally in health, pharmacy or another regulated category",
             "How they handled ad policies, approvals and rejections in their last role"],
            ["Recency",
             "Hands-on in the platforms within the last 12 months, current on attribution after recent privacy changes and on creative testing",
             "What has changed in their account setup in the past six months"],
            ["Builder pattern",
             "Has built a channel, a team or a testing system from scratch, not only optimised an existing one",
             "What they built that did not exist before they joined"],
        ],
        columns=["Hiring bar", "What great looks like", "How I test it"],
    )
    table(scorecard)
    st.subheader("Compliance is a must-have, not a nice-to-have")
    st.write(
        "UK rules ban advertising prescription-only medicines to the public, and the ASA has been actively enforcing "
        "this against weight-loss medicine ads since 2024 "
        "([ASA, July 2025](https://www.asa.org.uk/news/how-we-re-trimming-down-problem-ads-for-weight-loss-prescription-only-medicines.html)). "
        "The right buyer can scale spend while staying inside those rules, and can do the same under each European market's rules."
    )
    st.subheader("Red flags")
    st.markdown(
        "- Results claimed without the budget or time period behind them\n"
        "- Only agency-side account management with no spend ownership\n"
        "- No answer on how they measured incrementality"
    )

# ---------------------------------------------------------------- 3
with tabs[2]:
    st.header("Target companies")
    st.write(
        "The best candidates already buy media in a regulated, subscription category, so I would map outward from the "
        "closest match. Each tier gets a talent map of who owns paid acquisition, who reports to them and who is ready for a step up."
    )
    tiers = pd.DataFrame(
        [
            ["1. UK online health and pharmacy", "Numan, Voy, Juniper, Manual, Simple Online Pharmacy, MedExpress, Zava",
             "Same patients, same channels and the same advertising rules"],
            ["2. UK direct-to-consumer subscription", "Huel, Gousto, Bloom & Wild, Gymshark",
             "High-volume paid acquisition and payback discipline at scale"],
            ["3. European health tech", "Doctolib, Kry / Livi, TeleClinic",
             "Local market knowledge and native languages for Step 2 launches"],
            ["4. Performance agencies", "Brainlabs, Jellyfish and specialist health agencies",
             "Strong buyers who have run several large accounts and want to own one in-house"],
        ],
        columns=["Tier", "Where to look", "Why they fit"],
    )
    table(tiers)
    note("Before approaching tier 1, I would confirm with the Head of Talent and Legal any no-approach rules or partner sensitivities.")

# ---------------------------------------------------------------- 4
with tabs[3]:
    st.header("Three sourcing lanes")
    st.write(
        "The target is at least 70% of the pipeline from outbound, matching what I have delivered across my career. "
        "Inbound applicants are reviewed, but the search does not wait for them."
    )
    l1, l2, l3 = st.columns(3)
    with l1:
        card("1. X-ray & Recruiter", "Google X-ray to reach profiles beyond my network, then LinkedIn Recruiter to filter by company, tenure and location.")
    with l2:
        card("2. Company mapping", "Map each target company's growth team, identify the number two behind each head of paid media, and approach them directly.")
    with l3:
        card("3. Referrals", "Ask every strong candidate, including those who decline, for the best buyer they have worked with. Use paid-media communities and AIOS's own growth team for warm introductions.")
    st.write("")
    st.subheader("Example X-ray string (UK)")
    st.code(
        'site:linkedin.com/in ("media buyer" OR "paid social" OR "performance marketing" OR "paid acquisition") '
        '(Meta OR Facebook OR TikTok) ("DTC" OR "subscription" OR "health" OR "pharmacy") "United Kingdom" -recruiter -jobs',
        language="text",
    )
    st.write(
        'For Europe, I would swap the location and add local job titles, for example "Performance Marketing Manager" '
        'Germany or "Responsable Acquisition" France.'
    )
    st.caption(
        "Claude and Gemini speed up the research: summarising each target company's growth team and drafting first "
        "versions of outreach. I check every detail and edit every message before it is sent."
    )

# ---------------------------------------------------------------- 5
with tabs[4]:
    st.header("Outreach")
    st.write("Short, specific and about their next step, not a job advert. A first message plus two follow-ups over ten days.")
    st.markdown(
        '<div class="quote">Hi [Name], I saw you have been running paid social at [Company] through its growth from '
        "[specific detail]. I am hiring a Senior Media Buyer at AIOS (Bolt Pharmacy), which has grown from $7M to $450M ARR "
        "since April 2025 and is now launching across Europe. You would own spend and testing as we open new markets. "
        "Open to a 15-minute call this week?</div>",
        unsafe_allow_html=True,
    )
    st.write("")
    st.write("Each message names something real about the candidate's work, which is where the AI research step earns its keep.")

# ---------------------------------------------------------------- 6
with tabs[5]:
    st.header("Screening and calibration")
    st.write("Calibration happens early, so a weak pipeline is caught in week one, not week four.")
    stages = [
        ("Calibration batch (days 3 to 5)",
         "Share five to eight profiles with the hiring manager before any interviews: a mix of strong fits and deliberate stretches. Agree what \"yes\" looks like, then tighten the target list."),
        ("Recruiter screen (30 minutes)",
         "Budget ownership, channel depth, regulated-ads experience, motivation for a step up, and pay expectations up front."),
        ("Hiring manager interview",
         "A deep dive into one campaign they built, and what they would do in AIOS's first 90 days."),
        ("Practical exercise",
         "A short paid-media case using an anonymised AIOS-style brief: allocate a launch budget for a new European market while staying inside advertising rules."),
        ("Final and references",
         "Founder or growth leadership conversation, plus two references focused on spend results and judgement."),
    ]
    for i, (name, desc) in enumerate(stages, 1):
        st.markdown(f"**{i}. {name}** — {desc}")
    note(
        "After each stage, every candidate is marked advance, hold or decline against the scorecard, with one written line "
        "saying why. All stages and statuses are kept current in Ashby the same day, so nothing stalls."
    , kind="good")

# ---------------------------------------------------------------- 7
with tabs[6]:
    st.header("Closing: the step-up approach")
    st.write(
        "I target candidates who are ready to move up a level, not sideways. "
        "This approach has given me around a 90% offer-accept rate across my career."
    )
    w1, w2, w3 = st.columns(3)
    with w1:
        card("Who", "The number two in a strong growth team, or a senior buyer at a smaller brand, ready to own spend at a company growing faster than their current one.")
    with w2:
        card("Why they say yes", "The move is a real step up in scope, title, pay and equity, so the offer is not a close call against their current role.")
    with w3:
        card("Why they perform", "They are hungry to prove themselves at the higher level, and bring recent, hands-on platform skills.")
    st.write("")
    st.write(
        "Closing starts at the first call: I ask about pay, notice period, other processes and what would make them say yes. "
        "Before the offer, I pre-close the candidate on the numbers and timing, so there are no surprises. "
        "After the offer, I stay close through notice and into their first 90 days."
    )

# ---------------------------------------------------------------- 8
with tabs[7]:
    st.header("KPIs, timeline and scaling across Europe")
    st.write("The plan is measured against AIOS's own four Talent KPIs.")
    kpis = pd.DataFrame(
        [
            ["Time-to-fill", "Offer accepted within 30 days", "Typical one-to-two-week time-to-fill"],
            ["Outbound share of pipeline", "At least 70%", "Around 70% of hires from outbound"],
            ["Offer-accept rate", "90% or more", "Around 90%"],
            ["Ashby pipeline hygiene", "Every stage and status updated the same day", "Same discipline in Greenhouse and Bullhorn"],
        ],
        columns=["AIOS KPI", "Target for this search", "My track record"],
    )
    table(kpis)

    st.subheader("30-day plan")
    weeks = [
        ("Week 1", "Intake and scorecard agreed; tier map built; 60 to 80 profiles sourced; calibration batch shared."),
        ("Week 2", "Outreach running across all three lanes; 10 to 15 recruiter screens; first hiring manager interviews."),
        ("Week 3", "Practical exercises and final interviews with a shortlist of three; references started."),
        ("Week 4", "Offer, close and resignation support; start date agreed."),
    ]
    cols = st.columns(4)
    for col, (wk, desc) in zip(cols, weeks):
        with col:
            card(wk, desc)
    st.write("")

    st.subheader("Repeating it for Step 2")
    st.write(
        "Once the UK search is done, the scorecard, tier map and outreach become a playbook. For each new European market "
        "I would swap in local target companies and job titles, start sourcing six to eight weeks before launch, and keep a "
        "warm bench of buyers so the next market never waits for a hire."
    )

# ---------------------------------------------------------------- 9
with tabs[8]:
    st.header("Running this alongside three other searches")
    st.write(
        "A Talent Lead at AIOS never runs one search at a time. Here is how I would carry the Senior Media Buyer search "
        "alongside three other live searches across growth, clinical, product and technical roles, without letting "
        "quality, candidate communication or Ashby hygiene slip."
    )
    searches = pd.DataFrame(
        [
            ["Senior Media Buyer", "Growth", "1",
             "Drives patient acquisition in the UK and each new European market",
             "UK online health and DTC subscription brands; X-ray plus company mapping", "35%"],
            ["Clinical Pharmacist (Independent Prescriber)", "Clinical", "1",
             "Prescribing capacity sets how many patients can be safely treated each day",
             "GPhC-registered independent prescribers in online pharmacy and primary care; pharmacist networks and referrals; partner with AIOS's Clinical Recruiter", "25%"],
            ["Head of InfoSec", "Technical", "2",
             "Protects patient health data and supports regulatory approval in each new market",
             "Security leaders at UK fintech and health tech scale-ups; ISO 27001 and UK GDPR experience; assessed with my hands-on cloud security background", "25%"],
            ["Product Manager – Engagement", "Product", "3",
             "Keeps patients engaged and on treatment, which drives retention and revenue",
             "Consumer subscription and health app product teams; builder pattern and experiment track record", "15%"],
        ],
        columns=["Search", "Area", "Priority", "Why it matters to the plan", "Sourcing approach", "Share of my week"],
    )
    table(searches)
    st.caption("Priority is set by business impact on Steps 1 and 2 and agreed with the Head of Talent each week.")

    st.subheader("A typical week across four searches")
    d1, d2, d3 = st.columns(3)
    with d1:
        card("Mornings (UK and Europe)", "Outbound sourcing and outreach while UK and European candidates are online. Every search gets new profiles each day, highest priority first.")
    with d2:
        card("Afternoons", "Recruiter screens, interview coordination, references and closing conversations, with scorecard notes written up straight away.")
    with d3:
        card("Late afternoon to midday Pacific", "Available through midday Pacific (normally 8pm UK; 7pm during the short daylight-saving changeover periods). Async updates and live syncs with hiring managers across time zones; pipeline reviews and calibration questions raised early.")
    st.write("")

    st.subheader("How nothing stalls")
    st.markdown(
        "- **Daily:** every stage and candidate status updated in Ashby the same day, and every candidate who has spoken to me hears back within 48 hours.\n"
        "- **Weekly:** a one-page update per search covering pipeline by stage, outbound share, risks and the next actions, shared async before each hiring manager sync.\n"
        "- **Early warning:** if a search has no strong calibrated profiles by day 10, I change the target list or the search strings, and flag it rather than waiting.\n"
        "- **Reusable playbooks:** each finished search leaves behind a scorecard, target map and outreach template, so the next hire in a new European market starts faster."
    )

st.markdown(
    '<div class="footer">Prepared by Adam Baig · London, UK (fully remote) · Based on the public AIOS Talent Lead job description and AIOS careers page.</div>',
    unsafe_allow_html=True,
)
