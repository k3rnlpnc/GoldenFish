from flask import Flask, render_template, jsonify, request, abort, Blueprint
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager, jwt_required, get_jwt_identity
from apispec.ext.marshmallow import MarshmallowPlugin
from apispec import APISpec
from flask_apispec.extension import FlaskApiSpec
from flask_cors import CORS

from backend.config import *
from backend.models.Dream import Dream
from backend.models.User import User

app = Flask(__name__, template_folder="../frontend/templates", static_folder="../frontend/static")
app.config.from_object(Config)
client = app.test_client()
cors = CORS(app, resources={r"/*": {"origins": "*"}})

db = SQLAlchemy(app)
migrate = Migrate(app, db)

Base.metadata.create_all(engine)

docs = FlaskApiSpec()

app.config.update({
    'APISPEC_SPEC': APISpec(
        title='goldenfish',
        version='v1',
        openapi_version='2.0',
        plugins=[MarshmallowPlugin()],
    ),
    'APISPEC_SWAGGER_URL': '/swagger'
})


@app.teardown_appcontext
def shutdown_session(exception=None):
    session.remove()


from backend.controllers.UserController import users
from backend.controllers.DreamController import wishes
from backend.controllers.FriendController import friends

app.register_blueprint(users)
app.register_blueprint(wishes)
app.register_blueprint(friends)

docs.init_app(app)
jwt = JWTManager(app)

if __name__ == '__main__':
    app.run(debug=True)
