from django.shortcuts import render
from django.db.models import Sum
from profiles.models import donationHistory


def index(request):
    """ A view to return the index page, and render out the sum total of all
    donations made"""

    return render(request, 'home/index.html')