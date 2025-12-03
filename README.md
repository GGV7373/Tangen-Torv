# Tangen-Torv
Dette er netsiden + backedn for nettsiden til Tangen Torv resturang

# Frontend
HTML + CSS + JS

[] Lage templets for nettsiden
[] Lage statiske filer (CSS, JS, bilder)
[] Lage sider (Hjem, Meny, Reservasjon)


# Backend

Dijanog for backaned
PostgressSQl for databasen

[x] Lage Django prosjekt
[] Lage Django app for reservasjoner
[] Lage modeller for reservasjoner
[] Lage views for håndtering av reservasjoner
[] Lage URL-ruter for appen
[] Koble frontend med backend

## Mappestruktur

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
│   └── menu.html
│
└── static/
    ├── css/
    │   └── style.css
    ├── js/
    │   └── script.js
    └── img/
        └── (your images here)
