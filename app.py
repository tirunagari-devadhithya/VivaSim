"""
╔══════════════════════════════════════════════════════════════════╗
║              VivaSim — Explainable Interview Intelligence       ║
║                         Entry Point: app.py                     ║
╚══════════════════════════════════════════════════════════════════╝
"""

import os
from flask import Flask
from models.database import init_db


def create_app():
    """
    Application factory
    """
    app = Flask(__name__)

    # ================= CONFIG =================
    app.config["SECRET_KEY"] = os.environ.get(
        "SECRET_KEY",
        "vivasim-secret-key-change-in-production"
    )

    BASE_DIR = os.path.abspath(os.path.dirname(__file__))

    app.config["DATABASE_PATH"] = os.path.join(
        BASE_DIR,
        "database",
        "vivasim.db"
    )

    app.config["DEBUG"] = True

    # ================= DATABASE =================
    db_dir = os.path.join(BASE_DIR, "database")
    os.makedirs(db_dir, exist_ok=True)

    with app.app_context():
        init_db()

    # ================= BLUEPRINTS =================
    from routes.main_routes import main_bp
    from routes.interview_routes import interview_bp
    from routes.profile_routes import profile_bp

    app.register_blueprint(main_bp)
    app.register_blueprint(interview_bp)
    app.register_blueprint(profile_bp)

    print("=" * 60)
    print("VivaSim Flask app initialized successfully")
    print("Database:", app.config["DATABASE_PATH"])
    print("=" * 60)

    return app


if __name__ == "__main__":
    app = create_app()

    print("=" * 60)
    print("VivaSim — Explainable Interview Intelligence System")
    print("Running at: http://127.0.0.1:5000")
    print("=" * 60)

    app.run(
        host="0.0.0.0",
        port=5000,
        debug=True
    )