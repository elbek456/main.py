CREATE DATABASE sumdb;
USE sumdb;
CREATE TABLE cars
(
    id      BIGINT PRIMARY KEY AUTO_INCREMENT,
    brant   VARCHAR(50) NOT NULL,
    model   VARCHAR(50) NOT NULL,
    year    INT         NOT NULL,
    price   DECIMAL(10, 2),
    air_bak VARCHAR(50) NOT NULL

);

INSERT INTO CARS(brant, model, year, price, air_bak)
VALUES
        ('CHevrolet','damas',2024,9000,'FALSE'),
        ('Chevrolet','Kaptiva',2025,23000,'TRUE'),
        ('Chevralet','laseti',2019,14000,'TRUE'),
        ('Chevrolet','koblt',2023,18000,'TRUE')







