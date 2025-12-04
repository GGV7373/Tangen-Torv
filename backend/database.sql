
-- Table: Bord
CREATE TABLE IF NOT EXISTS Bord (
	id INT AUTO_INCREMENT PRIMARY KEY,
	navn VARCHAR(100) NOT NULL,
	antall_plasser INT NOT NULL
);

-- Table: Reservasjon
CREATE TABLE IF NOT EXISTS Reservasjon (
	id INT AUTO_INCREMENT PRIMARY KEY,
	bord_id INT NOT NULL,
	navn VARCHAR(100) NOT NULL,
	telefon VARCHAR(20) NOT NULL,
	dato DATE NOT NULL,
	tidspunkt TIME NOT NULL,
	antall_personer INT NOT NULL,
	CONSTRAINT fk_bord FOREIGN KEY (bord_id) REFERENCES Bord(id)
);

-- Indexes to speed up lookups by date/time and table
CREATE INDEX IF NOT EXISTS idx_res_bord ON Reservasjon (bord_id);
CREATE INDEX IF NOT EXISTS idx_res_datetime ON Reservasjon (dato, tidspunkt);

-- Prevent overlapping reservations for the same table at the exact date+time
-- Note: MySQL doesn't support functional constraints for time ranges.
-- This UNIQUE enforces one reservation per table per exact date+time slot.
ALTER TABLE Reservasjon
	ADD UNIQUE KEY IF NOT EXISTS uniq_bord_datetime (bord_id, dato, tidspunkt);

-- Seed data for tables
INSERT INTO Bord (navn, antall_plasser) VALUES
	('Bord 1', 4),
	('Bord 2', 2),
	('Bord 3', 6)
ON DUPLICATE KEY UPDATE navn=VALUES(navn), antall_plasser=VALUES(antall_plasser);

-- Example reservation (can be removed)
INSERT INTO Reservasjon (bord_id, navn, telefon, dato, tidspunkt, antall_personer)
VALUES (2, 'Ola', '12345678', '2024-06-10', '18:00:00', 2)
ON DUPLICATE KEY UPDATE navn=VALUES(navn), telefon=VALUES(telefon);

-- View: Available tables for a given date/time and party size
-- Usage: SELECT * FROM AvailableTables WHERE req_dato='2025-12-24' AND req_tid='18:00:00' AND req_antall=4;
DROP VIEW IF EXISTS AvailableTables;
CREATE VIEW AvailableTables AS
SELECT 
	b.id AS bord_id,
	b.navn,
	b.antall_plasser,
	CAST(NULL AS DATE) AS req_dato,
	CAST(NULL AS TIME) AS req_tid,
	CAST(NULL AS SIGNED) AS req_antall
FROM Bord b;

-- Helper query to find available tables at runtime:
-- Replace placeholders with desired values
-- SELECT b.id, b.navn, b.antall_plasser
-- FROM Bord b
-- WHERE b.antall_plasser >= @party_size
--   AND NOT EXISTS (
--     SELECT 1 FROM Reservasjon r
--     WHERE r.bord_id = b.id
--       AND r.dato = @res_date
--       AND r.tidspunkt = @res_time
--   )
-- ORDER BY b.antall_plasser ASC;

-- Optional: stored procedure to get available tables
DROP PROCEDURE IF EXISTS GetAvailableTables;
DELIMITER $$
CREATE PROCEDURE GetAvailableTables(IN res_date DATE, IN res_time TIME, IN party_size INT)
BEGIN
	SELECT b.id AS bord_id, b.navn, b.antall_plasser
	FROM Bord b
	WHERE b.antall_plasser >= party_size
		AND NOT EXISTS (
			SELECT 1 FROM Reservasjon r
			WHERE r.bord_id = b.id
				AND r.dato = res_date
				AND r.tidspunkt = res_time
		)
	ORDER BY b.antall_plasser ASC;
END $$
DELIMITER ;

-- Comments:
-- To check availability: CALL GetAvailableTables('2025-12-24','18:00:00',4);
-- To insert a reservation (after checking availability):
-- INSERT INTO Reservasjon (bord_id, navn, telefon, dato, tidspunkt, antall_personer)
-- VALUES (/*available bord_id*/ 1, 'Navn', 'Telefon', '2025-12-24', '18:00:00', 4);

