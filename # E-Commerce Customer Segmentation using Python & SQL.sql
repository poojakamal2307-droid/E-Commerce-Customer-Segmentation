CREATE DATABASE E_Commerce;
USE E_Commerce;

CREATE TABLE orders (
    InvoiceNo VARCHAR(20),
    CustomerID INT,
    InvoiceDate DATE,
    Quantity INT,
    UnitPrice FLOAT
);
INSERT INTO orders VALUES
('INV001',101,'2024-01-05',2,500),
('INV002',102,'2024-01-06',1,700),
('INV003',101,'2024-01-10',3,200),
('INV004',103,'2024-01-12',5,150),
('INV005',104,'2024-01-15',1,1200),
('INV006',102,'2024-01-18',4,300),
('INV007',105,'2024-01-20',2,800),
('INV008',101,'2024-01-22',1,400),
('INV009',103,'2024-01-25',6,100),
('INV010',104,'2024-01-28',2,900);
-- Total Revenue
SELECT SUM(Quantity*UnitPrice) AS Total_Revenue
FROM orders;
-- Top Customers
SELECT CustomerID,
SUM(Quantity*UnitPrice) AS Spending
FROM orders
GROUP BY CustomerID
ORDER BY Spending DESC;
-- Purchase Frequency
SELECT CustomerID,
COUNT(InvoiceNo) AS Orders
FROM orders
GROUP BY CustomerID;