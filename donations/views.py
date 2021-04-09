from django.shortcuts import render

# Create your views here.
def donations(request):
    """ A view to return the donations page"""
    return render(request, 'donations/donations.html')