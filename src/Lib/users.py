from src.db import executeQuery
from src.constants import testing

usersTable = "test_users" if testing else "users"
filtersTable = "test_filters" if testing else "filters"


def createNewUser(username, firstname, lastname, nickname, phone, email):
    return executeQuery('INSERT INTO %s (username, firstname, lastname, nickname, phone, email) VALUES (%s, %s, %s, %s, %s, %s)',
                        [usersTable, username, firstname, lastname, nickname, phone, email], commit=True)


def getNextMatchingRoomee(userId, filters):
    categoricalFilters = ""
    for key in filters:
        if filters[key].isdigit() is False and filters[key] != '':
            categoricalFilters += ' AND f.' + key + '="' + filters[key]+'"'
    return executeQuery('SELECT * \
                            FROM %s u \
                            JOIN %s AS f ON u.id=f.userId \
                            WHERE \
                            (f.age BETWEEN %s AND %s) AND \
                            (f.graduation_year BETWEEN %s AND %s) AND \
                            (f.clean BETWEEN %s AND %s) AND \
                            (f.noise BETWEEN %s AND %s)' + categoricalFilters
                        + ' AND u.id NOT IN ( \
                                SELECT likeId \
                                FROM likes \
                                WHERE userId = %s \
                            ) \
                            AND u.id NOT IN ( \
                                SELECT dislikeId \
                                FROM dislikes\
                                WHERE userId = %s \
                            ) \
                            AND u.id <> %s',
                        [usersTable, filtersTable, filters['min_age'], filters['max_age'],
                         filters['min_graduation_year'], filters['max_graduation_year'],
                         filters['min_clean'], filters['max_clean'],
                         filters['min_noise'], filters['max_noise'],
                         userId, userId, userId])


def getUserLikes(userId):
    likes = executeQuery("SELECT %s.id, firstname, lastname, bio \
                                FROM %s \
                                JOIN likes ON %s.id=likeId \
                                WHERE userId=%s", [usersTable, usersTable, usersTable, userId], fetchall=True)
    likes = [] if likes is None else likes
    return {"data": likes}


def getProfile(userId):
    return executeQuery('SELECT * \
                        FROM %s \
                        JOIN filters on id=filters.userId \
                        JOIN login_info on id=login_info.userId \
                        WHERE id=%s', [usersTable, userId])
