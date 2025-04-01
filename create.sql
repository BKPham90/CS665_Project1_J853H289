CREATE TABLE IF NOT EXISTS
    Airplanes (
        tail_number TEXT PRIMARY KEY,
        make TEXT,
        model TEXT,
        year INTEGER
);

CREATE TABLE IF NOT EXISTS
    Mechanics (
        mechanic_id INTEGER PRIMARY KEY AUTOINCREMENT,
        first_name TEXT,
        last_name TEXT,
        certification_last_renewed DATE
);

CREATE TABLE IF NOT EXISTS
    Parts (
        part_id INTEGER PRIMARY KEY,
        part_name TEXT,
        vendor_name TEXT,
        airworthiness_certified DATE
);

CREATE TABLE IF NOT EXISTS
    Services (
        service_id INTEGER PRIMARY KEY AUTOINCREMENT,
        service_description TEXT,
        service_date DATE,
        tail_number TEXT,
        part_id INTEGER,
        mechanic_id INTEGER,
        FOREIGN KEY (tail_number) REFERENCES Airplanes(tail_number),
        FOREIGN KEY (part_id) REFERENCES Parts(part_id)
        FOREIGN KEY (mechanic_id) REFERENCES Mechanics(mechanic_id)
);