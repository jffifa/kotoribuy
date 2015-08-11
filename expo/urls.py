# coding=utf-8

from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^index$', views.index, name='index'),
    url(r'^tag/(?P<tag_id>[0-9]+)$', views.tag_filter, name='tag_id'),
    url(r'^tag/search/(?P<tag_query>.+)$', views.tag_filter, name='tag_query'),
    url(r'^booth/(?P<booth_id>[0-9]+)$', views.booth_detail, name='booth_detail'),
]