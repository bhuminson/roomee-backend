from flask import jsonify, request, Blueprint
from flask_login import (
    UserMixin,
    current_user,
    login_required,
    login_user,
    logout_user,
)
import bcrypt
from src.Lib.login import *

from . import user

bp = Blueprint('login', __name__)


class User(UserMixin):
    ...


def get_user(user_id: int):
    return user.getUserProfile(user_id)


@bp.route("/login", methods=["GET", "POST"])
def login():
    data = request.json['data']
    username = data["username"]
    pword = data["password"].encode("utf-8")

    hashed = bcrypt.hashpw(pword, bcrypt.gensalt())

    pw = getPassword(username)
    id = getId(username)
    if pw is not None:
        if bcrypt.checkpw(pw.encode("utf-8"), hashed):
            user_model = User()
            user_model.id = id
            login_user(user_model)
            return ({"id": id})
    return jsonify({"login": False})


@bp.route("/data", methods=["GET"])
@login_required
def user_data():
    user = get_user(current_user.id)
    return jsonify({"username": user["username"]})


@bp.route("/getsession", methods=["GET"])
def check_session():
    if current_user.is_authenticated:
        return jsonify({"login": True})

    return jsonify({"login": False})


@bp.route("/logout", methods=["GET"])
@login_required
def logout():
    logout_user()
    return jsonify({"logout": True})
