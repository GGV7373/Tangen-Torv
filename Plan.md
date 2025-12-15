# Prosjektstatus og Fremdriftsplan

## Fullført arbeid

### Dag 1 — Oppsett og grunnmur (FULLFØRT)
- [X] Django-prosjekt opprettet med fullstendig mappehierarki
- [X] Templates-struktur: `base.html`, `home.html`, `menu.html`, `reserve.html`, `admin_reservations.html`
- [X] Statiske filer: `static/css/style.css`, `static/js/script.js`
- [X] Registrering-templates: `registration/login.html`
- [X] E-post-template: `emails/reservation_confirmation.html`

### Dag 2 — Database og modeller (FULLFØRT)
- [X] SQLite-database (`tangen-torv.db`) konfigurert
- [X] Modeller: `Bord` og `Reservasjon` med alle felter:
  - Bord: `id`, `navn`, `antall_plasser`
  - Reservasjon: `id`, `bord_id` (FK), `navn`, `telefon`, `dato`, `tidspunkt`, `antall_personer`, `epost`, `kommentar`
- [X] Database-schema dokumentert in `database.sql` og `Database.md`
- [X] Admin-panelet konfigurert med tilgang til begge modeller
- [X] Seed data for 6 bord

### Dag 3 — Views og URL-routing (FULLFØRT)
- [X] URL-routing konfigurert for alle sider
- [X] Views implementert: `home`, `menu`, `reserve`, `admin_reservations`
- [X] Autentisering: Login/logout-funksjonalitet
- [X] Staff-beskyttet admin-visning for reservasjoner

### Dag 4 — Skjema og forretningslogikk (FULLFØRT)
- [X] Reservasjonsskjema med validering
- [X] Forretningsregler implementert:
  - Tidsvindu: kun mellom kl. 12:00-23:00
  - Maks reservasjoner per dag: 10 (5 på søndager)
- [X] POST-håndtering med lagring til database
- [X] Django messages for suksess/feilmeldinger
- [X] E-postbekreftelse ved reservasjon (HTML-format)

### Dag 5 — Docker og deployment (FULLFØRT)
- [X] Docker-oppsett med `docker-compose.yml`
- [X] Tjenester konfigurert:
  - `sqlite-web`: Database-administrasjon (port 8080)
  - `app`: Django-applikasjon (port 5000)
  - `web`: Nginx reverse proxy (port 80)
- [X] Miljøvariabler for produksjon
- [X] E-postkonfigurasjon (SMTP Gmail)

## Pågående arbeid

### Database-synkronisering
- Problem: SQL-filen oppdateres ikke automatisk til lokal database
- Løsning nødvendig: Kjøre `database.sql` mot `tangen-torv.db`

## Gjenstående oppgaver

### Testing og kvalitetssikring
- [ ] Skrive enhetstester for modeller
- [ ] Skrive integrasjonstester for views
- [ ] Teste e-postfunksjonalitet i produksjonsmiljø
- [ ] Validere forretningsregler grundig

### Forbedringer og optimalisering
- [ ] Bordvalg-funksjonalitet (automatisk tildeling av ledig bord)
- [ ] Konfliktsjekk: sikre at samme bord ikke dobbeltbookes
- [ ] Admin-side for å sende e-post til eksisterende reservasjoner
- [ ] Responsivt design for mobil
- [ ] Forbedret feilhåndtering og logging

### Deployment
- [ ] Produksjons-secrets (SECRET_KEY, e-postpassord)
- [ ] HTTPS-konfigurasjon
- [ ] Backup-strategi for database
- [ ] Overvåking og logging

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

## Notater
- Database: SQLite (`backend/tangen-torv.db`)
- Django models bruker `managed = False` - schema håndteres manuelt via SQL
- E-post: Konfigurert med Gmail SMTP (se `settings.py` og `docker-compose.yml`)

