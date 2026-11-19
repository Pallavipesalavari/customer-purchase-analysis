-- Customer Purchase Pattern Analysis
-- Run this script in a compatible Apache Pig / Hadoop environment.
-- Input CSV columns: Customer_ID, Customer_Name, Product, Quantity, Price

purchases = LOAD 'customer_purchases.csv'
USING PigStorage(',')
AS (
    Customer_ID:chararray,
    Customer_Name:chararray,
    Product:chararray,
    Quantity:int,
    Price:double
);

-- Remove the CSV header row.
clean_data = FILTER purchases BY Customer_ID != 'Customer_ID';

-- Calculate the total amount for each transaction.
purchase_amount = FOREACH clean_data GENERATE
    Customer_ID,
    Customer_Name,
    Product,
    Quantity,
    Price,
    (Quantity * Price) AS Total_Amount;

-- Calculate total spending by each customer.
grouped_customers = GROUP purchase_amount BY (Customer_ID, Customer_Name);

customer_totals = FOREACH grouped_customers GENERATE
    group AS Customer,
    SUM(purchase_amount.Total_Amount) AS Total_Spending;

sorted_customers = ORDER customer_totals BY Total_Spending DESC;

-- Calculate total quantity purchased for each product.
grouped_products = GROUP clean_data BY Product;

product_totals = FOREACH grouped_products GENERATE
    group AS Product_Name,
    SUM(clean_data.Quantity) AS Total_Quantity;

sorted_products = ORDER product_totals BY Total_Quantity DESC;

DUMP sorted_customers;
DUMP sorted_products;
