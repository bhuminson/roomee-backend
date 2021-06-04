from src.db import executeQuery
import src.constants
from psycopg2 import sql, Binary


def getTables():
    return {
        'pfpTable': "test_profilepics" if src.constants.testing else "profilepics"
    }


def uploadImage(img, id):
    return executeQuery(sql.SQL("INSERT INTO {} (userId, img) VALUES (%s, %s)")
                        .format(sql.Identifier(getTables()["pfpTable"])),
                        [id, Binary(img)], commit=True)


def updateImage(img, id):
    return executeQuery(sql.SQL("UPDATE {} SET img=%s WHERE userId=%s")
                        .format(sql.Identifier(getTables()["pfpTable"])),
                        [Binary(img), id], commit=True)


def getUserImage(id):
    return executeQuery(sql.SQL("SELECT ENCODE(img,'base64') FROM {} WHERE userId=%s")
                        .format(sql.Identifier(getTables()["pfpTable"])), [id])


def deleteAllImages():
    executeQuery('ALTER SEQUENCE pfpids RESTART WITH 1',
                 [], commit=True)
    return executeQuery(sql.SQL('DELETE FROM {}')
                        .format(sql.Identifier(getTables()["pfpTable"])), [], commit=True)
