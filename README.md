# Customer Order Analysis

## Overview
This project analyzes customer orders for an e-commerce company using Python's built-in data structures. It classifies products, identifies customer purchasing patterns, and generates business insights to help managers make data-driven decisions.

## How to Run
1. Ensure you have Python 3.12+ and the required environment set up (a virtual environment is recommended).
2. Run the script:
   ```sh
   python customer_order_analysis.py
   ```
3. The analysis report will be printed to the console and saved as `report.txt` in the same directory.

## Data Structures Used
- **List:** To store customer names and order details.
- **Tuple:** Each order is a tuple of (customer name, product, price, category).
- **Dictionary:**
  - Maps customers to their products.
  - Maps products to categories.
  - Maps categories to products.
- **Set:** To store unique product categories and unique products.

## Assignment Tasks & Implementation

### 1. Store Customer Orders
- **List of customer names:**
  - `customers = [ ... ]`
- **Order details as tuples in a list:**
  - `order_details = [ (customer, product, price, category), ... ]`
- **Dictionary mapping customers to products:**
  - `cust_products = { customer: [products] }`

### 2. Classify Products by Category
- **Dictionary mapping products to categories:**
  - `product_to_category = { product: category }`
- **Set of unique product categories:**
  - `categories = set(product_to_category.values())`
- **Display all available categories:**
  - Printed in the report.

### 3. Analyze Customer Orders
- **Calculate total spending per customer:**
  - `calculate_customer_spending(order_details)`
- **Classify customers:**
  - High-value: > $100
  - Moderate: $50–$100
  - Low-value: < $50
- **Classification logic:**
  - `classify_customer(amount)`

### 4. Generate Business Insights
- **Total revenue per product category:**
  - `revenue_per_category(order_details)`
- **Unique products:**
  - `unique_products(order_details)`
- **Customers who purchased electronics:**
  - `customers_by_category(order_details, "Electronics")`
- **Top 3 highest-spending customers:**
  - `top_n_customers(spending, 3)`

### 5. Organize and Display Data
- **Summary of each customer’s spending and classification:**
  - Printed in a formatted table.
- **Customers who purchased from multiple categories:**
  - `customers_multiple_categories(order_details)`
- **Customers who bought both electronics and clothing:**
  - `customers_both_categories(order_details, "Electronics", "Clothing")`
- **All results are printed in a clear, tabular report and saved to `report.txt`.**

## File Outputs
- **report.txt:** Contains the full analysis report for easy submission or sharing.

## Customization
- To add more orders or categories, simply update the `order_details` list.
- The code is modular, with functions for each analysis step for easy extension.

## Contact
For questions or improvements, please reach out to the project maintainer.
