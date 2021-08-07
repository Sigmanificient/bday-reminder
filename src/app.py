from flask import Flask, render_template, redirect, url_for
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


@app.route('/', methods=('GET', 'POST'))
def index_page():
    return render_template('index.jinja2')


@app.route('/auth/login', methods=('GET', 'POST'))
def login_page():
    return render_template('auth/login.jinja2')


@app.route('/auth/register', methods=('GET', 'POST'))
def register_page():
    return render_template('auth/register.jinja2')


@app.route('/dashboard')
def dashboard_page():
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
