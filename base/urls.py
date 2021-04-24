from django.urls import path
from . import views

""" URL path defined here for 'base' app """
urlpatterns = [
    path('', views.index, name='home'),
]