from django.urls import path
from . import views

# URL path defined here for profiles app
urlpatterns = [
    path('', views.profile, name='profile'),
]