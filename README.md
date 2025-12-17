# Tangen-Torv
Dette er netsiden + backend for nettsiden til Tangen Torv restaurant.

Denne nettsiden har mulighet for å vise meny, informasjon om restauranten, åpningstider, ta imot reservasjoner fra kunder, vise kontaktinformasjon og admin-panel for å administrere reservasjoner.

## Fremdriftsplan
For detaljert prosjektstatus og planlegging, se [Plan.md](Plan.md)

## Kunde: Tangen Torv Restaurant
Beskrivelse av kunden og deres behov:

- Vise meny
- Vise åpningstider
- Mulighet for reservasjon av bord
- Vise kontaktinformasjon
- Admin-panel for håndtering av reservasjoner
- E-postbekreftelse ved reservasjon

## Teknologi

### Frontend
HTML + CSS + JavaScript

- [x] Lage templates for nettsiden (base, home, menu, reserve, admin)
- [x] Lage statiske filer (CSS, JS, bilder)
- [x] Lage sider (Hjem, Meny, Reservasjon)
- [x] Implementere responsivt design
- [x] Dark mode support
- [x] Admin reservasjonsvisning med grid layout

### Backend
Django for backend  
SQLite for databasen - se [Database.md](Database.md)

- [x] Lage Django prosjekt
- [x] Lage Django app for reservasjoner
- [x] Lage modeller for reservasjoner (Bord og Reservasjon)
- [x] Lage views for håndtering av reservasjoner
- [x] Lage URL-ruter for appen
- [x] Koble frontend med backend
- [x] Implementere forretningslogikk (tidsvindu, max per dag)
- [x] E-postbekreftelse ved reservasjon
- [x] Admin-panel for staff-brukere
- [x] Autentisering og autorisasjon

## Database
- **Type:** SQLite
- **Filnavn:** `tangen-torv.db`
- **Tabeller:**
  - `Bord`: id, navn, antall_plasser
  - `Reservasjon`: id, bord_id (FK), navn, telefon, dato, tidspunkt, antall_personer, epost, kommentar

Se [database.sql](backend/database.sql) for fullstendig schema.

## Forretningsregler
- Reservasjoner kun tillatt mellom kl. 12:00 og 23:00
- Maksimalt 10 reservasjoner per dag (5 på søndager)
- Unikt tidspunkt per bord

## Hvordan kjøre prosjektet

### Lokalt (utviklingsmiljø)
```bash
cd backend
python manage.py runserver
```
Applikasjonen kjører på http://127.0.0.1:8000/

### Med Docker
```bash
cd backend
docker-compose up
```
- Django-app: http://localhost:5000
- Nginx: http://localhost:80
- SQLite Web Admin: http://localhost:8080

## Mappestruktur
```plaintext
Tangen-Torv/
├── backend/
│   ├── docker-compose.yml
│   ├── Dockerfile
│   ├── manage.py
│   ├── requirements.txt
│   ├── database.sql
│   ├── tangen-torv.db
│   │
│   ├── Tangen-torv/
│   │   ├── __init__.py
│   │   ├── settings.py
│   │   ├── urls.py
│   │   ├── wsgi.py
│   │   └── asgi.py
│   │
│   ├── reservations/
│   │   ├── __init__.py
│   │   ├── admin.py
│   │   ├── apps.py
│   │   ├── models.py
│   │   ├── views.py
│   │   ├── urls.py
│   │   └── migrations/
│   │
│   ├── templates/
│   │   ├── base.html
│   │   ├── home.html
│   │   ├── reserve.html
│   │   ├── menu.html
│   │   ├── admin_reservations.html
│   │   ├── emails/
│   │   │   └── reservation_confirmation.html
│   │   └── registration/
│   │       └── login.html
│   │
│   ├── static/
│   │   ├── css/
│   │   │   └── style.css
│   │   ├── js/
│   │   │   └── script.js
│   │   └── img/
│   │
│   └── nginx/
│       ├── default.conf
│       └── Dockerfile
│
├── Database.md
├── Plan.md
├── README.md
└── LICENSE
```

## Funksjoner

### Kundesiden
- **Hjem:** Velkommen og oversikt
- **Meny:** Visning av restaurantens meny
- **Reservasjon:** Skjema for å bestille bord
  - Validering av dato, tid og antall gjester
  - E-postbekreftelse (valgfritt)
  - Kommentarfelt for spesielle ønsker

### Admin-panel (kun for staff)
- Oversikt over alle reservasjoner
- Filtrering etter dato
- Statistikk (total, siste 7 dager)
- Rutegraf (timeslots med reservasjoner)
- Grid-visning av reservasjoner med kort
- Detaljert liste-visning
- Send e-postbekreftelse til kunder
- Slette reservasjoner

## E-postkonfigurasjon
Systemet er konfigurert for å sende e-postbekreftelser via Gmail SMTP. Se [settings.py](backend/Tangen-torv/settings.py) eller [docker-compose.yml](backend/docker-compose.yml) for konfigurasjon.

## Dokumentasjon
- [Database.md](Database.md) - Database-modell og struktur
- [Plan.md](Plan.md) - Prosjektstatus og fremdriftsplan
- [database.sql](backend/database.sql) - SQLite schema og seed data

## Lisens
Se [LICENSE](LICENSE) for mer informasjon.
