Python 3.12.9 (tags/v3.12.9:fdb8142, Feb  4 2025, 15:27:58) [MSC v.1942 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.

= RESTART: C:/Users/pooja/AppData/Local/Programs/Python/Python312/E-Commerce Customer Segmentation.py

Dataset
   InvoiceNo  CustomerID InvoiceDate  Quantity  UnitPrice
0    INV001         101  2024-01-05         2      500.0
1    INV002         102  2024-01-06         1      700.0
2    INV003         101  2024-01-10         3      200.0
3    INV004         103  2024-01-12         5      150.0
4    INV005         104  2024-01-15         1     1200.0
5    INV006         102  2024-01-18         4      300.0
6    INV007         105  2024-01-20         2      800.0
7    INV008         101  2024-01-22         1      400.0
8    INV009         103  2024-01-25         6      100.0
9    INV010         104  2024-01-28         2      900.0

RFM Table
             Recency  Frequency  Monetary
CustomerID                              
101               6          3    2000.0
102              10          2    1900.0
103               3          2    1350.0
104               0          2    3000.0
105               8          1    1600.0

Final Segmentation
             Recency  Frequency  Monetary  ... M_score RFM_Score            Segment
CustomerID                                ...                                     
101               6          3    2000.0  ...       3       343    Loyal Customers
102              10          2    1900.0  ...       2       112  At Risk Customers
103               3          2    1350.0  ...       1       421   Recent Customers
104               0          2    3000.0  ...       4       434   Recent Customers
105               8          1    1600.0  ...       1       211  At Risk Customers

[5 rows x 8 columns]
