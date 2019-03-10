from django.urls import path, re_path
from django.conf.urls import include
from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets
from Unidades import views


urlpatterns = [
    re_path(r'^unidades/$', views.UnidadesList.as_view()),
    re_path(r'^unidades/(?P<pk>\d+)$', views.UnidadesList.as_view()),
]

