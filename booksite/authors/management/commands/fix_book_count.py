# -*- coding: utf-8 -*-

from django.core.exceptions import ImproperlyConfigured
from django.core.management.base import BaseCommand, CommandError
from django.db.models import Count, F
from django.utils.translation import ugettext_lazy as _


from authors.models import Author


class Command(BaseCommand):
    help = _("Update Author.book_count")

    def handle(self, *app_labels, **options):
        for i in Author.objects.all().annotate(bk=Count('book')):
            if i.bk != i.book_count:
                i.book_count = i.bk
                i.save()

