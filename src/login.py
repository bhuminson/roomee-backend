# This file was altered/created following the tutorial for backend on
# this website: https://testdriven.io/blog/flask-spa-auth/#frontend-served-separately-cross-domain
# Some parts of this file were moved to __init__.py to make it work

from flask import Flask, jsonify, request, Blueprint
from flask_cors import CORS
from flask_login import (
    LoginManager,
    UserMixin,
    current_user,
    login_required,
    login_user,
    logout_user,
)
from flask_wtf.csrf import CSRFProtect, generate_csrf
import psycopg2
from psycopg2.extras import RealDictCursor

import bcrypt

from . import user

bp = Blueprint('login', __name__)
host = "ec2-23-23-128-222.compute-1.amazonaws.com"
db = "d4n8vp78jra9c"
user = "zdtrqgmvvxojhg"
pw = "7a6b61d68568deb83ecfcd9d14a757ed8966fe017e0917194e065e4a0e340972"


class User(UserMixin):
    ...


def get_user(user_id: int):
    return user.getUserProfile(user_id)


@bp.route("/api/ping", methods=["GET"])
def home():
    return jsonify({"ping": "pong!"})


@bp.route("/api/getcsrf", methods=["GET"])
def get_csrf():
    token = generate_csrf()
    response = jsonify({"detail": "CSRF cookie set"})
    response.headers.set("X-CSRFToken", token)
    return response


@bp.route("/api/login", methods=["GET", "POST"])
def login():
    data = request.json['data']
    username = data["uname"]
    pword = data["pword"].encode("utf-8")

    hashed = bcrypt.hashpw(pword, bcrypt.gensalt())

    conn = None
    actual_password = None
    user_id = None
    try:
        conn = psycopg2.connect(
            host=host,
            database=db,
            user=user,
            password=pw)
        cur = conn.cursor(cursor_factory=RealDictCursor)
        cur.execute('SELECT password \
                                    FROM users \
                                    JOIN login_info on id=login_info.userId \
                                    WHERE username=%s', [username])
        actual_password = cur.fetchone()
        user_id = cur.execute('SELECT id \
                            FROM users \
                            WHERE username=%s', [username]).fetchone()
        print(conn)
        print(cur)
        print("here")
        print(actual_password)
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
            print('Database connection is closed.')

    if actual_password is not None:
        if bcrypt.checkpw(actual_password['password'].encode("utf-8"), hashed):
            user_model = User()
            user_model.id = user_id
            login_user(user_model)
            return jsonify({"login": True})
    return jsonify({"login": False})


@bp.route("/api/data", methods=["GET"])
@login_required
def user_data():
    user = get_user(current_user.id)
    return jsonify({"username": user["username"]})


@bp.route("/api/getsession", methods=["GET"])
def check_session():
    if current_user.is_authenticated:
        return jsonify({"login": True})

    return jsonify({"login": False})


@bp.route("/api/logout", methods=["GET"])
@login_required
def logout():
    logout_user()
    return jsonify({"logout": True})


if __name__ == "__main__":
    app.run(debug=True)
