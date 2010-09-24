# -*- coding: utf-8 -*-

from django.db import models

from helpers import validators as add_valid

# Create your models here.
class Author(models.Model):
    first_name = models.CharField(u"Имя", max_length=50)
    second_name = models.CharField(u"Отчество(second name)",
                                   max_length=50,
                                   blank=True)
    surname = models.CharField(u"Фамилия", max_length=50)
    nickname = models.CharField(u"Псевдоним", max_length=50, blank=True)
    birth_date = models.DateField(u"Дата рождения",
                                  blank=True,
                                  null=True,
                                  validators=[
                                        add_valid.in_past,
                                        add_valid.OlderThen(10)
                                      ])
    death_date = models.DateField(u"Дата смерти",
                                  blank=True,
                                  null=True,
                                  validators=[
                                        add_valid.in_past,
                                      ])
    photo = models.ImageField(u"Фото",
                              upload_to="uploads/authors/photo",
                              blank=True,
                              validators=[
                                    add_valid.MaxFileSize(1024*1024*3), 
                                  ])

    def __unicode__(self):
        return u"Автор: %s %s" %( self.first_name, self.surname)

    class Meta:
        verbose_name = u"Авторы"
        verbose_name_plural = u"Авторы"

