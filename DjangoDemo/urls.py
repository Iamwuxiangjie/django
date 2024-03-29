"""DjangoDemo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin

from app.controller.ErrorController import permission_denied, page_not_found, page_error
from app.controller.UserController import urlpatterns as user_urls
from app.controller.BookController import urlpatterns as book_urls

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),

    url(r'^user/', include(user_urls)),
    url(r'^book/', include(book_urls)),
]

handler403 = permission_denied
handler404 = page_not_found
handler500 = page_error
