from flask import Flask, Blueprint, request, jsonify
from . import db_setup
import psycopg2

bp = Blueprint('user', __name__)


# This function handles fetching the next user in the db that satisfies the user's filters.
# the user's filters will be passed in as query parameters and the function will use those to find
# matching users in the filters database. it will also have to cross reference the dislikes and likes database
# and avoid showing roomees who are already in those two tables for the user. Also shouldn't show the user.


# @bp.route('/search/<userId>', methods=['GET'])
# def getNextRoomee(userId):
#     filters = request.args
#     optionalFilters = ""
#     for key in filters:
#         if filters[key].isdigit() is False and filters[key] != '':
#             optionalFilters += ' AND f.' + key + '="' + filters[key]+'"'
#     roomee = db.execute('SELECT * \
#                         FROM users u \
#                         JOIN filters AS f ON u.id=f.userId \
#                         WHERE \
#                         (f.age BETWEEN ? AND ?) AND \
#                         (f.graduation_year BETWEEN ? AND ?) AND \
#                         (f.clean BETWEEN ? AND ?) AND \
#                         (f.noise BETWEEN ? AND ?)' + optionalFilters
#                         + ' AND u.id NOT IN ( \
#                             SELECT `like` \
#                             FROM likes \
#                             WHERE userId = ? \
#                         ) \
#                         AND u.id NOT IN ( \
#                             SELECT dislike \
#                             FROM dislikes\
#                             WHERE userId = ? \
#                         ) \
#                         AND u.id <> ?', (filters['min_age'], filters['max_age'],
#                                          filters['min_graduation_year'], filters['max_graduation_year'],
#                                          filters['min_clean'], filters['max_clean'], filters['min_noise'],
#                                          filters['max_noise'], userId, userId, userId)).fetchone()
#     return roomee if roomee is not None else {}


@bp.route('/like/<userId>', methods=['GET', 'POST'])
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
            host="localhost",
            database="roomee",
            user="postgres",
            password=" ")
        cur = conn.cursor()
        if request.method == "GET":
            cur.execute("SELECT users.id, Firstname, Lastname, bio \
                                FROM users \
                                JOIN likes ON users.id=likeId \
                                WHERE userId=%s", [userId])
            likes = cur.fetchall()
            print(likes)
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
                cur.execute("INSERT INTO dislikes (userId, likeId) VALUES(%s, %s)",
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


# @bp.route('/user/<userId>', methods=['GET'])
# def getUserProfile(userId):
#     db = db_setup.get_db()
#     userProfile = db.execute('SELECT * \
#                         FROM users \
#                         JOIN filters on id=filters.userId \
#                         JOIN login_info on id=login_info.userId \
#                         WHERE id=?', (userId)).fetchone()
#     db.close()
#     return userProfile


# @bp.route('/resetDislike/<userId>', methods=['DELETE'])
# def resetDislikes(userId):
#     db = db_setup.get_db()
#     db.execute('DELETE FROM dislikes WHERE userId=?', (userId))
#     db.commit()
#     db.close()
#     resp = jsonify(success=True)
#     resp.status_code = 201
#     return resp
