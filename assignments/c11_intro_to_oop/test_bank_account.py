import pytest
from bank_account import BankAccount


def test_bank_account_initial_to_be_zero():
    new_account = BankAccount()
    assert(new_account.get_balance() == 0)


def test_bank_account_instance():
    new_account = BankAccount()
    assert(isinstance(new_account, BankAccount) == True)


def test_bank_account_deposit():
    new_account = BankAccount()
    amount = 5
    new_account.deposit(amount)
    assert(new_account.get_balance() == amount)


def test_bank_account_deposit_integer_value_error():
    new_account = BankAccount()
    amount = 'Not an integer'
    with pytest.raises(ValueError):
        new_account.deposit(amount)


def test_bank_account_deposit_negative_value_error():
    new_account = BankAccount()
    amount = -200
    with pytest.raises(ValueError):
        new_account.deposit(amount)


def test_bank_account_withdraw_integer_value_error():
    new_account = BankAccount()
    amount = 'Not an integer'
    with pytest.raises(ValueError):
        new_account.withdraw(amount)


def test_bank_account_withdraw_negative_value_error():
    new_account = BankAccount()
    amount = -200
    with pytest.raises(ValueError):
        new_account.withdraw(amount)
