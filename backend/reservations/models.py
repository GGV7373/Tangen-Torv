from django.db import models


class Table(models.Model):
    number = models.PositiveIntegerField(unique=True)
    capacity = models.PositiveIntegerField()
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"Bord {self.number} (kapasitet: {self.capacity})"


class Reservation(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    date = models.DateField()
    time = models.TimeField()
    guests = models.PositiveIntegerField()
    table = models.ForeignKey(Table, on_delete=models.PROTECT, null=True, blank=True, related_name='reservations')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        table_part = f" bord {self.table.number}" if self.table_id else ""
        return f"{self.name}{table_part} - {self.date} {self.time} ({self.guests})"