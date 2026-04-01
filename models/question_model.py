# models/question_model.py

import sqlite3
from models.database import get_connection


def insert_default_questions():
    """
    Inserts default interview questions if table is empty.
    """

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT COUNT(*) FROM questions")
    count = cursor.fetchone()[0]

    if count == 0:
        cursor.execute("""
            INSERT INTO questions (question_text, category, difficulty, keywords)
            VALUES (?, ?, ?, ?)
        """, (
            "Explain polymorphism in object-oriented programming.",
            "Technical",
            "Medium",
            "polymorphism,inheritance,override,example"
        ))

        cursor.execute("""
            INSERT INTO questions (question_text, category, difficulty, keywords)
            VALUES (?, ?, ?, ?)
        """, (
            "Tell me about a challenge you faced and how you solved it.",
            "Behavioral",
            "Easy",
            "challenge,solution,learning,example"
        ))

    conn.commit()
    conn.close()


def get_all_questions():
    """
    Returns all interview questions in order.
    """

    conn = get_connection()
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()

    cursor.execute("""
        SELECT id, question_text, category, difficulty, keywords
        FROM questions
        ORDER BY id
    """)

    questions = cursor.fetchall()
    conn.close()
    return questions


def get_random_questions(limit=3):
    """
    Returns a specified number of random questions.
    """

    conn = get_connection()
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()

    cursor.execute("""
        SELECT id, question_text, category, difficulty, keywords
        FROM questions
        ORDER BY RANDOM()
        LIMIT ?
    """, (limit,))

    questions = cursor.fetchall()
    conn.close()
    return questions


def get_question_by_id(question_id):
    """
    Returns a specific question by ID.
    """
    conn = get_connection()
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()

    cursor.execute("""
        SELECT id, question_text, category, difficulty, keywords
        FROM questions
        WHERE id = ?
    """, (question_id,))

    question = cursor.fetchone()
    conn.close()
    return question
