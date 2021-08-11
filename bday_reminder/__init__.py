from os import path

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

DB_PATH = 'bday.db'

db = SQLAlchemy()


def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_PATH}'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)

    if not path.exists(DB_PATH):
        db.create_all(app=app)

    from .views import views
    app.register_blueprint(views, url_prefix='/')

    from .auth import auth
    app.register_blueprint(auth, url_prefix='/')

    return app
