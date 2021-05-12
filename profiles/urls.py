from django.urls import path
from . import views

# URL patterns associated with the profiles app
urlpatterns = [
    path('', views.profile, name='profile'),
    path('donation-history/', views.donationHistoryView, name='donationHistoryView'),
]