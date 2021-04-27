from django.shortcuts import render, redirect, reverse, get_object_or_404, HttpResponse
from django.views.decorators.http import require_POST
from django.contrib import messages
from django.conf import settings

from checkout.models import Order
import stripe

from donations.models import Product
from profiles.models import UserProfile
from profiles.forms import UserProfileForm


def checkout(request, item_id):

    donation = request.session.get('donation', {})
    donation[item_id]

    print(request.session['donation'])
    return render(request, 'checkout/checkout.html', donation)

def pay_now(request):

    donation = request.session.get('donation', {})

    order_form = OrderForm()
    template = 'checkout/checkout.html'

    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51IcwMYIXOx9uZSSgsHfRJknAxd9ghJVcy7xI83IdyiUfj7EZ7cjsdBwJBUvMNGKRZSb1bwN288Z7p83aLTb0Opoo00hIm3whET',
        'client_secret': 'test client secret',
    }

    return render(request, template, context)