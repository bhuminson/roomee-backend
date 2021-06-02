from src.db import executeQuery
from src.constants import testing
from psycopg2 import sql

usersTable = "test_users" if testing else "users"
loginTable = "test_login_info" if testing else "login_info"


def getPassword(username):
    return executeQuery(sql.SQL('SELECT password \
                                FROM {} \
                                JOIN {login} on id={login}.userId \
                                WHERE username=%s').format(sql.Identifier(usersTable), login=sql.Identifier(loginTable)),
                        [username]).get('password')


def getId(username):
    return executeQuery(sql.SQL('SELECT id \
                            FROM {} \
                            WHERE username=%s').format(sql.Identifier(usersTable)),
                        [username]).get('id')


def createNewLogin(password):
    return executeQuery(sql.SQL('INSERT INTO {} (password) VALUES (%s)')
                        .format(sql.Identifier(loginTable)),
                        [password], commit=True)


def deleteAllLogins():
    executeQuery('ALTER SEQUENCE loginids RESTART WITH 1',
                 [], commit=True)
    return executeQuery(sql.SQL('DELETE FROM {}')
                        .format(sql.Identifier(loginTable)), [], commit=True)
