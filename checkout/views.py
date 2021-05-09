from django.shortcuts import render, redirect, reverse, get_object_or_404, HttpResponse
from django.views.decorators.http import require_POST
from django.contrib import messages
from django.conf import settings

from checkout.models import Order
import stripe

from donations.models import Product
from profiles.models import UserProfile
from profiles.forms import UserProfileForm

stripe.api_key = "sk_test_51IcwMYIXOx9uZSSgQxT1iIVgoz5v1nbszaklyXojNDW3hKNt6a7RvDm22wVKEEunUiWbq5oi1CKzRi39M8LRsYKg00RVuThhvT"

def checkout(request, item_id):

    itemIdInt = int(item_id)
    product = Product.objects.get(id=itemIdInt)

    context = {
        "product": product
    }

    return render(request, "checkout/checkout.html", context)

def charge(request):

	if request.method == 'POST':
		print('Data:', request.POST)

		amount = int(request.POST['amount'])

		customer = stripe.Customer.create(
			email=request.POST['email'],
			name=request.POST['nickname'],
			source=request.POST['stripeToken']
			)

		charge = stripe.Charge.create(
			customer=customer,
			amount=amount*100,
			currency='gbp',
			description="Donation"
            )

	return redirect(reverse('success', args=[amount]))


def success_message(request, args):
	amount = args
	return render(request, 'checkout/checkout_success.html', {'amount':amount})