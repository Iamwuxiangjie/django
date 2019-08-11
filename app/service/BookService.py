# encoding:utf-8
from app.models import Book


def doList():
    return Book.objects.all()
