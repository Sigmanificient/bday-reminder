from flask import (
    Blueprint, session
)

bp = Blueprint('app', __name__, url_prefix='/app')


@bp.route('/dashboard')
def dashboard():
    if 'user_id' in session:
        print(session)
        return f'Logged in as {session["user_id"]}'

    return 'You are not logged in'
