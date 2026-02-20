import whois
from datetime import datetime
import tldextract
from scraper.scraper_layer import WebsiteData


def check_domain_age(data: WebsiteData):
    """
    Takes structured WebsiteData object.
    Uses data.url internally.
    Returns structured domain age information.
    """

    try:
        extracted = tldextract.extract(data.url)
        domain = f"{extracted.domain}.{extracted.suffix}"

        domain_info = whois.whois(domain)
        creation_date = domain_info.creation_date

        if not creation_date:
            return {
                "layer": "Timeline Layer",
                "risk_score": 0.0,
                "age_string": "Unknown"
            }

        if isinstance(creation_date, list):
            creation_date = creation_date[0]

        if creation_date.tzinfo is not None:
            creation_date = creation_date.replace(tzinfo=None)

        age_days = (datetime.now() - creation_date).days

        years = age_days // 365
        months = (age_days % 365) // 30
        days = (age_days % 365) % 30

        age_string = f"{years} years, {months} months, {days} days"

        # Graded risk scoring
        if age_days < 30:
            risk_score = 0.4
        elif age_days < 90:
            risk_score = 0.2
        elif age_days < 365:
            risk_score = 0.1
        else:
            risk_score = 0.0

        return {
            "layer": "Timeline Layer",
            "risk_score": risk_score,
            "age_string": age_string
        }

    except Exception as e:
        print("WHOIS error:", e)
        return {
            "layer": "Timeline Layer",
            "risk_score": 0.0,
            "age_string": "Unknown"
        }
