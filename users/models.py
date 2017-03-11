from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Profile(models.Model):

    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    centro = models.TextField(max_length=100, blank=False, null=True, default="")
    responsable = models.TextField(max_length=100, blank=False, null=True, default="")
    phone = models.TextField(max_length=9, blank=False, null=True, default="")

    def __unicode__(self):
        return self.centro