CREATE TABLE catalogue (
    city_1 VARCHAR(50) NOT NULL,
    city_2 VARCHAR(50) NOT NULL,
    nautical_miles INTEGER NOT NULL,
    time_minutes INTEGER NOT NULL,
    PRIMARY KEY (city_1, city_2)
);