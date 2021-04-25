from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Order
from django.conf import settings
from django.utils import timezone
from donations.models import Product
import stripe

"""
def checkout(request):
    return render(request, 'checkout/checkout.html')
"""


@login_required()
def checkout(request):
    if request.method == "POST":
        order_form = Order(request.POST)

        if order_form.is_valid():
            order = order_form.save(commit=False)
            order.save()

            total = 0
            for id, quantity in checkout.items():
                product = get_object_or_404(Product, pk=id)
                total = product.price
                order_line_item = OrderLineItem(
                    order=order,
                    product=product,
                )
                order_line_item.save()

            try:
                customer = stripe.Charge.create(
                    amount=int(total * 100),
                    currency="gbp",
                    description=request.user.email,
                    card=order.cleaned_data['stripe_id']
                )
            except stripe.error.CardError:
                messages.error(request, "Your card was declined!")

            if customer.paid:
                messages.error(request, "You have successfully paid")
                request.session['donation_history'] = {}
                return redirect(reverse('profile'))
            else:
                messages.error(request, "Unable to take payment")
        else:
            print(order.errors)
            messages.error(request, "We were unable to take a payment with that card!")
    else:
        payment_form = order()
        order_form = Order()

    return render(request, "checkout.html",
                  {"order_form": order_form, "payment_form": payment_form, "publishable": settings.STRIPE_PUBLIC_KEY})