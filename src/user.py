from flask import Blueprint, request, jsonify
from .db import executeQuery
from src.Lib.users import *

bp = Blueprint('user', __name__)


@bp.route('/search/<userId>', methods=['GET'])
def getNextRoomee(userId):
    filters = request.args
    return getNextMatchingRoomee(userId, filters)


@bp.route('/user/<userId>', methods=['GET'])
def getUserProfile(userId):
    return getProfile(userId)


@ bp.route('/like/<userId>', methods=['GET', 'POST'])
# route parameters
#     liked - boolean
#       whether to add roomee to likes or dislikes table
#     roomeeId - integer
#       the roomee that was liked/disliked
def like(userId):
    if request.method == "GET":
        return getUserLikes(userId)
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


@bp.route('/unlike', methods=['DELETE'])
def unlike():
    userId = request.args['userId']
    roomeeId = request.args['roomeeId']
    return executeQuery('DELETE FROM likes WHERE userId=%s AND likeId=%s', [
        userId, roomeeId], commit=True)


@bp.route('/resetDislike/<userId>', methods=['DELETE'])
def resetDislikes(userId):
    return executeQuery('DELETE FROM dislikes WHERE userId=%s', [userId], commit=True)


@bp.route('/resetLike/<userId>', methods=['DELETE'])
def resetLikes(userId):
    return executeQuery('DELETE FROM likes WHERE userId=%s', [userId], commit=True)
