from flask import Flask

def create_app() :
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'I Love You'

    from.views import views
    from.config import config

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(config, url_prefix='/')

    return app