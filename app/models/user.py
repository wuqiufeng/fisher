from sqlalchemy import Integer, SmallInteger, String, Column
from werkzeug.security import generate_password_hash

from app.models.base import Base, db

__auth__ = 'fuhz'



class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    email = Column(String(50), unique=True, nullable=False, comment='邮箱')
    auth = Column(SmallInteger, default=1, comment="用户权限")
    nickname = Column(String(24), nullable=False, comment="昵称")
    _password = Column('password', String(128), comment="密码")

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

