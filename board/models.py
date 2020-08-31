from __future__ import unicode_literals
from django.db import models
from django.urls import reverse
from taggit.managers import TaggableManager
from django.contrib.auth.models import User
from django.utils.text import slugify



from taggit.managers import TaggableManager

class BoardLI(models.Model):
    name = models.CharField('NAME', max_length=100)
    title = models.CharField('TITLE', max_length=50, blank=True)
    content = models.TextField('CONTENT')

    def __str__(self):
        return self.title


class Meta:
    verbose_name = 'post'
    verbose_name_plural = 'posts'
    db_table = 'board_posts'
    ordering = ('-modify_dt',)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('board:post_detail', args=(self.slug,))

    def get_previous(self):
        return self.get_previous_by_modify_dt()

    def get_next(self):
        return self.get_next_by_modify_dt()

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title, allow_unicode=True)
        super().save(*args, **kwargs)
