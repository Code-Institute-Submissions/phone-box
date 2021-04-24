from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

""" A user profile model for maintaining default delivery information and order history """
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


""" sets a reciever to be required, when user information is recieved, create an
instance and save the profile/user information. """
@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    """
    Create or update the user profile
    """
    if created:
        UserProfile.objects.create(user=instance)
    # Existing users: just save the profile
    instance.userprofile.save()