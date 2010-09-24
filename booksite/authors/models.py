# -*- coding: utf-8 -*-

from django.db import models

# Create your models here.
class Author(models.Model):
    first_name = models.CharField(u"Имя", max_length=50)
    second_name = models.CharField(u"Отчество(second name)",
                                   max_length=50,
                                   blank=True)
    surname = models.CharField(u"Фамилия", max_length=50)
    nickname = models.CharField(u"Псевдоним", max_length=50, blank=True)
    birth_date = models.DateField(u"Дата рождения", blank=True, null=True)
    death_date = models.DateField(u"Дата смерти", blank=True, null=True)

    def __unicode__(self):
        return u"Автор: %s %s" %( self.first_name, self.surname)

    class Meta:
        verbose_name = u"Авторы"
        verbose_name_plural = u"Авторы"

