from flask_apispec import use_kwargs, marshal_with
from flask import Blueprint, jsonify, request
from flask_jwt_extended import jwt_required, get_jwt_identity
from flask_cors import cross_origin

from backend.models.User import User
from backend.schemas import UserSchema, DreamSchema
from backend.storage.UserStorage import UserStorage
from backend.storage.DreamStorage import DreamStorage


friends = Blueprint('friends', __name__)

user_storage = UserStorage()
dream_storage = DreamStorage()


@friends.route('/friends/<int:friend_id>', methods=['GET'])
@cross_origin()
@jwt_required
@marshal_with(DreamSchema(many=True, only=('id', 'name', 'giver_username', 'giver_id')))
def get_friend_dreams(friend_id):
    try:
        dreams = dream_storage.get_unfulfilled_dreams(friend_id)
        serialized = []
        for dream in dreams:
            giver_username = None
            if dream.giver_id:
                giver = user_storage.get_by_id(dream.giver_id)
                giver_username = giver.username
            serialized.append({
                'id': dream.id,
                'name': dream.name,
                'giver_id': dream.giver_id,
                'giver_username': giver_username
            })
    except Exception as e:
        return {'message': str(e)}, 400
    return serialized


@friends.route('/friends/<int:dream_id>', methods=['GET'])
@cross_origin()
@jwt_required
@marshal_with(DreamSchema)
def get_friend_dream(dream_id):
    try:
        dream = dream_storage.get_by_id_only(dream_id)
    except Exception as e:
        return {'message': str(e)}, 400
    return dream


@friends.route('/friends/<int:friend_id>/<int:dream_id>', methods=['PUT'])
@cross_origin()
@jwt_required
@marshal_with(DreamSchema)
def put_in_gift_list(friend_id, dream_id):
    try:
        user_id = get_jwt_identity()
        dream = dream_storage.get_by_id(friend_id, dream_id)
        dream_storage.update(dream, giver_id=user_id)
    except Exception as e:
        return {'message': str(e)}, 400
    return dream


@friends.route('/users/<int:user_id>', methods=['PUT'])
@cross_origin()
@jwt_required
@marshal_with(UserSchema)
def add_friend(user_id):
    try:
        sender_id = get_jwt_identity()
        sender = user_storage.get_by_id(sender_id)
        recipient = user_storage.get_by_id(user_id)
        user_storage.add_request(sender, recipient)
    except Exception as e:
        return {'message': str(e)}, 400
    return '', 201


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


@friends.route('/friends/<int:friend_id>', methods=['DELETE'])
@cross_origin()
@jwt_required
def delete_friend(friend_id):
    try:
        user_id = get_jwt_identity()
        user = user_storage.get_by_id(user_id)
        friend = user_storage.get_by_id(friend_id)
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


@friends.route('/friends/requests/<int:sender_id>', methods=['PUT'])
@cross_origin()
@jwt_required
@marshal_with(UserSchema(only=('id', 'username', 'name', 'surname')))
def accept_request(sender_id):
    try:
        user_id = get_jwt_identity()
        user = user_storage.get_by_id(user_id)
        new_friend = user_storage.get_by_id(sender_id)
        user_storage.add_friend(user, new_friend)
        user_storage.delete_request(user, new_friend)
    except Exception as e:
        return {'message': str(e)}, 400
    return new_friend


@friends.route('/friends/requests/<int:sender_id>', methods=['DELETE'])
@cross_origin()
@jwt_required
def reject_request(sender_id):
    try:
        user_id = get_jwt_identity()
        user = user_storage.get_by_id(user_id)
        sender = user_storage.get_by_id(sender_id)
        user_storage.delete_request(user, sender)
    except Exception as e:
        return {'message': str(e)}, 400
    return '', 204


@friends.errorhandler(422)
def error_handlers(err):
    headers = err.data.get('headers', None)
    messages = err.data.get('messages', ['Invalid request'])
    if headers:
        return jsonify({'message': messages}), 400, headers
    else:
        return jsonify({'message': messages}), 400


from backend.app import docs
docs.register(get_friend_dreams, blueprint='friends')
docs.register(put_in_gift_list, blueprint='friends')
docs.register(add_friend, blueprint='friends')
docs.register(get_friends, blueprint='friends')
docs.register(get_friend_requests, blueprint='friends')
docs.register(delete_friend, blueprint='friends')
docs.register(accept_request, blueprint='friends')
docs.register(reject_request, blueprint='friends')