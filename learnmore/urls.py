from django.urls import path
from . import views

# URL path defined here for 'learn more' app
urlpatterns = [
    path('', views.learn_more, name='learn_more'),
]