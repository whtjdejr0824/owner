from django.urls import path, re_path
from board.views import BoardView, BoardViewDK
from django.contrib import admin

app_name = 'board'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', BoardView.as_view(), name='board'),
    path('<int:pk>/', BoardViewDK.as_view(), name='details'),
]