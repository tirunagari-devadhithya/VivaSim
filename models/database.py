import sqlite3
import os

# Database config
DB_FOLDER = "database"
DB_NAME = "vivasim.db"
DB_PATH = os.path.join(DB_FOLDER, DB_NAME)


from flask import current_app

def get_connection():
    """
    Create and return SQLite connection.
    """
    db_path = current_app.config.get(
        "DATABASE_PATH",
        DB_PATH
    )

    connection = sqlite3.connect(db_path)
    connection.row_factory = sqlite3.Row
    return connection


def init_db():
    """
    Initialize all required tables and seed question bank.
    """

    # Ensure DB folder exists
    if not os.path.exists(DB_FOLDER):
        os.makedirs(DB_FOLDER)

    conn = get_connection()
    cursor = conn.cursor()

    # ================= QUESTIONS TABLE =================
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS questions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            question_text TEXT NOT NULL,
            keywords TEXT NOT NULL,
            difficulty TEXT NOT NULL
        )
    """)

    # ================= RESPONSES TABLE =================
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS responses (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            question_id INTEGER,
            answer_text TEXT,
            total_score INTEGER,
            feedback TEXT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (question_id) REFERENCES questions(id)
        )
    """)

    # ================= USER PROFILE =================
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS user_profile (
            username TEXT PRIMARY KEY,
            communication REAL DEFAULT 0,
            technical_depth REAL DEFAULT 0,
            confidence REAL DEFAULT 0,
            total_sessions INTEGER DEFAULT 0
        )
    """)

    # ================= USER SETTINGS =================
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS user_settings (
            username TEXT PRIMARY KEY,
            keyword_weight REAL DEFAULT 0.6,
            structure_weight REAL DEFAULT 0.4
        )
    """)

    # ================= QUESTION BANK =================
    questions_data = [

        # EASY
        ("What is object-oriented programming?",
         "oop class object inheritance polymorphism",
         "easy"),

        ("Explain the difference between a list and a tuple in Python.",
         "list tuple mutable immutable python",
         "easy"),

        ("What is a REST API?",
         "rest api http request response client server",
         "easy"),

        ("What is machine learning?",
         "machine learning ai model data training",
         "easy"),

        ("What is a database?",
         "database table records rows columns sql",
         "easy"),

        # MEDIUM
        ("Explain polymorphism in object-oriented programming.",
         "polymorphism inheritance overriding interface example",
         "medium"),

        ("What is the difference between process and thread?",
         "process thread cpu memory concurrency",
         "medium"),

        ("How does a hash table work?",
         "hash key value collision lookup",
         "medium"),

        ("Explain normalization in DBMS.",
         "normalization database redundancy forms dependency",
         "medium"),

        ("Tell me about a challenge you faced and how you solved it.",
         "challenge solution learning example",
         "medium"),

        # HARD
        ("Design a scalable interview evaluation system architecture.",
         "architecture scalability database api load balancing",
         "hard"),

        ("Explain how polymorphism supports runtime flexibility in large systems.",
         "polymorphism runtime dynamic dispatch inheritance abstraction",
         "hard"),

        ("How would you optimize SQL queries for large datasets?",
         "sql indexing joins optimization performance",
         "hard"),

        ("Explain deadlock and its prevention techniques.",
         "deadlock mutual exclusion prevention scheduling",
         "hard"),

        ("How would you design an explainable AI scoring system?",
         "ai explainability scoring model feedback transparency",
         "hard")
    ]

    # Insert questions only if table is empty
    cursor.execute("SELECT COUNT(*) FROM questions")
    count = cursor.fetchone()[0]

    if count == 0:
        for question in questions_data:
            cursor.execute("""
                INSERT INTO questions
                (question_text, keywords, difficulty)
                VALUES (?, ?, ?)
            """, question)

    conn.commit()
    conn.close()