-- Active: 1764939728026@@127.0.0.1@3306
-- Active: 1764849528977@@127.0.0.1@3306@mydatabase
-- SQLite schema for Bord and Reservasjon (converted from MySQL)

PRAGMA foreign_keys = ON;

-- Table: Bord
CREATE TABLE IF NOT EXISTS Bord (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    navn TEXT NOT NULL,
    antall_plasser INTEGER NOT NULL
);

-- Table: Reservasjon
CREATE TABLE IF NOT EXISTS Reservasjon (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    bord_id INTEGER NOT NULL,
    navn TEXT NOT NULL,
    telefon TEXT NOT NULL,
    dato TEXT NOT NULL,         -- store ISO date 'YYYY-MM-DD'
    tidspunkt TEXT NOT NULL,    -- store time 'HH:MM:SS'
    antall_personer INTEGER NOT NULL,
    epost TEXT,                 -- customer's email (nullable)
    kommentar TEXT,             -- optional note from customer (nullable)
    CONSTRAINT fk_bord FOREIGN KEY (bord_id) REFERENCES Bord(id)
);

-- Indexes and unique constraint
CREATE INDEX IF NOT EXISTS idx_res_bord ON Reservasjon (bord_id);
CREATE INDEX IF NOT EXISTS idx_res_datetime ON Reservasjon (dato, tidspunkt);
CREATE UNIQUE INDEX IF NOT EXISTS uniq_bord_datetime ON Reservasjon (bord_id, dato, tidspunkt);

-- Seed data (SQLite doesn't support ON DUPLICATE KEY). Use INSERT OR REPLACE.
INSERT OR REPLACE INTO Bord (id, navn, antall_plasser) VALUES
    (1, 'Bord 1', 4),
    (2, 'Bord 2', 2),
    (3, 'Bord 3', 6),
    (4, 'Bord 4', 4),
    (5, 'Bord 5', 2),
    (6, 'Bord 6', 8);



-- Example reservation
INSERT OR REPLACE INTO Reservasjon (id, bord_id, navn, telefon, dato, tidspunkt, antall_personer, epost, kommentar)
VALUES (1, 2, 'Ola', '12345678', '2024-06-10', '18:00:00', 2, 'hello@gmail.com', 'Vennligst plasser meg ved vinduet.');

-- ---- Upgrade existing database (run once) ----
-- SQLite doesn't support IF NOT EXISTS for columns.
-- Run these ALTERs once against an existing DB to add the new fields.
-- If the columns already exist, these statements will fail; ignore those errors.
-- ALTER TABLE Reservasjon ADD COLUMN epost TEXT;
-- ALTER TABLE Reservasjon ADD COLUMN kommentar TEXT;

-- View: Available tables prototype (note: SQLite lacks parameterized views; keep columns simple)
DROP VIEW IF EXISTS AvailableTables;
CREATE VIEW AvailableTables AS
SELECT 
    b.id AS bord_id,
    b.navn,
    b.antall_plasser
FROM Bord b;
