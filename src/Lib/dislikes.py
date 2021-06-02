from src.db import executeQuery
from src.constants import testing
from psycopg2 import sql

dislikesTable = "test_dislikes" if testing else "dislikes"


def dislikeRoomee(userId, roomee):
    return executeQuery(sql.SQL("INSERT INTO dislikes (userId, dislikeId) VALUES(%s, %s)")
                        .format(sql.Identifier(dislikesTable)),
                        [userId, roomee], commit=True)


def clearDislikesTable(userId):
    return executeQuery(sql.SQL('DELETE FROM {} WHERE userId=%s')
                        .format(sql.Identifier(dislikesTable)),
                        [userId], commit=True)
