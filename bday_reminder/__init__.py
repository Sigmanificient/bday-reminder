from os import path

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

DB_PATH = 'bday.db'

db = SQLAlchemy()


def create_app() -> Flask:
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_PATH}'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app=app)

    if not path.isfile(DB_PATH):
        # Importing db models for the db to initialize.
        from bday_reminder.models import Birthday, User

        db.create_all(app=app)

    from .views import views
    app.register_blueprint(views, url_prefix='/')

    from .auth import auth
    app.register_blueprint(auth, url_prefix='/')

    return app
