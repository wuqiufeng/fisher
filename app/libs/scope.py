__auth__ = 'fuhz'


class Scope():
    allow_api = []
    allow_module = []
    forbidden = []

    def __add__(self, other):
        self.allow_api = self.allow_api + other.allow_api
        self.allow_api = list(set(self.allow_api))

        self.allow_module = self.allow_module + other.allow_module
        self.allow_module = list(set(self.allow_module))

        self.forbidden = self.forbidden + other.forbidden
        self.forbidden = list(set(self.forbidden))
        return self


class SuperScope(Scope):
    allow_api = ['v1.user+super_get_user',
                 'v1.user+super_delete_user']
    allow_module = ['v1.user']

    # def __init__(self):
    #     self + UserScope()


class AdminScope(Scope):
    allow_api = ['v1.admin', 'v1.A', 'v1.B']

    def __init__(self):
        self + UserScope()


class UserScope(Scope):
    allow_api = ['v1.user+get_user', 'v1.user+delete_user']
    forbidden = ['v1.user+super_get_user',
                 'v1.user+super_delete_user']

    def __init__(self):
        self + SuperScope()


# superScope = SuperScope()


def is_in_scope(scope, endpoint):
    # 放射
    # endpoint v1.view_func v1.redprint_name+view_func
    scope = globals()[scope]()
    splits = endpoint.split('+')
    red_name = splits[0]

    if endpoint in scope.forbidden:
        return False
    if endpoint in scope.allow_api:
        return True
    if red_name in scope.allow_module:
        return True
    else:
        return False
