#maya
balance = 0.0
def deposit(amount):
    global balance
    if amount > 0:
        balance += amount
        print(f"Deposited: ${amount:.2f}")
    else:
        print("Deposit amount must be positive.")

def withdraw(amount):
    global balance
    if amount > 0:
        if balance >= amount:
            balance -= amount
            print(f"Withdrew: ${amount:.2f}")
        else:
            print("Insufficient funds.")
    else:
        print("Withdrawal amount must be positive.")

def total():
    print(f"Current balance: ${balance:.2f}")

total()  # Initial balance

deposit(100.00)
total()

withdraw(50.00)
total()

deposit(250.75)
total()
