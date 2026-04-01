def analyze_keywords(tokens, keywords):
    """
    Compare tokens with expected keywords.
    """

    if isinstance(keywords, str):
        keywords = [k.strip().lower() for k in keywords.split(",")]

    tokens = [t.lower() for t in tokens]

    matched = [k for k in keywords if k in tokens]
    missing = [k for k in keywords if k not in tokens]

    if len(keywords) == 0:
        score = 0
    else:
        score = int((len(matched) / len(keywords)) * 100)

    return {
        "score": score,
        "matched": matched,
        "missing": missing
    }