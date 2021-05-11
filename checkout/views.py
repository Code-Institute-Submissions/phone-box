from django.shortcuts import render, redirect, reverse, get_object_or_404, HttpResponse
from django.views.decorators.http import require_POST
from django.contrib import messages
from django.conf import settings

from profiles.models import donationHistory
import stripe

from donations.models import Product
from profiles.models import UserProfile
from profiles.forms import UserProfileForm
from datetime import datetime

stripe.api_key = "sk_test_51IcwMYIXOx9uZSSgQxT1iIVgoz5v1nbszaklyXojNDW3hKNt6a7RvDm22wVKEEunUiWbq5oi1CKzRi39M8LRsYKg00RVuThhvT"

def checkout(request, item_id):
	""" A View to return the checkout page, and call product data from
	the SQLite3 database based on the data-_item-id passed via the urls from
	the donations page based on the user selection """

	itemIdInt = int(item_id)
	product = Product.objects.get(id=itemIdInt)

	context = {
        "product": product
    }
	return render(request, "checkout/checkout.html", context)


def charge(request):
	""" This view sends a post request with the card token to the stripe API
	and makes a payment, then redirects to a payment success message """
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

		if request.user.is_authenticated:

			myDate = datetime.now()
			formatedDate = myDate.strftime("%Y-%m-%d %H:%M:%S")
			user_profile_id = request.user.id
			username = request.user.username
			email = request.user.email
			package = Product.objects.get(price=amount)
			price = request.POST['amount']
			date = formatedDate

			user_donations = donationHistory(user_profile_id=user_profile_id, username=username, email=email,
				package=package, price=price, date=date)
			user_donations.save()

			return redirect(reverse('success', args=[amount]))

		else:

			myDate = datetime.now()
			formatedDate = myDate.strftime("%Y-%m-%d %H:%M:%S")
			username = "anonymous"
			email=request.POST['email']
			package = Product.objects.get(price=amount)
			price = request.POST['amount']
			date = formatedDate

			user_donations = donationHistory(username=username, email=email,
				package=package, price=price, date=date)
			user_donations.save()

			return redirect(reverse('success', args=[amount]))

		return redirect(reverse('success', args=[amount]))


def success_message(request, args):
	""" A view to return a payment success message """
	amount = args

	return render(request, 'checkout/checkout_success.html', {'amount':amount})