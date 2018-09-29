from sqlalchemy import Integer, SmallInteger, String, Column
from werkzeug.security import generate_password_hash, check_password_hash

from app.libs.error_code import NotFound, AuthFailed
from app.models.base import Base, db

__auth__ = 'fuhz'


class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    email = Column(String(50), unique=True, nullable=False, comment='邮箱')
    auth = Column(SmallInteger, default=1, comment="用户权限")
    nickname = Column(String(24), nullable=False, comment="昵称")
    _password = Column('password', String(128), comment="密码")


    def keys(self):
        return ['id', 'email', 'nickname', 'auth']

    def __getattr__(self, item):
        return getattr(self, item)


    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, raw):
        self._password = generate_password_hash(raw)

    @staticmethod
    def register_by_email(nikename, account, secert):
        with db.auto_commit():
            user = User()
            user.nickname = nikename
            user.email = account
            user.password = secert
            db.session.add(user)

    @staticmethod
    def verify(email, password):
        user = User.query.filter_by(email=email).first_or_404()
        if not user.check_password(password):
            raise AuthFailed()
        return {'uid': user.id}

    def check_password(self, raw):
        if not self._password:
            return False
        return check_password_hash(self._password, raw)

