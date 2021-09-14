from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path

db = SQLAlchemy()
DB_NAME = "database.db"

def create_app() :
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'I Love You'
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    db.init_app(app)

    from .views import views
    from .config import config

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(config, url_prefix='/')

    from .datab import User, Note

    create_database(app)

    return app

def create_database(app):
    if not path.exists('website/' + DB_NAME):
        db.create_all(app=app)
        print('Created Database!')
