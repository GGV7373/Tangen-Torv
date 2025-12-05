from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('reserve/', views.reserve, name='reserve'),
    path('menu/', views.menu, name='menu'),
    path('availability/', views.availability, name='availability'),
    path('reserve/submit/', views.submit_reservation, name='submit_reservation'),
    path('reserve/success/', views.reserve_success, name='reserve_success'),
]
