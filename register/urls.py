from django.urls import path
from . import views

# URL path defined here for register app
urlpatterns = [
    path('', views.register, name='register'),
]