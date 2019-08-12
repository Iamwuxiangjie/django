#!/usr/bin/python
# -*- coding: UTF-8 -*-

import socket
import re


def get_request(conn):
    data = conn.recv(8096)
    params = data.split('\r\n')
    request = {"connection": conn}
    for index, item in enumerate(params):
        if index != 0:
            content = re.match(r'(.*): (.*)', str(item), re.M | re.I)
            if content:
                request[content.group(1)] = content.group(2)
        else:
            content = str(item).split(' ')
            if content and len(content) > 1:
                request['method'] = content[0]
                request['url'] = content[1]
    return request


def get_response(request, router):
    response = {}
    try:
        for item in router:
            if request['url'] and item['path'] == request['url']:
                response['code'] = 200
                response['data'] = item['handler'](request)
                break
        if 'code' not in response:
            response['code'] = 404
            response['data'] = '404'

    except BaseException, message:
        response['data'] = str(message)
        response['code'] = 500
    finally:
        return response


def return_response(request, response):
    conn = request['connection']
    header = 'HTTP/1.1 ' + str(response['code']) + ' OK\r\n\r\n'
    conn.send(bytes(str(header)))
    conn.send(bytes(str(response['data'])))


def start(router):
    s = socket.socket()
    host = '127.0.0.1'
    port = 8000
    s.bind((host, port))
    s.listen(5)
    while True:
        c, addr = s.accept()
        try:
            request = get_request(c)
            response = get_response(request, router)
            return_response(request, response)
        except BaseException, message:
            print 'error:' + str(message)
        finally:
            c.close()
