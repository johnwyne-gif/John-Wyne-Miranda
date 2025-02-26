class BankAccount:
    def __init__(self, account_number, owner, balance=0):
        self.account_number = account_number
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited: ${amount}. New balance: ${self.balance}")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew: ${amount}. New balance: ${self.balance}")
        else:
            print("Insufficient funds!")

    def display_balance(self):
        print(f"Account Balance: ${self.balance}")

account = BankAccount("123456789", "John Doe", 1000)
account.display_balance()
account.deposit(500)
account.withdraw(200)
account.withdraw(1500) 
account.display_balance()
