from flask import Blueprint

from app.libs.redprint import Redprint

__auth__ = 'fuhz'


# book = Blueprint('book', __name__)

api = Redprint('book')

@api.route('/get')
def get_book():
    return "book"


def create_book():
    return 'create book'