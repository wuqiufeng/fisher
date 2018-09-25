from flask import Flask

__auth__ = 'fuhz'


def register_blueprint(app):
    from app.api.v1.book import book
    from app.api.v1.user import user
    app.register_blueprint(book)
    app.register_blueprint(user)


def create_app():
    app = Flask(__name__)
    app.config.from_object('app.config.setting')
    app.config.from_object('app.config.secure')

    register_blueprint(app)

    return app
