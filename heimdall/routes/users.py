import names
from flask import Blueprint, jsonify

# from heimdall.models import db
from heimdall.models.user import User


bp = Blueprint("users", __name__)


@bp.route("/", methods=["GET"])
def home():
    def get_random_user_data(user_id=0):
        first_name = names.get_first_name()
        last_name = names.get_last_name()
        return User(
            id=user_id,
            name=f"{first_name} {last_name}",
            email=f"{first_name[0]}.{last_name}@gmail.com".lower(),
        ).to_json()

    data = [get_random_user_data(i + 1) for i in range(10)]
    return jsonify(data)


@bp.route("/new", methods=["GET"])
def create_user():
    """Create a user."""
    # username = request.args.get("user")
    # email = request.args.get("email")
    new_user = User(name="username", email="email")
    # db.session.add(new_user)  # Adds new User record to database
    # db.session.commit()  # Commits all changes
    return jsonify(message=f"New user {new_user} created successfully")
