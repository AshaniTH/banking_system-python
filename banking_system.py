# banking_system.py

class BankAccount:
    def __init__(self, account_number, account_holder, initial_balance=0):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = initial_balance
        self.transaction_history = []

class BankingSystem:
    def __init__(self):
        self.accounts = {}
        self.next_account_number = 1001  # Starting account number
    
    def create_account(self):
        print("\n--- Create New Account ---")
        name = input("Enter account holder name: ")
        initial_deposit = float(input("Enter initial deposit amount: "))
        
        if initial_deposit < 0:
            print("Initial deposit cannot be negative!")
            return
        
        account_number = self.next_account_number
        self.next_account_number += 1
        
        new_account = BankAccount(account_number, name, initial_deposit)
        self.accounts[account_number] = new_account
        
        # Record initial deposit
        new_account.transaction_history.append(f"Account created with initial deposit: ${initial_deposit:.2f}")
        
        print(f"\nAccount created successfully!")
        print(f"Account Number: {account_number}")
        print(f"Account Holder: {name}")
        print(f"Initial Balance: ${initial_deposit:.2f}")

# Main program
if __name__ == "__main__":
    bank = BankingSystem()
    bank.create_account()