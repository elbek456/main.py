CREATE DATABASE IF NOT EXISTS marker_db;
USE marker_db;

CREATE TABLE IF NOT EXISTS products
(
    product_id   INT PRIMARY KEY,
    product_name VARCHAR(100) NOT NULL,
    category     VARCHAR(50)  NOT NULL,
    price        DECIMAL(10, 2),
    stock        INT,
    supplier     VARCHAR(100) NOT NULL,
    added_date   DATE
);


INSERT INTO products(product_id, product_name, category, price, stock, supplier, added_date)
VALUES (1, 'Samsung Galaxy A54', 'Telefon', 4500000.00, 15, 'Samsung Uzbekistan', '2025-01-20'),
       (2, 'HP Pavilion Laptop', 'Notebook', 8500000.00, 10, 'HP Distribution', '2025-01-15'),
       (3, 'LG Televizor', 'TV', 3000000.00, 8, 'LG Electronics', '2025-01-18'),
       (4, 'Beko Dazmol', 'Dazmol', 250000.00, 25, 'Beko Distribution', '2025-01-14'),
       (5, 'Xiaomi Redmi Note 13', 'Telefon', 4000000.00, 20, 'Xiaomi Distribution', '2025-01-22'),
       (6, 'Dyson V11', 'Chang yutgich', 6000000.00, 5, 'Dyson Distribution', '2025-01-21'),
       (7, 'Samsung kir yuvish mashinasi', 'Maishiy texnika', 3500000.00, 5, 'Samsung Uzbekistan', '2025-01-21'),
       (8, 'Sony 55" Smart TV', 'TV', 5000000.00, 10, 'Sony Electronics', '2025-01-19'),
       (9, 'Lenovo ThinkPad', 'Notebook', 9000000.00, 12, 'Lenovo Distribution', '2025-01-17'),
       (10, 'Philips Dazmol', 'Dazmol', 180000.00, 50, 'Philips Electronics', '2025-01-16'),
       (11, 'Xiaomi Mi 11', 'Telefon', 5500000.00, 30, 'Xiaomi Distribution', '2025-01-23'),
       (12, 'Miele Chang yutgich', 'Chang yutgich', 10000000.00, 8, 'Miele Distribution', '2025-01-25'),
       (13, 'Samsung QLED TV', 'TV', 4500000.00, 12, 'Samsung Uzbekistan', '2025-01-21'),
       (14, 'LG OLED TV', 'TV', 5500000.00, 10, 'LG Electronics', '2025-01-23'),
       (15, 'Sony PlayStation 5', 'Oyin konsoli', 7000000.00, 7, 'Sony Electronics', '2025-01-18'),
       (16, 'Huawei MateBook', 'Notebook', 7500000.00, 6, 'Huawei Distribution', '2025-01-20');


SELECT product_name, category, price, stock, supplier, added_date
FROM products
ORDER BY category;

SELECT product_name,
       category,
       price,
       stock,
       supplier,
       added_date,
       (price * stock) AS total_value
FROM products;


SELECT product_name, category, price, stock, supplier, added_date
FROM products
WHERE added_date > '2025-01-15'
ORDER BY added_date DESC;


SELECT products.category, AVG(price) AS average_prise, SUM(products.stock) AS total_stock
FROM products
GROUP BY category;






















