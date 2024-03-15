def add_product(product_name, price, quantity):
    """
    Create a dictionary object for a product with the given parameters.
    """
    product = {
        "product_name": product_name,
        "price": price,
        "quantity": quantity
    }
    return product

def update_price(product, new_price):
    """
    Update the price of the product in the dictionary.
    """
    product["price"] = new_price
    return product

def update_quantity(product, quantity_change):
    """
    Update the quantity of the product in the dictionary.
    """
    product["quantity"] += quantity_change
    return product

# Add a new product
product1 = add_product("Laptop", 999.99, 10)
print("Product 1:", product1)

# Update the price of the product
product1 = update_price(product1, 899.99)
print("Updated Product 1 (price):", product1)

# Update the quantity of the product
product1 = update_quantity(product1, -3)
print("Updated Product 1 (quantity):", product1)
