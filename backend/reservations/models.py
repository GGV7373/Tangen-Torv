from django.db import models


class Bord(models.Model):
    id = models.AutoField(primary_key=True)
    navn = models.TextField()
    antall_plasser = models.IntegerField()

    class Meta:
        db_table = 'Bord'
        managed = False

    def __str__(self):
        return f"{self.navn} ({self.antall_plasser})"


class Reservation(models.Model):
    id = models.AutoField(primary_key=True)
    bord = models.ForeignKey(Bord, on_delete=models.CASCADE, db_column='bord_id')
    navn = models.TextField()
    telefon = models.TextField()
    dato = models.CharField(max_length=10)
    tidspunkt = models.CharField(max_length=8)
    antall_personer = models.IntegerField()

    class Meta:
        db_table = 'Reservasjon'
        managed = False

    def __str__(self):
        return f"{self.navn} - {self.dato} {self.tidspunkt} ({self.antall_personer})"