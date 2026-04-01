import sqlite3

DB_PATH = "database/vivasim.db"


def get_connection():
    """
    Create database connection.
    """
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn


def initialize_profile_table():
    """
    Create user profile table if it doesn't exist.
    """
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS user_profile (
            username TEXT PRIMARY KEY,
            communication REAL DEFAULT 0,
            technical_depth REAL DEFAULT 0,
            confidence REAL DEFAULT 0,
            total_sessions INTEGER DEFAULT 0
        )
    """)

    conn.commit()
    conn.close()


def get_profile(username="demo_user"):
    """
    Fetch user profile scores.
    """
    initialize_profile_table()

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "SELECT * FROM user_profile WHERE username=?",
        (username,)
    )

    profile = cursor.fetchone()

    conn.close()

    return profile


def update_profile_scores(username, keyword_score, structure_score, final_score):
    """
    Update running average scores after each interview.
    """

    initialize_profile_table()

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "SELECT * FROM user_profile WHERE username=?",
        (username,)
    )

    row = cursor.fetchone()

    if row is None:
        # First interview attempt
        cursor.execute("""
            INSERT INTO user_profile
            (username, communication, technical_depth, confidence, total_sessions)
            VALUES (?, ?, ?, ?, ?)
        """, (
            username,
            structure_score,
            keyword_score,
            final_score,
            1
        ))

    else:
        previous_sessions = row["total_sessions"]
        new_sessions = previous_sessions + 1

        new_communication = round(
            (
                row["communication"] * previous_sessions
                + structure_score
            ) / new_sessions,
            1
        )

        new_technical_depth = round(
            (
                row["technical_depth"] * previous_sessions
                + keyword_score
            ) / new_sessions,
            1
        )

        new_confidence = round(
            (
                row["confidence"] * previous_sessions
                + final_score
            ) / new_sessions,
            1
        )

        cursor.execute("""
            UPDATE user_profile
            SET communication=?,
                technical_depth=?,
                confidence=?,
                total_sessions=?
            WHERE username=?
        """, (
            new_communication,
            new_technical_depth,
            new_confidence,
            new_sessions,
            username
        ))

    conn.commit()
    conn.close()