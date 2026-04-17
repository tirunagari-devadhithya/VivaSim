def analyze_keywords(tokens, expected_keywords):
    """
    Flexible keyword relevance scoring.
    Supports phrase splitting + partial match.
    """

    token_set = set([token.lower() for token in tokens])

    expected = expected_keywords.lower().split()

    matched = []
    missing = []

    for keyword in expected:
        # partial / exact word match
        if keyword.lower() in token_set:
            matched.append(keyword)
        else:
            # soft stem-like match
            found = any(keyword in token or token in keyword for token in token_set)

            if found:
                matched.append(keyword)
            else:
                missing.append(keyword)

    score = round((len(matched) / len(expected)) * 100)

    return {
        "score": score,
        "matched_keywords": matched,
        "missing_keywords": missing
    }