    Airplanes (tail_number, make, model, year)
VALUES
INSERT INTO
    ('N21126', 'Cessna', '172M Skyhawk', 1974),
    ('N147KD', 'Cessna', '152', 1979),
    ('N900XP', 'Beechcraft','35 Bonanza', 1970),
    ('N56RVA', 'Piper', 'J-3 Cub', 1940),
    ('N738AB', 'Mooney', 'M20A', 1959),
    ('N528CJ', 'Mooney', 'M20C', 1960),
    ('N202KM', 'Cirrus', 'SR22', 2001),
    ('N8731T', 'Cirrus', 'SD20', 1999),
    ('N94RWS', 'Diamond', 'DA40', 2005),
    ('N605FX', 'Diamond', 'DA20', 2004)
;

INSERT INTO
    Mechanics (mechanic_id, first_name, last_name, certification_last_renewed)
VALUES
    (11, 'Alice', 'Kilpatrick', '2025-03-01'),
    (20, 'Bob', 'Lamb', '2024-01-22'),
    (30, 'Carol', 'Morrison', '2024-03-31'),
    (40, 'David', 'Nguyen', '2025-02-24'),
    (50, 'Emily', 'Oliphant', '2024-08-22'),
    (60, 'Frank', 'Pham', '2024-10-30'),
    (70, 'Gemma', 'Smith', '2025-01-10'),
    (80, 'Hank', 'Thomas', '2025-02-12'),
    (90, 'Isabel', 'Ubuntu', '2024-11-22'),
    (99, 'Jack', 'Ventus', '2024-12-04')
;

INSERT INTO
    Parts (part_id, part_name, vendor_name, airworthiness_certified)
VALUES
    (100, 'Tires', 'Goodyear', '2024-07-01'),
    (200, 'Brakes', 'Goodyear', '2023-08-18'),
    (300, 'Batteries', 'Energizer', '2023-09-01'),
    (400, 'Tail Light', 'General Electric', '2025-01-05'),
    (500, 'Navigation Lights', 'General Electric', '2024-05-12'),
    (600, 'Propeller', 'Spin Aviation', '2024-06-14'),
    (700, 'Engine', 'Lycoming', '2023-10-04'),
    (800, 'Fuel Gauge', 'Safety First Avionics', '2023-12-20'),
    (900, 'GPS', 'Garmin', '2024-07-31'),
    (999, 'Transponder', 'Safety First Avionics', '2025-03-05')
;

INSERT INTO
    Services (service_id, service_description, service_date, tail_number, part_id, mechanic_id)
VALUES
    (1000, 'Replacement', '2025-03-14', 'N605FX', 999, 50),
    (2000, 'Software Update', '2025-03-20', 'N94RWS', 900, 60),
    (3000, 'Replacement', '2025-03-14', 'N8731T', 100, 40),
    (4000, 'Replacement', '2025-03-14', 'N738AB', 400, 70),
    (5000, 'Repair', '2025-03-14', 'N900XP', 600, 30),
    (6000, 'Replacement', '2025-03-14', 'N147KD', 200, 80),
    (7000, 'Inspection', '2025-03-14', 'N21126', 700, 20),
    (8000, 'Replacement', '2025-03-14', 'N202KM', 300, 11),
    (9000, 'Inspection', '2025-03-14', 'N528CJ', 700, 99),
    (9999, 'Replacement', '2025-03-14', 'N605FX', 800, 50)
;