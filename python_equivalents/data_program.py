#!/usr/bin/env python3
"""
Python equivalent of DataProgram.cob
Account Management System - Data Access Layer
"""

class DataProgram:
    """Data storage and access layer"""
    
    def __init__(self):
        self.storage_balance = 1000.00  # Default starting balance
    
    def read_balance(self) -> float:
        """Read balance from storage"""
        return self.storage_balance
    
    def write_balance(self, balance: float):
        """Write balance to storage"""
        self.storage_balance = balance