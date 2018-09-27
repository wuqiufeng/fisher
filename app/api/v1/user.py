from flask import Blueprint
from flask import request

from app.libs.enums import ClientTypeEnum
from app.libs.redprint import Redprint
from app.validator.forms import ClientForm

__auth__ = 'fuhz'


api = Redprint('user')

@api.route('/get')
def get_user():
    return 'i am fuhz'



