from wtforms.validators import DataRequired, Email, Regexp, Length, ValidationError
from wtforms import StringField, IntegerField
from app.libs.enums import ClientTypeEnum
from app.models.user import User
from app.validator.base import BaseForm as Form

__auth__ = 'fuhz'




class ClientForm(Form):
    account = StringField(validators=[DataRequired(message="不允许为空"), Length(min=1, max=32)])
    secret = StringField()
    type = IntegerField(validators=[DataRequired()])

    def validate_type(self, value):
        try:
            client = ClientTypeEnum(value.data)
        except ValueError as e:
            raise e
        self.type.data = client



class UserEmailForm(ClientForm):
    account = StringField(validators=[
        Email(message='validate email')
    ])
    secret = StringField(validators=[
        DataRequired(),
        Regexp(r'^[A-Za-z0-9_*&$#@]{6,22}$', message="请输入6到22位密码")
    ])
    nickname = StringField(validators=[DataRequired(),
                                       Length(min=2, max=22)])

    def validate_account(self, value):
        if User.query.filter_by(email=value.data).first():
            raise ValidationError(message='账号已经存在')
