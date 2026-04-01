# Response model
from models.database import get_connection


def save_response(question_id, answer_text, total_score, feedback):
    """
    Stores a user's evaluated response in the database.
    This ensures that scoring and feedback are permanently traceable.
    """

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO responses (
            question_id,
            answer_text,
            total_score,
            feedback
        )
        VALUES (?, ?, ?, ?)
    """, (
        question_id,
        answer_text,
        total_score,
        feedback
    ))

    conn.commit()
    conn.close()


def get_all_responses():
    """
    Retrieves all past responses.
    Useful for progress tracking and review.
    """

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT id, question_id, answer_text, total_score, feedback, created_at
        FROM responses
        ORDER BY created_at DESC
    """)

    responses = cursor.fetchall()
    conn.close()

    return responses


def get_responses_by_question(question_id):
    """
    Retrieves all responses related to a specific question.
    Helps analyze repeated attempts and improvement.
    """

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT id, answer_text, total_score, feedback, created_at
        FROM responses
        WHERE question_id = ?
        ORDER BY created_at DESC
    """, (question_id,))

    responses = cursor.fetchall()
    conn.close()

    return responses
