# coding=utf-8

from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^index$', views.index),
    url(r'^tag/(?P<tag_id>[0-9]+)$', views.tag_filter),
    url(r'^tag/search/(?P<tag_query>.+)$', views.tag_filter),
]