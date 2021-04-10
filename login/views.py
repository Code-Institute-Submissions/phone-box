from django.shortcuts import render

# Login Views created here.
def login(request):
    """ A view to return the login page"""
    return render(request, 'login/login.html')