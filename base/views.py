from django.shortcuts import render
from django.db.models import Sum
from profiles.models import donationHistory


def index(request):
    """ A view to return the index template/landing page (the first view the user will see
    when they visit the site """

    return render(request, 'home/index.html')