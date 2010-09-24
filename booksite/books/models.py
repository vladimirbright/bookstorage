# -*- coding: utf-8 -*-


from django.db import models

from authors.models import Author
from helpers import validators as add_valid


class Book(models.Model):
    title = models.CharField(u"Название", max_length=250)
    authors = models.ManyToManyField(Author, verbose_name=u"Авторы")

    abstract = models.CharField(u"Аннотация", max_length=400, blank=True)
    page_count = models.PositiveIntegerField(u"Количество страниц",
                                             blank=True,
                                             null=True)
    cover = models.ImageField(u"Обложка",
                              upload_to="uploads/books/covers",
                              blank=True,
                              validators=[
                                    add_valid.MaxFileSize(1024*1024*3),
                                  ])

    def __unicode__(self):
        _authors = ", ".join(map(lambda x: u"%s %s" %(x.first_name,x.surname),\
                                 self.authors.all()))
        return u"Книга: %s, авторы: %s" %(self.title, _authors)

    class Meta:
        verbose_name = u"Книга"
        verbose_name_plural = u"Книги"

