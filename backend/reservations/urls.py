from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('reserve/', views.reserve, name='reserve'),
    path('menu/', views.menu, name='menu'),
    path('admin-reservations/', views.admin_reservations, name='admin_reservations'),
    path('admin-reservations/send-email/<int:pk>/', views.send_reservation_email, name='send_reservation_email'),
    path('admin-reservations/delete/<int:pk>/', views.delete_reservation, name='delete_reservation'),
]
