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
    visible_phone = ''
    visible_email = ''
    return executeQuery(sql.SQL('INSERT INTO {} (age, gender, school, major, school_year, graduation_year, \
                        leasing_q, car, pet, clean, noise, drink, smoke, visible_phone, visible_email) \
                        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)').format(sql.Identifier(getTables()['filtersTable'])),
                        [age, gender, school, major, school_year, graduation_year, leasing_q,
                         car, pet, clean, noise, drink, smoke, visible_phone, visible_email], commit=True)


def deleteAllFilters():
    executeQuery('ALTER SEQUENCE filterids RESTART WITH 1',
                 [], commit=True)
    return executeQuery(sql.SQL('DELETE FROM {}')
                        .format(sql.Identifier(getTables()['filtersTable'])), [], commit=True)
