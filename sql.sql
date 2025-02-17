# 1-misoll
# CREATE DATABASE autoDB;
# USE autoDB;
#
# CREATE TABLE cars
# (
#     id          BIGINT PRIMARY KEY AUTO_INCREMENT,
#     brand       VARCHAR(64) NOT NULL,
#     model       VARCHAR(64) NOT NULL,
#     year        INT         NOT NULL,
#     price       DECIMAL(12, 2),
#     has_airbags BOOL        NULL
# );
#
# ALTER TABLE cars
#     ADD COLUMN num_of_rats BIGINT NOT NULL;
#
# ALTER TABLE cars
#     DROP COLUMN num_of_rats;
#
# INSERT INTO cars (brand, model, year, price, has_airbags)
# VALUES ('Toyota', 'Camry', 2023, 26000, TRUE),
#        ('Daewoo', 'Damas', 2025, 99000, FALSE),
#        ('Honda', 'Civic', 2022, 23000, TRUE),
#        ('Ford', 'Mustang', 2024, 30000, TRUE),
#        ('Chevrolet', 'Silverado', 2023, 45000, FALSE),
#        ('Mercedes-Benz', 'C-Class', 2023, 45000, TRUE),
#        ('Hyundai', 'Tucson', 2022, 25000, FALSE);

# 2-misoll
# CREATE DATABASE booksDB;
# USE booksDB;
#
# CREATE TABLE books
# (
#     id             BIGINT PRIMARY KEY AUTO_INCREMENT,
#     title          VARCHAR(128) NOT NULL UNIQUE,
#     author         VARCHAR(64)  NOT NULL,
#     year_published INT          NOT NULL,
#     price          DECIMAL(10, 2)
# );
#
# ALTER TABLE books
#     ADD COLUMN genre VARCHAR(32) NOT NULL;
# ALTER TABLE books
#     ADD COLUMN is_available BOOL DEFAULT TRUE;
#
# ALTER TABLE books
#     DROP COLUMN is_available;
#
# INSERT INTO books (title, author, year_published, price, genre)
# VALUES ('Qiyomat', 'Tolstoy', 1899, 25.50, 'Classic'),
#        ('The Great Gatsby', 'F. Scott Fitzgerald', 1925, 15.99, 'Fiction'),
#        ('Inferno', 'Dan Brown', 2013, 12.99, 'Mystery'),
#        ('Sapiens', 'Yuval Noah Harari', 2011, 22.50, 'Non-Fiction'),
#        ('Harry Potter', 'J.K. Rowling', 1997, 30.00, 'Fantasy');
#

# 3-MISOLL
# CREATE DATABASE studentDB;
# USE studentDB;
# CREATE TABLE students
# (
#     id         BIGINT PRIMARY KEY AUTO_INCREMENT,
#     fIRst_name VARCHAR(64) NOT NULL,
#     age        INT         NOT NULL,
#     course     INT         NOT NULL
# );
#
# INSERT INTO students (first_name, age, course)
# VALUES ('Aziz', 19, 1),
#        ('Shahnoza', 20, 2),
#        ('Bekzod', 21, 3),
#        ('Dilafruz', 22, 4),
#        ('Islom', 18, 1),
#        ('Ziyoda', 20, 2),
#        ('Sardor', 21, 3),
#        ('Madina', 22, 4),
#        ('Jasur', 19, 1),
#        ('Laziza', 23, 4);
#
# SELECT *
# FROM students;


# CREATE DATABASE company;
# USE company;
#
# CREATE TABLE employees
# (
#     id         INT AUTO_INCREMENT PRIMARY KEY,
#     first_name VARCHAR(50)  NOT NULL,
#     last_name  VARCHAR(50)  NOT NULL,
#     department VARCHAR(100) NOT NULL,
#     position   VARCHAR(100) NOT NULL,
#     salary     DECIMAL(10, 2) CHECK (salary BETWEEN 700000 AND 7000000)
# );
#
# INSERT INTO employees (first_name, last_name, department, position, salary)
# VALUES ('John', 'Doe', 'IT', 'Software Engineer', 2500000),
#        ('Jane', 'Smith', 'HR', 'HR Manager', 1800000),
#        ('Robert', 'Brown', 'Finance', 'Financial Analyst', 2000000),
#        ('Emily', 'Johnson', 'Marketing', 'Marketing Specialist', 1500000),
#        ('Michael', 'Wilson', 'IT', 'System Administrator', 2200000),
#        ('Sarah', 'Anderson', 'Finance', 'Accountant', 1700000),
#        ('David', 'Martinez', 'Sales', 'Sales Manager', 2100000),
#        ('Laura', 'Hernandez', 'HR', 'Recruiter', 1400000);
#
# SELECT *
# FROM employees;
#
# SELECT *
# FROM employees
# ORDER BY department;
#
# SELECT *
# FROM employees
# ORDER BY salary DESC
# LIMIT 5;
#
# SELECT department, AVG(salary) AS average_salary
# FROM employees
# GROUP BY department;

# SQLda ORDER BY operatori natijalarni o‘sish (ASC) yoki kamayish (DESC) tartibida saralash uchun ishlatiladi.
# GROUP BY operatori SQLda ma'lumotlarni guruhlash va agregat funksiyalar bilan ishlash uchun ishlatiladi.
# Sql  malumotlar bazasi bilan ishlash bu xam dasturlash tiliga kiradi
