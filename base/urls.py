from django.urls import path
from . import views

# URL path defined here for 'home' app
urlpatterns = [
    path('', views.index, name='home'),
]