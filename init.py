from src import register
from src import user
from flask import Flask
from flask_cors import CORS

app = Flask(__name__, instance_relative_config=True)
CORS(app)
app.register_blueprint(user.bp)
app.register_blueprint(register.bp)


@app.route('/')
def index():
    return "<h1>This is the backend for the Roomee app.</h1>"
