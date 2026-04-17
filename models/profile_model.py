from models.database import get_connection


def get_profile(username="demo_user"):
    """
    Fetch user profile scores.
    Creates default row if user doesn't exist.
    """
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT *
        FROM user_profile
        WHERE username = ?
    """, (username,))

    profile = cursor.fetchone()

    if not profile:
        cursor.execute("""
            INSERT INTO user_profile
            (username, communication, technical_depth, confidence, total_sessions)
            VALUES (?, 0, 0, 0, 0)
        """, (username,))
        conn.commit()

        cursor.execute("""
            SELECT *
            FROM user_profile
            WHERE username = ?
        """, (username,))
        profile = cursor.fetchone()

    conn.close()
    return profile


def update_profile_scores(username, keyword_score, structure_score, final_score):
    """
    Update running average profile metrics after each interview.
    """
    conn = get_connection()
    cursor = conn.cursor()

    # Ensure row exists
    cursor.execute("""
        SELECT *
        FROM user_profile
        WHERE username = ?
    """, (username,))

    profile = cursor.fetchone()

    if not profile:
        cursor.execute("""
            INSERT INTO user_profile
            (username, communication, technical_depth, confidence, total_sessions)
            VALUES (?, 0, 0, 0, 0)
        """, (username,))
        conn.commit()

        cursor.execute("""
            SELECT *
            FROM user_profile
            WHERE username = ?
        """, (username,))
        profile = cursor.fetchone()

    current_comm = profile["communication"]
    current_tech = profile["technical_depth"]
    current_conf = profile["confidence"]
    sessions = profile["total_sessions"]

    new_sessions = sessions + 1

    # Running average update
    new_comm = round(
        ((current_comm * sessions) + structure_score) / new_sessions, 2
    )

    new_tech = round(
        ((current_tech * sessions) + keyword_score) / new_sessions, 2
    )

    new_conf = round(
        ((current_conf * sessions) + final_score) / new_sessions, 2
    )

    cursor.execute("""
        UPDATE user_profile
        SET communication = ?,
            technical_depth = ?,
            confidence = ?,
            total_sessions = ?
        WHERE username = ?
    """, (
        new_comm,
        new_tech,
        new_conf,
        new_sessions,
        username
    ))

    conn.commit()
    conn.close()