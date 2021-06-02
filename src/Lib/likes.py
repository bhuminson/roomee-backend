from src.db import executeQuery
import src.constants
from psycopg2 import sql


def getTables():
    return {
        'likesTable': "test_likes" if src.constants.testing else "likes"
    }


def likeRoomee(userId, roomee):
    return executeQuery(sql.SQL("INSERT INTO {} (userId, likeId) VALUES(%s, %s)")
                        .format(sql.Identifier(getTables()['likesTable'])),
                        [userId, roomee], commit=True)


def removeLike(userId, roomee):
    return executeQuery(sql.SQL('DELETE FROM {} WHERE userId=%s AND likeId=%s')
                        .format(sql.Identifier(getTables()['likesTable'])),
                        [userId, roomee], commit=True)


def clearLikesTable(userId):
    executeQuery(sql.SQL('DELETE FROM {} WHERE userId=%s')
                 .format(sql.Identifier(getTables()['likesTable'])),
                 [userId], commit=True)
