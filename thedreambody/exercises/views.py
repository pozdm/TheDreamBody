from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect
from django.urls import reverse
from django.template.loader import render_to_string


menu = [{'title': 'Главная', 'id': 'home'},
        {'title': 'Тренировки', 'id': 'training'},
        {'title': 'Питание', 'id': 'eat'},
        {'title': 'Информация', 'id': 'about'},
        {'title': 'Вход в аккаунт', 'id': 'login'},
        ]


def index(request):
    data = {
        'title': 'Главная страница',
        'menu': menu,
    }
    return render(request, 'exercises/index.html', context=data)


def about(request):
    return render(request, 'exercises/about.html', context={'title': 'О сайте', 'menu': menu,})


def training(request):
    return render(request, 'exercises/training.html', context={'title': 'Тренировки', 'menu': menu,})


def eat(request):
    return render(request, 'exercises/eat.html', context={'title': 'Еда', 'menu': menu,})


def login(request):
    return render(request, 'exercises/login.html', context={'title': 'Вход в систему', 'menu': menu,})


def exercises(request):
    pass


def page_not_found(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')