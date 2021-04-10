from django.shortcuts import render

# Profile Views created here.
def profile(request):
    """ A view to return the profile page"""
    return render(request, 'profiles/profile.html')