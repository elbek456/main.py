CREATE DATABASE Najot_talim;
USE Najot_talim;
CREATE TABLE user
(
    id       BIGINT PRIMARY KEY AUTO_INCREMENT,
    name     VARCHAR(64) NOT NULL,
    surname  VARCHAR(64) NOT NULL,
    age      INT         NOT NULL,
    username INT         NOT NULL,
    passvord INT         NOT NULL,
    gender   INT         NOT NULL
);


INSERT INTO user (name, surname, age, username, passvord, gender)
VALUES ('Ali', 'Karimov', 25, 'ali25', 'ali12345', 'Erkak'),
       ('Madina', 'Usmonova', 22, 'madina22', 'madina2024', 'Ayol'),
       ('Javohir', 'Rahmonov', 28, 'javohir_r', 'javohir1996', 'Erkak'),
       ('Dilrabo', 'Sodiqova', 38, 'dilrabo_s', 'dilrabo777', 'Ayol'),
       ('Otabek', 'Yuldashev', 30, 'otabek30', 'otabek000', 'Erkak'),
       ('Shahzoda', 'Nazarova', 21, 'shahzoda_n', 'shahzoda123', 'Ayol'),
       ('Sanjar', 'Turg‘unov', 27, 'sanjar_t', 'sanjar4321', 'Erkak'),
       ('Mohira', 'Qodirova', 23, 'mohira_q', 'mohira654', 'Ayol'),
       ('Baxtiyor', 'Norbo‘tayev', 29, 'baxtiyor_n', 'baxtiyor999', 'Erkak'),
       ('Gulnoza', 'Hamidova', 26, 'gulnoza_h', 'gulnoza321', 'Ayol');

SELECT age AS 'yosh'
FROM user
WHERE age>15 AND age>30;

SELECT username FROM user WHERE age = 17;




