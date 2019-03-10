from django.urls import path, re_path
from django.conf.urls import include
from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets
from Profile import views


urlpatterns = [
    re_path(r'^profile/$', views.ProfileList.as_view()),
    re_path(r'^profile/(?P<pk>\d+)$', views.ProfileList.as_view()),
]

