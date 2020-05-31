from flask import Flask, render_template, jsonify, request, abort
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager

from backend.config import *
from backend.models.User import User
from backend.models.Dream import Dream
from backend.models.Gift import Gift

app = Flask(__name__, template_folder="../frontend/templates", static_folder="../frontend/static")
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:fyrfyr@localhost:5432/goldenfish'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
client = app.test_client()

db = SQLAlchemy(app)
migrate = Migrate(app, db)


Base.metadata.create_all(engine)

jwt = JWTManager(app)


'''
@app.route('/test')
def insert():
    user1 = User(email='lol@mail.com',
                name='user1',
                surname='sur',
                password='pass',
                username='user1')
    user2 = User(email='lal@mail.com',
                 name='user2',
                 surname='sur',
                 password='pass',
                 username='user2')
    dream = Dream(1, 'Lexus')
    user1.friend_requests = [user2]
    session.add(user1)
    session.add(user2)
    session.add(dream)
    session.commit()
    return 'OK'
'''

@app.route('/')
def main():
    return render_template('index.html')


@app.route('/registration')
def register():
    return render_template('registration.html')


@app.route('/authentication')
def authenticate():
    return render_template('authentication.html')

# REST API Url's
@app.route('/mywishes/<int:user_id>', methods=['GET'])
def get_dreams(user_id):
    dreams = Dream.query.filter_by(owner_id=user_id).all()
    serialized = []
    for dream in dreams:
        serialized.append({
            'id': dream.id,
            'owner_id': dream.owner_id,
            'name': dream.name,
            'description': dream.description,
            'image_link': dream.image_link,
            'store_link': dream.store_link,
            'is_fulfilled': dream.is_fulfilled
        })
    return jsonify(serialized)


@app.route('/mywishes/<int:user_id>', methods=['POST'])
def put_dream(user_id):
    new_dream = Dream(**request.json)
    session.add(new_dream)
    session.commit()
    serialized = {
        'id': new_dream.id,
        'owner_id': new_dream.owner_id,
        'name': new_dream.name,
        'description': new_dream.description,
        'image_link': new_dream.image_link,
        'store_link': new_dream.store_link,
        'is_fulfilled': new_dream.is_fulfilled
    }
    return jsonify(serialized)


@app.route('/mywishes/<int:user_id>/<int:dream_id>', methods=['GET'])
def get_dream(user_id, dream_id):
    dream = Dream.query.filter_by(owner_id=user_id, id=dream_id).first()
    if not dream:
        return {'message': 'Not found this dream'}, 400
    serialized = {
        'id': dream.id,
        'owner_id': dream.owner_id,
        'name': dream.name,
        'description': dream.description,
        'image_link': dream.image_link,
        'store_link': dream.store_link,
        'is_fulfilled': dream.is_fulfilled
    }
    return jsonify(serialized)


@app.route('/mywishes/<int:user_id>/<int:dream_id>', methods=['PUT'])
def update_dream(user_id, dream_id):
    dream = Dream.query.filter_by(owner_id=user_id, id=dream_id).first()
    if not dream:
        return {'message': 'Not found this dream'}, 400
    update_data = request.json
    for key, value in update_data.items():
        setattr(dream, key, value)
    session.commit()
    serialized = {
        'id': dream.id,
        'owner_id': dream.owner_id,
        'name': dream.name,
        'description': dream.description,
        'image_link': dream.image_link,
        'store_link': dream.store_link,
        'is_fulfilled': dream.is_fulfilled
    }
    return jsonify(serialized)


@app.route('/mywishes/<int:user_id>/<int:dream_id>', methods=['DELETE'])
def delete_dream(user_id, dream_id):
    dream = Dream.query.filter_by(owner_id=user_id, id=dream_id).first()
    if not dream:
        return {'message': 'Not found this dream'}, 400
    session.delete(dream)
    session.commit()
    return '', 204

#@app.route('/registration', methods=['POST'])
#def register():
#    params = request.json
#    user = User(**params)
#    session.add(user)
#    session.commit()
#    token = user.get_token()
#    return {'access_token': token}


@app.teardown_appcontext
def shutdown_session(exception=None):
    session.remove()


if __name__ == '__main__':
    app.run(debug=True)
