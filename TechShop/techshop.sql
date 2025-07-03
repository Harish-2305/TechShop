-- Task:1. Database Design:

-- 1.Create the database named "TechShop"
Create database techshop;
use techshop;

/*2. Define the schema for the Customers, Products, Orders, OrderDetails and Inventory tables
based on the provided schema.*/

-- (1)Creating the Customers Table

create table customers
(
customerID int primary key auto_increment,
FirstName varchar(30) not null,
LastName varchar(30) not null,
Email varchar(50) unique not null,
Phone bigint unique not null,
Address text not null
);
desc customers;
-- (2)Creating products table

Create table products
(
productID int primary key auto_increment,
productName varchar(50) not null,
Description text,
Price decimal(10,2) not null check(price>0) 
);
desc products;

alter table products auto_increment=100;


-- (3)creating orders table

create table orders
(
orderID int primary key auto_increment,
customerID int references customers(customerID),
Orderdate date,
TotalAmount decimal(10,2) 
);
alter table orders auto_increment=210; 
desc orders;

-- (4)creating orderdetails table

create table if not exists orderdetails
(
orderdetailID int primary key auto_increment,
orderID int references orders(orderID),
productID int references customers(productID),
quantity int not null check(quantity>0)
);
alter table orderdetails auto_increment=300;
desc orderdetails;


-- (5)creating table Inventory

create table if not exists inventory
(
inventoryID int primary key auto_increment,
productID int references product(productID),
Quantityinstock int not null check(quantityinstock>0),
laststockupdate date not null
);
alter table inventory auto_increment=400;
desc inventory;

-- 5. Insert at least 10 sample records

-- Inserting values in customer table
insert into customers (FirstName,LastName,Email,phone,Address)
values('Saravanan','vel','saravanan8@gmail.com',9943445603,'123,MG Road,Karur,639007,India'),
('Harish','Saran','Harish23@gmail.com',7643645703,'45,Anna Salai,Chennai,600002,India'),
('Barani','selva','barani08@gmail.com',8756789055,'12th park street,Kolkata,Westbengal'),
('Santhosh','Raj','santhoshraj@gmail.com',8989679758,'89 SV Road,Mumbai,Maharashtra,400058,India'),
('Ajeesh','Samy','Ajeeshsm@gmail.com',8923673409,'17 Sector 22B,Chandigarh, 160022,India'),
('Jithu','doss','jithuphoto@gmail.com',9879348967,'78 Thillai Nagar,Trichy,Tamil Nadu,620018,India'),
('Nithish','Mulla','mulla25@gmail.com',9361163474,'12VOC Street, Madurai, Tamil Nadu, 625001, India'),
('Surya','Kali','jaisurya@gmail.com',8078566989,'22 GandhiRoad,Salem,Tamil Nadu,636007,India'),
('Bala','mani','balalucid@gmail.com',9878347865,'56 NorthStreet,Erode,Tamil Nadu,638001,India'),
('Sudhar','Hari','sanxo@gmail.com',8767505578,'67 Bazaar Street,Thanjavur,Tamil Nadu,613001,India');
select * from customers;

-- Inserting values in table products
insert into products (productName,Description,price)
values('Samsung Galaxy M14', '5G Smartphone 6.6 display, 6000mAh battery', 13499),
('HP Pavilion x360', '2-in-1 Laptop Intel i5 12th Gen, 8GB RAM, 512GB SSD', 72999),
('Sony WH-1000XM5', 'Wireless Headphones Noise Cancelling, 30 hrs battery', 29990),
('Apple iPad 10th Gen', 'Tablet 10.9-inch, A14 Bionic chip, 64GB Wi-Fi', 39990),
('Realme Narzo 60', '5G Smartphone 64MP Camera, 5000mAh Battery', 15999),
('Logitech MX Master 3S', 'Wireless Mouse Ergonomic, Bluetooth, USB-C', 9495),
('ASUS TUF Gaming F15', 'Gaming Laptop i7 11th Gen, RTX 3050, 16GB RAM', 84990),
('Samsung 27" Curved Monitor', 'Monitor Full HD, 75Hz, AMD FreeSync', 14499),
('Amazon Echo Dot (5th Gen)', 'Smart Speaker Alexa, improved bass, compact design', 4999),
('SanDisk Extreme 1TB SSD', 'Portable SSD USB 3.2, 1050MB/s read speed', 11999);
select * from products;

-- inserting values in table orders

