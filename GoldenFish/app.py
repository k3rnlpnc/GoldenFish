from flask import Flask, render_template
import config

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = config['postgresql://127.0.0.1:65372/goldenfish']
#db = SQLAlchemy(app)


@app.route('/')
def hello_world():
    return render_template('index.html')


if __name__ == '__main__':
    app.debug = True
    app.run()
