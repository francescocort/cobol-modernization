#!/usr/bin/env python3
"""
Unit tests for MainProgram class
Tests the main menu interface functionality
"""

import unittest
from unittest.mock import patch, MagicMock
from python_equivalents.main_program import MainProgram


class TestMainProgram(unittest.TestCase):
    """Test cases for MainProgram class"""
    
    def setUp(self):
        """Set up test fixtures"""
        self.program = MainProgram()
        self.program.operations_service = MagicMock()
    
    def test_initialization(self):
        """Test that MainProgram initializes correctly"""
        self.assertTrue(self.program.continue_flag)
        self.assertIsNotNone(self.program.operations_service)
    
    @patch('builtins.input', return_value='1')
    def test_get_user_choice_valid(self, mock_input):
        """Test getting valid user choice"""
        choice = self.program.get_user_choice()
        self.assertEqual(choice, 1)
    
    @patch('builtins.input', return_value='invalid')
    def test_get_user_choice_invalid(self, mock_input):
        """Test getting invalid user choice"""
        choice = self.program.get_user_choice()
        self.assertEqual(choice, 0)
    
    def test_handle_choice_view_balance(self):
        """Test handling choice 1 (view balance)"""
        self.program.handle_choice(1)
        self.program.operations_service.view_balance.assert_called_once()
    
    def test_handle_choice_credit(self):
        """Test handling choice 2 (credit account)"""
        self.program.handle_choice(2)
        self.program.operations_service.credit_account.assert_called_once()
    
    def test_handle_choice_debit(self):
        """Test handling choice 3 (debit account)"""
        self.program.handle_choice(3)
        self.program.operations_service.debit_account.assert_called_once()
    
    def test_handle_choice_exit(self):
        """Test handling choice 4 (exit)"""
        self.program.handle_choice(4)
        self.assertFalse(self.program.continue_flag)
    
    def test_handle_choice_invalid(self):
        """Test handling invalid choice"""
        # This should not raise an exception and should not call any service methods
        self.program.handle_choice(99)
        self.program.operations_service.view_balance.assert_not_called()
        self.program.operations_service.credit_account.assert_not_called()
        self.program.operations_service.debit_account.assert_not_called()
    
    @patch('builtins.print')
    def test_display_menu(self, mock_print):
        """Test that display_menu prints expected output"""
        self.program.display_menu()
        
        # Check that expected menu items were printed
        calls = [call for call in mock_print.call_args_list]
        menu_text = '\n'.join(str(call) for call in calls)
        
        self.assertIn('Account Management System', menu_text)
        self.assertIn('View Balance', menu_text)
        self.assertIn('Credit Account', menu_text)
        self.assertIn('Debit Account', menu_text)
        self.assertIn('Exit', menu_text)


if __name__ == '__main__':
    unittest.main()