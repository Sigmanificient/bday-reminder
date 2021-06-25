import functools

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)
from werkzeug.security import check_password_hash, generate_password_hash

from flaskr.db import get_db

bp = Blueprint('auth', __name__, url_prefix='/auth')


@bp.route('/register', methods=('GET', 'POST'))
def register():
    error = None

    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        db = get_db()

        if not username or not password:
            error = 'Identifiant requis et Mot de passe requis.'
        elif db.execute(
            'SELECT id FROM users WHERE username = ?', (username,)
        ).fetchone() is not None:
            error = f"L'utilisateur {username} est déjà enregistré."

        if error is None:
            db.execute(
                'INSERT INTO users (username, authentication_string) VALUES (?, ?)',
                (username, generate_password_hash(password))
            )
            db.commit()
            return redirect(url_for('auth.login'))

    return render_template('auth/register.html', error=error)


@bp.route('/login', methods=('GET', 'POST'))
def login():
    error = None

    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        db = get_db()

        error = None
        user = db.execute(
            'SELECT * FROM users WHERE username = ?', (username,)
        ).fetchone()

        if user is None:
            error = 'Utilisateur ou mot de passe incorrect'

        elif not check_password_hash(user['authentication_string'], password):
            error = 'Utilisateur ou mot de passe incorrect'

        if error is None:
            session.clear()
            session['user_id'] = user['id']
            return redirect('..')

    return render_template('auth/login.html', error=error)


@bp.before_app_request
def load_logged_in_user():
    user_id = session.get('user_id')

    if user_id is None:
        g.user = None
    else:
        g.user = get_db().execute(
            'SELECT * FROM users WHERE id = ?', (user_id,)
        ).fetchone()


@bp.route('/logout')
def logout():
    session.clear()
    return redirect('..')
