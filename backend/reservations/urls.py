from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('reserve/', views.reserve, name='reserve'),
    path('menu/', views.menu, name='menu'),
    path('admin-reservations/', views.admin_reservations, name='admin_reservations'),
]
