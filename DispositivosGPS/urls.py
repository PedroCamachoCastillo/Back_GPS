from django.urls import path, re_path
from django.conf.urls import include
from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets
from DispositivosGPS import views


urlpatterns = [
    re_path(r'^dispositivos/$', views.DispositivosGPSList.as_view()),
    re_path(r'^dispositivos/(?P<pk>\d+)$', views.DispositivosGPSList.as_view()),
]

