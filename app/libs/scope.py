__auth__ = 'fuhz'


class SuperScope():
    allow_api = ['v1.super_get_user']

class AdminScope():
    allow_api = ['v1.admin_get_user']


class UserScope():
    allow_api = ['v1.user']



def is_in_scope(scope, endpoint):
    # 放射
    scope = globals()[scope]()
    if endpoint in scope.allow_api:
         return True
    else:
        return False
