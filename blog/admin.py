from django.contrib import admin

from blog.models import BlogBoard

@admin.register(BlogBoard)
class BlogBoardAdmin(admin.ModelAdmin):
    list_display = ('title',)