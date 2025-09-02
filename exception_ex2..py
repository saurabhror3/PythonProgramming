# 1. Define custom exception
class InsufficientFundsError(Exception):
    def __init__(self, message="Insufficient funds for this withdrawal."):
        super().__init__(message)


# 2. Define the BankAccount class
class BankAccount:
    def __init__(self, account_number, balance=0.0):
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited ${amount:.2f}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if amount > self.balance:
            raise InsufficientFundsError(f"Attempted to withdraw ${amount:.2f}, but only ${self.balance:.2f} available.")
        elif amount <= 0:
            print("Withdrawal amount must be positive.")
        else:
            self.balance -= amount
            print(f"Withdrew ${amount:.2f}")

    def __str__(self):
        return f"Account {self.account_number} | Balance: ${self.balance:.2f}"


# 3. Main function to demonstrate usage
def main():
    # Create a new bank account
    account = BankAccount("ACC123", 100.0)
    print(account)

    # Deposit funds
    account.deposit(50)

    # Successful withdrawal
    try:
        account.withdraw(30)
    except InsufficientFundsError as e:
        print("Error:", e)

    # Attempt to overdraw
    try:
        account.withdraw(200)
    except InsufficientFundsError as e:
        print("Error:", e)

    # Final account status
    print(account)


# Run the program
main()
