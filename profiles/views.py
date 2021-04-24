from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import UserProfile
from .forms import UserProfileForm

""" a view to return the user dashboard @login_required is a guard decorator to
make sure the user is logged in in order to access certain features defined/called
in the view """
@login_required
def profile(request):
    """ ends user data defined in the UserProfile model, and existed in the database
    fields to the request to view the profile page, and sets its as a local varibale
    'profile_data' to be used to display in the user dashboard."""
    profile_data: UserProfile = request.user.userprofile
    return render(request, 'profiles/profile.html', {'profile': profile_data})


""" a view to return donation history """
def donation_history(request):
    return render(request, 'profiles/donation_history.html')