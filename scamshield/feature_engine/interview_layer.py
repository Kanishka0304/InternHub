def check_interview_anomalies(text):

    text_lower = text.lower()
    risk_score = 0.0

    no_interview_keywords = [
        "no interview",
        "direct selection",
        "automatic selection",
        "instant selection"
    ]

    instant_offer_keywords = [
        "instant offer letter",
        "offer within 24 hours",
        "same day selection",
        "guaranteed offer"
    ]

    for keyword in no_interview_keywords:
        if keyword in text_lower:
            print("⚠ No interview claim detected:", keyword)
            risk_score += 0.4
            break

    for keyword in instant_offer_keywords:
        if keyword in text_lower:
            print("⚠ Instant offer claim detected:", keyword)
            risk_score += 0.4
            break

    return risk_score