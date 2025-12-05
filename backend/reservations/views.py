from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from django.contrib import messages
from .models import Reservation


def home(request: HttpRequest) -> HttpResponse:
    return render(request, 'home.html')


def reserve(request: HttpRequest) -> HttpResponse:
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        date_str = request.POST.get('date')
        time_str = request.POST.get('time')
        guests_str = request.POST.get('guests')

        if not all([name, email, phone, date_str, time_str, guests_str]):
            messages.error(request, 'Vennligst fyll ut alle feltene.')
        else:
            try:
                from datetime import date as _date, time as _time
                # Parse ISO formats from input controls
                y, m, d = map(int, date_str.split('-'))
                hh, mm = map(int, time_str.split(':'))
                parsed_date = _date(y, m, d)
                parsed_time = _time(hh, mm)
                guests_val = int(guests_str)

                Reservation.objects.create(
                    name=name,
                    email=email,
                    phone=phone,
                    date=parsed_date,
                    time=parsed_time,
                    guests=guests_val,
                )
                messages.success(request, 'Reservasjonen er registrert!')
                return redirect('reserve')
            except ValueError:
                messages.error(request, 'Ugyldig dato, tid eller antall gjester.')
            except Exception as e:
                messages.error(request, f'Kunne ikke lagre reservasjonen. Prøv igjen. Feil: {e}')

    return render(request, 'reserve.html')

def menu(request: HttpRequest) -> HttpResponse:
    return render(request, 'menu.html')
