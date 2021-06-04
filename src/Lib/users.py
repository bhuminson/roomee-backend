from src.db import executeQuery
import src.constants
from psycopg2 import sql


def getTables():
    return {
        'usersTable': "test_users" if src.constants.testing else "users",
        'filtersTable': "test_filters" if src.constants.testing else "filters",
        'likesTable': "test_likes" if src.constants.testing else "likes",
        'dislikesTable': "test_dislikes" if src.constants.testing else "dislikes",
        'loginTable': "test_login_info" if src.constants.testing else "login_info"
    }


def createNewUser(data):
    username = data['username']
    firstname = data['firstname']
    lastname = data['lastname']
    nickname = data['nickname']
    phone = data['phone']
    email = data['email']
    bio = data['bio']
    return executeQuery(sql.SQL('INSERT INTO {} (username, firstname, lastname, nickname, phone, email, bio) VALUES (%s, %s, %s, %s, %s, %s, %s)')
                        .format(sql.Identifier(getTables()['usersTable'])),
                        [username, firstname, lastname, nickname, phone, email, bio], commit=True)


def updateUser(data):
    username = data['username']
    firstname = data['firstname']
    lastname = data['lastname']
    nickname = data['nickname']
    phone = data['phone']
    email = data['email']
    bio = data['bio']
    return executeQuery(sql.SQL('UPDATE {} SET firstname=%s, lastname=%s, nickname=%s, phone=%s, email=%s, bio=%s WHERE username=%s')
                        .format(sql.Identifier(getTables()['usersTable'])),
                        [firstname, lastname, nickname, phone, email, bio, username], commit=True)


def getNextMatchingRoomee(userId, filters):
    categoricalFilters = ""
    for key in filters:
        if filters[key].isdigit() is False and filters[key] != '':
            categoricalFilters += ' AND f.' + key + " = \'" + filters[key]+"\'"
    return executeQuery(sql.SQL('SELECT * \
                            FROM {} u \
                            JOIN {} AS f ON u.id=f.userId \
                            WHERE \
                            (f.age BETWEEN %s AND %s) AND \
                            (f.graduation_year BETWEEN %s AND %s) AND \
                            (f.clean BETWEEN %s AND %s) AND \
                            (f.noise BETWEEN %s AND %s)' + categoricalFilters
                                + ' AND u.id NOT IN ( \
                                SELECT likeId \
                                FROM {} \
                                WHERE userId = %s \
                            ) \
                            AND u.id NOT IN ( \
                                SELECT dislikeId \
                                FROM {}\
                                WHERE userId = %s \
                            ) \
                            AND u.id <> %s').format(sql.Identifier(getTables()['usersTable']),
                                                    sql.Identifier(
                                                        getTables()['filtersTable']),
                                                    sql.Identifier(
                                                        getTables()['likesTable']),
                                                    sql.Identifier(getTables()['dislikesTable'])),
                        [filters['min_age'], filters['max_age'],
                         filters['min_graduation_year'], filters['max_graduation_year'],
                         filters['min_clean'], filters['max_clean'],
                         filters['min_noise'], filters['max_noise'],
                         userId, userId, userId])


def getUserLikes(userId):
    likes = executeQuery(sql.SQL("SELECT {table}.id, firstname, lastname, bio \
                                FROM {table} \
                                JOIN {likes} ON {table}.id=likeId \
                                WHERE userId=%s").format(table=sql.Identifier(getTables()['usersTable']),
                                                         likes=sql.Identifier(getTables()['likesTable'])), [userId], fetchall=True)
    likes = [] if likes is None else likes
    return {"data": likes}


def getProfile(userId):
    return executeQuery(sql.SQL('SELECT * \
                        FROM {users} \
                        JOIN {filters} on id=filters.userId \
                        JOIN {login} on id=login_info.userId \
                        WHERE id=%s').format(users=sql.Identifier(getTables()['usersTable']),
                                             filters=sql.Identifier(
                                                 getTables()['filtersTable']),
                                             login=sql.Identifier(getTables()['loginTable'])), [userId])


def deleteAllUsers():
    executeQuery('ALTER SEQUENCE userids RESTART WITH 1',
                 [], commit=True)
    return executeQuery(sql.SQL('DELETE FROM {}')
                        .format(sql.Identifier(getTables()['usersTable'])), [], commit=True)
