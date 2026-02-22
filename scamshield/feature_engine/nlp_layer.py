import re

def check_urgency_language(text):
    text_lower = text.lower()

    # ----------------------------
    # 1️⃣ Urgency & Pressure Words
    # ----------------------------
    urgency_keywords = [
        "urgent",
        "apply now",
        "limited seats",
        "hurry",
        "immediate joining",
        "limited time",
        "act fast",
        "closing soon",
        "last chance"
    ]

    # ----------------------------
    # 2️⃣ Unrealistic Promises
    # ----------------------------
    promise_keywords = [
        "guaranteed placement",
        "100% job guarantee",
        "earn ₹",
        "earn rs",
        "high salary",
        "work from home and earn",
        "no experience needed",
        "easy money",
        "quick income"
    ]

    # ----------------------------
    # 3️⃣ Interview Bypass
    # ----------------------------
    bypass_keywords = [
        "no interview",
        "instant offer",
        "direct selection",
        "automatic selection"
    ]

    # ----------------------------
    # 4️⃣ Payment Manipulation
    # ----------------------------
    payment_pressure = [
        "refundable fee",
        "processing fee",
        "security deposit",
        "registration amount"
    ]

    # ----------------------------
    # Count occurrences
    # ----------------------------
    urgency_count = sum(keyword in text_lower for keyword in urgency_keywords)
    promise_count = sum(keyword in text_lower for keyword in promise_keywords)
    bypass_count = sum(keyword in text_lower for keyword in bypass_keywords)
    payment_count = sum(keyword in text_lower for keyword in payment_pressure)

    # ----------------------------
    # 5️⃣ Exclamation Manipulation
    # ----------------------------
    exclamation_count = text.count("!")

    # ----------------------------
    # 6️⃣ ALL CAPS Detection
    # ----------------------------
    words = text.split()
    caps_words = [w for w in words if w.isupper() and len(w) > 3]
    caps_ratio = len(caps_words) / len(words) if words else 0

    # ----------------------------
    # Risk Calculation
    # ----------------------------
    risk_score = 0.0

    # Urgency pressure
    if urgency_count >= 3:
        risk_score += 0.2
    elif urgency_count >= 1:
        risk_score += 0.1

    # Unrealistic promises
    if promise_count >= 2:
        risk_score += 0.2
    elif promise_count >= 1:
        risk_score += 0.1

    # Interview bypass
    if bypass_count >= 1:
        risk_score += 0.2

    # Payment manipulation words
    if payment_count >= 1:
        risk_score += 0.2

    # Excessive exclamation
    if exclamation_count > 5:
        risk_score += 0.1

    # Too many ALL CAPS words
    if caps_ratio > 0.05:
        risk_score += 0.1

    # Cap max NLP risk
    if risk_score > 0.5:
        risk_score = 0.5

    return risk_score