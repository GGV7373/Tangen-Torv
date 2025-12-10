from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from django.contrib import messages
from django.db.models import Count
from .models import Reservation
from django.contrib.auth.decorators import login_required, user_passes_test
from django.conf import settings
from django.shortcuts import get_object_or_404


def home(request: HttpRequest) -> HttpResponse:
    return render(request, 'home.html')


def reserve(request: HttpRequest) -> HttpResponse:
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        date_str = request.POST.get('date')
        time_str = request.POST.get('time')
        guests_str = request.POST.get('guests')

        if not all([name, phone, date_str, time_str, guests_str]):
            messages.error(request, 'Vennligst fyll ut alle feltene.')
        else:
            try:
                # Store as text per SQLite schema (YYYY-MM-DD / HH:MM:SS)
                y, m, d = map(int, date_str.split('-'))
                hh, mm = map(int, time_str.split(':'))
                parsed_date = f"{y:04d}-{m:02d}-{d:02d}"
                parsed_time = f"{hh:02d}:{mm:02d}:00"
                guests_val = int(guests_str)

                # Business rules: booking time window and max per day
                # Allow reservations between 12:00 and 23:00 inclusive
                if not (12 <= hh <= 23):
                    messages.error(request, 'Bestilling er kun tillatt mellom kl. 12:00 og 23:00.')
                    return render(request, 'reserve.html')

                # Compute weekday: Monday=0 .. Sunday=6
                import datetime as _dt
                weekday = _dt.date(y, m, d).weekday()
                # Max per day: default 10, Sunday (6) max 5
                max_per_day = 5 if weekday == 6 else 10
                current_count = Reservation.objects.filter(dato=parsed_date).count()
                if current_count >= max_per_day:
                    messages.error(request, f'Maks antall reservasjoner for {parsed_date} er nådd (grense {max_per_day}).')
                    return render(request, 'reserve.html')

                # Default to first table (bord_id=1) if no table selection exists yet
                Reservation.objects.create(
                    navn=name,
                    telefon=phone,
                    dato=parsed_date,
                    tidspunkt=parsed_time,
                    antall_personer=guests_val,
                    bord_id=1,
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


@login_required
@user_passes_test(lambda u: u.is_staff)
def admin_reservations(request: HttpRequest) -> HttpResponse:
    reservations = Reservation.objects.order_by('-id')[:50]
    total = Reservation.objects.count()
    counts_by_date = list(
        Reservation.objects.values('dato').annotate(count=Count('id')).order_by('-dato')
    )
    db_path = settings.DATABASES['default']['NAME']
    return render(
        request,
        'admin_reservations.html',
        {"reservations": reservations, "total": total, "counts_by_date": counts_by_date, "db_path": db_path}
    )


@login_required
@user_passes_test(lambda u: u.is_staff)
def delete_reservation(request: HttpRequest, pk: int) -> HttpResponse:
    if request.method == 'POST':
        res = get_object_or_404(Reservation, pk=pk)
        res.delete()
        messages.success(request, 'Reservasjonen ble slettet.')
    return redirect('admin_reservations')
