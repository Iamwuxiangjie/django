# encoding:utf-8
from django.shortcuts import render, HttpResponseRedirect
from app.service.UserService import *
from app.service.BookService import *
from django.conf.urls import url
from app.models import Book,User


def login(req):
    if req.method == 'POST':
        name = req.POST.get('name')
        password = req.POST.get('password')
        result = doLogin(name, password)

        if result.get('code') == 200:
            req.session['currentUser'] = result.get('data').name
            return HttpResponseRedirect('/user/index.html')
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
    if not(req.session.get('currentUser') is None):
        del req.session['currentUser']
    return HttpResponseRedirect('/user/login')

def index(req):
    book_list = Book.objects.all()
    user_list = User.objects.all()
    return render(req, 'user/index.html', {'book_list': book_list,'user_list':user_list})

urlpatterns = [
    url(r'login$', login),
    url(r'register$', register),
    url(r'logout$', logout),
    url(r'index$', index),
]