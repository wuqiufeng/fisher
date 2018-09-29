from app.libs.error import APIException

__auth__ = 'fuhz'

class Success(APIException):
    code = 201
    msg = 'ok'
    error_code = 0

class DeleteSuccess(Success):
    # code = 204 资源被删除 content为空
    code = 202
    error_code = 1


class ServerError(APIException):
    code = 500
    msg = "sorry, we make a mistake"
    error_code = 999

class ClientTypeError(APIException):
    code = 400
    msg = 'client is invalid'
    error_code = 1006


class ParameterException(APIException):
    code = 400
    msg = 'client is invalid'
    error_code = 1000

class NotFound(APIException):
    code = 404
    msg = 'the resource are not found'
    error_code = 1001

class AuthFailed(APIException):
    code = 401
    error_code = 1005
    msg = 'authorzation failed'


class Forbidden(APIException):
    code = 403
    error_code = 1003
    msg = 'forbidden, not in scope'