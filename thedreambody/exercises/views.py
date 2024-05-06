from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return HttpResponse('страница приложения the dream body')


def categories(request):
    return HttpResponse('упражнения на группы мышц')

