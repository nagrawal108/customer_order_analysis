

from io import StringIO

# Task 1: Data Preparation
customers = [
    "Alice", "Bob", "Charlie", "Diana", "Ethan", "Fiona", "George", "Hannah",
    "Ian", "Julia", "Kevin", "Laura", "Michael", "Nina", "Oscar", "Paula"
]

orders = [
    ("Alice", "Laptop", 1200, "Electronics"),
    ("Bob", "Smartphone", 800, "Electronics"),
    ("Charlie", "Book", 20, "Books"),
    ("Diana", "Headphones", 150, "Electronics"),
    ("Ethan", "Shoes", 100, "Fashion"),
    ("Fiona", "Dress", 80, "Fashion"),
    ("George", "Watch", 200, "Accessories"),
    ("Hannah", "Bag", 150, "Fashion"),
    ("Ian", "Tablet", 300, "Electronics"),
    ("Julia", "Camera", 500, "Electronics"),
    ("Kevin", "Shoes", 120, "Fashion"),
    ("Michael", "Laptop", 1300, "Electronics"),
    ("Nina", "Smartphone", 900, "Electronics"),
    ("Oscar", "Watch", 250, "Accessories"),
    ("Paula", "Dress", 90, "Fashion")
]

def print_report():
    # Customer Orders
    customer_orders = {}
    for order in orders:
        customer, product, price, category = order
        if customer not in customer_orders:
            customer_orders[customer] = []
        customer_orders[customer].append((product, price, category))

    # Product Categories
    product_categories = {product: category for _, product, _, category in orders}
    unique_categories = set(product_categories.values())

    # Customer Spending
    customer_spending = {}
    for order in orders:
        customer, _, price, _ = order
        if customer not in customer_spending:
            customer_spending[customer] = 0
        customer_spending[customer] += price

    # Value Classifications
    high_value_customers = [customer for customer, spending in customer_spending.items() if spending > 1000]
    moderate_value_customers = [customer for customer, spending in customer_spending.items() if 500 <= spending <= 1000]
    low_value_customers = [customer for customer, spending in customer_spending.items() if spending < 500]

    # Category Revenue
    category_revenue = {}
    for order in orders:
        _, _, price, category = order
        if category not in category_revenue:
            category_revenue[category] = 0
        category_revenue[category] += price

    # Unique Products
    unique_products = set(order[1] for order in orders)

    # Electronics Customers
    electronics_customers = [
        customer
        for customer, cust_orders in customer_orders.items()
        if any(product_categories.get(product) == "Electronics" for product, _, _ in cust_orders)
    ]

    # Top Customers
    top_customers = sorted(customer_spending.items(), key=lambda x: x[1], reverse=True)[:3]

    # Customers by Category
    customer_categories = {}
    for customer, cust_orders in customer_orders.items():
        categories = set(
            product_categories.get(product)
            for product, _, _ in cust_orders
            if product in product_categories
        )
        customer_categories[customer] = categories
    multi_category_customers = [customer for customer, categories in customer_categories.items() if len(categories) > 1]

    # Customers who purchased both Electronics and Fashion
    electronics_and_clothing_customers = [
        customer for customer, categories in customer_categories.items()
        if "Electronics" in categories and "Fashion" in categories
    ]

    # Report Output
    report = StringIO()
    report.write("\n--- Customer Order Analysis Report ---\n\n")
    report.write("List of customers:\n")
    for customer in customers:
        report.write(f"{customer}\n")
    report.write("\nCustomer Orders:\n")
    for order in orders:
        report.write(f"{order}\n")
    report.write("\nCustomer Orders Dictionary:\n")
    for customer, cust_orders in customer_orders.items():
        report.write(f"{customer}: {cust_orders}\n")
    report.write("\nProduct Categories Dictionary:\n")
    for product, category in product_categories.items():
        report.write(f"{product}: {category}\n")
    report.write("\nUnique Product Categories:\n")
    for category in unique_categories:
        report.write(f"{category}\n")
    report.write("\nAvailable Product Categories:\n")
    for category in unique_categories:
        report.write(f"{category}\n")
    report.write("\nCustomer Spending:\n")
    for customer, spending in customer_spending.items():
        report.write(f"{customer}: ${spending}\n")
    report.write("\nHigh-Value Customers:\n")
    for customer in high_value_customers:
        report.write(f"{customer}\n")
    report.write("\nModerate-Value Customers:\n")
    for customer in moderate_value_customers:
        report.write(f"{customer}\n")
    report.write("\nLow-Value Customers:\n")
    for customer in low_value_customers:
        report.write(f"{customer}\n")
    report.write("\nTotal Revenue per Product Category:\n")
    for category, revenue in category_revenue.items():
        report.write(f"{category}: ${revenue}\n")
    report.write("\nUnique Products Sold:\n")
    for product in unique_products:
        report.write(f"{product}\n")
    report.write("\nCustomers Who Purchased Electronics:\n")
    for customer in electronics_customers:
        report.write(f"{customer}\n")
    report.write("\nTop Three Highest-Spending Customers:\n")
    for customer, spending in top_customers:
        report.write(f"{customer}: ${spending}\n")
    report.write("\nCustomers Who Purchased from Multiple Categories:\n")
    for customer in multi_category_customers:
        report.write(f"{customer}\n")
    report.write("\nCustomers Who Purchased Both Electronics and Clothing:\n")
    for customer in electronics_and_clothing_customers:
        report.write(f"{customer}\n")
    print(report.getvalue())

print_report()



    