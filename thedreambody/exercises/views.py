from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect
from django.urls import reverse
from django.template.loader import render_to_string


menu = [{'title': 'Главная', 'id': 'home'},
        {'title': 'Тренировки', 'id': 'training'},
        {'title': 'Питание', 'id': 'eat'},
        {'title': 'Информация', 'id': 'about'},
        {'title': 'Вход', 'id': 'login'},
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
    data = [
        {'title': 'Подтягивания', 'picture': 'https://mosturnik.ru/wp-content/uploads/0/0/b/00be913ea0488eecf55181be741ecfa5.png', 'info': 'Описание'},
        {'title': 'Жим лежа', 'picture': 'https://put-sily.ru/wp-content/uploads/5/2/a/52a1352f0413b7023c1032e2f7591b2e.jpeg', 'info': 'Описание'},
        {'title': 'Французский жим', 'picture': 'https://avatars.mds.yandex.net/i?id=deb879830f4e9b475049e539333843a886901117-10638736-images-thumbs&n=13', 'info': 'Описание'},
    ]
    return render(request, 'exercises/training.html', context={'title': 'Тренировки', 'menu': menu, 'data': data, })


def eat(request):
    return render(request, 'exercises/eat.html', context={'title': 'Еда', 'menu': menu,})


def login(request):
    return render(request, 'exercises/login.html', context={'title': 'Вход в систему', 'menu': menu,})


def exercises(request):
    pass


def page_not_found(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')