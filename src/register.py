
from src.db import executeQuery
from flask import (Blueprint, request)
import psycopg2

bp = Blueprint('register', __name__)


@bp.route('/register', methods=['POST'])
def register():
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

    if error is None:
        executeQuery('INSERT INTO users (username, firstname, lastname, nickname, phone, email) VALUES (%s, %s, %s, %s, %s, %s)',
                     [username, firstname, lastname, nickname, phone, email], commit=True)
        return executeQuery('INSERT INTO filters (age, gender, school, major, school_year, graduation_year, leasing_q, car, pet, clean, noise, drink, smoke, visible_phone, visible_email) \
                        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)',
                            [age, gender, school, major, school_year, graduation_year, leasing_q,
                             car, pet, clean, noise, drink, smoke, visible_phone, visible_email], commit=True)


@bp.route('/image/<userId>', methods=['GET', 'POST'])
def image(userId):
    if request.method == "GET":
        img = executeQuery(
            "SELECT ENCODE(img,'base64') FROM profilepics WHERE id=%s", [userId])
        return {"img": img}
    elif request.method == "POST":
        image = request.files.get('img')
        img = image.read()
        return executeQuery("INSERT INTO profilepics (img) VALUES (%s)",
                            [psycopg2.Binary(img)], commit=True)
