from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import UserProfile
from .forms import UserProfileForm


def profile(request):
    """ a view to return the user dashboard """
    return render(request, 'profiles/profile.html')