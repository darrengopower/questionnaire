# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url
from .views import IndexView, PollDetailView, ResultsView, vote

urlpatterns = patterns('',

    url(r'^$', IndexView.as_view(), name='index'),
    url(r'^(?P<pk>\d+)/$', PollDetailView.as_view(), name='detail'),
    url(r'^(?P<poll_id>\d+)/vote/$', vote, name='vote'),
    url(r'^(?P<pk>\d+)/results/$', ResultsView.as_view(), name='results'),
)

