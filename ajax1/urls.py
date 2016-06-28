#coding:utf-8
from django.conf.urls import patterns, include, url
from views import *
urlpatterns = patterns('',
    url(r'^$',index),
    url(r'^json/',json),
    url(r'^get1/',get1),
)
