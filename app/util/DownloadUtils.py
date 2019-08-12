#!/usr/bin/python
# -*- coding: UTF-8 -*-
from django.shortcuts import HttpResponse
import os

projectName = 'django'


def getAbsPath(directory, file_name):
    source_path = os.path.abspath(os.path.dirname(__file__))
    root_path = source_path[:source_path.find(projectName + "\\") + len(projectName + "\\")]
    target_path = os.path.abspath(root_path + 'static\\' + directory + '\\' + file_name)
    return target_path


def doDownload(directory, file_name):
    file_path = getAbsPath(directory, file_name)
    the_file = open(file_path, 'rb')
    response = HttpResponse(the_file)
    response['Content-Type'] = 'application/octet-stream'
    response['Content-Disposition'] = 'attachment;filename="' + file_name + '"'
    return response


def doUpload(request, directory):
    file_object = request.FILES.get("file_object", None)
    if not file_object:
        return {'code': 500, 'message': '找不到文件'}

    target = open(getAbsPath(directory, file_object.name), 'wb+')

    for chunk in file_object.chunks():
        target.write(chunk)
    target.close()
    return {'code': 200, 'message': '文件上传成功'}
