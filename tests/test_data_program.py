#!/usr/bin/env python3
"""
Unit tests for DataProgram class
Tests the data access layer functionality
"""

import unittest
from python_equivalents.data_program import DataProgram


class TestDataProgram(unittest.TestCase):
    """Test cases for DataProgram class"""
    
    def setUp(self):
        """Set up test fixtures"""
        self.data_program = DataProgram()
    
    def test_initialization(self):
        """Test that DataProgram initializes correctly"""
        self.assertEqual(self.data_program.storage_balance, 1000.00)
    
    def test_read_balance(self):
        """Test read_balance method"""
        balance = self.data_program.read_balance()
        self.assertEqual(balance, 1000.00)
        self.assertEqual(self.data_program.storage_balance, 1000.00)
    
    def test_write_balance(self):
        """Test write_balance method"""
        new_balance = 1500.50
        self.data_program.write_balance(new_balance)
        self.assertEqual(self.data_program.storage_balance, new_balance)
        
        # Verify the change persists
        balance = self.data_program.read_balance()
        self.assertEqual(balance, new_balance)
    
    def test_write_balance_zero(self):
        """Test write_balance with zero balance"""
        self.data_program.write_balance(0.00)
        self.assertEqual(self.data_program.storage_balance, 0.00)
    
    def test_write_balance_negative(self):
        """Test write_balance with negative balance"""
        self.data_program.write_balance(-50.00)
        self.assertEqual(self.data_program.storage_balance, -50.00)
    
    def test_multiple_operations(self):
        """Test multiple read/write operations"""
        # Initial read
        balance1 = self.data_program.read_balance()
        self.assertEqual(balance1, 1000.00)
        
        # Write new value
        self.data_program.write_balance(2000.00)
        
        # Read updated value
        balance2 = self.data_program.read_balance()
        self.assertEqual(balance2, 2000.00)
        
        # Write another value
        self.data_program.write_balance(500.75)
        
        # Read final value
        balance3 = self.data_program.read_balance()
        self.assertEqual(balance3, 500.75)


if __name__ == '__main__':
    unittest.main()