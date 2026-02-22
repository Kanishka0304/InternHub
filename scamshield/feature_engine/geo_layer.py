import whois
import tldextract

# List of high-risk countries (example, you can expand)
HIGH_RISK_COUNTRIES = [
    "CN", "RU", "NG", "PK"
]


def check_geo_risk(url):
    try:
        extracted = tldextract.extract(url)
        domain = f"{extracted.domain}.{extracted.suffix}"

        domain_info = whois.whois(domain)

        country = domain_info.country

        if not country:
            return 0.1  

        if isinstance(country, list):
            country = country[0]

        print("Domain Country:", country)

        if country in HIGH_RISK_COUNTRIES:
            return 0.4

        return 0.0

    except Exception as e:
        print("Geo layer error:", e)
        return 0.1