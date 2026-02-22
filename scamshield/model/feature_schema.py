# model/feature_schema.py

# ----------------------------
# Official Feature Order
# ----------------------------
FEATURE_NAMES = [
    "domain_risk",
    "payment_flag",
    "ssl_risk",
    "email_risk",
    "nlp_risk",
    "pattern_boost",
    "complaint_risk",
    "similarity_risk",
    "geo_risk",
    "contact_risk",
    "interview_risk",
    "company_risk",
    "linguistic_risk",
    "recruiter_risk",
    "document_risk"
]


# ----------------------------
# Convert Feature Dict → ML Vector
# ----------------------------
def dict_to_vector(feature_dict):
    """
    Converts feature dictionary to ordered list
    according to FEATURE_NAMES.
    """
    return [feature_dict.get(name, 0.0) for name in FEATURE_NAMES]


# ----------------------------
# Validate Feature Completeness
# ----------------------------
def validate_features(feature_dict):
    """
    Ensures all expected features are present.
    """
    missing = [
        name for name in FEATURE_NAMES
        if name not in feature_dict
    ]

    if missing:
        raise ValueError(f"Missing features: {missing}")

    return True