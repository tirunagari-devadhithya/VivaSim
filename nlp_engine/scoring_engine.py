# nlp_engine/scoring_engine.py

from models.database import get_connection

def calculate_total_score(keyword_result, structure_result):
    """
    Calculates the final interview score dynamically querying DB.
    """
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT keyword_weight, structure_weight
        FROM user_settings
        WHERE username = ?
    """, ("demo_user",))

    row = cursor.fetchone()
    conn.close()

    if row:
        kw_weight = row["keyword_weight"]
        st_weight = row["structure_weight"]
    else:
        kw_weight = 0.6
        st_weight = 0.4
        
    # Extract scores safely
    keyword_score = keyword_result.get("score", 0)
    structure_score = structure_result.get("score", 0)

    # Clamp values between 0–100
    keyword_score = max(0, min(keyword_score, 100))
    structure_score = max(0, min(structure_score, 100))

    # Weighted calculation
    score = (
        (keyword_score * kw_weight) +
        (structure_score * st_weight)
    )

    return int(round(score))