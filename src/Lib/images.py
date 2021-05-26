from src.db import executeQuery
from src.constants import testing
from psycopg2 import sql, Binary

pfpTable = "test_profilepics" if testing else "profilepics"


def uploadImage(img):
    return executeQuery(sql.SQL("INSERT INTO {} (img) VALUES (%s)")
                        .format(sql.Identifier(pfpTable)),
                        [Binary(img)], commit=True)


def getUserImage(id):
    return executeQuery(sql.SQL("SELECT ENCODE(img,'base64') FROM {} WHERE id=%s")
                        .format(sql.Identifier(pfpTable)), [id])


def deleteAllImages():
    executeQuery('ALTER SEQUENCE pfpids RESTART WITH 1',
                 [], commit=True)
    return executeQuery(sql.SQL('DELETE FROM {}')
                        .format(sql.Identifier(pfpTable)), [], commit=True)
