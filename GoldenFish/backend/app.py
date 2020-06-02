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


@app.route('/')
def main():
    return render_template('index.html')

# REST API Url's
@app.route('/registration', methods=['POST'])
@use_kwargs(UserSchema)
@marshal_with(AuthSchema)
def register(**kwargs):
    user = User(**kwargs)
    session.add(user)
    session.commit()
    token = user.get_token()
    return {'access_token': token}


@app.route('/authentication', methods=['POST'])
@use_kwargs(UserSchema(only=('email', 'password')))
@marshal_with(AuthSchema)
def authenticate(**kwargs):
    user = User.authenticate(**kwargs)
    token = user.get_token()
    return {'access_token': token}


@app.route('/mywishes', methods=['GET'])
@jwt_required
@marshal_with(DreamSchema(many=True))
def get_dreams():
    user_id = get_jwt_identity()
    dreams = Dream.query.filter_by(owner_id=user_id).all()
    return dreams


@app.route('/mywishes', methods=['POST'])
@jwt_required
@use_kwargs(DreamSchema)
@marshal_with(DreamSchema)
def put_dream(**kwargs):
    user_id = get_jwt_identity()
    new_dream = Dream(owner_id=user_id, **kwargs)
    session.add(new_dream)
    session.commit()
    return new_dream


@app.route('/mywishes/<int:dream_id>', methods=['GET'])
@jwt_required
@marshal_with(DreamSchema)
def get_dream(dream_id):
    user_id = get_jwt_identity()
    dream = Dream.query.filter_by(owner_id=user_id, id=dream_id).first()
    if not dream:
        return {'message': 'Not found this dream'}, 400
    return dream


@app.route('/mywishes/<int:dream_id>', methods=['PUT'])
@jwt_required
@use_kwargs(DreamSchema)
@marshal_with(DreamSchema)
def update_dream(dream_id, **kwargs):
    user_id = get_jwt_identity()
    dream = Dream.query.filter_by(owner_id=user_id, id=dream_id).first()
    if not dream:
        return {'message': 'Not found this dream'}, 400
    for key, value in kwargs.items():
        setattr(dream, key, value)
    session.commit()
    return dream


@app.route('/mywishes/<int:dream_id>', methods=['DELETE'])
@jwt_required
@marshal_with(DreamSchema)
def delete_dream(dream_id):
    user_id = get_jwt_identity()
    dream = Dream.query.filter_by(owner_id=user_id, id=dream_id).first()
    if not dream:
        return {'message': 'Not found this dream'}, 400
    session.delete(dream)
    session.commit()
    return '', 204


@app.teardown_appcontext
def shutdown_session(exception=None):
    session.remove()


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
