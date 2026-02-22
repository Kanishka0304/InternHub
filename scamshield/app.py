from scraper.scraper_layer import fetch_website_data

from feature_engine.timeline_layer import check_domain_age
from feature_engine.payment_layer import check_payment_keywords
from feature_engine.website_layer import check_ssl_certificate
from feature_engine.email_layer import check_free_email
from feature_engine.nlp_layer import check_urgency_language
from feature_engine.pattern_layer import check_dangerous_patterns
from feature_engine.complaint_layer import check_complaint_database
from feature_engine.similarity_layer import check_text_similarity
from feature_engine.geo_layer import check_geo_risk
from feature_engine.contact_layer import check_contact_behavior
from feature_engine.interview_layer import check_interview_anomalies
from feature_engine.company_layer import check_company_authenticity
from feature_engine.linguistic_layer import check_linguistic_manipulation
from feature_engine.recruiter_layer import check_recruiter_authenticity
from feature_engine.document_layer import check_document_scam_signals

from risk_engine.rule_engine import calculate_rule_score


if __name__ == "__main__":
    url = input("Enter Internship URL: ")

    data = fetch_website_data(url)

    if data:

        domain_risk, age_info = check_domain_age(url)
        payment_flag = check_payment_keywords(data["text"])
        ssl_risk = check_ssl_certificate(url)
        email_risk = check_free_email(data["emails"])
        nlp_risk = check_urgency_language(data["text"])

        pattern_boost = check_dangerous_patterns(
            domain_risk,
            payment_flag,
            email_risk,
            nlp_risk
        )

        complaint_risk = check_complaint_database(
            url,
            data["emails"],
            data["phones"]
        )

        similarity_risk = check_text_similarity(data["text"])
        geo_risk = check_geo_risk(url)

        contact_risk = check_contact_behavior(
            data["text"],
            data["emails"],
            data["phones"]
        )

        interview_risk = check_interview_anomalies(data["text"])

        company_risk = check_company_authenticity(
            data["text"],
            data["title"],
            data["links"],
            domain_risk
        )

        linguistic_risk = check_linguistic_manipulation(
            data["text"],
            domain_risk,
            payment_flag
        )

        recruiter_risk = check_recruiter_authenticity(
            data["text"],
            data["emails"],
            data["links"],
            domain_risk,
            payment_flag,
            email_risk
        )

        document_risk = check_document_scam_signals(
            data["text"],
            payment_flag,
            domain_risk
        )

        rule_prob = calculate_rule_score(
            domain_risk,
            payment_flag,
            ssl_risk,
            email_risk,
            nlp_risk,
            pattern_boost,
            complaint_risk,
            similarity_risk,
            geo_risk,
            contact_risk,
            interview_risk,
            company_risk,
            linguistic_risk,
            recruiter_risk,
            document_risk
        )

        print("\n============================")
        print("Domain Age:", age_info)
        print("Emails Found:", data["emails"])
        print("Phones Found:", data["phones"])
        print("----------------------------")
        print("Domain Risk:", domain_risk)
        print("SSL Risk:", ssl_risk)
        print("Email Risk:", email_risk)
        print("NLP Risk:", nlp_risk)
        print("Pattern Boost:", pattern_boost)
        print("Complaint Risk:", complaint_risk)
        print("Similarity Risk:", similarity_risk)
        print("Geo Risk:", geo_risk)
        print("Contact Risk:", contact_risk)
        print("Interview Risk:", interview_risk)
        print("Company Risk:", company_risk)
        print("Linguistic Risk:", linguistic_risk)
        print("Recruiter Risk:", recruiter_risk)
        print("Document Risk:", document_risk)
        print("============================")

        print("Fraud Probability:", round(rule_prob * 100, 2), "%")

        if rule_prob >= 0.8:
            print("Risk Level: VERY HIGH")
        elif rule_prob >= 0.6:
            print("Risk Level: HIGH")
        elif rule_prob >= 0.3:
            print("Risk Level: MEDIUM")
        else:
            print("Risk Level: LOW")

    else:
        print("Failed to fetch website.")