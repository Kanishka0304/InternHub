def check_payment_keywords(text):
    payment_keywords = [
        "registration fee",
        "processing fee",
        "pay ₹",
        "pay now",
        "upi",
        "crypto",
        "refundable deposit"
    ]

    text_lower = text.lower()

    for keyword in payment_keywords:
        if keyword in text_lower:
            return 1  # suspicious

    return 0  # safe