class BankAccount:
    def __init__(self, account_number, balance, date_of_opening, customer_name):
        self.account_number = account_number
        self.balance = balance
        self.date_of_opening = date_of_opening
        self.customer_name = customer_name

    def deposit(self, amount):
        self.balance += amount
        return amount

    def withdraw(self, amount):
        if self.balance < amount:
            return "Insufficient balance."
        else:
            self.balance -= amount
            return amount

    def check_balance(self):
        print(f"Current balance: {self.balance}")

    def customer_details(self):
        print("Customer Details:")
        print(f"Name: {self.customer_name}")
        print(f"Account Number: {self.account_number}")
        print(f"Date of Opening: {self.date_of_opening}")
        print(f"Balance: {self.balance}")
# Create the BankAccount class
account = BankAccount("39147897", 5000, "2023-06-30", "Kingsley Ombongi")

# Deposit money
deposit_amount = account.deposit(1000)
print(f"Amount deposited: {deposit_amount}")

# Withdraw money
withdraw_amount = account.withdraw(2000)
print(f"Amount withdrawn: {withdraw_amount}")

# Check balance
account.check_balance()

# Print customer details
account.customer_details()
