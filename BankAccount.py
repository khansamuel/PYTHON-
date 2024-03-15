import datetime
class BankAccount:
    def __init__(self, customer_name, account_number, balance=0, date_of_opening=None): 
        
        self.customer_name = customer_name
        self.account_number = account_number
        self.balance = balance
        self.date_of_opening = date_of_opening if date_of_opening else datetime.date.today()

    def deposit(self, amount):
        self.balance += amount
        return f"Deposited: ${amount:.2f}. New balance: ${self.balance:.2f}"

    def withdraw(self, amount):
        if amount > self.balance:
            return "Insufficient funds."
        self.balance -= amount
        return f"Withdrawn: ${amount:.2f}. New balance: ${self.balance:.2f}"

    def check_balance(self):
        print(f"Current balance: ${self.balance:.2f}")

    def customer_details(self):
        print(f"""
Customer Name: {self.customer_name}
Account Number: {self.account_number}
Date of Opening: {self.date_of_opening}
Current Balance: ${self.balance:.2f}
""")

# Example usage
account1 = BankAccount("John Doe", 123456, 1000, "2023-10-26")

print(account1.deposit(500))
print(account1.withdraw(200))
account1.check_balance()
account1.customer_details()

  

    