from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView
from blog.models import BlogBoard

# TemplateView
class BlogView(ListView):
    template_name = 'post.html'
    model = BlogBoard



