from django.urls import path
from . import views

# URL path defined here for 'donations' app
urlpatterns = [
    path('', views.donations, name='donations'),
]