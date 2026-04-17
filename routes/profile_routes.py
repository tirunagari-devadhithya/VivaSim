from flask import Blueprint, render_template
from models.profile_model import get_profile
from models.database import get_connection

profile_bp = Blueprint(
    "profile",
    __name__,
    template_folder="../templates"
)


@profile_bp.route("/profile")
def profile_page():
    """
    Render profile dashboard with scores
    and recent interview sessions.
    """
    print(">>> PROFILE ROUTE HIT <<<")
    print("READ DB:", get_connection().execute("PRAGMA database_list").fetchall())

    profile = get_profile("demo_user")

    # convert Row → dict
    profile_dict = dict(profile) if profile else {}

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT r.id,
               r.total_score,
               r.created_at,
               q.question_text
        FROM responses r
        JOIN questions q
            ON r.question_id = q.id
        ORDER BY r.created_at DESC
        LIMIT 5
    """)

    sessions = cursor.fetchall()

    # convert sessions → list of dicts
    sessions_list = [dict(s) for s in sessions]

    conn.close()

    print("PROFILE OUT:", profile_dict)
    print("SESSIONS OUT:", sessions_list[:2])

    return render_template(
        "profile.html",
        profile=profile_dict,
        sessions=sessions_list
    )