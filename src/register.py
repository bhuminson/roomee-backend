from src.Lib.images import *
from src.Lib.filters import *
from src.Lib.users import *
from flask import (Blueprint, request, jsonify)

bp = Blueprint('register', __name__)


@bp.route('/register', methods=['POST'])
def register():
    data = request.json
    createNewUser(data)
    createNewUserFilters(data)
    resp = jsonify(success=True)
    resp.status_code = 200
    return resp


@bp.route('/image/<userId>', methods=['GET', 'POST'])
def image(userId):
    if request.method == "GET":
        return getUserImage(userId)
    elif request.method == "POST":
        image = request.files.get('img')
        img = image.read()
        return uploadImage(img)


@bp.route('/resetImages', methods=['DELETE'])
def resetImages():
    return deleteAllImages()
