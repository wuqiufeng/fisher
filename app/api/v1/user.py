from flask import Blueprint

__auth__ = 'fuhz'


user = Blueprint('user', __name__)

@user.route('/v1/user/get')
def get_user():
    return 'i am fuhz'




