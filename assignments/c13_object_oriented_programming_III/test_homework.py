import pytest
import re

# INSTRUCTIONS
# You should be familiar with the basics of PyTest already.
# Don't worry too much about the internals of the tests, you will have a lesson about testing in OOP.
# For the time being just make sure the tests pass.

# Create your classes in a solution.py file or adjust the following import statement to the name you decided to use.
# Both files should be in the same folder:
# - my_homework_folder
#   - solution.py (or something_else.py)
#   - test_homework.py

from solution import BankAccount

# To make this test suite work with your code replace the following variable with a reference to your class.
# IMPORTANT: Don't instantiate the class here! A.K.A. Don't use the () after the name!.
Bank_Account_Class = BankAccount

# Follow the instructions in the class slides (27 to 29). All these tests should pass.
# Just run "pytest my_homework" from the command line.


def test_maximum_loan_cannot_be_exceeded():
    """
    Tests that a loan cannot exceed an amount of 1,000,000.
    :return:
    """
    bank_account = Bank_Account_Class(242, "Some dude")

    with pytest.raises(ValueError):
        bank_account.grant_loan(2_000_000, 365)


def test_loan_payday_cannot_be_less_than_30():
    """
    Tests that a loan with a less than 30 days to pay back cannot be granted.
    """
    bank_account = Bank_Account_Class(242, "Some dude")

    with pytest.raises(ArithmeticError):
        bank_account.grant_loan(500, 15)


def test_loan_granted():
    """
    Tests that:
        - The account's balance after a loan is granted is equal to the initial balance plus the amount of the loan.
        - The days_to_pay_loan attribute stores the correct number of days to pay back after a loan is granted.
    """
    bank_account = Bank_Account_Class(242, "Some dude")
    initial_balance = bank_account.balance

    bank_account.grant_loan(5_000, 100)
    assert bank_account.balance == initial_balance + 5_000
    assert bank_account.days_to_pay_loan == 100


def test_customer_service_address_is_same_for_all_instances():
    """
    Tests that all instances of BankAccount return the same email address when
    the get_customer_service_address method is called.
    """
    bank_account = Bank_Account_Class(242, "Some dude")
    bank_account_2 = Bank_Account_Class(2049, "Some other dude")

    assert bank_account.get_customer_service_address() == bank_account_2.get_customer_service_address()
    assert bank_account.get_customer_service_address() is bank_account_2.get_customer_service_address()


def test_customer_service_address_is_an_email_address():
    """
    Tests that the string returned when calling the get_customer_service_address method is a valid email.
    :return:
    """
    bank_account = Bank_Account_Class(242, "Some dude")

    assert re.match(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)", bank_account.get_customer_service_address())


def test_correct_attribute_types():
    """
    Tests that the Class has the required public attributes and types after instantiation.
    """
    bank_account = Bank_Account_Class(242, "Someone")

    bank_account.grant_loan(100, 30)

    assert isinstance(bank_account.account_number, int)
    assert isinstance(bank_account.client_name, str)
    assert isinstance(bank_account.balance, int)
    assert isinstance(bank_account.days_to_pay_loan, int)
