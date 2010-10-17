# -*- coding: utf-8 -*-

u"""
    Дополнительные валидаторы.
"""
from datetime import datetime, date, timedelta

from django.core.exceptions import ValidationError
from django.template.defaultfilters import filesizeformat
from django.utils.translation import ugettext_lazy as _


# Временные валидаторы
def in_future(value):
    if (isinstance(value, date) and value < date.today()) or \
       (isinstance(value, datetime) and value < datetime.now()):
        raise ValidationError(_("Only in future"))


def in_past(value):
    if (isinstance(value, date) and value > date.today()) or \
       (isinstance(value, datetime) and value > datetime.now()):
        raise ValidationError(_("Only in past"))


# Возрастные валидаторы
class YoungerThen(object):
    message = _("Too old. Maximum %(years)d years old.")
    max_age = None

    def __init__(self, max_age):
        self.max_age = int(max_age)

    def __call__(self, value):
        now = date.today()
        max_age_date = now - timedelta(days=365*self.max_age)
        if value < max_age_date:
            raise ValidationError(self.message % { "years": self.max_age })


class OlderThen(object):
    message = _("Very young. At least %(years)d years old.")
    min_age = None

    def __init__(self, min_age):
        self.min_age = int(min_age)

    def __call__(self, value):
        now = date.today()
        min_age_date = now - timedelta(days=365*self.min_age)
        if value > min_age_date:
            raise ValidationError(self.message % { "years": self.min_age })


# Файловые валидаторы
class MaxFileSize(object):
    message = _("Maximum file size is %(size)s")
    max_size = None

    def __init__(self, max_size):
        self.max_size = int(max_size)

    def __call__(self, value):
        if value.size > self.max_size:
            raise ValidationError(self.message % \
                                    { "size": filesizeformat(self.max_size) } )


class MinFileSize(object):
    message = _("Minimum file size is %(size)s")
    min_size = None

    def __init__(self, min_size):
        self.min_size = int(min_size)

    def __call__(self, value):
        if value.size < self.min_size:
            raise ValidationError(self.message % \
                                     { "size": filesizeformat(self.min_size) })

