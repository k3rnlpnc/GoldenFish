from flask_apispec import use_kwargs, marshal_with
from flask import Blueprint, jsonify, request
from flask_jwt_extended import jwt_required, get_jwt_identity

from backend.models.User import User
from backend.schemas import UserSchema
from backend.storage.UserStorage import UserStorage
from backend.storage.FriendStorage import FriendStorage


friends = Blueprint('friends', __name__)

user_storage = UserStorage()
friends_storage = FriendStorage()


@friends.route('/search', methods=['GET'])
@jwt_required
@marshal_with(UserSchema(many=True))
def get_search_by_username_list():
    try:
        username = request.args.get('username')
        search_list = user_storage.search_by_username(username)
    except Exception as e:
        return {'message': str(e)}, 400
    return search_list


@friends.route('/friends', methods=['GET'])
@jwt_required
@marshal_with(UserSchema(many=True))
def get_friends():
    try:
        user_id = get_jwt_identity()
        user_friends = user_storage.get_friends(user_id)
    except Exception as e:
        return {'message': str(e)}, 400
    return user_friends


@friends.route('/friends/requests', methods=['GET'])
@jwt_required
@marshal_with(UserSchema(many=True))
def get_friend_requests():
    try:
        user_id = get_jwt_identity()
        user_friend_requests = user_storage.get_friend_requests(user_id)
    except Exception as e:
        return {'message': str(e)}, 400
    return user_friend_requests

