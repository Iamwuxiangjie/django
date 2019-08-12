# encoding:utf-8
from django.conf.urls import url
from django.shortcuts import render, HttpResponseRedirect, HttpResponse

from app.models import Book, User
from app.service.UserService import *
from app.util.JSONUtils import *


def login(req):
    if req.method == 'POST':
        name = req.POST.get('name')
        password = req.POST.get('password')
        result = doLogin(name, password)

        if result.get('code') == 200:
            req.session['currentUser'] = result.get('data').name
            return HttpResponseRedirect('/user/index')
        else:
            return render(req, 'user/login.html', {'error': result.get('error')})
    else:
        return render(req, 'user/login.html', {'error': ''})


def register(req):
    if req.method == 'POST':
        name = req.POST.get('name')
        password = req.POST.get('password')
        result = doRegister(name, password)

        if result.get('code') == 200:
            req.session['currentUser'] = result.get('data').name
            return HttpResponseRedirect('/user/index')
        else:
            return render(req, 'user/register.html', {'error': result.get('error')})
    else:
        return render(req, 'user/register.html', {'error': ''})


def logout(req):
    if not (req.session.get('currentUser') is None):
        del req.session['currentUser']
    return HttpResponseRedirect('/user/login')


def index(req):
    book_list = Book.objects.all()
    user_list = User.objects.all()
    return render(req, 'user/index.html', {'book_list': book_list, 'user_list': user_list})


def get(request, user_id):
    if request.method == 'GET':
        return return_json_object(User.objects.get(id=user_id))
    else:
        return HttpResponse('不支持该请求')


def list(request):
    if request.method == 'GET':
        return return_json_array(User.objects.all())
    else:
        return HttpResponse('不支持该请求')


urlpatterns = [
    url(r'login$', login),
    url(r'register$', register),
    url(r'logout$', logout),
    url(r'index$', index),

    url(r'get/(?P<user_id>.*)/$', get),
    url(r'list$', list),
]
