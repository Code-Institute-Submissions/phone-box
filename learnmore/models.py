from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.
"""
class SubscriptionMailingList(models.Model):
    user = models.ForeignKey('user', on_delete=models.NULL, null=True)
    email = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.user.username
"""