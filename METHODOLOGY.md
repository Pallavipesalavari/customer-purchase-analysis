# Project Methodology

## 1. Data input
The application starts with a small built-in sample dataset. A user can instead upload
a CSV file containing `Customer_ID`, `Customer_Name`, `Product`, `Quantity`, and `Price`.

## 2. Data validation and preparation
- Check that all required columns are present.
- Convert customer identifiers, names, and product names to text.
- Convert quantity and price to numeric values.
- Remove rows with invalid numeric quantity or price.
- Exclude rows where quantity or price is negative.
- Calculate transaction amount as quantity multiplied by price.

## 3. Customer analysis
Group transactions by customer ID and customer name, sum transaction amounts,
and sort customers by total spending in descending order.

## 4. Product analysis
Group transactions by product, sum purchased quantities, and sort products
by total quantity in descending order.

## 5. Dashboard presentation
Show the transaction dataset, summary metrics, customer spending table and chart,
product quantity table and chart, and key findings.

## Implementation note
The current Streamlit dashboard performs these operations with Python and pandas.
The separate `.pig` file demonstrates equivalent analysis logic in Apache Pig Latin;
the dashboard does not execute Pig or Hadoop.
