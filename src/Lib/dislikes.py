from src.db import executeQuery
from src.constants import testing
from psycopg2 import sql

dislikesTable = "test_likes" if testing else "likes"


def dislikeRoomee(userId, roomee):
    return executeQuery(sql.SQL("INSERT INTO {} (userId, likeId) VALUES(%s, %s)")
                        .format(sql.Identifier(dislikesTable)),
                        [userId, roomee], commit=True)


def resetDislikes(userId):
    executeQuery(sql.SQL('DELETE FROM {} WHERE userId=%s')
                 .format(sql.Identifier(dislikesTable)),
                 [userId], commit=True)
