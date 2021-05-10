from django.urls import path
from . import views

urlpatterns = [
    path('', views.profile, name='profile'),
    path('donation-history/', views.donationHistoryView, name='donationHistoryView'),
]