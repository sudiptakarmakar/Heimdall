from flask import Blueprint, jsonify


bp = Blueprint("home", __name__)


@bp.route("/", methods=["GET", "POST"])
def home():
    return jsonify(message="Hello from home")
