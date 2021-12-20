from django.urls import path

from . import views

urlpatterns = [
    path('new_app', views.index,name='new_app'),
]