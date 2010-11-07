# -*- coding: utf-8 -*-

from django.conf import settings
from django.core.paginator import Paginator, InvalidPage, EmptyPage
from django.http import HttpResponse, Http404
from django.shortcuts import redirect, get_object_or_404, render_to_response
from django.template import RequestContext
from django.views.generic.simple import direct_to_template

from authors.models import Author, FirstLetter


AUTHORS_PER_PAGE = getattr(settings, 'AUTHORS_PER_PAGE', 50)


def authors_list_by_letter(request, letter):
    letter = get_object_or_404(FirstLetter, letter=letter)
    authors = Author.objects.filter(letter=letter).order_by('surname')
    c = {
            "authors": authors,
            "letters": FirstLetter.objects.all().order_by('letter')
        }
    return render_to_response('authors/list.html', c,
                              context_instance=RequestContext(request))


def authors_list_all(request):
    authors = Author.objects.all().order_by('surname')
    c = {
            "authors": authors,
            "letters": FirstLetter.objects.all().order_by('letter')
        }
    return render_to_response('authors/list.html', c,
                              context_instance=RequestContext(request))


def authors_details(request, pk):
    author = get_object_or_404(Author, pk=pk)
    c = { "author": author }
    return render_to_response('authors/details.html', c,
                              context_instance=RequestContext(request))

