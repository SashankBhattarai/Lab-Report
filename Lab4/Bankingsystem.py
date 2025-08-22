# Initialize customer file
def initialize():
    try:
        with open("customers.txt", "r") as f:
            if f.readline().strip() == "":
                raise Exception("Empty file")
    except:
        with open("customers.txt", "w") as f:
            f.write("Sashank,1234,7000\n")
            f.write("Rahul,5678,8000\n")
            f.write("Samrat,9101,1000\n")

# Load customers into dictionary
def load_customers():
    customers = {}
    try:
        with open("customers.txt", "r") as f:
            for line in f:
                parts = line.strip().split(",")
                if len(parts) == 3:
                    name, acc, bal = parts
                    try:
                        customers[acc.strip()] = [name.strip(), float(bal)]
                    except ValueError:
                        continue
    except:
        print("Error loading customers.")
    return customers

# Save customers back to file
def save_customers(customers):
    try:
        with open("customers.txt", "w") as f:
            for acc, (name, bal) in customers.items():
                f.write(f"{name},{acc},{bal}\n")
    except:
        print("Error saving customers.")

# Log transaction (no timestamp)
def log_transaction(acc, type_, amount):
    try:
        with open("transactions.txt", "a") as f:
            f.write(f"{acc},{type_},{amount}\n")
    except:
        print("Error logging transaction.")

# Show transaction history for an account
def show_history(acc):
    found = False
    try:
        with open("transactions.txt", "r") as f:
            print(f"\nTransaction history for account {acc}:")
            for line in f:
                parts = line.strip().split(",")
                if len(parts) == 3 and parts[0] == acc:
                    print(f"{parts[1]} of amount {parts[2]}")
                    found = True
        if not found:
            print("No transactions found.")
    except:
        print("Error reading transaction history.")

# Deposit function
def deposit(customers, acc, amount):
    if acc in customers:
        customers[acc][1] += amount
        log_transaction(acc, "Deposit", amount)
        print(f"Deposit successful. New balance: {customers[acc][1]}")
    else:
        print("Account not found.")

# Withdraw function
def withdraw(customers, acc, amount):
    if acc in customers:
        if customers[acc][1] >= amount:
            customers[acc][1] -= amount
            log_transaction(acc, "Withdraw", amount)
            print(f"Withdrawal successful. New balance: {customers[acc][1]}")
        else:
            print("Insufficient balance.")
    else:
        print("Account not found.")

# Main program
initialize()
customers = load_customers()

while True:
    print("\nMenu:")
    print("1. Deposit")
    print("2. Withdraw")
    print("3. View Transaction History")
    print("4. Exit")
    choice = input("Enter choice: ").strip()

    if choice in ["1", "2"]:
        acc = input("Enter account number: ").strip()
        if acc not in customers:
            print("Account not found.")
            continue
        try:
            amount = float(input("Enter amount: ").strip())
            if amount <= 0:
                print("Amount must be greater than 0.")
                continue
        except ValueError:
            print("Invalid amount.")
            continue

        if choice == "1":
            deposit(customers, acc, amount)
        else:
            withdraw(customers, acc, amount)

    elif choice == "3":
        acc = input("Enter account number: ").strip()
        if acc not in customers:
            print("Account not found.")
        else:
            show_history(acc)

    elif choice == "4":
        save_customers(customers)
        print("Goodbye.")
        break
    else:
        print("Invalid choice.")