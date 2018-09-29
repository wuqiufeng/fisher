from flask import Blueprint

from app.api.v1 import client
from app.api.v1 import token
from app.api.v1 import user, book

__auth__ = 'fuhz'


def create_blueprint_v1():
    bp_v1 = Blueprint('v1', __name__)
    user.api.register(bp_v1)
    book.api.register(bp_v1)
    client.api.register(bp_v1)
    token.api.register(bp_v1)

    return bp_v1