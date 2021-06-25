from flask import (
    Blueprint, session
)

bp = Blueprint('dashboard', __name__, url_prefix='/dashboard')

# app.secret_key =


@bp.route('/dashboard')
def dashboard():
    if 'username' in session:
        return f'Logged in as {session["username"]}'
    return 'You are not logged in'
