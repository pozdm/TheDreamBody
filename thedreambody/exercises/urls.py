from django.urls import path, register_converter
from . import views
from . import converters


register_converter(converters.FourDigitYearConverter, 'year4')

urlpatterns = [
    path('', views.index, name='home'),
    path('about/', views.about, name='about'),
    path('training/', views.training, name='training'),
    path('eat/', views.eat, name='eat'),
    path('login/', views.login, name='login'),

    path('training/exercises/', views.exercises, name='exercises'),

    # path('archive/<year4:year>/', views.archive, name='archive'),
]