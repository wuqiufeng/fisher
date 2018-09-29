from flask import Blueprint, jsonify
from flask import request

from app.libs.enums import ClientTypeEnum
from app.libs.error_code import NotFound
from app.libs.redprint import Redprint
from app.models.user import User
from app.validator.forms import ClientForm

from app.libs.token_auth import auth

__auth__ = 'fuhz'


api = Redprint('user')



@api.route('/<int:uid>', methods=['GET'])
@auth.login_required
def get_user(uid):
    user = User.query.get_or_404(uid)
    return jsonify(user)



@api.route('', methods=['POST'])
def update_user():
    return 'update_user fuhz'



@api.route('', methods=['DELETE'])
def delete_user():
    return 'delete_user fuhz'



@api.route('', methods=['POST'])
def create_user():
    return 'create_user fuhz'




