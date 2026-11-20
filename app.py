import pandas as pd
import streamlit as st

st.set_page_config(
    page_title="AIOS Hiring Plan | Senior Media Buyer | Adam Baig",
    page_icon="🎯",
    layout="wide",
)

NAVY = "#1F3864"
st.markdown(
    f"""
    <style>
    h1, h2, h3 {{ color: {NAVY}; }}
    .block-container {{ max-width: 1100px; padding-top: 2rem; }}
    .lead {{ font-size: 1.1rem; line-height: 1.6; }}
    .quote {{ border-left: 4px solid {NAVY}; padding: 0.6rem 1rem; background: rgba(31,56,100,0.06); border-radius: 4px; }}
    </style>
    """,
    unsafe_allow_html=True,
)

# ---------------------------------------------------------------- header
st.title("Hiring a Senior Media Buyer for AIOS's European Blitzscale")
st.markdown(
    "**A 30-day search plan by Adam Baig** · Talent Lead, Full-Cycle Recruiter & Outbound Headhunter · "
    "[LinkedIn](https://www.linkedin.com/in/adambaiguk) · "
    "[GitHub](https://github.com/SkynetAI-Labs) · [GitLab](https://gitlab.com/SkynetAI-Labs)"
)

c1, c2, c3, c4 = st.columns(4)
c1.metric("Target time-to-fill", "30 days")
c2.metric("Outbound share of pipeline", "≥ 70%")
c3.metric("Offer-accept target", "≥ 90%")
c4.metric("Ashby hygiene", "Same-day")

st.divider()

tabs = st.tabs([
    "1. Why it matters",
    "2. Scorecard",
    "3. Target companies",
    "4. Sourcing",
    "5. Outreach",
    "6. Screening",
    "7. Closing",
    "8. KPIs & Europe",
])

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
        st.subheader("Step 1 → $1B ARR by end of 2026")
        st.write("UK growth from 3k to 200k active GLP-1 patients needs paid acquisition that scales without wasting spend.")
    with b:
        st.subheader("Step 2 → $10B ARR by end of 2028")
        st.write("Blitzscaling Europe means opening new markets one after another, and each one needs local media buying expertise from day one.")
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
    st.dataframe(scorecard, hide_index=True, use_container_width=True)
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
    st.dataframe(tiers, hide_index=True, use_container_width=True)
    st.info("Before approaching tier 1, I would confirm with the Head of Talent and Legal any no-approach rules or partner sensitivities.")

# ---------------------------------------------------------------- 4
with tabs[3]:
    st.header("Three sourcing lanes")
    st.write(
        "The target is at least 70% of the pipeline from outbound, matching what I have delivered across my career. "
        "Inbound applicants are reviewed, but the search does not wait for them."
    )
    l1, l2, l3 = st.columns(3)
    with l1:
        st.subheader("1. X-ray & Recruiter")
        st.write("Google X-ray to reach profiles beyond my network, then LinkedIn Recruiter to filter by company, tenure and location.")
    with l2:
        st.subheader("2. Company mapping")
        st.write("Map each target company's growth team, identify the number two behind each head of paid media, and approach them directly.")
    with l3:
        st.subheader("3. Referrals")
        st.write("Ask every strong candidate, including those who decline, for the best buyer they have worked with. Use paid-media communities and AIOS's own growth team for warm introductions.")
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
    st.success(
        "After each stage, every candidate is marked advance, hold or decline against the scorecard, with one written line "
        "saying why. All stages and statuses are kept current in Ashby the same day, so nothing stalls."
    )

# ---------------------------------------------------------------- 7
with tabs[6]:
    st.header("Closing: the step-up approach")
    st.write(
        "I target candidates who are ready to move up a level, not sideways. "
        "This approach has given me around a 90% offer-accept rate across my career."
    )
    w1, w2, w3 = st.columns(3)
    w1.markdown("**Who**\n\nThe number two in a strong growth team, or a senior buyer at a smaller brand, ready to own spend at a company growing faster than their current one.")
    w2.markdown("**Why they say yes**\n\nThe move is a real step up in scope, title, pay and equity, so the offer is not a close call against their current role.")
    w3.markdown("**Why they perform**\n\nThey are hungry to prove themselves at the higher level, and bring recent, hands-on platform skills.")
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
    st.dataframe(kpis, hide_index=True, use_container_width=True)

    st.subheader("30-day plan")
    weeks = [
        ("Week 1", "Intake and scorecard agreed; tier map built; 60 to 80 profiles sourced; calibration batch shared."),
        ("Week 2", "Outreach running across all three lanes; 10 to 15 recruiter screens; first hiring manager interviews."),
        ("Week 3", "Practical exercises and final interviews with a shortlist of three; references started."),
        ("Week 4", "Offer, close and resignation support; start date agreed."),
    ]
    cols = st.columns(4)
    for col, (wk, desc) in zip(cols, weeks):
        col.markdown(f"**{wk}**\n\n{desc}")

    st.subheader("Repeating it for Step 2")
    st.write(
        "Once the UK search is done, the scorecard, tier map and outreach become a playbook. For each new European market "
        "I would swap in local target companies and job titles, start sourcing six to eight weeks before launch, and keep a "
        "warm bench of buyers so the next market never waits for a hire."
    )

st.divider()
st.caption("Prepared by Adam Baig · London, UK (fully remote) · Based on the public AIOS Talent Lead job description.")
