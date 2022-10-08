from django.contrib import admin
from django.urls import include, path, re_path
from .views import *
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('',  views.index, name="index"),
    # path('news',  views.news, name="news"),
    # path('',  Index.as_view(), name="index"),
    path('schedule',  views.schedule, name="schedule"),
    # path('latestnews',  views.latestnews, name="latestnews"),
    path('latestnews/<int:pid>', views.latestnews, name='latestnews'),
]