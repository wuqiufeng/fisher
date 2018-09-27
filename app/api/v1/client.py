from flask import request

from app.libs.enums import ClientTypeEnum
from app.libs.error_code import ClientTypeError
from app.libs.redprint import Redprint
from app.models.user import User
from app.validator.forms import ClientForm, UserEmailForm

__auth__ = 'fuhz'

api = Redprint('client')



@api.route('/register', methods=['POST'])
def create_client():
    form = ClientForm(data=request.json)
    if form.validate():
        promise = {
            ClientTypeEnum.USER_EMAIL: __register_user_by_email
        }
        promise[form.type.data]()
    else:
        raise ClientTypeError()
    return "success"


def __register_user_by_email():
    form = UserEmailForm(data=request.json)
    if form.validate():
        User.register_by_email(form.nickname.data,
                               form.account.data,
                               form.secret.data)
