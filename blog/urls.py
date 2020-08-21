from django.urls import path, re_path
from blog.views import BlogView
from django.contrib import admin

app_name = 'blog'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', BlogView.as_view(), name='blog'),
]