insert into orders (customerID,orderdate,totalamount)
values (5,'2025-05-23',15999),
(10,'2025-05-23',11999),
(1,'2025-05-25', 13499),
(3,'2025-05-26',29990),
(2,'2025-05-27',72999),
(4,'2025-05-29',  39990),
(7,'2025-05-30',84990),
(8,'2025-06-01',14499),
(6,'2025-06-02',9495),
(9,'2025-06-05',4999);
select * from orders;

-- insering values in tables orderdetails
insert into orderdetails (orderID,productID,quantity)
values (211,109,1),
(215,103,2),
(210,104,1),
(217,107,1),
(218,105,1),
(213,102,2),
(216,106,1),
(212,100,1),
(214,101,1),
(219,108,2);
select * from orderdetails;

-- inserting values in table inventory
insert into inventory (productID,quantityinstock,laststockupdate)
values(100,10,'2025-05-23'),
(101,2,'2025-05-23'),
(102,2,'2025-05-24'),
(103,5,'2025-05-22'),
(104,3,'2025-05-22'),
(105,6,'2025-05-21'),
(106,2,'2025-05-24'),
(107,1,'2025-05-26'),
(108,2,'2025-05-27'),
(109,5,'2025-05-21');
select * from inventory;

-- TASK 2  (2: Select, Where, Between, AND, LIKE:)
-- 1. Write an SQL query to retrieve the names and emails of all customers.
select concat(FirstName," ",LastName)'NAME',Email from customers;

-- 2. Write an SQL query to list all orders with their order dates and corresponding customer names. 
select 
c.FirstName,o.Orderdate
from customers as c join orders as o
where c.customerID=o.customerID;

-- 3. Write an SQL query to insert a new customer record into the "Customers" table. Include customer information such as name, email, and address.
insert into customers (FirstName,LastName,Email,phone,Address)
values('Vasanth','Sekar','Vasanthvs@gmail.com',9734908866,'12,Pachal,Namakkal,657007,India');
select * from customers;

-- 4.Write an SQL query to update the prices of all electronic gadgets in the "Products" table by increasing them by 10%. 
set sql_safe_updates=0;
update products set price=price*.10;
select * from products;

-- 5.  Write an SQL query to delete a specific order and its associated order details from the "Orders" and "OrderDetails" tables. 
delete from Orders where orderID=214;
select * from orders;
delete from Orderdetails where orderID=214;
select * from orderdetails;

-- 6. Write an SQL query to insert a new order into the "Orders" table. Include the customer ID, order date, and any other necessary information. 
insert into orders (customerID,Orderdate,Totalamount) 
values (2,'2025-06-02',11999);
select * from orders;

-- 7. Write an SQL query to update the contact information (e.g., email and address) of a specific customer in the "Customers" table.
update customers set Email='Harishsaran@gmail.com',Phone=7639166703 where customerID=2;
select * from customers;

 -- 8. Write an SQL query to recalculate and update the total cost of each order in the "Orders" table based on the prices and quantities in the "OrderDetails" table.
UPDATE Orders
SET TotalAmount = (
    SELECT SUM(Products.Price * OrderDetails.Quantity)
    FROM OrderDetails
    JOIN Products ON OrderDetails.ProductID = Products.ProductID
    WHERE OrderDetails.OrderID = Orders.OrderID
);
select * from Orders;

-- 9. Write an SQL query to delete all orders and their associated order details for a specific customer from the "Orders" and "OrderDetails" tables.
delete from orderdetails
where orderID=(select orderID from Orders where customerID=5);
select * from Orderdetails;
delete from Orders where customerID=5;
select * from Orders;

-- 10. Write an SQL query to insert a new electronic gadget product into the "Products" table, including product name, category, price, and any other relevant details.
insert into products (productName,Description,price)
values ('Vivo Y72 5G','5G smartphone,6000mAH battery,8GB RAM and 128GB ROM',21000);
select * from products;

-- 11. Write an SQL query to update the status of a specific order in the "Orders" table (e.g., from "Pending" to "Shipped").
alter table Orders add column status varchar(20) default 'pending';
update Orders set status='Shipped' where orderID=216;
update Orders set status='Shipped' where orderID=213;
select * from Orders;

-- 12. Write an SQL query to calculate and update the number of orders placed by each customer in the "Customers" table based on the data in the "Orders" table. 
alter table customers add column no_of_Orders int;
update customers set no_of_Orders=
(select count(*) from Orders where customers.customerID=Orders.customerID);
select * from Customers;







