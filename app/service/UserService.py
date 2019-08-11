# encoding:utf-8
from app.models import User
import datetime


def doLogin(name, password):
    if name == '' or password == '':
        return {'code': 500, 'error': u'请输入用户名或密码'}
    users = User.objects.filter(name=name, password=password)
    if len(users) == 0:
        return {'code': 500, 'error': u'请输入正确的用户名或密码'}
    else:
        return {'code': 200, 'data': users[0]}


def doRegister(name, password):
    if name == '' or password == '':
        return {'code': 500, 'error': u'请输入用户名或密码'}
    users = User.objects.filter(name=name)
    if len(users) == 0:
        user = User(name=name, password=password,createTime=datetime.datetime.now())
        user.save()
        return {'code': 200, 'data': user}
    else:
        return {'code': 500, 'error': u'该用户名已经被占用,请重新填入用户名'}
