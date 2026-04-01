# nlp_engine/scoring_engine.py

def calculate_total_score(keyword_result, structure_result):
    """
    Calculates the final interview score using rule-based weighting.

    Inputs
    -------
    keyword_result : dict
        Output from keyword_analysis
    structure_result : dict
        Output from structure_analysis

    Returns
    -------
    int
        Final score between 0 and 100
    """

    # Weight configuration (transparent for viva explanation)
    KEYWORD_WEIGHT = 0.6
    STRUCTURE_WEIGHT = 0.4

    # Extract scores safely
    keyword_score = keyword_result.get("score", 0)
    structure_score = structure_result.get("score", 0)

    # Clamp values between 0–100
    keyword_score = max(0, min(keyword_score, 100))
    structure_score = max(0, min(structure_score, 100))

    # Weighted calculation
    total_score = (
        (keyword_score * KEYWORD_WEIGHT) +
        (structure_score * STRUCTURE_WEIGHT)
    )

    return round(total_score)