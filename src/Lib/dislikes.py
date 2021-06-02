from src.db import executeQuery
import src.constants
from psycopg2 import sql


def getTables():
    return {
        'dislikesTable': "test_dislikes" if src.constants.testing else "dislikes"
    }


def dislikeRoomee(userId, roomee):
    return executeQuery(sql.SQL("INSERT INTO dislikes (userId, dislikeId) VALUES(%s, %s)")
                        .format(sql.Identifier(getTables()['dislikesTable'])),
                        [userId, roomee], commit=True)


def clearDislikesTable(userId):
    return executeQuery(sql.SQL('DELETE FROM {} WHERE userId=%s')
                        .format(sql.Identifier(getTables()['dislikesTable'])),
                        [userId], commit=True)
