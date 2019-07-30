# encoding:utf-8
from app.models import User


def doLogin(name, password):
    if name == '' or password == '':
        return {'code': 500, 'error': u'请输入用户名或密码'}
    users = User.objects.filter(name=name, password=password)
    if len(users) == 0:
        return {'code': 500, 'error': u'请输入正确的用户名或密码'}
    else:
        return {'code': 200, 'data': users[0]}
