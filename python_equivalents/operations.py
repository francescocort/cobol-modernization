#!/usr/bin/env python3
"""
Python equivalent of Operations.cob
Account Management System - Business Logic Layer
"""

class Operations:
    """Business logic for account operations"""
    
    def __init__(self):
        self.data_service = DataProgram()
        self.final_balance = 1000.00  # Default starting balance
    
    def view_balance(self):
        """View current account balance"""
        self.final_balance = self.data_service.read_balance()
        print(f"Current balance: {self.final_balance:.2f}")
    
    def credit_account(self):
        """Credit amount to account"""
        try:
            amount = float(input("Enter credit amount: ").strip())
            self.final_balance = self.data_service.read_balance()
            self.final_balance += amount
            self.data_service.write_balance(self.final_balance)
            print(f"Amount credited. New balance: {self.final_balance:.2f}")
        except ValueError:
            print("Invalid amount entered.")
    
    def debit_account(self):
        """Debit amount from account"""
        try:
            amount = float(input("Enter debit amount: ").strip())
            self.final_balance = self.data_service.read_balance()
            
            if self.final_balance >= amount:
                self.final_balance -= amount
                self.data_service.write_balance(self.final_balance)
                print(f"Amount debited. New balance: {self.final_balance:.2f}")
            else:
                print("Insufficient funds for this debit.")
        except ValueError:
            print("Invalid amount entered.")