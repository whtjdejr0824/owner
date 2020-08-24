from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView
from board.models import BoardLI
from django.views.generic import ListView, DetailView
from django.views.generic.dates import ArchiveIndexView, YearArchiveView, MonthArchiveView, DayArchiveView, TodayArchiveView
from django.views.generic import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy

# TemplateView
class BoardView(ListView):
    template_name = 'board_list.html'
    model = BoardLI
    context_object_name = "boards"
    paginate_by = 10

class BoardViewDV(DetailView):
    template_name = 'board_detail.html'
    model = BoardLI
    context_object_name = 'details'

class BoardCreateView(CreateView):
    model = BoardLI
    template_name = 'board_form.html'
    fields = ['name', 'title', 'content']
    # initial = {'slug': 'auto-filling-do-not-input'}
    success_url = reverse_lazy('board:board')

    def form_valid(self, form):
        return super().form_valid(form)

