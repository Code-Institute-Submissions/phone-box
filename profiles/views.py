from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import UserProfile
from .forms import UserProfileForm


@login_required
def profile(request):
    """ a view to return the user dashboard """
    profile_data: UserProfile = request.user.userprofile
    return render(request, 'profiles/profile.html', {'profile': profile_data})


def donation_history(request):
    """ a view to return donation history """
    return render(request, 'profiles/donation_history.html')