-- Database migration script for Account Management System
-- Migration: 002_create_transaction_log
-- Description: Create transaction log table for audit trail

-- PostgreSQL version
CREATE TABLE IF NOT EXISTS transaction_log (
    id SERIAL PRIMARY KEY,
    account_id INTEGER NOT NULL,
    transaction_type VARCHAR(10) NOT NULL CHECK (transaction_type IN ('CREDIT', 'DEBIT', 'BALANCE_CHECK')),
    amount DECIMAL(10, 2) NOT NULL,
    balance_after DECIMAL(10, 2) NOT NULL,
    transaction_date TIMESTAMP WITH TIME ZONE NOT NULL DEFAULT CURRENT_TIMESTAMP,
    reference VARCHAR(100),
    status VARCHAR(20) NOT NULL DEFAULT 'COMPLETED',
    FOREIGN KEY (account_id) REFERENCES accounts(id) ON DELETE CASCADE
);

-- Create index for transaction date
CREATE INDEX IF NOT EXISTS idx_transaction_log_date ON transaction_log(transaction_date);

-- Create index for account_id
CREATE INDEX IF NOT EXISTS idx_transaction_log_account ON transaction_log(account_id);

-- Create index for transaction type
CREATE INDEX IF NOT EXISTS idx_transaction_log_type ON transaction_log(transaction_type);