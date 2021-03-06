from flask_apispec import use_kwargs, marshal_with
from flask import Blueprint, jsonify
from flask_cors import cross_origin
from flask_jwt_extended import jwt_required, get_jwt_identity

from backend.models.User import User
from backend.schemas import UserSchema, AuthSchema
from backend.storage.UserStorage import UserStorage


users = Blueprint('users', __name__)

user_storage = UserStorage()


@users.route('/registration', methods=['POST'])
@cross_origin()
@use_kwargs(UserSchema)
@marshal_with(AuthSchema)
def register(**kwargs):
    try:
        user = User(**kwargs)
        user_storage.save(user)
        token = user.get_token()
    except Exception as e:
        return {'message': str(e)}, 400
    return {'access_token': token}


@users.route('/authentication', methods=['POST'])
@cross_origin()
@use_kwargs(UserSchema(only=('email', 'password')))
@marshal_with(AuthSchema)
def authenticate(**kwargs):
    try:
        user = user_storage.authenticate(**kwargs)
        token = user.get_token()
    except Exception as e:
        return {'message': str(e)}, 400
    return {'access_token': token}


@users.route('/profile', methods=['GET'])
@cross_origin()
@jwt_required
@marshal_with(UserSchema(only=('id', 'email', 'username', 'name', 'surname', 'birthday')))
def get_profile():
    try:
        user_id = get_jwt_identity()
        user = user_storage.get_by_id(user_id)
    except Exception as e:
        return {'message': str(e)}, 400
    return user


@users.route('/profile', methods=['PUT'])
@cross_origin()
@jwt_required
@use_kwargs(UserSchema(only=('email', 'username', 'name', 'surname', 'birthday')))
@marshal_with(UserSchema(only=('email', 'username', 'name', 'surname', 'birthday')))
def update_profile(**kwargs):
    try:
        user_id = get_jwt_identity()
        user = user_storage.get_by_id(user_id)
        user_storage.update(user, **kwargs)
    except Exception as e:
        return {'message': str(e)}, 400
    return user


@users.route('/users', methods=['GET'])
@cross_origin()
@jwt_required
@marshal_with(UserSchema(many=True, only=('id', 'username', 'name', 'surname')))
def get_users():
    try:
        users = user_storage.get_all()
    except Exception as e:
        return {'message': str(e)}, 400
    return users


@users.route('/users/<int:user_id>', methods=['GET'])
@cross_origin()
@jwt_required
@marshal_with(UserSchema(only=('id', 'username', 'name', 'surname', 'birthday')))
def get_user(user_id):
    try:
        user = user_storage.get_by_id(user_id)
    except Exception as e:
        return {'message': str(e)}, 400
    return user


@users.route('/users', methods=['POST'])
@cross_origin()
@jwt_required
@use_kwargs(UserSchema(only=('username',)))
@marshal_with(UserSchema(many=True, only=('id', 'username', 'name', 'surname')))
def get_search_by_username(username):
    try:
        search_list = user_storage.search_by_username(username)
    except Exception as e:
        return {'message': str(e)}, 400
    return search_list


@users.errorhandler(422)
def error_handlers(err):
    headers = err.data.get('headers', None)
    messages = err.data.get('messages', ['Invalid request'])
    if headers:
        return jsonify({'message': messages}), 400, headers
    else:
        return jsonify({'message': messages}), 400


from backend.app import docs
docs.register(register, blueprint='users')
docs.register(authenticate, blueprint='users')
docs.register(get_users, blueprint='users')
docs.register(get_profile, blueprint='users')
docs.register(update_profile, blueprint='users')
docs.register(get_search_by_username, blueprint='users')