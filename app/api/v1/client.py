from flask import request

from app.libs.enums import ClientTypeEnum
from app.libs.error_code import ClientTypeError, Success
from app.libs.redprint import Redprint
from app.models.user import User
from app.validator.forms import ClientForm, UserEmailForm

__auth__ = 'fuhz'

api = Redprint('client')



@api.route('/register', methods=['POST'])
def create_client():
    form = ClientForm().validate_for_api()
    promise = {
        ClientTypeEnum.USER_EMAIL: __register_user_by_email
    }
    promise[form.type.data]()
    # 异常处理 未知异常 AOP 出口
    return Success()


def __register_user_by_email():
    form = UserEmailForm().validate_for_api()
    User.register_by_email(form.nickname.data,
                               form.account.data,
                               form.secret.data)
