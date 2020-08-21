from __future__ import unicode_literals
from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

class Information(models.Model):
    name = models.CharField(max_length=50, blank=True)
    address = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return self.name