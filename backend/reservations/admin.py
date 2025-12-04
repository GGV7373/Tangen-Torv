from django.contrib import admin
from .models import Table, Reservation

@admin.register(Table)
class TableAdmin(admin.ModelAdmin):
	list_display = ("number", "capacity", "is_active")
	list_filter = ("is_active",)


@admin.register(Reservation)
class ReservationAdmin(admin.ModelAdmin):
	list_display = ("name", "date", "time", "guests", "table")
	list_filter = ("date", "time")
