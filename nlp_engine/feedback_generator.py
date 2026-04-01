def generate_feedback(keyword_result, structure_result):

    feedback = []

    if keyword_result["score"] > 70:
        feedback.append("Strength: You included several important technical concepts.")
    else:
        missing = ", ".join(keyword_result["missing"])
        feedback.append(f"Weakness: Important keywords missing: {missing}")

    if structure_result["score"] < 60:
        feedback.append("Improvement: Expand your explanation with more sentences.")
    else:
        feedback.append("Strength: Your explanation structure is clear.")

    return " ".join(feedback)