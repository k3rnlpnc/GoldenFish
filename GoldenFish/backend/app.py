from flask import Flask, render_template, jsonify, request
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from backend.config import SecurityConfig
from backend.config import *
from backend.models.User import User
from backend.models.Dream import Dream
from backend.models.Gift import Gift

app = Flask(__name__, template_folder="../frontend/templates", static_folder="../frontend/static")
db = SQLAlchemy(app)
migrate = Migrate(app, db)

Session = sessionmaker(bind=engine)
session = Session()

Base = declarative_base()
Base.metadata.create_all(engine)

jwt = JWTManager(app)

session.close()


@app.route('/')
def hello_world():
    return render_template('index.html')


@app.route('/registration')
def register():
    return render_template('registration.html')


@app.route('/authentication')
def authenticate():
    return render_template('authentication.html')


#@app.route('/registration', methods=['POST'])
#def register():
#    params = request.json
#    user = User(**params)
#    session.add(user)
#    session.commit()
#    token = user.get_token()
#    return {'access_token': token}


if __name__ == '__main__':
    app.run(debug=True)
