from flask import Blueprint, render_template
from models.profile_model import get_profile

profile_bp = Blueprint("profile", __name__)


@profile_bp.route("/profile")
def profile():

    profile_data = get_profile("demo_user")

    return render_template(
        "profile.html",
        profile=profile_data
    )