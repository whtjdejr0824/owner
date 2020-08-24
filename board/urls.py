from django.urls import path, re_path
from board.views import *
from django.contrib import admin

app_name = 'board'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', BoardView.as_view(), name='board'),
    path('<int:pk>/', BoardViewDK.as_view(), name='details'),

    # Example: /board/archive/
    path('archive/', BoardAV.as_view(), name='Board_archive'),

    # Example: /board/archive/2020/
    path('archive/<int:year>/', BoardYAV.as_view(), name='post_year_archive'),
    # Example: /board/archive/2020/Aug/
    path('archive/<int:year>/<str:month>/', BoardMAV.as_view(), name='post_month_archive'),
    # Example: /board/archive/2019/Aug/25/
    path('archive/<int:year>/<str:month>/<int:day>/', BoardDAV.as_view(), name='post_day_archive'),
    # Example: /board/archive/today/
    path('archive/today/', BoardTAV.as_view(), name='post_today_archive'),
]