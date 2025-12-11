from django.apps import AppConfig
from django.conf import settings


class ReservationsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'reservations'

    def ready(self):
        # Auto-upgrade SQLite schema to include epost and kommentar if missing
        try:
            from django.db import connection
            # Only attempt on SQLite
            if 'sqlite' not in settings.DATABASES['default']['ENGINE']:
                return
            with connection.cursor() as cur:
                cur.execute("PRAGMA table_info(Reservasjon)")
                cols = {row[1] for row in cur.fetchall()}
                to_add = []
                if 'epost' not in cols:
                    to_add.append("ALTER TABLE Reservasjon ADD COLUMN epost TEXT")
                if 'kommentar' not in cols:
                    to_add.append("ALTER TABLE Reservasjon ADD COLUMN kommentar TEXT")
                for ddl in to_add:
                    try:
                        cur.execute(ddl)
                    except Exception:
                        # Ignore if already added by race/other process
                        pass
        except Exception:
            # Don't block app startup on upgrade failure
            pass
