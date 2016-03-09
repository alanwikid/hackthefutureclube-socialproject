"""hackthefutureclub routes
author: @alanwikid
"""
# coding: utf-8
from django.conf.urls import url
import django.views.defaults 
from views import index


urlpatterns = (
    url(r'^$', index, name='homepage'),
    url(r'^mail/', 'views.mail', name='mail'),
    url(r'^404/$', django.views.defaults.page_not_found, ),
)

