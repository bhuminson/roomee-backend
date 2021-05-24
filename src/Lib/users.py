from src.db import executeQuery
from src.constants import testing
from psycopg2 import sql

usersTable = "test_users" if testing else "users"
filtersTable = "test_filters" if testing else "filters"


def createNewUser(data):
    username = data['username']
    firstname = data['firstname']
    lastname = data['lastname']
    nickname = data['nickname']
    phone = data['phone']
    email = data['email']
    return executeQuery('INSERT INTO %s (username, firstname, lastname, nickname, phone, email) VALUES (%s, %s, %s, %s, %s, %s)',
                        [usersTable, username, firstname, lastname, nickname, phone, email], commit=True)


def getNextMatchingRoomee(userId, filters):
    categoricalFilters = ""
    for key in filters:
        if filters[key].isdigit() is False and filters[key] != '':
            categoricalFilters += ' AND f.' + key + '="' + filters[key]+'"'
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
                                FROM likes \
                                WHERE userId = %s \
                            ) \
                            AND u.id NOT IN ( \
                                SELECT dislikeId \
                                FROM dislikes\
                                WHERE userId = %s \
                            ) \
                            AND u.id <> %s').format(sql.Identifier(usersTable), sql.Identifier(filtersTable)),
                        [filters['min_age'], filters['max_age'],
                         filters['min_graduation_year'], filters['max_graduation_year'],
                         filters['min_clean'], filters['max_clean'],
                         filters['min_noise'], filters['max_noise'],
                         userId, userId, userId])


def getUserLikes(userId):
    likes = executeQuery(sql.SQL("SELECT {table}.id, firstname, lastname, bio \
                                FROM {table} \
                                JOIN likes ON {table}.id=likeId \
                                WHERE userId=%s").format(table=sql.Identifier(usersTable)), [userId], fetchall=True)
    likes = [] if likes is None else likes
    return {"data": likes}


def getProfile(userId):
    return executeQuery(sql.SQL('SELECT * \
                        FROM {} \
                        JOIN filters on id=filters.userId \
                        JOIN login_info on id=login_info.userId \
                        WHERE id=%s').format(sql.Identifier(usersTable)), [userId])
