# Tangen-Torv
Dette er netsiden + backedn for nettsiden til Tangen Torv resturang

Denne nettsiden skal ha mulighet for å vise meny, informasjon om restauranten, åpningstider, ta imot reservasjoner fra kunder, vise kontaktinformasjon og andre relevante kundetjenester.

# For dagsplan se Plan.md [her](Plan.md)


# Kunde : Tangen Torv Resturang
Beskrivelse av kunden og deres behov:

- Vise meny
- Vise åpningstider
- Mulighet for reservasjon av bord
- Vise kontaktinformasjon
- Andre kundetjenester


# Frontend
HTML + CSS + JS

 - [x] Lage templets for nettsiden
 - [x] Lage statiske filer (CSS, JS, bilder)
 - [ ] Lage sider (Hjem, Meny, Reservasjon, Åpningstider, Kontakt)
 - [ ] Lage templets for nettsiden
 - [ ] Lage statiske filer (CSS, JS, bilder)
 - [ ] Lage sider (Hjem, Meny, Reservasjon, Åpningstider, Kontakt)


# Backend

Dijanog for backaend
PostgressSQl for databasen

 - [x] Lage Django prosjekt
 - [ ] Lage Django app for reservasjoner
 - [ ] Lage modeller for reservasjoner
 - [ ] Lage views for håndtering av reservasjoner
 - [ ] Lage URL-ruter for appen
 - [ ] Koble frontend med backend


## Mappestruktur
```plaintext
tangen-torv/
├── docker-yml
├── manage.py
│
├── tangen-torv/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── asgi.py
│
├── reservations/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   └── migrations/
│       └── __init__.py
│
├── templates/
│   ├── base.html
│   ├── home.html
│   ├── reserve.html
│   ├── menu.html
│   ├── opening_hours.html
│   └── contact.html
│
└── static/
    ├── css/
    │   └── style.css
    ├── js/
    │   └── script.js
    └── img/
        └── (bilder)
```
