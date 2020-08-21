from django.urls import path, re_path
from address.views import AddressView, AddressViewDK
from django.contrib import admin

app_name = 'address'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', AddressView.as_view(), name='address'),
    path('<int:pk>/', AddressViewDK.as_view(), name='detail'),
]