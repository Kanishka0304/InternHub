def check_document_scam_signals(text, payment_flag, domain_risk):

    text_lower = text.lower()
    risk_score = 0.0

    # Only activate document suspicion in risky context
    high_risk_context = (payment_flag == 1 or domain_risk > 0.3)

    if not high_risk_context:
        return 0.0

    # ----------------------------
    #  Offer Letter Download Traps
    # ----------------------------
    offer_keywords = [
        "download offer letter",
        "get offer letter instantly",
        "offer letter after payment",
        "instant offer letter"
    ]

    for keyword in offer_keywords:
        if keyword in text_lower:
            print("⚠ Suspicious offer letter claim:", keyword)
            risk_score += 0.3
            break

    # ----------------------------
    #  Certificate Payment Claims
    # ----------------------------
    certificate_keywords = [
        "certificate after payment",
        "pay for certificate",
        "training certificate fee",
        "processing fee for certificate"
    ]

    for keyword in certificate_keywords:
        if keyword in text_lower:
            print("⚠ Certificate payment trap detected:", keyword)
            risk_score += 0.3
            break

    # ----------------------------
    #  Fake Digital Signature Claims
    # ----------------------------
    if "digitally signed" in text_lower and payment_flag == 1:
        print("⚠ Suspicious digital signature claim")
        risk_score += 0.2

    if risk_score > 0.5:
        risk_score = 0.5

    return risk_score