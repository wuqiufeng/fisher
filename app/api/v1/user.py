from flask import Blueprint, jsonify
from flask import g
from flask import request

from app.libs.enums import ClientTypeEnum
from app.libs.error_code import NotFound, DeleteSuccess, AuthFailed
from app.libs.redprint import Redprint
from app.models.base import db
from app.models.user import User
from app.validator.forms import ClientForm

from app.libs.token_auth import auth

__auth__ = 'fuhz'


api = Redprint('user')


@api.route('/<int:uid>', methods=['DELETE'])
@auth.login_required
def super_delete_user(uid):
    is_admin = g.user.is_admin
    if not is_admin:
        raise AuthFailed()



@api.route('/<int:uid>', methods=['GET'])
@auth.login_required
def super_get_user(uid):
    user = User.query.filter_by(id=uid).first_or_404()
    return jsonify(user)


@api.route('', methods=['GET'])
@auth.login_required
def get_user():
    uid = g.user.uid
    user = User.query.filter_by(id=uid).first_or_404()
    return jsonify(user)


@api.route('', methods=['POST'])
def update_user():
    return 'update_user fuhz'



@api.route('', methods=['DELETE'])
@auth.login_required
def delete_user():
    # 线程隔离
    uid = g.user.uid
    with db.auto_commit():
        user = User.query.filter_by(id=uid).first_or_404()
        # user = User.query.get_or_404(uid)
        user.delete()
    return DeleteSuccess()



@api.route('', methods=['POST'])
def create_user():
    return 'create_user fuhz'




