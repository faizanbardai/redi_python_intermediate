import uuid

from bank_account import SavingsAccount, BankAccount, CurrentAccount, Customer, PrivateCustomer, BusinessCustomer

ACCOUNT_CLASS = BankAccount
SAVINGS_CLASS = SavingsAccount
CURRENT_CLASS = CurrentAccount

CUSTOMER_CLASS = Customer
BUSINESS_CUSTOMER = BusinessCustomer
PRIVATE_CUSTOMER = PrivateCustomer


def test_account_number_is_generated_on_instantiation():
    """
    Checks that upon instantiation, the Bank Account class generates a UUID and stores it as a string
    in it's _account_number attribute.
    :return:
    """
    account = ACCOUNT_CLASS()

    assert isinstance(account._account_number, str)
    assert uuid.UUID(account._account_number)


def test_interest_is_correctly_calculated_savings():
    """
    Checks that the interest for the savings account is calculated correctly.
    :return:
    """
    amount_to_deposit = 500
    expected_interest = 17.5

    instance = SAVINGS_CLASS()

    instance.deposit(amount_to_deposit)

    assert expected_interest == instance.calculate_interest()


def test_interest_is_correctly_calculated_current():
    """
    Checks that the interest for the current account is calculated correctly.
    :return:
    """
    amount_to_deposit = 500
    expected_interest = 7.5

    instance = CURRENT_CLASS()

    instance.deposit(amount_to_deposit)

    assert expected_interest == instance.calculate_interest()


def test_name_is_set_business_user():
    """
    Checks that:
    - The constructor of the BusinessCustomer class takes one argument (company name)
    - The string passed in that argument is stored in both _name and company_name variables and that GmbH is suffixed
    - The value of ._name is returned correctly when calling get_name()
    :return:
    """
    instance = BUSINESS_CUSTOMER("My Company")

    assert instance.company_name == "My Company GmbH"
    assert instance.get_name() == "My Company GmbH"


def test_name_is_set_private_user():
    """
    Checks that:
    - The constructor of the PrivateCustomer class takes two arguments (first name and last name).
    - The first name is stored in the _first_name instance variable.
    - The last name is stored in the _last_name instance variable.
    - The fist name and last name values are "joined" using whitespace and stored in the _name instance variable.
    - The value of ._name is returned correctly when calling get_name().
    :return:
    """
    instance = PrivateCustomer("John", "Doe")

    assert instance.first_name == "John"
    assert instance.last_name == "Doe"

    assert instance._name == "John Doe"
    assert instance.get_name() == "John Doe"


def test_add_bank_accounts():
    """
    Checks that after adding accounts to a Customer instance, the correct accounts are present in the customer's
    _accounts instance variable.

    :return:
    """
    savings_account = SavingsAccount()
    savings_account.deposit(100)

    current_account = CurrentAccount()
    current_account.deposit(200)

    customer = PRIVATE_CUSTOMER("Jane", "Doe")
    customer.add_account(savings_account)
    customer.add_account(current_account)

    assert len(customer._accounts) == 2
    assert customer._accounts[0]._balance == 100
    assert customer._accounts[1]._balance == 200


def test_get_info():
    """
    Checks that after adding two accounts to a Customer instance
    the correct message is returned when calling the get_info() method.
    :return:
    """
    savings_account = SavingsAccount()
    savings_account.deposit(100)

    current_account = CurrentAccount()
    current_account.deposit(200)

    customer = PRIVATE_CUSTOMER("Jane", "Doe")
    assert customer.get_info() == "Jane Doe: 0"

    customer.add_account(savings_account)
    customer.add_account(current_account)
    assert customer.get_info() == "Jane Doe: 2"
