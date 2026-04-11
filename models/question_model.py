from models.database import get_connection


def get_all_questions():
    """
    Return all interview questions.
    """
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT id, question_text, keywords, difficulty
        FROM questions
        ORDER BY id
    """)

    questions = cursor.fetchall()
    conn.close()

    return questions


def get_random_questions(limit=3):
    """
    Return random questions from all difficulty levels.
    """
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT id, question_text, keywords, difficulty
        FROM questions
        ORDER BY RANDOM()
        LIMIT ?
    """, (limit,))

    questions = cursor.fetchall()
    conn.close()

    return questions


def get_questions_by_difficulty(level, limit=3):
    """
    Return random questions by selected difficulty.
    level -> easy / medium / hard
    """
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT id, question_text, keywords, difficulty
        FROM questions
        WHERE difficulty = ?
        ORDER BY RANDOM()
        LIMIT ?
    """, (level.lower(), limit))

    questions = cursor.fetchall()
    conn.close()

    return questions


def get_question_by_id(question_id):
    """
    Return question by ID.
    """
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT id, question_text, keywords, difficulty
        FROM questions
        WHERE id = ?
    """, (question_id,))

    question = cursor.fetchone()
    conn.close()

    return question