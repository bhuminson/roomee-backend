from src.db import executeQuery
import src.constants
from psycopg2 import sql


def getTables():
    return {
        'filtersTable': "test_filters" if src.constants.testing else "filters"
    }


def createNewUserFilters(data):
    age = data['age']
    gender = data['gender']
    school = data['school']
    major = data['major']
    school_year = data['school_year']
    graduation_year = data['graduation_year']
    leasing_q = data['leasing_q']
    car = data['car']
    pet = data['pet']
    clean = data['clean']
    noise = data['noise']
    drink = data['drink']
    smoke = data['smoke']
    drugs = data['drugs']
    visible_phone = ''
    visible_email = ''
    return executeQuery(sql.SQL('INSERT INTO {} (age, gender, school, major, school_year, graduation_year, \
                        leasing_q, car, pet, clean, noise, drink, smoke, drugs, visible_phone, visible_email) \
                        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)').format(sql.Identifier(getTables()['filtersTable'])),
                        [age, gender, school, major, school_year, graduation_year, leasing_q,
                         car, pet, clean, noise, drink, smoke, drugs, visible_phone, visible_email], commit=True)


def updateFilters(data):
    id = data['id']
    age = data['age']
    gender = data['gender']
    school = data['school']
    major = data['major']
    school_year = data['school_year']
    graduation_year = data['graduation_year']
    leasing_q = data['leasing_q']
    car = data['car']
    pet = data['pet']
    clean = data['clean']
    noise = data['noise']
    drink = data['drink']
    smoke = data['smoke']
    drugs = data['drugs']
    visible_phone = ''
    visible_email = ''
    return executeQuery(sql.SQL('UPDATE {} SET age=%s, gender=%s, school=%s, major=%s, school_year=%s, graduation_year=%s, \
                        leasing_q=%s, car=%s, pet=%s, clean=%s, noise=%s, drink=%s, smoke=%s, drugs=%s, visible_phone=%s, visible_email=%s \
                        WHERE userId=%s').format(sql.Identifier(getTables()['filtersTable'])),
                        [age, gender, school, major, school_year, graduation_year, leasing_q,
                         car, pet, clean, noise, drink, smoke, drugs, visible_phone, visible_email, id], commit=True)


def deleteAllFilters():
    executeQuery('ALTER SEQUENCE filterids RESTART WITH 1',
                 [], commit=True)
    return executeQuery(sql.SQL('DELETE FROM {}')
                        .format(sql.Identifier(getTables()['filtersTable'])), [], commit=True)
