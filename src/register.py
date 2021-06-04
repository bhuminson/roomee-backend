from src.Lib.images import *
from src.Lib.filters import *
from src.Lib.users import *
from src.Lib.login import *
from flask import (Blueprint, request, jsonify)

bp = Blueprint('register', __name__)


@bp.route('/register', methods=['POST', 'PUT'])
def register():
    if request.method == "POST":
        data = request.json
        createNewUser(data)
        createNewUserFilters(data)
        createNewLogin(data['password'])
        resp = jsonify(success=True)
        resp.status_code = 201
        return resp
    elif request.method == "PUT":
        data = request.json
        updateUser(data)
        updateFilters(data)
        resp = jsonify(success=True)
        resp.status_code = 200
        return resp


@bp.route('/image/<userId>', methods=['GET', 'POST', 'PUT'])
def image(userId):
    if request.method == "GET":
        return getUserImage(userId)
    elif request.method in ("POST", "PUT"):
        image = request.files.get('img')
        img = image.read()
        if(getUserImage(userId)):
            return updateImage(img, userId)
        return uploadImage(img, userId)


@bp.route('/resetImages', methods=['DELETE'])
def resetImages():
    return deleteAllImages()
