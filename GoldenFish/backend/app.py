from flask import Flask, render_template, jsonify, request, abort
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager, jwt_required, get_jwt_identity
from apispec.ext.marshmallow import MarshmallowPlugin
from apispec import APISpec
from flask_apispec.extension import FlaskApiSpec
from flask_apispec import use_kwargs, marshal_with

from backend.config import *
from backend.models.User import User
from backend.models.Dream import Dream
from backend.models.Gift import Gift
from backend.storage.DreamStorage import DreamStorage
from backend.storage.UserStorage import UserStorage
from backend.schemas import *

app = Flask(__name__, template_folder="../frontend/templates", static_folder="../frontend/static")
app.config.from_object(Config)
client = app.test_client()

db = SQLAlchemy(app)
migrate = Migrate(app, db)


Base.metadata.create_all(engine)

jwt = JWTManager(app)

docs = FlaskApiSpec()
docs.init_app(app)
app.config.update({
    'APISPEC_SPEC': APISpec(
        title='goldenfish',
        version='v1',
        openapi_version='2.0',
        plugins=[MarshmallowPlugin()],
    ),
    'APISPEC_SWAGGER_URL': '/swagger'
})

dream_storage = DreamStorage()
user_storage = UserStorage()

# REST API Url's
@app.route('/registration', methods=['POST'])
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


@app.route('/authentication', methods=['POST'])
@use_kwargs(UserSchema(only=('email', 'password')))
@marshal_with(AuthSchema)
def authenticate(**kwargs):
    try:
        user = user_storage.authenticate(**kwargs)
        token = user.get_token()
    except Exception as e:
        return {'message': str(e)}, 400
    return {'access_token': token}


@app.route('/mywishes', methods=['GET'])
@jwt_required
@marshal_with(DreamSchema(many=True))
def get_dreams():
    try:
        user_id = get_jwt_identity()
        dreams = dream_storage.get_all(user_id)
    except Exception as e:
        return {'message': str(e)}, 400
    return dreams


@app.route('/mywishes', methods=['POST'])
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


@app.route('/mywishes/<int:dream_id>', methods=['GET'])
@jwt_required
@marshal_with(DreamSchema)
def get_dream(dream_id):
    try:
        user_id = get_jwt_identity()
        dream = dream_storage.get_by_id(user_id, dream_id)
    except Exception as e:
        return {'message': str(e)}, 400
    return dream


@app.route('/mywishes/<int:dream_id>', methods=['PUT'])
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


@app.route('/mywishes/<int:dream_id>', methods=['DELETE'])
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


@app.teardown_appcontext
def shutdown_session(exception=None):
    session.remove()


@app.errorhandler(422)
def error_handlers(err):
    headers = err.data.get('headers', None)
    messages = err.data.get('messages', ['Invalid request'])
    if headers:
        return jsonify({'message': messages}), 400, headers
    else:
        return jsonify({'message': messages}), 400


# Generating SWAGGER documentation
docs.register(register)
docs.register(authenticate)
docs.register(get_dreams)
docs.register(get_dream)
docs.register(update_dream)
docs.register(put_dream)
docs.register(delete_dream)

if __name__ == '__main__':
    app.run(debug=True)
