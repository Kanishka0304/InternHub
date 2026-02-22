def calculate_rule_score(domain_risk, payment_flag, ssl_risk,
                         email_risk, nlp_risk,
                         pattern_boost, complaint_risk,
                         similarity_risk, geo_risk,
                         contact_risk, interview_risk,
                         company_risk, linguistic_risk,
                         recruiter_risk, document_risk):

    score = 0

    score += domain_risk
    score += ssl_risk
    score += email_risk
    score += nlp_risk
    score += pattern_boost
    score += complaint_risk
    score += similarity_risk
    score += geo_risk
    score += contact_risk
    score += interview_risk
    score += company_risk
    score += linguistic_risk
    score += recruiter_risk
    score += document_risk

    if payment_flag == 1:
        score += 0.4

    if score > 1:
        score = 1.0

    return score