from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import UserProfile
from django import forms

class UserProfileForm(forms.ModelForm):
    model = UserProfile
    exclude = ('user',)
    placeholders = {
        'first_name': 'First Name',
        'last_name': 'Last Name',
        'username': 'Username',
        'email': 'Email',
        'password1': 'Password',
    }
