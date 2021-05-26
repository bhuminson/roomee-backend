from src.Lib.likes import *
from src.Lib.dislikes import *
from src.Lib.users import *
from flask import Blueprint, request, jsonify


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
            return likeRoomee(userId, roomee)
        return dislikeRoomee(userId, roomee)


@bp.route('/unlike', methods=['DELETE'])
def unlike():
    userId = request.args['userId']
    roomeeId = request.args['roomeeId']
    return removeLike(userId, roomeeId)


@bp.route('/resetDislike/<userId>', methods=['DELETE'])
def resetDislikes(userId):
    return clearDislikesTable(userId)


@bp.route('/resetLike/<userId>', methods=['DELETE'])
def resetLikes(userId):
    return clearLikesTable(userId)
