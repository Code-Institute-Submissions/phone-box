from django.shortcuts import render

# Register Views created here.
def register(request):
    """ A view to return the register page"""
    return render(request, 'register/register.html')