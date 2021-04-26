from django.shortcuts import render, redirect, reverse, get_object_or_404
from .models import Product
import os
import stripe

""" A view to return the donations page"""
def donations(request):

    products = Product.objects.all()

    context = {
        'products': products,
    }
    
    return render(request, 'donations/donations.html', context)
