# Prosjektplan (5 dager)

Denne planen bryter ned arbeidet per dag med mål, konkrete oppgaver, leveranser og sjekkpunkter.

## Dag 1 — Oppsett og grunnmur
- Mål: Kjørende Django-prosjekt med mappeoppsett, base-template og statiske filer.
- Oppgaver:
	- Opprette prosjektstruktur og mappehierarki (templates, static/css, static/js, static/img).
	- Starte Django-prosjekt og bekrefte at serveren starter lokalt.
	- Konfigurere `settings.py` for `TEMPLATES` og `STATICFILES_DIRS`.
	- Lage `base.html` + enkel `home.html` med nav til Hjem/Meny/Reservasjon.
	- Legge inn `.gitignore` og initial commit.
- Leveranser:
	- Kjørende server på http://127.0.0.1:8000/.
	- Skjelett for templates og statiske filer.
	- PR/commit med oppsett.
- Sjekkpunkter:
	- `python manage.py runserver` fungerer uten feil.
	- Enkle sider rendres fra templates.

## Dag 2 — Reservasjoner (modeller og admin)
- Mål: Definert `Reservation`-modell og tilgjengelig i admin.
- Oppgaver:
	- Opprette app `reservations` og legge i `INSTALLED_APPS`.
	- Modellfelt: `name`, `email`, `phone`, `date`, `time`, `guests`, `created_at`.
	- Kjør `makemigrations` og `migrate`.
	- Registrere modellen i `admin.py` med nyttig `list_display`/filtre.
	- Opprette superbruker og teste admin-panelet.
- Leveranser:
	- Databasetabeller opprettet og vises i admin.
	- Skjermbilde av admin-liste for reservasjonsobjekter.
- Sjekkpunkter:
	- `python manage.py makemigrations && python manage.py migrate` er OK.
	- `python manage.py createsuperuser` og innlogging i `/admin/` fungerer.

## Dag 3 — Views, URL-er og templates
- Mål: Ruter for Hjem, Meny og Reservasjon med grunnleggende visninger.
- Oppgaver:
	- Lage `reservations.urls` og koble til prosjektets `urls.py`.
	- Implementere `home`, `menu`, `reserve`-views.
	- Templates: `home.html`, `menu.html`, `reserve.html` (skjema visning, ingen lagring ennå).
	- Grunnleggende styling i `static/css/style.css`.
- Leveranser:
	- Navigasjon mellom sider fungerer.
	- Skjermbilder av hver side.
- Sjekkpunkter:
	- Alle ruter svarer med HTTP 200 og riktig template.

## Dag 4 — Koble frontend og backend (skjema → lagring)
- Mål: Innsendt reservasjon lagres i DB med enkel validering og tilbakemelding.
- Oppgaver:
	- Lage `ModelForm` for `Reservation`.
	- Håndtere `POST` i `reserve`-view, validere og lagre.
	- Vise suksessmelding/redirect etter innsending (Django messages).
	- Enkel klientside-validering (HTML5-attributter) ved behov.
- Leveranser:
	- Full flyt: Skjema → validering → lagring → bekreftelse.
	- Et par test-innslag i databasen verifisert i admin.
- Sjekkpunkter:
	- Ugyldige data gir feilmeldinger i form.
	- Gyldige data dukker opp i admin-listen.

## Dag 5 — Test, feilretting og deploy-klargjøring
- Mål: Stabilt minimumsprodukt og klar plan for deploy.
- Oppgaver:
	- Legge til enkle tester (modell + view). Sette opp `pytest` om ønskelig.
	- Rydde opp i `README.md` (kjøre-instruksjoner) og `requirements.txt`.
	- Prod-innstillinger: `ALLOWED_HOSTS`, statiske filer, `.env`-støtte.
	- Velge deploy (f.eks. Railway/Render) eller Docker-klargjøring.
- Leveranser:
	- `requirements.txt`, oppdatert README, enkel test-suite som kjører grønt.
	- Deploy-notat med steg for valgt plattform.
- Sjekkpunkter:
	- `python manage.py collectstatic` fungerer for prod-setup (om aktuelt).
	- Minst én grønn test for hver del (modell/view).

## Strekkmål (om tid)
- Enkel e-postbekreftelse (console backend i dev).
- Paginering/søk i admin og/eller egen liste-side.
- Bedre design og mobiltilpasning.

## Daglige rutiner
- Start: Kort status og plan for dagen (10 min).
- Midt på dagen: Sjekkpunkt og prioriteringsjustering (5 min).
- Slutt: Oppsummering, commit/PR, oppdater `README.md`/Plan.

