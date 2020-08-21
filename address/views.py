from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView
from address.models import Information

# TemplateView
class AddressView(ListView):
    template_name = 'information.html'
    model = Information

class AddressViewDK(DetailView):
    template_name = 'address_detail.html'
    model = Information
    context_object_name = 'detail'