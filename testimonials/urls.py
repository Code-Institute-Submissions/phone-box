from django.urls import path
from . import views

# URL path defined here for 'testimonials' app
urlpatterns = [
    path('', views.testimonials, name='testimonials'),
]