import re
import secrets

from flask import Flask, render_template, redirect, url_for, request, session
from flask_sqlalchemy import SQLAlchemy

from src.security import sha512

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///bday.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

app.config.from_object(__name__)
app.secret_key = secrets.token_urlsafe(32)

USERNAME_PATTERN = r'^([\w -]){4,32}$'
PASSWORD_PATTERN = r'^(.*(?=.{8,})(?=.*[a-zA-Z])(?=.*\d).*){8,32}$'


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


@app.route('/', methods=('GET', 'POST'))
def index_page():
    return render_template('index.jinja2')


@app.route('/auth/login', methods=('GET', 'POST'))
def login_page():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        if username and password:
            login = User.query.filter_by(
                pseudo=username,
                password=sha512(password)
            ).first()

            if login is not None:
                session['user'] = {'name': username}
                return redirect(url_for('dashboard_page'))

    return render_template('auth/login.jinja2')


@app.route('/auth/register', methods=('GET', 'POST'))
def register_page():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        confirm_password = request.form['confirm_password']

        if (
            re.match(USERNAME_PATTERN, username)
            and re.match(PASSWORD_PATTERN, password)
            and confirm_password
            and confirm_password == password
        ):
            new_user = User(
                pseudo=username,
                password=sha512(password)
            )

            db.session.add(new_user)
            db.session.commit()

            session['user'] = {'name': username}
            return redirect(url_for('dashboard_page'))

    return render_template('auth/register.jinja2')


@app.route('/dashboard')
def dashboard_page():
    user = session.get('user')

    if not user:
        return redirect(url_for('login_page'))

    if not user.get('name'):
        return redirect(url_for('login_page'))

    return render_template('dashboard.jinja2')


@app.route('/auth/delete', methods=('GET', 'POST'))
def delete_account_page():
    return render_template('auth/delete.jinja2')


@app.route('/legal')
def legal_page():
    return render_template('legal.jinja2')


@app.route('/logout/')
def logout():
    return redirect(url_for('index'))


if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)
