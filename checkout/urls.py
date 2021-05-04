from django.urls import path
from . import views

urlpatterns = [
    path('add/<item_id>', views.checkout, name='checkout'),
]