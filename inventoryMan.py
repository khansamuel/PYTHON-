from datetime import datetime

class Product:
    def __init__(self, product_id, product_name, quantity_in_stock):
        self.product_id = product_id
        self.product_name = product_name
        self.quantity_in_stock = quantity_in_stock

class SimpleProduct(Product):
    def __init__(self, product_id, product_name, quantity_in_stock, unit_price):
        super().__init__(product_id, product_name, quantity_in_stock)
        self.unit_price = unit_price
    
    def calculate_value(self):
        return self.quantity_in_stock * self.unit_price

class PerishableProduct(SimpleProduct):
    def __init__(self, product_id, product_name, quantity_in_stock, unit_price, expiry_date):
        super().__init__(product_id, product_name, quantity_in_stock, unit_price)
        self.expiry_date = expiry_date
    
    def calculate_value(self):
        return self.quantity_in_stock * self.unit_price

class DigitalProduct(SimpleProduct):
    def __init__(self, product_id, product_name, quantity_in_stock, unit_price, price):
        super().__init__(product_id, product_name, quantity_in_stock, unit_price)
        self.price = price
    
    def calculate_value(self):
        return self.quantity_in_stock * self.unit_price

# User input
name = input("Enter product name: ")
product_id = input("Enter product ID: ")
quantity_in_stock = int(input("Enter quantity in stock: "))
unit_price = float(input("Enter the unit price: "))

# Creating objects
simple_product = SimpleProduct(product_id, name, quantity_in_stock, unit_price)

# Printing the calculated value
print("Total value of the simple product:", simple_product.calculate_value())
