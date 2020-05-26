from flask import Flask, render_template
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

from backend.config import *
from backend.models import User
from backend.models import Dream
from backend.models import Gift

app = Flask(__name__)
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
