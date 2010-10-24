# -*- coding: utf-8 -*-

from django.conf.urls.defaults import *
from django.core.urlresolvers import reverse
from django.views.generic.simple import redirect_to


urlpatterns = patterns('authors.views',
    url(r'^$', 'authors_list_all', name='all'),
    url(r'^(\d+)/$', 'authors_details', name='details'),
    url(r'^letter/$', redirect_to, { "url": '/authors/', "permanent": True }),
    url(r'^letter/([^\/]+)$', 'authors_list_by_letter', name='letter'),
)

