from django.contrib import admin
from .models import Reservation

@admin.register(Reservation)
class ReservationAdmin(admin.ModelAdmin):
	list_display = ("name", "email", "phone", "date", "time", "guests", "created_at")
	search_fields = ("name", "email", "phone")
	list_filter = ("date", "time")
