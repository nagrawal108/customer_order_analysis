### Course-End Project
#### Analyzing Customer Orders Using Python
#### By Nikhil Agrawal

# --- Constants ---
HIGH_VALUE_THRESHOLD = 100
MODERATE_VALUE_THRESHOLD = 50

# --- Data Structures ---
from typing import List, Tuple, Dict, Set

customers: List[str] = ["Nikhil", "Krishna", "Radha", "Gaura", "Nitai"]

order_details: List[Tuple[str, str, int, str]] = [
    ("Nikhil", "Pen", 20, "Office Supply"),
    ("Nikhil", "Erasers", 20, "Office Supply"),
    ("Krishna", "Camera", 25, "Electronics"),
    ("Krishna", "SD Card", 15, "Electronics"),
    ("Radha", "Milk", 3, "Groceries"),
    ("Gaura", "Filtered Water", 10, "Groceries"),
    ("Nitai", "Bhagavad Gita", 20, "Books"),
    ("Nikhil", "T-shirt", 40, "Clothing"),
    ("Krishna", "Jeans", 60, "Clothing"),
    ("Radha", "Headphones", 80, "Electronics"),
    ("Gaura", "Notebook", 5, "Office Supply"),
    ("Nitai", "Lamp", 30, "Home Essentials"),
]


# Build customer to products dictionary - Task 2.1
cust_products: Dict[str, List[str]] = {}
for name, product, price, category in order_details:
    cust_products.setdefault(name, []).append(product)

# Build product to category mapping - Task 2.2
product_to_category: Dict[str, str] = {}
for _, product, _, category in order_details:
    product_to_category[product] = category

# Build category to products mapping
category_to_products: Dict[str, Set[str]] = {}
for _, product, _, category in order_details:
    category_to_products.setdefault(category, set()).add(product)

# Set of unique product categories
categories: Set[str] = set(product_to_category.values())


# --- Analysis Functions ---
def calculate_customer_spending(order_details: List[Tuple[str, str, int, str]]) -> Dict[str, int]:
    """Calculate total spending for each customer."""
    spending: Dict[str, int] = {}
    for name, _, price, _ in order_details:
        spending[name] = spending.get(name, 0) + price
    return spending

def classify_customer(amount: int) -> str:
    """Classify customer based on total spending."""
    if amount > HIGH_VALUE_THRESHOLD:
        return "High-value"
    elif MODERATE_VALUE_THRESHOLD <= amount <= HIGH_VALUE_THRESHOLD:
        return "Moderate"
    else:
        return "Low-value"

def revenue_per_category(order_details: List[Tuple[str, str, int, str]]) -> Dict[str, int]:
    """Calculate total revenue per product category."""
    revenue: Dict[str, int] = {}
    for _, _, price, category in order_details:
        revenue[category] = revenue.get(category, 0) + price
    return revenue

def unique_products(order_details: List[Tuple[str, str, int, str]]) -> Set[str]:
    """Return a set of unique products sold."""
    return set(prod for _, prod, _, _ in order_details)

def customers_by_category(order_details: List[Tuple[str, str, int, str]], target_category: str) -> List[str]:
    """Return a sorted list of customers who purchased from a given category."""
    return sorted(set(name for name, _, _, category in order_details if category == target_category))

def top_n_customers(spending: Dict[str, int], n: int = 3) -> List[Tuple[str, int]]:
    """Return the top n customers by spending."""
    return sorted(spending.items(), key=lambda x: x[1], reverse=True)[:n]

def customers_multiple_categories(order_details: List[Tuple[str, str, int, str]]) -> List[str]:
    """Return customers who purchased from multiple categories."""
    cust_cats: Dict[str, Set[str]] = {}
    for name, _, _, category in order_details:
        cust_cats.setdefault(name, set()).add(category)
    return sorted([name for name, cats in cust_cats.items() if len(cats) > 1])

def customers_both_categories(order_details: List[Tuple[str, str, int, str]], cat1: str, cat2: str) -> List[str]:
    """Return customers who bought from both specified categories."""
    cat1_customers = set(name for name, _, _, category in order_details if category == cat1)
    cat2_customers = set(name for name, _, _, category in order_details if category == cat2)
    return sorted(list(cat1_customers & cat2_customers))

# --- Main Analysis ---

import sys
from io import StringIO

def print_report():
    report = StringIO()
    print("\n--- Customer Order Analysis Report ---\n", file=report)

    print("List of customers:", ', '.join(customers), file=report)
    print("\nOrder details:", file=report)
    print(f"{'Customer':<10} | {'Product':<15} | {'Price':>6} | {'Category':<16}", file=report)
    print("-"*55, file=report)
    for name, product, price, category in order_details:
        print(f"{name:<10} | {product:<15} | ${price:>5} | {category:<16}", file=report)

    print("\nProducts each customer has ordered:", file=report)
    for cust, prods in cust_products.items():
        print(f"{cust:<10}: {', '.join(prods)}", file=report)

    print("\nAvailable product categories:", file=report)
    for cat in sorted(categories):
        print(f"- {cat}", file=report)

    # Customer spending and classification
    spending = calculate_customer_spending(order_details)
    print("\nCustomer spending and classification:", file=report)
    print(f"{'Customer':<10} | {'Total Spent':>11} | {'Classification':<12}", file=report)
    print("-"*40, file=report)
    for cust in customers:
        amt = spending.get(cust, 0)
        classification = classify_customer(amt)
        print(f"{cust:<10} | ${amt:>10} | {classification:<12}", file=report)

    # Revenue per category
    revenue = revenue_per_category(order_details)
    print("\nTotal revenue per product category:", file=report)
    print(f"{'Category':<16} | {'Revenue':>8}", file=report)
    print("-"*28, file=report)
    for cat, amt in revenue.items():
        print(f"{cat:<16} | ${amt:>7}", file=report)

    # Unique products
    print("\nUnique products sold:", ', '.join(sorted(unique_products(order_details))), file=report)

    # Customers who purchased Electronics
    electronics_customers = customers_by_category(order_details, "Electronics")
    print("\nCustomers who purchased Electronics:", ', '.join(electronics_customers), file=report)

    # Top 3 highest-spending customers
    print("\nTop 3 highest-spending customers:", file=report)
    for name, amt in top_n_customers(spending, 3):
        print(f"{name}: ${amt}", file=report)

    # Customers who purchased from multiple categories
    multi_cat_customers = customers_multiple_categories(order_details)
    print("\nCustomers who purchased from multiple categories:", ', '.join(multi_cat_customers), file=report)

    # Customers who bought both Electronics and Clothing
    both_elec_cloth = customers_both_categories(order_details, "Electronics", "Clothing")
    print("\nCustomers who bought both Electronics and Clothing:", ', '.join(both_elec_cloth), file=report)

    print("\n--- End of Report ---\n", file=report)
    return report.getvalue()

# Print to console and write to file
report_content = print_report()
print(report_content)
with open("report.txt", "w", encoding="utf-8") as f:
    f.write(report_content)
