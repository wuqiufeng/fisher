from flask import Blueprint

__auth__ = 'fuhz'


book = Blueprint('book', __name__)

@book.route('/v1/book/get')
def get_book():
    return "book"


def create_book():
    return 'create book'