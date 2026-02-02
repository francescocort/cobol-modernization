-- Database migration script for Account Management System
-- Migration: 001_create_accounts_table
-- Description: Create accounts table to replace COBOL data storage

-- PostgreSQL version
CREATE TABLE IF NOT EXISTS accounts (
    id SERIAL PRIMARY KEY,
    account_number VARCHAR(50) UNIQUE NOT NULL,
    balance DECIMAL(10, 2) NOT NULL DEFAULT 1000.00,
    currency VARCHAR(3) NOT NULL DEFAULT 'USD',
    created_at TIMESTAMP WITH TIME ZONE NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE NOT NULL DEFAULT CURRENT_TIMESTAMP,
    is_active BOOLEAN NOT NULL DEFAULT TRUE
);

-- Create index for faster balance queries
CREATE INDEX IF NOT EXISTS idx_accounts_balance ON accounts(balance);

-- Create index for account number lookup
CREATE INDEX IF NOT EXISTS idx_accounts_number ON accounts(account_number);

-- Insert default account (equivalent to COBOL's default balance)
INSERT INTO accounts (account_number, balance)
SELECT 'DEFAULT_ACCOUNT', 1000.00
WHERE NOT EXISTS (SELECT 1 FROM accounts WHERE account_number = 'DEFAULT_ACCOUNT');

-- Create function to update updated_at timestamp
CREATE OR REPLACE FUNCTION update_updated_at()
RETURNS TRIGGER AS $$
BEGIN
    NEW.updated_at = CURRENT_TIMESTAMP;
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

-- Create trigger to automatically update updated_at
CREATE TRIGGER trigger_update_accounts_updated_at
BEFORE UPDATE ON accounts
FOR EACH ROW
EXECUTE FUNCTION update_updated_at();