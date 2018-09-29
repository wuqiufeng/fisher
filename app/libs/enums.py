from enum import Enum

__auth__ = 'fuhz'


class ClientTypeEnum(Enum):
    USER_EMAIL = 100
    USER_MOBILE = 101

    # 微信小程序
    USER_MINA = 200
    # 微信公众号ClientTypeEnum
    USER_WX = 201
