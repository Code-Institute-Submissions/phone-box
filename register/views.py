from django.shortcuts import render, redirect
from django.contrib.auth.models import auth
from .models import UserProfile
from .forms import UserProfileForm

# Register Views created here.

def register(request):

    if request.method == "POST":
        model = UserProfile
        forms = UserProfileForm

        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        user = UserProfile.objects.create(
            first_name=first_name, last_name=last_name, username=username,
            email=email, password=password1)
        user.save();
        print('User Created')
        return (request, "register.html")

    else:
        return render(request, 'register/register.html')