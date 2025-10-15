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
        self.next_account_number = 1001
    
    def create_account(self):
        print("\n--- Create New Account ---")
        name = input("Enter account holder name: ")
        
        try:
            initial_deposit = float(input("Enter initial deposit amount: $"))
        except ValueError:
            print("Invalid amount! Please enter a valid number.")
            return
        
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
    
    def deposit(self):
        print("\n--- Deposit Money ---")
        try:
            account_number = int(input("Enter account number: "))
        except ValueError:
            print("Invalid account number!")
            return
        
        if account_number not in self.accounts:
            print("Account not found!")
            return
        
        try:
            amount = float(input("Enter deposit amount: $"))
        except ValueError:
            print("Invalid amount!")
            return
        
        if amount <= 0:
            print("Deposit amount must be positive!")
            return
        
        account = self.accounts[account_number]
        account.balance += amount
        account.transaction_history.append(f"Deposited: ${amount:.2f}")
        
        print(f"\nDeposit successful!")
        print(f"New balance: ${account.balance:.2f}")
    
    def withdraw(self):
        print("\n--- Withdraw Money ---")
        try:
            account_number = int(input("Enter account number: "))
        except ValueError:
            print("Invalid account number!")
            return
        
        if account_number not in self.accounts:
            print("Account not found!")
            return
        
        try:
            amount = float(input("Enter withdrawal amount: $"))
        except ValueError:
            print("Invalid amount!")
            return
        
        if amount <= 0:
            print("Withdrawal amount must be positive!")
            return
        
        account = self.accounts[account_number]
        
        if amount > account.balance:
            print("Insufficient funds!")
            return
        
        account.balance -= amount
        account.transaction_history.append(f"Withdrew: ${amount:.2f}")
        
        print(f"\nWithdrawal successful!")
        print(f"New balance: ${account.balance:.2f}")
    
    def check_balance(self):
        print("\n--- Check Balance ---")
        try:
            account_number = int(input("Enter account number: "))
        except ValueError:
            print("Invalid account number!")
            return
        
        if account_number not in self.accounts:
            print("Account not found!")
            return
        
        account = self.accounts[account_number]
        print(f"\nAccount Holder: {account.account_holder}")
        print(f"Account Number: {account.account_number}")
        print(f"Current Balance: ${account.balance:.2f}")