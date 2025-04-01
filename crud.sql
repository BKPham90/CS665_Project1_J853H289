-- CREATE
INSERT INTO
    Airplanes (tail_number, make, model, year)
VALUES
    ('N457RJ', 'Cessna', '172M Skyhawk', 1976)
;

-- READ
SELECT
    *
FROM
    Services
WHERE
    service_date BETWEEN '2024-10-01' AND '2024-12-25'
;

-- UPDATE
UPDATE
    Parts
SET
    part_name = 'Elevator'
WHERE
    part_id = 600
;

-- DELETE
DELETE FROM
    Mechanics
WHERE
    mechanic_id = 70
;