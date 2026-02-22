def check_free_email(emails):
    free_domains = [
        "gmail.com",
        "yahoo.com",
        "outlook.com",
        "hotmail.com",
        "protonmail.com"
    ]

    for email in emails:
        domain = email.split("@")[-1].lower()
        if domain in free_domains:
            return 0.3  # suspicious

    return 0.0  # safe