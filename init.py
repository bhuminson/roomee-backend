import os
from src import db_setup
from src import auth
from src import user
from flask import Flask
from flask_cors import CORS
import psycopg2

app = Flask(__name__, instance_relative_config=True)
CORS(app)
app.register_blueprint(user.bp)
app.register_blueprint(auth.bp)


@app.route('/')
def index():
    return "<h1>This is the backend for the Roomee app.</h1>"


# def connect():
#     """ Connect to the PostgreSQL database server """
#     conn = None
#     try:
#         conn = psycopg2.connect(
#             host="localhost",
#             database="roomee",
#             user="postgres",
#             password=" ")
#         cur = conn.cursor()

#         cur.execute('SELECT * from users')
#         cur.close()
#     except (Exception, psycopg2.DatabaseError) as error:
#         print(error)
#     finally:
#         if conn is not None:
#             conn.close()
#             print('Database connection closed.')


# connect()
