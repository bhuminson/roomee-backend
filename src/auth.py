import functools

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for, jsonify
)
from werkzeug.security import check_password_hash, generate_password_hash

from . import db_setup

bp = Blueprint('auth', __name__)


@bp.route('/register', methods=['POST'])
def register():
    if request.method == 'POST':
        print(request.json)
        username = request.json['username']
        password = request.json['password']
        firstname = request.json['Firstname']
        lastname = request.json['Lastname']
        nickname = request.json['Nickname']
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

        db = get_db()
        error = None

        if username == '':
            error = 'Username is required.'
        elif password == '':
            error = 'Password is required.'

        # broken
        # elif db.execute(
        #     'SELECT id FROM users WHERE username = ?', (username)
        # ).fetchone() is not None:
        #     error = 'User {} is already registered.'.format(username)

        if error is None:
            db.execute(
                'INSERT INTO users (username, firstname, lastname, nickname, phone, email) VALUES (?, ?, ?, ?, ?, ?)',
                (username, firstname, lastname, nickname, phone, email)
            )
            # broken
            # db.execute(
            #     'INSERT INTO login_info (password) VALUES ( ?)',
            #     (password)
            # )
            db.execute(
                'INSERT INTO filters (age, gender, school, major, school_year, graduation_year, leasing_q, car, pet, clean, noise, drink, smoke, visible_phone, visible_email) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)',
                (age, gender, school, major, school_year, graduation_year, leasing_q,
                 car, pet, clean, noise, drink, smoke, visible_phone, visible_email)
            )
            db.commit()
            db.close()
            resp = jsonify(success=True)
            resp.status_code = 201
            return resp
        return error, 201
    resp = jsonify(success=True)
    resp.status_code = 201
    return resp


@bp.route('/login', methods=('GET', 'POST'))
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        db = get_db()
        error = None
        user = db.execute(
            'SELECT * FROM login WHERE username = ?', (username,)
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
            'SELECT * FROM users WHERE id = ?', (user_id,)
        ).fetchone()


@bp.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('index'))
