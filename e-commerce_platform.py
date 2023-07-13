def add_product(product_name, price, quantity):
    product = {
        "product_name": product_name,
        "price": price,
        "quantity": quantity
    }
    return product

def update_price(product, new_price):
    product["price"] = new_price
    return product

def update_quantity(product, quantity_change):
    product["quantity"] += quantity_change
    return product
# Add a product
product1 = add_product("Shirt", 60, 50)
print(product1)  # {'product_name': 'Shirt', 'price': 60, 'quantity': 50}

# Update the price of a product
product1 = update_price(product1, 70)
print(product1)  # {'product_name': 'Shirt', 'price': 70, 'quantity': 50}

# Update the quantity of a product
product1 = update_quantity(product1, -20)
print(product1)  # {'product_name': 'Shirt', 'price': 70, 'quantity': 40}
