# Database-modell

## Bord
En liste over bord som kan reserveres.

| id | navn      | antall_plasser |
|----|-----------|----------------|
| 1  | Bord 1    | 4              |
| 2  | Bord 2    | 2              |
| 3  | Bord 3    | 6              |
| ...| ...       | ...            |

## Reservasjon
Reservasjoner knyttes til et bord via fremmednøkkel.

| id | bord_id (FK) | navn | telefon | dato       | tidspunkt | antall_personer |
|----|--------------|------|---------|------------|-----------|-----------------|
| 1  | 2            | Ola  | 12345678| 2024-06-10 | 18:00     | 2               |
| ...| ...          | ...  | ...     | ...        | ...       | ...             |

- `bord_id` er en fremmednøkkel som peker til `Bord.id`.

## Fremmednøkler og relasjoner
- **Bord** har en primærnøkkel `id`.
- **Reservasjon** har en fremmednøkkel `bord_id` som refererer til `Bord.id`.
- En reservasjon kan kun opprettes hvis det aktuelle bordet er ledig på ønsket dato og tidspunkt.

## Sjekk om bord er ledig (pseudo-SQL)
For å reservere et bord må man sjekke om det finnes en reservasjon for det bordet på ønsket tidspunkt:

```sql
SELECT * FROM reservasjon
WHERE bord_id = {ønsket_bord_id}
  AND dato = '{ønsket_dato}'
  AND tidspunkt = '{ønsket_tidspunkt}'
```

Hvis ingen rader returneres, er bordet ledig og kan reserveres.

## Eksempel på tabell-relasjoner

```plaintext
Bord (1) <--- (M) Reservasjon
```
- Ett bord kan ha mange reservasjoner, men ikke samtidig.
- Reservasjon har en fremmednøkkel til Bord.
