import uuid

from django.db import models
from django.db.models import Sum
from django.conf import settings
from profiles.models import UserProfile, User

# Create your models here.

class SubscriptionMailingList(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    email = models.CharField(max_length=255, null=True, blank=True)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name