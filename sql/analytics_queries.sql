-- Total Revenue
SELECT SUM(revenue) AS total_revenue
FROM sales_data;

-- Average Order Value
SELECT AVG(revenue) AS avg_order_value
FROM sales_data;

-- Top 10 Highest Orders
SELECT *
FROM sales_data
ORDER BY revenue DESC
LIMIT 10;

-- Total Quantity Sold
SELECT SUM(quantityordered) AS total_items_sold
FROM sales_data;

-- Revenue Distribution
SELECT ordernumber, revenue
FROM sales_data
ORDER BY revenue DESC;