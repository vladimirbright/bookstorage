# -*- coding: utf-8 -*-

from django.contrib import admin
from django import forms

from books.models import *

class BookAdminForm(forms.ModelForm):
    class Meta:
        model = Book
        widgets = {
                "abstract": forms.Textarea,
            }


class BookAdmin(admin.ModelAdmin):
    search_fields = ( 'title', )
    raw_id_fields = ( 'authors', )
    form = BookAdminForm
admin.site.register(Book, BookAdmin)


class BookFileAdmin(admin.ModelAdmin):
    pass
admin.site.register(BookFile, BookFileAdmin)
