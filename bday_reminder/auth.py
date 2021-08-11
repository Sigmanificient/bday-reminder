import re
from datetime import datetime

from flask import (
    Blueprint, render_template, request, redirect, session, url_for
)

from . import db
from .models import Birthday, User
from .security import sha512

USERNAME_PATTERN = r'^([\w\d-]){4,32}$'
PASSWORD_PATTERN = (
    r'^.*(?=.{8,})(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[-_ @#$%^&+=]).*$'
)

auth = Blueprint("auth", __name__)


@auth.route('/auth/login', methods=('GET', 'POST'))
def login_page():
    if session.get('user'):
        return redirect(url_for('dashboard_page'))
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        if username and password:
            login = User.query.filter_by(
                pseudo=username,
                password=sha512(password)
            ).first()

            if login is not None:
                session['user'] = {
                    'name': username,
                    'id': login.id,
                    'birthday': login.birthday
                }

                return redirect(url_for('dashboard_page'))

    return render_template('auth/login.jinja2')


@auth.route('/auth/register', methods=('GET', 'POST'))
def register_page():
    if session.get('user'):
        return redirect(url_for('dashboard_page'))
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        confirm_password = request.form['confirm_password']
        birthday = request.form['date']

        if (
            re.match(USERNAME_PATTERN, username)
            and re.match(PASSWORD_PATTERN, password)
            and confirm_password
            and confirm_password == password
            and birthday
        ):
            new_user = User(
                pseudo=username,
                password=sha512(password),
                birthday=birthday
            )

            db.session.add(new_user)
            db.session.commit()

            session['user'] = {'name': username}
            return redirect(url_for('dashboard_page'))

    return render_template(
        'auth/register.jinja2',
        USERNAME_PATTERN=USERNAME_PATTERN,
        PASSWORD_PATTERN=PASSWORD_PATTERN
    )


@auth.route('/dashboard', methods=('GET', 'POST'))
def dashboard_page():
    user = session.get('user')

    if not user:
        return redirect(url_for('login_page'))

    if not user.get('name'):
        return redirect(url_for('login_page'))

    if request.method == 'POST':
        username = request.form['username']
        date = request.form['date']

        if username and date:
            new_birthday = Birthday(
                person_name=username,
                person_birthday=date,
                user_id=user.get('id')
            )

            db.session.add(new_birthday)
            db.session.commit()

    birthdays = Birthday.query.filter_by(user_id=user.get('id')).all()
    now = datetime.now()

    return render_template(
        'dashboard.jinja2',
        birthdays=birthdays,
        today_birthdays=[
            birthday
            for birthday in birthdays
            if birthday.person_birthday.endswith(
                f'-{now.month:02}-{now.day:02}'
            )
        ]
    )


@auth.route('/auth/edit', methods=('GET', 'POST'))
def edit_page():
    user = session.get('user')

    if not user:
        return redirect(url_for('login_page'))

    if not user.get('name'):
        return redirect(url_for('login_page'))

    if request.method == 'POST':
        if request.form.get('new_password'):
            new_password = request.form['new_password']
            confirm_password = request.form['confirm_new_password']
            old_password = request.form['old_password']

            if (
                    User.query.filter_by(
                        pseudo=user.get('name'), password=sha512(old_password)
                    ).first()
                    and new_password == confirm_password
            ):
                user = User.query.filter_by(pseudo=user.get('name')).first()
                user.password = sha512(new_password)
                db.session.commit()

        elif request.form.get('new_username'):
            new_username = request.form['new_username']
            confirm_username = request.form['confirm_new_username']

            if (
                    new_username == confirm_username
                    and not User.query.filter_by(pseudo=new_username).first()
            ):
                user = User.query.filter_by(pseudo=user.get('name')).first()
                user.pseudo = new_username
                db.session.commit()

                session['user'] = {'name': new_username}

    return render_template('auth/edit.jinja2')


@auth.route('/auth/delete', methods=('GET', 'POST'))
def delete_account_page():
    user = session.get('user')

    if not user:
        return redirect(url_for('login_page'))

    if not user.get('name'):
        return redirect(url_for('login_page'))
    if request.method == 'POST' and user.get('name') == request.form.get(
            'account_name'
    ):
        db.session.delete(User.query.filter_by(pseudo=user.get('name')).first())
        db.session.commit()
        return redirect(url_for('logout'))
    return render_template('auth/delete.jinja2')


@auth.route('/delete/<index>')
def delete_user(index):
    user = session.get('user')

    if not user:
        return {}

    if not user.get('name'):
        return {}

    if not index.isdigit():
        return {}

    db.session.delete(
        Birthday.query.filter_by(
            user_id=user.get('id'),
            id=int(index)
        ).first()
    )

    db.session.commit()

    return {}


@auth.route('/logout/')
def logout():
    if session.get('user'):
        session.pop('user')

    return redirect(url_for('index_page'))
