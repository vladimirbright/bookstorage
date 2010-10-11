# -*- coding: utf-8 -*-

from django.conf import settings
from django.conf.urls.defaults import *
from django.contrib import admin

admin.autodiscover()

direct = 'django.views.generic.simple.direct_to_template'

urlpatterns = patterns('',
    url( r'^$', direct, { 'template': 'index.html'}, name='index'),
    url( r'^authors/$', direct, { 'template': 'authors.html'}, name='authors'),
    url( r'^books/$', direct, { 'template': 'books.html'}, name='books'),
    url( r'^genres/$', direct, { 'template': 'genres.html'}, name='genres'),
    url( r'^reading/$', direct, { 'template': 'reading.html'}, name='reading'),
    url( r'^my-library/$', direct, { 'template': 'my.html'}, name='my'),

    (r'^admin/', include(admin.site.urls)),
)
