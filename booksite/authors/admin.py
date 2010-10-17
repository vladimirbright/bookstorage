# -*- coding: utf-8 -*-

from django.contrib import admin

from authors.models import *


class AuthorAdmin(admin.ModelAdmin):
    search_fields = ( 'first_name', 'second_name', 'surname', 'nickname' )
    list_filter = ( 'letter', )
admin.site.register(Author, AuthorAdmin)


class LetterAdmin(admin.ModelAdmin):
    pass
admin.site.register(FirstLetter, LetterAdmin)

