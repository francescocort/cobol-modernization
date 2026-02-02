#!/usr/bin/env python3
"""
Python equivalent of MainProgram.cob
Account Management System - Main Menu Interface
"""

class MainProgram:
    """Main menu interface for the Account Management System"""
    
    def __init__(self):
        self.continue_flag = True
        self.operations_service = Operations()
    
    def run(self):
        """Main program loop"""
        while self.continue_flag:
            self.display_menu()
            choice = self.get_user_choice()
            self.handle_choice(choice)
        
        print("Exiting the program. Goodbye!")
    
    def display_menu(self):
        """Display the main menu"""
        print("-" * 32)
        print("Account Management System")
        print("1. View Balance")
        print("2. Credit Account")
        print("3. Debit Account")
        print("4. Exit")
        print("-" * 32)
        print("Enter your choice (1-4): ")
    
    def get_user_choice(self) -> int:
        """Get and validate user choice"""
        try:
            choice = int(input().strip())
            return choice
        except ValueError:
            return 0
    
    def handle_choice(self, choice: int):
        """Handle user menu choice"""
        if choice == 1:
            self.operations_service.view_balance()
        elif choice == 2:
            self.operations_service.credit_account()
        elif choice == 3:
            self.operations_service.debit_account()
        elif choice == 4:
            self.continue_flag = False
        else:
            print("Invalid choice, please select 1-4.")

if __name__ == "__main__":
    program = MainProgram()
    program.run()