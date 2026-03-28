#Create a list of customers
customers = [
	"Alice",
	"Bob",
	"Charlie",
	"Diana",
	"Ethan",
	"Fiona",
	"George",
	"Hannah",
	"Ian",
	"Julia",
	"Kevin",
	"Laura",
	"Michael",
	"Nina",
	"Oscar",
	"Paula"
]

#Print the list of customers
print("List of customers:")
for customer in customers:
    print(customer)
    

#Store each customer's order details (customer name, product, price, category) as tuples inside a list
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
    ("Laura", "Book", 25, "Books"),
    ("Michael", "Laptop", 1300, "Electronics"),
    ("Nina", "Smartphone", 900, "Electronics"),
    ("Oscar", "Watch", 250, "Accessories"),
    ("Paula", "Dress", 90, "Fashion")
]

#print my orders    
print("\nCustomer Orders:")
for order in orders:
    print(order)   

     