#!/usr/bin/python
# -*- coding: UTF-8 -*-

from handler import Login

router = [
    {'path': '/', 'handler': Login.login}
]