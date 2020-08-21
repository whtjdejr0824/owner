from __future__ import unicode_literals
from django.db import models
from django.urls import reverse

class BlogBoard(models.Model):
    title = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return self.title
