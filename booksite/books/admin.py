# -*- coding: utf-8 -*-

from django.contrib import admin

from books.models import *


class BookAdmin(admin.ModelAdmin):
    search_fields = ( 'title', )
admin.site.register(Book, BookAdmin)


class BookFileAdmin(admin.ModelAdmin):
    pass
admin.site.register(BookFile, BookFileAdmin)
