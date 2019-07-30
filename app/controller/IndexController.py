# encoding:utf-8
from django.shortcuts import render
from app.service.IndexService import doList


def index(req):
    list = doList()
    return render(req, 'user/index.html', {'list': list})
