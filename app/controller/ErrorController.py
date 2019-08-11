from django.shortcuts import render_to_response


def page_not_found(request):
    response = render_to_response('error/404.html', {})
    response.status_code = 404
    return response


def page_error(request):
    response = render_to_response('error/500.html', {})
    response.status_code = 500
    return response


def permission_denied(request):
    response = render_to_response('error/403.html', {})
    response.status_code = 403
    return response
