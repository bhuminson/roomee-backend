import os
from src import auth
from src import user
from src import login
from flask import Flask
from flask_cors import CORS
from flask_login import (
    LoginManager
)
import psycopg2

app = Flask(__name__, static_folder="public",
            instance_relative_config=True)
CORS(app,
    resources={r"*": {"origins": "http://localhost:3000"}},
    expose_headers=["Content-Type", "x-csrftoken"],
    supports_credentials=True,)
app.config.update(
    DEBUG=True,
    SECRET_KEY="secret_sauce",
    SESSION_COOKIE_HTTPONLY=True,
    REMEMBER_COOKIE_HTTPONLY=True,
    SESSION_COOKIE_SAMESITE="Lax",
)

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.session_protection = "strong"
login_manager.login_message = "Welcome to Roomee!"

@login_manager.user_loader
def load_user(id: int):
    user_data = user.getUserProfile(id)
    if user_data:
        user_model = User()
        user_model.id = user_data["id"]
        return user_model
    return None

app.register_blueprint(user.bp)
app.register_blueprint(auth.bp)
app.register_blueprint(login.bp)

@app.route('/')
def index():
    return "<h1>This is the backend for the Roomee app.</h1>"
