from flask import Blueprint, jsonify
from flask_apispec import use_kwargs, marshal_with
from flask_jwt_extended import jwt_required, get_jwt_identity

from backend.models.Dream import Dream
from backend.schemas import DreamSchema
from backend.storage.DreamStorage import DreamStorage
from backend.app import docs


wishes = Blueprint('wishes', __name__)

dream_storage = DreamStorage()


@wishes.route('/mywishes', methods=['GET'])
@jwt_required
@marshal_with(DreamSchema(many=True))
def get_dreams():
    try:
        user_id = get_jwt_identity()
        dreams = dream_storage.get_all(user_id)
    except Exception as e:
        return {'message': str(e)}, 400
    return dreams


@wishes.route('/mywishes', methods=['POST'])
@jwt_required
@use_kwargs(DreamSchema)
@marshal_with(DreamSchema)
def put_dream(**kwargs):
    try:
        user_id = get_jwt_identity()
        new_dream = Dream(owner_id=user_id, **kwargs)
        dream_storage.save(new_dream)
    except Exception as e:
        return {'message': str(e)}, 400
    return new_dream


@wishes.route('/mywishes/<int:dream_id>', methods=['GET'])
@jwt_required
@marshal_with(DreamSchema)
def get_dream(dream_id):
    try:
        user_id = get_jwt_identity()
        dream = dream_storage.get_by_id(user_id, dream_id)
    except Exception as e:
        return {'message': str(e)}, 400
    return dream


@wishes.route('/mywishes/<int:dream_id>', methods=['PUT'])
@jwt_required
@use_kwargs(DreamSchema)
@marshal_with(DreamSchema)
def update_dream(dream_id, **kwargs):
    try:
        user_id = get_jwt_identity()
        dream = dream_storage.get_by_id(user_id, dream_id)
        dream_storage.update(**kwargs)
    except Exception as e:
        return {'message': str(e)}, 400
    return dream


@wishes.route('/mywishes/<int:dream_id>', methods=['DELETE'])
@jwt_required
@marshal_with(DreamSchema)
def delete_dream(dream_id):
    try:
        user_id = get_jwt_identity()
        dream = dream_storage.get_by_id(user_id, dream_id)
        dream_storage.remove(dream)
    except Exception as e:
        return {'message': str(e)}, 400
    return '', 204


@wishes.errorhandler(422)
def error_handlers(err):
    headers = err.data.get('headers', None)
    messages = err.data.get('messages', ['Invalid request'])
    if headers:
        return jsonify({'message': messages}), 400, headers
    else:
        return jsonify({'message': messages}), 400


docs.register(get_dreams, blueprint='wishes')
docs.register(get_dream, blueprint='wishes')
docs.register(update_dream, blueprint='wishes')
docs.register(put_dream, blueprint='wishes')
docs.register(delete_dream, blueprint='wishes')