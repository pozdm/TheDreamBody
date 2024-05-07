from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render


def index(request):
    return HttpResponse('<h1>Страница приложения the dream body</h1>')


def categories(request, cat_id):
    return HttpResponse(f'<h1>Упражнения на группы мышц</h1><p>id: {cat_id}</p>')


def categories_by_slug(reguest, cat_slug):
    return HttpResponse(f'<h1>Упражнения на группы мышц</h1><p>slug: {cat_slug}</p>')


def archive(request, year):
    if year == 2003:
        raise Http404()

    return HttpResponse(f'<h1>Архив по годам</h1><p>{year}</p>')


def page_not_found(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')