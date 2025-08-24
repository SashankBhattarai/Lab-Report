class BankAccount:
    def __init__(self, account_holder, account_number, balance=0):
        self.account_holder = account_holder
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited: {amount}")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew: {amount}")
        else:
            print("Insufficient balance")

    def show_balance(self):
        print(f"Current balance: {self.balance}")

acc1 = BankAccount("BOBBY", "1234", 25000)
acc1.show_balance()
acc1.deposit(10000)
acc1.withdraw(7000)
acc1.show_balance()
