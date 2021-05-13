from flask import Flask, Blueprint, request, jsonify
from .db import executeQuery

bp = Blueprint('user', __name__)


@bp.route('/search/<userId>', methods=['GET'])
def getNextRoomee(userId):
    # NOT SECURE NEEDS TO BE FIXED SOON
    filters = request.args
    optionalFilters = ""
    for key in filters:
        if filters[key].isdigit() is False and filters[key] != '':
            optionalFilters += ' AND f.' + key + '="' + filters[key]+'"'
    return executeQuery('SELECT * \
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
                            AND u.id <> %s',
                        [filters['min_age'], filters['max_age'],
                         filters['min_graduation_year'], filters['max_graduation_year'],
                         filters['min_clean'], filters['max_clean'],
                         filters['min_noise'], filters['max_noise'],
                         userId, userId, userId])


@ bp.route('/like/<userId>', methods=['GET', 'POST'])
# route parameters
#     liked - boolean
#       whether to add roomee to likes or dislikes table
#     roomeeId - integer
#       the roomee that was liked/disliked
def like(userId):
    if request.method == "GET":
        likes = executeQuery("SELECT users.id, firstname, lastname, bio \
                                FROM users \
                                JOIN likes ON users.id=likeId \
                                WHERE userId=%s", [userId], fetchall=True)
        likes = [] if likes is None else likes
        return {"data": likes}
    elif request.method == "POST":
        liked = request.args.get('liked')
        roomee = request.args.get('roomeeId')
        if not liked or not roomee:
            resp = jsonify(success=False)
            resp.status_code = 500
        if liked == "true":
            return executeQuery("INSERT INTO likes (userId, likeId) VALUES(%s, %s)",
                                [userId, roomee], commit=True)
        return executeQuery("INSERT INTO dislikes (userId, dislikeId) VALUES(%s, %s)",
                            [userId, roomee], commit=True)


@bp.route('/user/<userId>', methods=['GET'])
def getUserProfile(userId):
    return executeQuery('SELECT * \
                        FROM users \
                        JOIN filters on id=filters.userId \
                        JOIN login_info on id=login_info.userId \
                        WHERE id=%s', [userId])


@bp.route('/resetDislike/<userId>', methods=['DELETE'])
def resetDislikes(userId):
    return executeQuery('DELETE FROM dislikes WHERE userId=%s', [userId], commit=True)


@bp.route('/unlike', methods=['DELETE'])
def unlike():
    userId = request.args['userId']
    roomeeId = request.args['roomeeId']
    return executeQuery('DELETE FROM likes WHERE userId=%s AND likeId=%s', [
        userId, roomeeId], commit=True)
