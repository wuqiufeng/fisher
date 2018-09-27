from werkzeug.exceptions import HTTPException

__auth__ = 'fuhz'


class ClientTypeError(HTTPException):
    code = 400

    description = (
        'client is invalid'
    )