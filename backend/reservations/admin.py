from django.contrib import admin
from .models import Reservation, Bord

@admin.register(Reservation)
class ReservationAdmin(admin.ModelAdmin):
	list_display = ("navn", "telefon", "dato", "tidspunkt", "antall_personer", "bord")
	list_filter = ("dato", "tidspunkt")
	search_fields = ("navn", "telefon")
	actions = ["delete_selected"]
	list_display_links = ("navn",)

@admin.register(Bord)
class BordAdmin(admin.ModelAdmin):
	list_display = ("navn", "antall_plasser")
	search_fields = ("navn",)
	actions = ["delete_selected"]
	list_display_links = ("navn",)

# No stored email model; emails are provided at reservation time and in admin form
