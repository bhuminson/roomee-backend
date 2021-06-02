from src.db import executeQuery
import src.constants
from psycopg2 import sql


def getTables():
    return {
        'usersTable': "test_users" if src.constants.testing else "users",
        'loginTable': "test_login_info" if src.constants.testing else "login_info"
    }


def getPassword(username):
    return executeQuery(sql.SQL('SELECT password \
                                FROM {} \
                                JOIN {login} on id={login}.userId \
                                WHERE username=%s').format(sql.Identifier(getTables()['usersTable']), login=sql.Identifier(getTables()['loginTable'])),
                        [username]).get('password')


def getId(username):
    return executeQuery(sql.SQL('SELECT id \
                            FROM {} \
                            WHERE username=%s').format(sql.Identifier(getTables()['usersTable'])),
                        [username]).get('id')


def createNewLogin(password):
    return executeQuery(sql.SQL('INSERT INTO {} (password) VALUES (%s)')
                        .format(sql.Identifier(getTables()['loginTable'])),
                        [password], commit=True)


def deleteAllLogins():
    executeQuery('ALTER SEQUENCE loginids RESTART WITH 1',
                 [], commit=True)
    return executeQuery(sql.SQL('DELETE FROM {}')
                        .format(sql.Identifier(getTables()['loginTable'])), [], commit=True)
