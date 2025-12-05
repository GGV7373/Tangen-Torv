from django.db import models


class Table(models.Model):
<<<<<<< Updated upstream
    number = models.PositiveIntegerField(unique=True)
    capacity = models.PositiveIntegerField()
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"Bord {self.number} (kapasitet: {self.capacity})"
=======
    name = models.CharField(max_length=100)
    seats = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.name} ({self.seats})"
>>>>>>> Stashed changes


class Reservation(models.Model):
    table = models.ForeignKey(Table, on_delete=models.CASCADE, related_name="reservations")
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    date = models.DateField()
    time = models.TimeField()
    guests = models.PositiveIntegerField()
    table = models.ForeignKey(Table, on_delete=models.PROTECT, null=True, blank=True, related_name='reservations')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        indexes = [
            models.Index(fields=["table"]),
            models.Index(fields=["date", "time"]),
        ]
        constraints = [
            models.UniqueConstraint(fields=["table", "date", "time"], name="uniq_table_datetime"),
        ]

    def __str__(self):
<<<<<<< Updated upstream
        table_part = f" bord {self.table.number}" if self.table_id else ""
        return f"{self.name}{table_part} - {self.date} {self.time} ({self.guests})"
=======
        return f"{self.name} - {self.table} - {self.date} {self.time} ({self.guests})"
>>>>>>> Stashed changes
