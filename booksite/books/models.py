# -*- coding: utf-8 -*-

from django.contrib.auth.models import User
from django.db import models

from authors.models import Author
from helpers import validators as add_valid


class Book(models.Model):
    title = models.CharField(u"Название", max_length=250)
    authors = models.ManyToManyField(Author, verbose_name=u"Авторы")

    abstract = models.CharField(u"Аннотация", max_length=400, blank=True)
    cover = models.ImageField(u"Обложка",
                              upload_to="uploads/books/covers",
                              blank=True,
                              validators=[
                                    add_valid.MaxFileSize(1024*1024*3),
                                  ])
    owner = models.ForeignKey(User, verbose_name=u"Заливший")
    added = models.DateTimeField(u"Добавлен", auto_now_add=True)

    def __unicode__(self):
        _authors = ", ".join(map(lambda x: u"%s %s" %(x.first_name,x.surname),\
                                 self.authors.all()))
        return u"Книга: %s, авторы: %s" %(self.title, _authors)

    class Meta:
        verbose_name = u"Книга"
        verbose_name_plural = u"Книги"


class BookFile(models.Model):
    book = models.ForeignKey(Book, verbose_name=u"Книга")
    file = models.FileField(u"Файл",
                            upload_to="uploads/books/files",
                            validators=[
                                    add_valid.MaxFileSize(1024*1024*10),
                                ])
    owner = models.ForeignKey(User, verbose_name=u"Заливший")
    added = models.DateTimeField(u"Добавлен", auto_now_add=True)

    def __unicode__(self):
        return u"Файл к книге: %s" %(self.book.title)

    class Meta:
        verbose_name = u"Файл к книге"
        verbose_name_plural = u"Файлы к книгам"

