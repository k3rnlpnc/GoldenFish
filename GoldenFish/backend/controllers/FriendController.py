from flask_apispec import use_kwargs, marshal_with
from flask import Blueprint, jsonify, request
from flask_jwt_extended import jwt_required, get_jwt_identity
from flask_cors import cross_origin

from backend.models.User import User
from backend.models.Gift import Gift
from backend.schemas import UserSchema, DreamSchema, UserPageSchema
from backend.storage.UserStorage import UserStorage
from backend.storage.DreamStorage import DreamStorage


friends = Blueprint('friends', __name__)

user_storage = UserStorage()
dream_storage = DreamStorage()


@friends.route('/users/<int:user_id>', methods=['GET'])
@cross_origin()
@jwt_required
@marshal_with(UserPageSchema)
def get_user_info(user_id):
    try:
        current_id = get_jwt_identity()
        user = user_storage.get_by_id(user_id)
        dreams = dream_storage.get_unfulfilled_dreams(user_id)
        user_info = {}
        user_info['user'] = user
        user_info['dreams'] = []
        for dream in dreams:
            giver_username = ''
            if dream.giver_id:
                giver = user_storage.get_by_id(dream.giver_id)
                giver_username = giver.username
            user_info['dreams'].append({
                'id': dream.id,
                'name': dream.name,
                'giver_id': dream.giver_id,
                'giver_username': giver_username
            })
    except Exception as e:
        return {'message': str(e)}, 400
    return user_info


@friends.route('/users/<int:friend_id>', methods=['POST'])
@cross_origin()
@jwt_required
@use_kwargs(DreamSchema)
@marshal_with(DreamSchema)
def put_in_gift_list(friend_id):
    try:
        user_id = get_jwt_identity()
        data = request.json
        dream = dream_storage.get_by_id(friend_id, data['dream_id'])
        dream_storage.update(dream, giver_id=user_id)
    except Exception as e:
        return {'message': str(e)}, 400
    return dream


@friends.route('/users', methods=['GET'])
@cross_origin()
@jwt_required
@marshal_with(UserSchema(many=True, only=('id', 'username', 'name', 'surname')))
def get_all():
    try:
        users = user_storage.get_all()
    except Exception as e:
        return {'message': str(e)}, 400
    return users


@friends.route('/users', methods=['POST'])
@cross_origin()
@jwt_required
@use_kwargs(UserSchema(only=('username',)))
@marshal_with(UserSchema(many=True, only=('id', 'username', 'name', 'surname')))
def get_search_by_username_list(username):
    try:
        search_list = user_storage.search_by_username(username)
    except Exception as e:
        return {'message': str(e)}, 400
    return search_list


@friends.route('/users', methods=['POST'])
@cross_origin()
@jwt_required
@use_kwargs(UserSchema(only=('id',)))
@marshal_with(UserSchema)
def add_friend(id):
    try:
        sender_id = get_jwt_identity()
        sender = user_storage.get_by_id(sender_id)
        recipient = user_storage.get_by_id(id)
        recipient.friend_requests.append(sender)
        user_storage.update(recipient)
    except Exception as e:
        return {'message': str(e)}, 400
    return ''


@friends.route('/friends', methods=['GET'])
@cross_origin()
@jwt_required
@marshal_with(UserSchema(many=True, only=('id', 'username', 'name', 'surname')))
def get_friends():
    try:
        user_id = get_jwt_identity()
        user_friends = user_storage.get_friends(user_id)
    except Exception as e:
        return {'message': str(e)}, 400
    return user_friends


@friends.route('/friends', methods=['DELETE'])
@cross_origin()
@jwt_required
@use_kwargs(UserSchema(only=('id',)))
@marshal_with(UserSchema)
def delete_friend(id):
    try:
        user_id = get_jwt_identity()
        user = user_storage.get_by_id(user_id)
        friend = user_storage.get_by_id(id)
        user_storage.delete_friend(user, friend)
    except Exception as e:
        return {'message': str(e)}, 400
    return '', 204


@friends.route('/friends/requests', methods=['GET'])
@cross_origin()
@jwt_required
@marshal_with(UserSchema(many=True, only=('id', 'username', 'name', 'surname')))
def get_friend_requests():
    try:
        user_id = get_jwt_identity()
        user_friend_requests = user_storage.get_friend_requests(user_id)
    except Exception as e:
        return {'message': str(e)}, 400
    return user_friend_requests


@friends.route('/friends/requests', methods=['POST'])
@cross_origin()
@jwt_required
@use_kwargs(UserSchema(only=('id',)))
@marshal_with(UserSchema(only=('id', 'username', 'name', 'surname')))
def accept_request(id):
    try:
        user_id = get_jwt_identity()
        user = user_storage.get_by_id(user_id)
        new_friend = user_storage.get_by_id(id)
        user_storage.add_friend(user, new_friend)
        user_storage.delete_request(user, new_friend)
    except Exception as e:
        return {'message': str(e)}, 400
    return new_friend


@friends.route('/friends/requests', methods=['POST'])
@cross_origin()
@jwt_required
@use_kwargs(UserSchema(only=('id',)))
@marshal_with(UserSchema(only=('id', 'username', 'name', 'surname')))
def reject_request(id):
    try:
        user_id = get_jwt_identity()
        user = user_storage.get_by_id(user_id)
        sender = user_storage.get_by_id(id)
        user_storage.delete_request(user, sender)
    except Exception as e:
        return {'message': str(e)}, 400
    return '', 204


from backend.app import docs
docs.register(get_search_by_username_list, blueprint='friends')