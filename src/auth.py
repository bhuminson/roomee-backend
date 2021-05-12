import functools
from .constants import host, db, user, pw
from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for, jsonify
)
from werkzeug.security import check_password_hash, generate_password_hash
import psycopg2
from psycopg2.extras import RealDictCursor
import json

bp = Blueprint('auth', __name__)


@bp.route('/register', methods=['POST'])
def register():
    res = None
    try:
        conn = psycopg2.connect(
            host=host,
            database=db,
            user=user,
            password=pw)
        cur = conn.cursor(cursor_factory=RealDictCursor)
        username = request.json['username']
        password = request.json['password']
        firstname = request.json['firstname']
        lastname = request.json['lastname']
        nickname = request.json['nickname']
        phone = request.json['phone']
        email = request.json['email']
        age = request.json['age']
        gender = request.json['gender']
        school = request.json['school']
        major = request.json['major']
        school_year = request.json['school_year']
        graduation_year = request.json['graduation_year']
        leasing_q = request.json['leasing_q']
        car = request.json['car']
        pet = request.json['pet']
        clean = request.json['clean']
        noise = request.json['noise']
        drink = request.json['drink']
        smoke = request.json['smoke']
        visible_phone = ''
        visible_email = ''

        error = None

        if username == '':
            error = 'Username is required.'
        elif password == '':
            error = 'Password is required.'

        # # broken
        # # elif db.execute(
        # #     'SELECT id FROM users WHERE username = %s', (username)
        # # ).fetchone() is not None:
        # #     error = 'User {} is already registered.'.format(username)

        if error is None:
            cur.execute(
                'INSERT INTO users (username, firstname, lastname, nickname, phone, email) VALUES (%s, %s, %s, %s, %s, %s)',
                [username, firstname, lastname, nickname, phone, email]
            )
            # broken
            # db.execute(
            #     'INSERT INTO login_info (password) VALUES ( %s)',
            #     (password)
            # )
            cur.execute(
                'INSERT INTO filters (age, gender, school, major, school_year, graduation_year, leasing_q, car, pet, clean, noise, drink, smoke, visible_phone, visible_email) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)',
                [age, gender, school, major, school_year, graduation_year, leasing_q,
                 car, pet, clean, noise, drink, smoke, visible_phone, visible_email]
            )
            conn.commit()
            resp = jsonify(success=True)
            resp.status_code = 201
            res = resp
            print("posted new user")
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
            print('Database connection closed.')
        return res


@bp.route('/image', methods=['GET', 'POST'])
def image():
    conn = None
    res = None
    image = request.files.get('img')
    try:
        conn = psycopg2.connect(
            host=host,
            database=db,
            user=user,
            password=pw)
        cur = conn.cursor(cursor_factory=RealDictCursor)
        if request.method == "GET":
            print("getting profile image")
            cur.execute("SELECT ENCODE(img,'base64') FROM profilepics")
            pic = cur.fetchone()
            print(pic)
            res = {"img": pic}
        elif request.method == "POST":
            img = image.read()
            print(psycopg2.Binary(img))
            cur.execute("INSERT INTO profilepics (img) VALUES (%s)",
                        [psycopg2.Binary(img)])
            conn.commit()
            resp = jsonify(success=True)
            resp.status_code = 201
            res = resp
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
            print('Database connection closed.')
        return res


@bp.route('/login', methods=('GET', 'POST'))
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        db = get_db()
        error = None
        user = db.execute(
            'SELECT * FROM login WHERE username = %s', (username,)
        ).fetchone()

        if user is None:
            error = 'Incorrect username.'
        elif not check_password_hash(user['password'], password):
            error = 'Incorrect password.'

        if error is None:
            session.clear()
            session['user_id'] = user['id']
            return redirect(url_for('index'))

        flash(error)

    return 'Login Page'


@bp.before_app_request
def load_logged_in_user():
    user_id = session.get('user_id')

    if user_id is None:
        g.user = None
    else:
        g.user = get_db().execute(
            'SELECT * FROM users WHERE id = %s', (user_id,)
        ).fetchone()


@bp.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('index'))
