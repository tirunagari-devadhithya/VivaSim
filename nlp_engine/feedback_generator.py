def generate_feedback(keyword_result, structure_result):
    """
    Generate explainable feedback based on keyword
    and structure analysis.
    """

    feedback_points = []

    # Safely read missing keywords
    missing_keywords = keyword_result.get(
        "missing_keywords",
        []
    )

    matched_keywords = keyword_result.get(
        "matched_keywords",
        []
    )

    structure_score = structure_result.get(
        "score",
        0
    )

    # Keyword feedback
    if missing_keywords:
        missing = ", ".join(missing_keywords)

        feedback_points.append(
            f"Weakness: Important keywords missing: {missing}"
        )

    if matched_keywords:
        feedback_points.append(
            "Strength: You covered important concepts."
        )

    # Structure feedback
    if structure_score >= 80:
        feedback_points.append(
            "Strength: Your answer structure is clear and concise."
        )

    elif structure_score >= 50:
        feedback_points.append(
            "Improvement: Add slightly more detail for better clarity."
        )

    else:
        feedback_points.append(
            "Improvement: Expand your explanation with more sentences."
        )

    return " | ".join(feedback_points)