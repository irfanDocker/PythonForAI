##1. Store Customer Orders

##Create a list of customer names

names = ["Shawn", "James", "Sarah","David"]


##Store each customer’s order details (name, product, price, category) as tuples inside a list

orders = [("Shawn", "Wireless Mouse", 99.9, "Electric device"),
          ("James", "Iphone 17", 1199.9, "Electric device"),
          ("Sarah", "Apple", 2.9, "Fruit"),
          ("David", "USB-C Cable", 9.9, "Electric device")]


##Use a dictionary where keys are customer names and values are lists of ordered products

Customer_Order = {}

#for order in orders:
    #Customer_Order[orders[0]].append((orders[1], orders[2],orders[3]))

# print(Customer_Order)
# print(orders)
# print(orders[0])
# print(orders[0][0])

for i in range(len(orders)):
    print(orders[i])
    # Customer_Order[orders[i][0]] = (orders[i][1],orders[i][2],orders[i][3])
    Customer_Order.setdefault(orders[i][0], []).append((orders[i][1], orders[i][2], orders[i][3]))

print(Customer_Order)

##2. Classify Products by Category
##Use a dictionary to map each product to its category
product_category_map = {}
for i in range(len(orders)):
    print(orders[i])
    product_category_map[orders[i][1]] = orders[i][3]

print(product_category_map)
##Create a set of unique product categories

unique_product_categories = set()

for order in orders:
    print(order)
    unique_product_categories.add(order[3])

##Display all available categories
print(unique_product_categories)

##3. Analyze Customer Orders

customerSummary = {}
print(customerSummary)

##Use loops to calculate each customer’s total spending
for customer, orders in Customer_Order.items():
    print(customer)
    print(orders)
    total_spent = 0

    for product, price, category in orders:
        total_spent += price

    ##Classification criteria:
    ##Above $100: High-value buyer
    ##$50–$100: Moderate buyer
    ##Below $50: Low-value buyer
    if total_spent > 100:
        classification = "High-value buyer"
    elif total_spent >=50 and total_spent <= 100:
        classification = "Moderate buyer"
    else:
        classification = "Low value buyer"

    customerSummary[customer] = {"total" : total_spent, "class" : classification}

    # Display result
    for customer, data in customerSummary.items():
        print(customer, " total money spent $", data["total"], " ", data["class"])




##4. Generate Business Insights
##Calculate total revenue per product category using a dictionary##
##Extract unique products using sets
##Use list comprehension to find customers who purchased electronics
##Identify top 3 highest-spending customers


# Total revenue per category
# Total revenue per category
category_revenue = {}

for customer, order_list in Customer_Order.items():
    for product, price, category in order_list:
        category_revenue[category] = category_revenue.get(category, 0) + price

print("Total Revenue per Category:")
for category, revenue in category_revenue.items():
    print(f"{category}: ${revenue:.2f}")


##Extract unique products using sets


orders = [("Shawn", "Wireless Mouse", 99.9, "Electric device"),
          ("James", "Iphone 17", 1199.9, "Electric device"),
          ("Sarah", "Apple", 2.9, "Fruit"),
          ("David", "USB-C Cable", 9.9, "Electric device")]

unique_products = set()
for name, product, price, category in orders:
    unique_products.add(product)

print(unique_products)

##5. Organize and Display Data
##Print a summary of each customer’s total spending and classification
print("Customer Spending Summary:")
for customer, data in customerSummary.items():
    print(f"{customer}: ${data['total']:.2f} → {data['class']}")
##Use set operations to find customers purchasing from multiple categories

categories_by_customer = {}
for customer, order_list in Customer_Order.items():
    # create a set of categories this customer bought from
    categories = {category for _, _, category in order_list}
    categories_by_customer[customer] = categories

# find those with more than one category
multi_category_customers = [cust for cust, cats in categories_by_customer.items() if len(cats) > 1]
print("Customers buying from multiple categories:", multi_category_customers)

##Identify customers who bought both Electronics and Clothing1

target_categories = {"Electric device", "Clothing"}

both_electronics_and_clothing = [
    cust for cust, cats in categories_by_customer.items()
    if target_categories.issubset(cats)
]