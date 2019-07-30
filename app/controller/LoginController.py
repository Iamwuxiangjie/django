# encoding:utf-8
from django.shortcuts import render, HttpResponseRedirect
from app.service.LoginService import doLogin


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


def logout(req):
    if not(req.session.get('currentUser') is None):
        del req.session['currentUser']
    return HttpResponseRedirect('/user/login')
