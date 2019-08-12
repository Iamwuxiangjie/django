# encoding:utf-8
from django.conf.urls import url

from app.util.DownloadUtils import *


def download(request, file_name):
    return doDownload('download', file_name)


def upload(request):
    if request.method == 'POST':
        result = doUpload(request, 'download')
        return HttpResponse(result['message'])
    else:
        return HttpResponse('请求错误')


urlpatterns = [
    url(r'download/(?P<file_name>.*)/$', download),
    url(r'upload$', upload),
]
