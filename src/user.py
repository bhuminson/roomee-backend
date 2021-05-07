from flask import Flask, Blueprint, request, jsonify
import psycopg2
from psycopg2.extras import RealDictCursor
import os

bp = Blueprint('user', __name__)
host = "ec2-18-215-111-67.compute-1.amazonaws.com"
db = "dbv08kj3kcvmh2"
user = "ejhswicwaijxhi"
pw = "b6d132d6465d2a329db0a0e1365f67319ab8ddc71785f61dc75f6fe460e17078"

# This function handles fetching the next user in the db that satisfies the user's filters.
# the user's filters will be passed in as query parameters and the function will use those to find
# matching users in the filters database. it will also have to cross reference the dislikes and likes database
# and avoid showing roomees who are already in those two tables for the user. Also shouldn't show the user.


@bp.route('/search/<userId>', methods=['GET'])
def getNextRoomee(userId):
    conn = None
    res = {}
    filters = request.args
    optionalFilters = ""
    try:
        conn = psycopg2.connect(
            host=host,
            database=db,
            user=user,
            password=pw)
        cur = conn.cursor(cursor_factory=RealDictCursor)
        for key in filters:
            if filters[key].isdigit() is False and filters[key] != '':
                optionalFilters += ' AND f.' + key + '="' + filters[key]+'"'
        cur.execute('SELECT * \
                            FROM users u \
                            JOIN filters AS f ON u.id=f.userId \
                            WHERE \
                            (f.age BETWEEN %s AND %s) AND \
                            (f.graduation_year BETWEEN %s AND %s) AND \
                            (f.clean BETWEEN %s AND %s) AND \
                            (f.noise BETWEEN %s AND %s)' + optionalFilters
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
                            AND u.id <> %s', [filters['min_age'], filters['max_age'],
                                              filters['min_graduation_year'], filters['max_graduation_year'],
                                              filters['min_clean'], filters['max_clean'], filters['min_noise'],
                                              filters['max_noise'], userId, userId, userId])
        roomee = cur.fetchone()
        print(roomee)
        res = roomee if roomee is not None else {}
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
            print('Database connection closed.')
        return res


@ bp.route('/like/<userId>', methods=['GET', 'POST'])
# route parameters
#     liked - boolean
#       whether to add roomee to likes or dislikes table
#     roomeeId - integer
#       the roomee that was liked/disliked
def like(userId):
    conn = None
    res = None
    try:
        conn = psycopg2.connect(
            host=host,
            database=db,
            user=user,
            password=pw)
        cur = conn.cursor(cursor_factory=RealDictCursor)
        if request.method == "GET":
            cur.execute("SELECT users.id, Firstname, Lastname, bio \
                                FROM users \
                                JOIN likes ON users.id=likeId \
                                WHERE userId=%s", [userId])
            likes = cur.fetchall()
            likes = [] if likes is None else likes
            res = {"data": likes}
        elif request.method == "POST":
            liked = request.args.get('liked')
            roomee = request.args.get('roomeeId')
            if not liked or not roomee:
                resp = jsonify(success=False)
                resp.status_code = 500
                res = resp
            if liked == "true":
                cur.execute("INSERT INTO likes (userId, likeId) VALUES(%s, %s)",
                            [userId, roomee])
            else:
                cur.execute("INSERT INTO dislikes (userId, dislikeId) VALUES(%s, %s)",
                            [userId, roomee])
            conn.commit()
            resp = jsonify(success=True)
            resp.status_code = 201
            res = resp
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
            print('Database connection closed.')
        return res


@bp.route('/user/<userId>', methods=['GET'])
def getUserProfile(userId):
    res = None
    try:
        conn = psycopg2.connect(
            host=host,
            database=db,
            user=user,
            password=pw)
        cur = conn.cursor(cursor_factory=RealDictCursor)
        cur.execute('SELECT * \
                        FROM users \
                        JOIN filters on id=filters.userId \
                        JOIN login_info on id=login_info.userId \
                        WHERE id=?', (userId))
        res = cur.fetchone()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
            print('Database connection closed.')
        return res


@bp.route('/resetDislike/<userId>', methods=['DELETE'])
def resetDislikes(userId):
    res = None
    try:
        conn = psycopg2.connect(
            host=host,
            database=db,
            user=user,
            password=pw)
        cur = conn.cursor(cursor_factory=RealDictCursor)
        cur.execute('DELETE FROM dislikes WHERE userId=%s', [userId])
        conn.commit()
        resp = jsonify(success=True)
        resp.status_code = 201
        res = resp
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
            print('Database connection closed.')
        return res
