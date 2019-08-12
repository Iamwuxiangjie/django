#!/usr/bin/python
# -*- coding: UTF-8 -*-

import json

from django.core import serializers
from django.http import HttpResponse
from django.http import JsonResponse


def get_json_object(json_object):
    source = json_object['fields']
    source['id'] = json_object['pk']
    return source


def parse_json_object(json_object):
    return get_json_object(json.loads(serializers.serialize('json', [json_object]))[0])


def return_json_object(json_object):
    return HttpResponse(JsonResponse(parse_json_object(json_object), safe=False), content_type="application/json")


def parse_json_array(json_array):
    target = []
    source = json.loads(serializers.serialize('json', json_array))
    for item in source:
        target.append(get_json_object(item))
    return target


def return_json_array(json_array):
    return HttpResponse(JsonResponse(parse_json_array(json_array), safe=False), content_type="application/json")
