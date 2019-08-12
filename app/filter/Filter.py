# -*- coding: utf-8 -*-
from django.shortcuts import HttpResponseRedirect

try:
    from django.utils.deprecation import MiddlewareMixin  # Django 1.10.x
except ImportError:
    MiddlewareMixin = object  # Django 1.4.x - Django 1.9.x


class LoginFilter(MiddlewareMixin):
    not_filter = ['/user/login', '/user/register']

    def process_request(self, req):
        if (req.path not in self.not_filter) and (not req.session.get('currentUser', None)):
            return HttpResponseRedirect('/user/login')
