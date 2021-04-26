from django.shortcuts import render, redirect, reverse, get_object_or_404, HttpResponse
from django.views.decorators.http import require_POST
from django.contrib import messages
from django.conf import settings

from checkout.models import Order
import stripe

from donations.models import Product
from profiles.models import UserProfile
from profiles.forms import UserProfileForm


def checkout(request):

    return render(request, 'checkout/checkout.html')