from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
<<<<<<< Updated upstream
from .models import Table, Reservation
from django.utils.dateparse import parse_date, parse_time
=======
from django.db.models import Q
from .models import Table, Reservation
>>>>>>> Stashed changes


def home(request: HttpRequest) -> HttpResponse:
    return render(request, 'home.html')
<<<<<<< Updated upstream
=======


def reserve(request: HttpRequest) -> HttpResponse:
    return render(request, 'reserve.html')

def menu(request: HttpRequest) -> HttpResponse:
    return render(request, 'menu.html')


def availability(request: HttpRequest) -> HttpResponse:
    date = request.GET.get('date')
    time = request.GET.get('time')
    guests = request.GET.get('guests')

    available = []
    error = None
    if date and time and guests:
        try:
            guests_int = int(guests)
            # Tables with enough seats and not reserved at the exact slot
            reserved_table_ids = Reservation.objects.filter(date=date, time=time).values_list('table_id', flat=True)
            available = Table.objects.filter(seats__gte=guests_int).exclude(id__in=list(reserved_table_ids)).order_by('seats')
        except ValueError:
            error = "Guests must be a number"

    context = {
        'available_tables': available,
        'date': date or '',
        'time': time or '',
        'guests': guests or '',
        'error': error,
    }
    return render(request, 'availability.html', context)


def submit_reservation(request: HttpRequest) -> HttpResponse:
    if request.method == 'POST':
        table_id = request.POST.get('table_id')
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        date = request.POST.get('date')
        time = request.POST.get('time')
        guests = request.POST.get('guests')

        if not all([table_id, name, phone, date, time, guests]):
            return render(request, 'reserve.html', {'error': 'All required fields must be filled.'})

        try:
            table = Table.objects.get(id=table_id)
            guests_int = int(guests)
            if guests_int > table.seats:
                return render(request, 'reserve.html', {'error': 'Guests exceed table capacity.'})

            Reservation.objects.create(
                table=table,
                name=name,
                email=email or '',
                phone=phone,
                date=date,
                time=time,
                guests=guests_int,
            )
            return redirect('reserve_success')
        except Table.DoesNotExist:
            return render(request, 'reserve.html', {'error': 'Selected table not found.'})
        except Exception as e:
            return render(request, 'reserve.html', {'error': f'Could not create reservation: {e}'})

    return render(request, 'reserve.html')


def reserve_success(request: HttpRequest) -> HttpResponse:
    return render(request, 'reserve_success.html')
>>>>>>> Stashed changes
