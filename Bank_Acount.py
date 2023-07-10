class BankAccount:
    def __init__(self, account_number, balance, date_of_opening, customer_name):
        self.account_number = account_number
        self.balance = balance
        self.date_of_opening = date_of_opening
        self.customer_name = customer_name

    def deposit(self, amount):
        self.balance =self.balance + amount
        return amount

    def withdraw(self, amount):
        if amount > self.balance:
            return "Insufficient balance"
        self.balance = self.balance - amount
        return amount

    def check_balance(self):
        print("Current balance:", self.balance)

    def customer_details(self):
        print("Customer Name:", self.customer_name)
        print("Account Number:", self.account_number)
        print("Date of Opening:", self.date_of_opening)
        print("Balance:", self.balance)

my_account = BankAccount("987654321", 1000, "2023-07-10", "Kingsley Ombongi")

# Deposit
deposited_amount = my_account.deposit(500)
print("Deposited amount:", deposited_amount)

# Withdraw 
withdrawn_amount = my_account.withdraw(200)
print("Withdrawn amount:", withdrawn_amount)

# Check the current balance
my_account.check_balance()

# Print customer details
my_account.customer_details()
