from django.shortcuts import render, redirect
import os
import stripe

""" A view to return the donations page"""
def donations(request):
    return render(request, 'donations/donations.html')
