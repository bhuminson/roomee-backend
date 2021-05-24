from src.db import executeQuery
from src.constants import testing
from psycopg2 import sql

likesTable = "test_likes" if testing else "likes"


def likeRoomee(userId, roomee):
    return executeQuery(sql.SQL("INSERT INTO {} (userId, likeId) VALUES(%s, %s)")
                        .format(sql.Identifier(likesTable)),
                        [userId, roomee], commit=True)


def removeLike(userId, roomee):
    return executeQuery(sql.SQL('DELETE FROM {} WHERE userId=%s AND likeId=%s')
                        .format(sql.Identifier(likesTable)),
                        [userId, roomee], commit=True)


def resetLikes(userId):
    executeQuery(sql.SQL('DELETE FROM {} WHERE userId=%s')
                 .format(sql.Identifier(likesTable)),
                 [userId], commit=True)
