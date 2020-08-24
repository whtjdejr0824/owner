from __future__ import unicode_literals
from django.db import models
from django.urls import reverse
from taggit.managers import TaggableManager

class BoardLI(models.Model):
    name = models.CharField('NAME', max_length=100)
    title = models.CharField('TITLE', max_length=50, blank=True)
    content = models.TextField('CONTENT')


    def __str__(self):
        return self.title

    def get_absoulte_url(self):  # 현재 데이터의 절대 경로 추출
        return reverse('board:board', args=(self.slug,))
    #
    # def get_previous(self): # 이전 데이터 추출
    #     return self.get_previous_by_modify_dt()
    #
    # def get_next(self): # 다음 데이터 추출
    #     return self.get_next_by_modify_dt()

