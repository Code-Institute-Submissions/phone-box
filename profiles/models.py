from django.db import models
from django.db.models import Sum
from django.conf import settings
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


""" A user profile model for defining user information to be recorded in the SQLite3
database """
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    default_first_name = models.CharField(max_length=200, null=True, blank=True)
    default_last_name = models.CharField(max_length=200, null=True, blank=True)
    default_username = models.CharField(max_length=20, null=True, blank=True)
    default_email = models.CharField(max_length=80, null=True, blank=True)
    default_street_address1 = models.CharField(max_length=200, null=True, blank=True)
    default_street_address1 = models.CharField(max_length=200, null=True, blank=True)
    default_postcode = models.CharField(max_length=7, null=True, blank=True)
    default_password = models.CharField(max_length=40, null=True, blank=True)

    def __str__(self):
        return self.user.username


@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    """
    Sets a reciever to be required, when user information is recieved, create an
    instance and save the profile/user information. 
    Create or update the user profile.
    """
    if created:
        UserProfile.objects.create(user=instance)
    # Existing users: just save the profile
    instance.userprofile.save()

""" A class defining tables in the database to be used to record a donation entry, each
time a stripe payment is made through the stripe API """
class donationHistory(models.Model):
    user_profile = models.ForeignKey(UserProfile, on_delete=models.SET_NULL,
                                     null=True, blank=True, related_name='donationHistory')
    package = models.CharField(max_length=200, null=True, blank=True)
    price = models.DecimalField(decimal_places=0, max_digits=3, null=True, blank=True)
    username = models.CharField(max_length=200, null=True, blank=True)
    email = models.EmailField(max_length=254, null=False, blank=False)
    date = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name