# -*- coding: utf-8 -*-

u"""
    Дополнительные валидаторы.
"""
from datetime import datetime, date, timedelta

from django.core.exceptions import ValidationError
from django.template.defaultfilters import filesizeformat


# Временные валидаторы
def in_future(value):
    if (isinstance(value, date) and value < date.today()) or \
       (isinstance(value, datetime) and value < datetime.now()):
        raise ValidationError(u"Только в будущем")


def in_past(value):
    if (isinstance(value, date) and value > date.today()) or \
       (isinstance(value, datetime) and value > datetime.now()):
        raise ValidationError(u"Только в прошлом")


# Возрастные валидаторы
class YoungerThen(object):
    message = u"Слишком старый. Максимум %d лет"
    max_age = None

    def __init__(self, max_age):
        self.max_age = int(max_age)

    def __call__(self, value):
        now = date.today()
        max_age_date = now - timedelta(days=365*self.max_age)
        if value < max_age_date:
            raise ValidationError(self.message % self.max_age)


class OlderThen(object):
    u""" Старше чем """
    message = u"Слишком молодой. Минимум %d лет"
    min_age = None

    def __init__(self, min_age):
        self.min_age = int(min_age)

    def __call__(self, value):
        now = date.today()
        min_age_date = now - timedelta(days=365*self.min_age)
        if value > min_age_date:
            raise ValidationError(self.message % self.min_age)


# Файловые валидаторы
class MaxFileSize(object):
    message = u"Максимальный размер файла %s"
    max_size = None

    def __init__(self, max_size):
        self.max_size = int(max_size)

    def __call__(self, value):
        if value.size > self.max_size:
            raise ValidationError(self.message %filesizeformat(self.max_size))


class MinFileSize(object):
    message = u"Минимальный размер файла %s"
    min_size = None

    def __init__(self, min_size):
        self.min_size = int(min_size)

    def __call__(self, value):
        if value.size < self.min_size:
            raise ValidationError(self.message %filesizeformat(self.min_size))
