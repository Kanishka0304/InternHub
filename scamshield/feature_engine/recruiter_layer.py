def check_recruiter_authenticity(text, emails, links,
                                 domain_risk,
                                 payment_flag,
                                 email_risk):

    text_lower = text.lower()
    risk_score = 0.0

    # Only activate recruiter suspicion for risky domains
    high_risk_context = (
        domain_risk > 0.3 or
        payment_flag == 1 or
        email_risk > 0
    )

    if not high_risk_context:
        return 0.0

    # ----------------------------
    # 1️⃣ Generic Recruiter Titles
    # ----------------------------
    generic_titles = [
        "hr manager",
        "hr team",
        "recruitment team",
        "talent acquisition",
        "hiring manager"
    ]

    for title in generic_titles:
        if title in text_lower:
            print("⚠ Suspicious generic recruiter title:", title)
            risk_score += 0.2
            break

    # ----------------------------
    # 2️⃣ No LinkedIn Mention
    # ----------------------------
    linkedin_links = [
        link for link in links
        if link and "linkedin.com" in link.lower()
    ]

    if len(linkedin_links) == 0:
        print("⚠ No LinkedIn recruiter reference")
        risk_score += 0.2

    # ----------------------------
    # 3️⃣ Personal Email Recruiter
    # ----------------------------
    for email in emails:
        if any(domain in email.lower() for domain in
               ["gmail", "yahoo", "outlook", "proton"]):
            print("⚠ Recruiter using personal email")
            risk_score += 0.2
            break

    if risk_score > 0.4:
        risk_score = 0.4

    return risk_score