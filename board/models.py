from __future__ import unicode_literals
from django.db import models
from django.urls import reverse

class BoardLI(models.Model):
    name = models.CharField('NAME', max_length=100)
    title = models.CharField('TITLE', max_length=50, blank=True)
    content = models.TextField('CONTENT')

    def __str__(self):
        return self.name