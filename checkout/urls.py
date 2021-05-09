from django.urls import path
from . import views

urlpatterns = [
    path('add/<item_id>', views.checkout, name='checkout'),
    path('', views.charge, name="charge"),
    path('success/<str:args>/', views.success_message, name="success"),
]