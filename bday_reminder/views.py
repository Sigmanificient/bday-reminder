from flask import Blueprint, render_template

from . import User

views = Blueprint("views", __name__)


@views.route('/', methods=('GET', 'POST'))
def index_page():
    return render_template('index.jinja2')


@views.route('/legal')
def legal_page():
    return render_template('legal.jinja2')


@views.route('/api/search/<user>')
def search_user(user):
    found_user = User.query.filter_by(pseudo=user).first()
    if not found_user:
        return {}

    return {
        'id': found_user.id,
        'name': found_user.pseudo,
        'birthday': found_user.birthday
    }
