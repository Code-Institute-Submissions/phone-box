from django.urls import path
from . import views

# URL path defined here for login app
urlpatterns = [
    path('', views.login, name='login'),
]