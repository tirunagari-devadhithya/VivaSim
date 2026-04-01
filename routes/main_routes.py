# Main routes
from flask import Blueprint, render_template

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

@main_bp.route("/profile")
def profile():
    return render_template("profile.html")

@main_bp.route("/settings")
def settings():
    return render_template("settings.html")
