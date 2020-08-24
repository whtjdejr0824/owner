from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView
from board.models import BoardLI
from django.views.generic import ListView, DetailView
from django.views.generic.dates import ArchiveIndexView, YearArchiveView, MonthArchiveView, DayArchiveView, TodayArchiveView

# TemplateView
class BoardView(ListView):
    template_name = 'board_list.html'
    model = BoardLI
    context_object_name = "boards"
    paginate_by = 10

class BoardViewDK(DetailView):
    template_name = 'board_details.html'
    model = BoardLI
    context_object_name = 'details'

# ArchiveView
class BoardAV(ArchiveIndexView):
    model= BoardLI
    date_field = 'modify_dt'

class BoardYAV(YearArchiveView):
    model= BoardLI
    date_field = 'modify_dt'
    make_object_list = True

class BoardMAV(MonthArchiveView):
    model= BoardLI
    date_field = 'modify_dt'
    month_format = '%m'

class BoardDAV(DayArchiveView):
    model= BoardLI
    date_field = 'modify_dt'
    month_format = '%m'

class BoardTAV(TodayArchiveView):
    model= BoardLI
    date_field = 'modify_dt'
    month_format = '%m'