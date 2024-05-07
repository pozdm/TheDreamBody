from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect
from django.urls import reverse


def index(request):
    return HttpResponse('<h1>Страница приложения the dream body</h1>')


def categories(request, cat_id):
    return HttpResponse(f'<h1>Упражнения на группы мышц</h1><p>id: {cat_id}</p>')


def categories_by_slug(reguest, cat_slug):
    if cat_slug == 'index':
        return redirect('home', permanent=True)

    return HttpResponse(f'<h1>Упражнения на группы мышц</h1><p>slug: {cat_slug}</p>')


def archive(request, year):
    if year == 2003:
        raise Http404()

    if year == 7777:
        uri = reverse('cats', args=('music', ))
        return redirect(uri)

    return HttpResponse(f'<h1>Архив по годам</h1><p>{year}</p>')


def page_not_found(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')