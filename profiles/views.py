from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from profiles.models import UserProfile, donationHistory, SubscriptionMailingList
from .forms import UserProfileForm


@login_required
def profile(request):
    """ a view to return the user dashboard @login_required is a guard decorator to
    make sure the user is logged in in order to access certain features defined/called
    in the view.
    ends user data defined in the UserProfile model, and existed in the database
    fields to the request to view the profile page, and sets its as a local variable
    'profile_data' to be used to display in the user dashboard."""
    profile_data: UserProfile = request.user.userprofile

    return render(request, 'profiles/profile.html', {'profile': profile_data})


def donationHistoryView(request):
    """ A view to render out personalised donation history for the
    user currently logged in. filtered entries by user id """
    user_profile_id = request.user.id
    user_donations = donationHistory.objects.all().filter(user_profile_id=user_profile_id)

    context = {
        'user_donations': user_donations,
    }

    return render(request, 'profiles/donation_history.html', context)

def subscribeToNewsletter(request):
    """ A view to handle Mailing list subscriptions """

    if request.is_ajax():
        data =  request.GET['data']

        if data == True:
            user_id = request.user.id
            email = request.user.email

            subscribe = SubscriptionMailingList(user_id=user_id, email=email)
            subscribe.save()

        elif data == False:
            user_id = request.user.id
            email = request.user.email

            subscribe = SubscriptionMailingList.objects.filter(user_id=user_id).delete()