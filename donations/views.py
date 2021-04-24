from django.shortcuts import render, redirect

""" A view to return the donations page"""
def donations(request):
    return render(request, 'donations/donations.html')


""" A view to return a charge of 5£ """
def charge_cheap(request):
    product = product.objects.name("Cheap")

    if request.method == "POST":
        ('Product:', product)
    return redirect("checkout/checkout.html", args=[product])


""" A view to return a charge of 50£ """
def charge_nice(request):
    product = product.objects.name("Nice")

    if request.method == "POST":
        ('Product:', product)
    return redirect("checkout/checkout.html", args=[product])


""" A view to return a charge of 500£ """
def charge_big_spender(request):
    product = product.objects.name("Big Spender")

    if request.method == "POST":
        ('Product:', product)
    return redirect("checkout/checkout.html", args=[product])