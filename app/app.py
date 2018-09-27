from flask import Flask

__auth__ = 'fuhz'


def register_blueprint(app):
    # from app.api.v1.book import book
    # from app.api.v1.user import user
    # app.register_blueprint(book)
    # app.register_blueprint(user)

    from app.api.v1 import create_blueprint_v1
    app.register_blueprint(create_blueprint_v1(), url_prefix='/v1')


def register_plug(app):
    from app.models.base import db
    db.init_app(app)
    with app.app_context():
        db.create_all()


def create_app():
    app = Flask(__name__)
    app.config.from_object('app.config.secure')
    app.config.from_object('app.config.setting')

    register_blueprint(app)
    register_plug(app)
    return app
