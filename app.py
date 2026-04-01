"""
╔══════════════════════════════════════════════════════════════════╗
║              VivaSim — Explainable Interview Intelligence         ║
║                         Entry Point: app.py                       ║
╚══════════════════════════════════════════════════════════════════╝

This is the main entry point for the VivaSim Flask application.

Responsibilities:
  - Initialize the Flask application
  - Register all route blueprints
  - Set up the database on first run
  - Configure app settings (secret key, debug mode, etc.)
  - Launch the development server

Author: VivaSim Team
Version: 1.0.0
"""

import os
from flask import Flask
from models.database import init_db


# ─────────────────────────────────────────────
# 1. APPLICATION FACTORY
# ─────────────────────────────────────────────

def create_app():
    """
    Application factory function.

    Using a factory pattern makes the app:
      - Easier to test (create fresh instances per test)
      - Easier to configure for different environments
      - Cleanly separates initialization logic

    Returns:
        Flask: Configured Flask application instance
    """

    app = Flask(__name__)

    # ──────────────────────────────────────────
    # 2. CONFIGURATION
    # ──────────────────────────────────────────

    # Secret key is used by Flask for:
    #   - Session signing (tamper-proof cookies)
    #   - CSRF protection (if added later)
    # In production, load this from an environment variable.
    app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'vivasim-secret-key-change-in-production')

    # Path to the SQLite database file.
    # The 'database' folder must exist before running.
    BASE_DIR = os.path.abspath(os.path.dirname(__file__))
    app.config['DATABASE_PATH'] = os.path.join(BASE_DIR, 'database', 'vivasim.db')

    # Debug mode — set to False in production
    app.config['DEBUG'] = True

    # ──────────────────────────────────────────
    # 3. DATABASE INITIALIZATION
    # ──────────────────────────────────────────

    # Ensure the database folder exists
    db_dir = os.path.join(BASE_DIR, 'database')
    os.makedirs(db_dir, exist_ok=True)

    # Initialize the database tables and seed default questions
    # This is safe to call multiple times — it uses CREATE TABLE IF NOT EXISTS
    with app.app_context():
        init_db()

    # ──────────────────────────────────────────
    # 4. BLUEPRINT REGISTRATION
    # ──────────────────────────────────────────

    # Import route blueprints
    # Blueprints allow us to split routes across multiple files cleanly
    from routes.main_routes import main_bp
    from routes.interview_routes import interview_bp

    # Register blueprints with the app
    # 'main_bp'      → handles: /, /about
    # 'interview_bp' → handles: /interview, /submit, /result
    app.register_blueprint(main_bp)
    app.register_blueprint(interview_bp)

    return app


# ─────────────────────────────────────────────
# 5. RUN THE APPLICATION
# ─────────────────────────────────────────────

# This block only runs when you execute: python app.py
# It does NOT run when imported by a test or WSGI server (e.g., Gunicorn)

if __name__ == '__main__':
    app = create_app()

    print("=" * 60)
    print("  VivaSim — Explainable Interview Intelligence System")
    print("  Running at: http://127.0.0.1:5000")
    print("=" * 60)

    app.run(
        host='0.0.0.0',   # Listen on all network interfaces
        port=5000,          # Default Flask port
        debug=True          # Auto-reload on code changes (dev only)
    )
