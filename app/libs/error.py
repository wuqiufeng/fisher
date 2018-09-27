from werkzeug.exceptions import HTTPException

__auth__ = 'fuhz'

class APIException(HTTPException):
    pass