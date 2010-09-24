# -*- coding: utf-8 -*-

from django.conf import settings
from django.conf.urls.defaults import *
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    # Example:
    # (r'^booksite/', include('booksite.foo.urls')),

    (r'^admin/', include(admin.site.urls)),
)
