#!/usr/bin/env python3
"""
Unit tests for Operations class
Tests the business logic for account operations
"""

import unittest
from unittest.mock import patch, MagicMock
from python_equivalents.operations import Operations


class TestOperations(unittest.TestCase):
    """Test cases for Operations class"""
    
    def setUp(self):
        """Set up test fixtures"""
        self.operations = Operations()
        self.operations.data_service = MagicMock()
        self.operations.final_balance = 1000.00
    
    def test_initialization(self):
        """Test that Operations initializes correctly"""
        self.assertIsNotNone(self.operations.data_service)
        self.assertEqual(self.operations.final_balance, 1000.00)
    
    def test_view_balance(self):
        """Test view_balance method"""
        self.operations.data_service.read_balance.return_value = 1500.00
        
        with patch('builtins.print') as mock_print:
            self.operations.view_balance()
            
        self.operations.data_service.read_balance.assert_called_once()
        mock_print.assert_called_with("Current balance: 1500.00")
        self.assertEqual(self.operations.final_balance, 1500.00)
    
    @patch('builtins.input', return_value='250.50')
    def test_credit_account_valid(self, mock_input):
        """Test credit_account with valid amount"""
        self.operations.data_service.read_balance.return_value = 1000.00
        
        with patch('builtins.print') as mock_print:
            self.operations.credit_account()
            
        self.operations.data_service.read_balance.assert_called_once()
        self.operations.data_service.write_balance.assert_called_once_with(1250.50)
        mock_print.assert_called_with("Amount credited. New balance: 1250.50")
        self.assertEqual(self.operations.final_balance, 1250.50)
    
    @patch('builtins.input', return_value='invalid')
    def test_credit_account_invalid(self, mock_input):
        """Test credit_account with invalid amount"""
        with patch('builtins.print') as mock_print:
            self.operations.credit_account()
            
        self.operations.data_service.read_balance.assert_not_called()
        self.operations.data_service.write_balance.assert_not_called()
        mock_print.assert_called_with("Invalid amount entered.")
    
    @patch('builtins.input', return_value='100.00')
    def test_debit_account_valid(self, mock_input):
        """Test debit_account with valid amount and sufficient funds"""
        self.operations.data_service.read_balance.return_value = 1000.00
        
        with patch('builtins.print') as mock_print:
            self.operations.debit_account()
            
        self.operations.data_service.read_balance.assert_called_once()
        self.operations.data_service.write_balance.assert_called_once_with(900.00)
        mock_print.assert_called_with("Amount debited. New balance: 900.00")
        self.assertEqual(self.operations.final_balance, 900.00)
    
    @patch('builtins.input', return_value='1500.00')
    def test_debit_account_insufficient_funds(self, mock_input):
        """Test debit_account with insufficient funds"""
        self.operations.data_service.read_balance.return_value = 1000.00
        
        with patch('builtins.print') as mock_print:
            self.operations.debit_account()
            
        self.operations.data_service.read_balance.assert_called_once()
        self.operations.data_service.write_balance.assert_not_called()
        mock_print.assert_called_with("Insufficient funds for this debit.")
        self.assertEqual(self.operations.final_balance, 1000.00)
    
    @patch('builtins.input', return_value='invalid')
    def test_debit_account_invalid(self, mock_input):
        """Test debit_account with invalid amount"""
        with patch('builtins.print') as mock_print:
            self.operations.debit_account()
            
        self.operations.data_service.read_balance.assert_not_called()
        self.operations.data_service.write_balance.assert_not_called()
        mock_print.assert_called_with("Invalid amount entered.")


if __name__ == '__main__':
    unittest.main()