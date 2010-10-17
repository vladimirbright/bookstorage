# -*- coding: utf-8 -*-

from django.db import models
from django.utils.translation import ugettext_lazy as _

from helpers import validators as add_valid


class FirstLetter(models.Model):
    letter = models.SlugField(_('letter'), max_length=5)

    def __unicode__(self):
        return _('Letter: %(letter)s') % { "letter": self.letter }

    class Meta:
        ordering = ( 'letter', )


class Author(models.Model):
    first_name = models.CharField(_('Name'), max_length=150, blank=True)
    second_name = models.CharField(_('Second name'),
                                   max_length=150,
                                   blank=True)
    surname = models.CharField(_('Surname (name of organisation)'),
                               max_length=150)
    nickname = models.CharField(_('Nickname'), max_length=150, blank=True)
    birth_date = models.DateField(_('Birthday'),
                                  blank=True,
                                  null=True,
                                  validators=[
                                        add_valid.in_past,
                                        add_valid.OlderThen(10)
                                      ])
    death_date = models.DateField(_('Deathday'),
                                  blank=True,
                                  null=True,
                                  validators=[
                                        add_valid.in_past,
                                      ])
    photo = models.ImageField(_('Photo'),
                              upload_to="uploads/authors/photo",
                              blank=True,
                              validators=[
                                    add_valid.MaxFileSize(1024*1024*3),
                                  ])
    letter = models.ForeignKey(FirstLetter,
                               verbose_name=_('First letter'),
                               null=True,
                               default=None)

    def save(self, *args, **kwargs):
        letter, created = \
             FirstLetter.objects.get_or_create(letter=self.surname[:1].lower())
        self.letter = letter
        return super(Author, self).save(*args, **kwargs)

    def __unicode__(self):
        return _("Author: %(name)s %(surname)s") %{
                                                    "name": self.first_name,
                                                    "surname": self.surname
                                                  }

    class Meta:
        verbose_name = _('Author')
        verbose_name_plural = _('Authors')

