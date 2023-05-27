from django.urls import path

from . import views

app_name = 'slackbot'

urlpatterns = [
    path('', views.index, name='index'),
]
