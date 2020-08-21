from django.views.generic import TemplateView
from django.shortcuts import render

# TemplateView
class HomeView(TemplateView):
    template_name = 'index.html'
