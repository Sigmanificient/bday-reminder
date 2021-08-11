from os import path

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from .models import Birthday, User

DB_PATH = 'bday.db'

db = SQLAlchemy()


def create_app():
    app = Flask(__name__)
    app.config['SQL_ALCHEMY_DATABASE_URL'] = f'sqlite:///{DB_PATH}'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)

    if not path.exists(DB_PATH):
        db.create_all()
        create_dummy_user()

    from .views import views
    app.register_blueprint(views, url_prefix='/')

    from .auth import auth
    app.register_blueprint(auth, url_prefix='/')

    return app


def create_dummy_user():
    dummy_user = User(
        pseudo="dummy",
        password=(
            "ee26b0dd4af7e749aa1a8ee3c10ae9923f618980772e473f8819a5d4940e0db27a"
            "c185f8a0e1d5f84f88bc887fd67b143732c304cc5fa9ad8e6f57f50028a8ff"
        ),
        birthday="2001-12-11"
    )

    db.session.add(dummy_user)
    db.session.commit()
