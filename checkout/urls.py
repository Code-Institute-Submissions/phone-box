from django.urls import path
from . import views

# URL patterns associated with the checkout app
urlpatterns = [
    path('add/<item_id>', views.checkout, name='checkout'),
    path('', views.charge, name="charge"),
    path('success/<str:args>/', views.success_message, name="success"),
]