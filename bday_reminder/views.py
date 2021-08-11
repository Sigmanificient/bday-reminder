"""All views that does not require any authentication."""

from typing import Union, Dict, Optional

from flask import Blueprint, render_template
from bday_reminder.models import User

views = Blueprint("views", __name__)


@views.route('/', methods=('GET', 'POST'))
def index_page() -> str:
    """The Index page."""
    return render_template('index.jinja2')


@views.route('/legal')
def legal_page() -> str:
    """A page that hold legal information."""
    return render_template('legal.jinja2')


@views.route('/api/search/<user>')
def search_user(user: str) -> Dict[str, Union[str, int]]:
    """An endpoint to retrieve user birthday."""
    found_user: Optional[User] = User.query.filter_by(pseudo=user).first()

    if not found_user:
        return {}

    return {
        'id': found_user.id,
        'name': found_user.pseudo,
        'birthday': found_user.birthday
    }
