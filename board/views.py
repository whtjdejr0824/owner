from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView
from board.models import BoardLI, models
from django.views.generic import ListView, DetailView
from django.views.generic.dates import ArchiveIndexView, YearArchiveView, MonthArchiveView, DayArchiveView, \
    TodayArchiveView
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


class BoardUpdateView(UpdateView):
    model = BoardLI
    fields = ['name', 'title', 'content']  # 폼 모델에 사용할 필드  폼 모델 자동 생성
    success_url = reverse_lazy('board:board')
    template_name = 'board_form.html'


class BoardDeleteView(DeleteView):
    model = BoardLI
    success_url = reverse_lazy('board:board')
    template_name = 'board_delete.html'


# class BoardChangeLV(LoginRequiredMixin, ListView):
#     template_name = 'board/board_change_list.html'
#     def get_queryset(self):
#         return Board.objects.filter(owner=self.request.user)
