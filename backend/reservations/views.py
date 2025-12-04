from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from .models import Table, Reservation
from django.utils.dateparse import parse_date, parse_time


def home(request: HttpRequest) -> HttpResponse:
    return render(request, 'home.html')
