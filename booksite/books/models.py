# -*- coding: utf-8 -*-

from django.conf import settings
from django.contrib.auth.models import User
from django.db import models
from django.db.models.fields.files import FieldFile
from django.db.models import F
from django.db.models.signals import post_save, pre_delete, m2m_changed
from django.utils.translation import ugettext_lazy as _

from authors.models import Author
from helpers import validators as add_valid


DEFAULT_IMAGE_3_4 = getattr(settings, "DEFAULT_IMAGE_3_4", None)

class Book(models.Model):
    title = models.CharField(_("Title"), max_length=250)
    authors = models.ManyToManyField(Author, verbose_name=_("Authors"))

    abstract = models.CharField(_("Abstract"), max_length=400, blank=True)
    cover = models.ImageField(_("Cover"),
                              upload_to="uploads/books/covers",
                              blank=True,
                              validators=[
                                    add_valid.MaxFileSize(1024*1024*3),
                                  ])
    owner = models.ForeignKey(User, verbose_name=_("Uploader"))
    added = models.DateTimeField(_("Added"), auto_now_add=True)

    @property
    def safe_cover(self):
        if not self.cover and DEFAULT_IMAGE_3_4:
            return FieldFile(self, self.cover, DEFAULT_IMAGE_3_4)
        return self.cover

    def __unicode__(self):
        _authors = ", ".join(map(lambda x: u"%s %s" %(x.first_name,x.surname),\
                                 self.authors.all()))
        return _("Book: %(book)s, authors: %(authors)s") % \
                                  { "book" : self.title, "authors": _authors }

    class Meta:
        verbose_name = _("Book")
        verbose_name_plural = _("Books")


def inc_or_dec_author_book_count(sender, instance, action, pk_set, **kwargs):
    print action
    print pk_set
    if not pk_set:
        return
    _add = False
    _del = False
    if action == 'post_add':
        _add = True
    elif action == 'post_remove':
        _del = True
    elif action == 'post_clear':
        _del = True
    else:
        return
    if _add is True:
        Author.objects.filter(pk__in=pk_set)\
                      .update(book_count=F('book_count') + 1)
    elif _del is True:
        Author.objects.filter(pk__in=pk_set)\
                      .update(book_count=F('book_count') - 1)
m2m_changed.connect(inc_or_dec_author_book_count, Book.authors.through,
                                                dispatch_uid="books.count.m2m")


class BookFile(models.Model):
    book = models.ForeignKey(Book, verbose_name=_("Book"))
    file = models.FileField(_("File"),
                            upload_to="uploads/books/files",
                            validators=[
                                    add_valid.MaxFileSize(1024*1024*10),
                                ])
    owner = models.ForeignKey(User, verbose_name=_("Uploader"))
    added = models.DateTimeField(_("Added"), auto_now_add=True)

    def __unicode__(self):
        return _("File %(id)d to book %(title)s") % \
                                    { "id": self.pk, "title": self.book.title }

    class Meta:
        verbose_name = _("Book file")
        verbose_name_plural = _("Book files")

