from flask import Flask, render_template
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

from config import *
from models.User import User

app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:fyrfyr@localhost:5432/goldenfish"
db = SQLAlchemy(app)
migrate = Migrate(app, db)

Session = sessionmaker(bind=engine)
session = Session()

Base.metadata.create_all(engine)

session.close()


@app.route('/')
def hello_world():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
