from django.shortcuts import render, redirect, reverse, get_object_or_404
from .models import Product
import os
from profiles.models import donationHistory, UserProfile


def donations(request):
    """ A view to return the donations page and call product data from 
    the SQLite3 databse """
    products = Product.objects.all()

    context = {
        'products': products,
    }
    
    return render(request, 'donations/donations.html', context)

