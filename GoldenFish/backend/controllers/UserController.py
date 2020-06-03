from flask_apispec import use_kwargs, marshal_with
from flask import Blueprint, jsonify

from backend.models.User import User
from backend.schemas import UserSchema, AuthSchema
from backend.storage.UserStorage import UserStorage
from backend.app import docs


users = Blueprint('users', __name__)

user_storage = UserStorage()


@users.route('/registration', methods=['POST'])
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
@use_kwargs(UserSchema(only=('email', 'password')))
@marshal_with(AuthSchema)
def authenticate(**kwargs):
    try:
        user = user_storage.authenticate(**kwargs)
        token = user.get_token()
    except Exception as e:
        return {'message': str(e)}, 400
    return {'access_token': token}


@users.errorhandler(422)
def error_handlers(err):
    headers = err.data.get('headers', None)
    messages = err.data.get('messages', ['Invalid request'])
    if headers:
        return jsonify({'message': messages}), 400, headers
    else:
        return jsonify({'message': messages}), 400


docs.register(register, blueprint='users')
docs.register(authenticate, blueprint='users')