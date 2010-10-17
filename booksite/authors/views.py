# -*- coding: utf-8 -*-

from django.conf import settings
from django.core.paginator import Paginator, InvalidPage, EmptyPage
from django.http import HttpResponse, Http404
from django.shortcuts import redirect, get_object_or_404
from django.views.generic.simple import direct_to_template
# Create your views here.

from authors.models import Author, FirstLetter

AUTHORS_PER_PAGE = getattr(settings, 'AUTHORS_PER_PAGE', 50)

def authors_list(request, authors_qs, context=None):
    # Пагинация
    paginator = Paginator(authors_qs, AUTHORS_PER_PAGE)
    try:
        page = int(request.GET.get('page', '1'))
    except ValueError:
        page = 1
    try:
        authors_page = paginator.page(page)
    except (EmptyPage, InvalidPage):
        authors_page = paginator.page(paginator.num_pages)
    c = {
            "authors": authors_page.object_list,
            "authors_page": authors_page,
            "letters": FirstLetter.objects.all().order_by('letter')
        }
    return direct_to_template(request, 'authors.html', c)


def authors_list_by_letter(request, letter):
    letter = get_object_or_404(FirstLetter, letter=letter)
    authors = Author.objects.filter(letter=letter).order_by('surname')
    return authors_list(request, authors)


def authors_list_all(request):
    authors = Author.objects.all().order_by('surname')
    return authors_list(request, authors)


def authors_details(request, pk):
    author = get_object_or_404(pk=pk)
    return HttpResponse(u"%s" % author)

