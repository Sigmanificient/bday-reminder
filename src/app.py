from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///bday.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


# DB Model
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    pseudo = db.Column(db.String(32))
    password = db.Column(db.String(128))
    birthday = db.Column(db.Date, default=None)


class Birthday(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, primary_key=True)
    person_name = db.Column(db.String(32))
    person_birthday = db.Column(db.Date)


@app.route('/')
def index():
    pass
    # return render_template('index')


@app.route('/login')
def login():
    pass
    # return render_template('login page')


@app.route('/register')
def register():
    pass
    # return render_template('register page')


@app.route('/dashboard')
def dashboard():
    pass
    # return render_template('dashboard page')


@app.route('/delete')
def delete():
    pass
    # return render_template('delete page')


@app.route('/legal')
def legal():
    pass
    # return render_template('legal page')


if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)
