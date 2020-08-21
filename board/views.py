from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView
from board.models import BoardLI

# TemplateView
class BoardView(ListView):
    template_name = 'board_list.html'
    model = BoardLI

class BoardViewDK(DetailView):
    template_name = 'board_details.html'
    model = BoardLI
    context_object_name = 'details'