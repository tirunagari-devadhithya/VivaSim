# Database helper
import sqlite3
import os

# Path to SQLite database
DB_FOLDER = "database"
DB_NAME = "vivasim.db"
DB_PATH = os.path.join(DB_FOLDER, DB_NAME)


def get_connection():
    """
    Creates and returns a connection to the SQLite database.
    Using a single function ensures consistent DB access.
    """
    connection = sqlite3.connect(DB_PATH)
    connection.row_factory = sqlite3.Row
    return connection


def init_db():
    """
    Initializes database and required tables.
    This function runs once when the application starts.
    """

    # Ensure database folder exists
    if not os.path.exists(DB_FOLDER):
        os.makedirs(DB_FOLDER)

    conn = get_connection()
    cursor = conn.cursor()

    # Questions table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS questions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            question_text TEXT NOT NULL,
            category TEXT,
            difficulty TEXT,
            keywords TEXT
        )
    """)

    # Responses table
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

    # Skill profile table (important for explainability)
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS skill_profile (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            communication REAL,
            technical REAL,
            confidence REAL
        )
    """)
    cursor.execute("""
        INSERT OR IGNORE INTO questions
        (id, question_text, category, difficulty, keywords)
        VALUES
        (1, 'What is REST API?',
         'Technical', 'Medium',
         'rest api client server http'),

        (2, 'Explain Object-Oriented Programming.',
         'Technical', 'Medium',
         'class object inheritance polymorphism encapsulation')
    """)
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
