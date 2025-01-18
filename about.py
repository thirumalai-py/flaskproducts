# about.py
from flask import Blueprint, render_template

# Define a Blueprint for the about page
about_bp = Blueprint("about", __name__, template_folder="templates")

@about_bp.route("/about")
def about():
    return render_template("templates/about.html")
