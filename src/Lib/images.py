from src.db import executeQuery
import src.constants
from psycopg2 import sql, Binary


def getTables():
    return {
        'pfpTable': "test_profilepics" if src.constants.testing else "profilepics"
    }


def uploadImage(img):
    return executeQuery(sql.SQL("INSERT INTO {} (img) VALUES (%s)")
                        .format(sql.Identifier(getTables()["test_profilepics"])),
                        [Binary(img)], commit=True)


def getUserImage(id):
    return executeQuery(sql.SQL("SELECT ENCODE(img,'base64') FROM {} WHERE id=%s")
                        .format(sql.Identifier(getTables()["test_profilepics"])), [id])


def deleteAllImages():
    executeQuery('ALTER SEQUENCE pfpids RESTART WITH 1',
                 [], commit=True)
    return executeQuery(sql.SQL('DELETE FROM {}')
                        .format(sql.Identifier(getTables()["test_profilepics"])), [], commit=True)
