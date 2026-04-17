# Main routes
from flask import Blueprint, render_template, request
from models.database import get_connection

# Create a Blueprint for main routes
main_bp = Blueprint(
    "main",
    __name__,
    template_folder="../templates"
)

@main_bp.route("/")
def index():
    """
    Landing page of VivaSim.
    Acts as the entry point for the interview simulation.
    """
    return render_template("index.html")

@main_bp.route("/settings", methods=["GET", "POST"])
def settings():
    if request.method == "POST":
        language = request.form.get("language")
        difficulty = request.form.get("difficulty")
        category = request.form.get("category")
        keyword_weight = float(request.form.get("keyword_weight", 0.6))
        structure_weight = float(request.form.get("structure_weight", 0.4))

        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("""
            INSERT INTO user_settings (username, keyword_weight, structure_weight)
            VALUES (?, ?, ?)
            ON CONFLICT(username) DO UPDATE SET
                keyword_weight = excluded.keyword_weight,
                structure_weight = excluded.structure_weight
        """, ("demo_user", keyword_weight, structure_weight))

        conn.commit()
        conn.close()

        print("✅ SETTINGS SAVED:", language, difficulty, category, keyword_weight, structure_weight)

    return render_template("settings.html")
