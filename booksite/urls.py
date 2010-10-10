# -*- coding: utf-8 -*-

from django.conf import settings
from django.conf.urls.defaults import *
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    url( r'^$', 'django.views.generic.simple.direct_to_template',
                                                { 'template': 'index.html'}),

    (r'^admin/', include(admin.site.urls)),
)
