from django.contrib import admin
from django.urls import path, include
from ..devices import views
from ..users import views
from django.views.generic.base import TemplateView


app_name = 'devices'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home'), name='home'),
    path('users/', include('users.urls'), name='users'),
    path('users/dashboard/', views.dashboard, name='dashboard'),
]

