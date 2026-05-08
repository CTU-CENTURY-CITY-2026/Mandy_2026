CREATE DATABASE ApexLogisticsDB;
USE ApexLogisticsDB;


CREATE TABLE tblUsers (
    user_id INT PRIMARY KEY IDENTITY(1,1),
    username VARCHAR(50) NOT NULL,
    password VARCHAR(50) NOT NULL,
    role VARCHAR(20) NOT NULL
);


CREATE TABLE tblProducts (
    product_id INT PRIMARY KEY IDENTITY(1,1),
    name VARCHAR(100) NOT NULL,
    price DECIMAL(10,2) NOT NULL,
    stock_qty INT NOT NULL
);


CREATE TABLE tblOrders (
    order_id INT PRIMARY KEY IDENTITY(1,1),
    user_id INT,
    product_id INT,
    quantity INT NOT NULL
);


CREATE TABLE tblWarehouses (
    warehouse_id INT PRIMARY KEY IDENTITY(1,1),
    location VARCHAR(100) NOT NULL,
    capacity INT NOT NULL
);


INSERT INTO tblUsers (username, password, role) VALUES
('lily', 'pass123', 'admin'),
('thabo', 'pass456', 'staff'),
('kea', 'pass789', 'manager'),
('nikki', 'pass000', 'staff'),
('eve', 'pass111', 'admin');

INSERT INTO tblProducts (name, price, stock_qty) VALUES
('Laptop', 999.99, 50),
('Mouse', 25.00, 200),
('Keyboard', 45.50, 150),
('Monitor', 350.00, 75),
('USB Hub', 15.99, 300);

INSERT INTO tblOrders (user_id, product_id, quantity) VALUES
(1, 1, 2),
(2, 3, 5),
(3, 2, 1),
(4, 5, 10),
(5, 4, 3);

INSERT INTO tblWarehouses (location, capacity) VALUES
('KwaZulu-Natal', 5000),
('North West', 3000),
('Western Cape', 4000),
('Limpopo', 2500),
('Gauteng', 3500);
