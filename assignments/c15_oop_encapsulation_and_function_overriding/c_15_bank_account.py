import uuid


class BankAccount:
    def __init__(self):
        self._account_number = str(uuid.uuid4())
        self._balance = 0

    def withdraw(self, amount: int) -> None:
        if amount > self._balance:
            raise ValueError("Insufficient funds")
        self._balance -= amount

    def deposit(self, amount: int) -> None:
        self._balance += amount

    def show_balance(self) -> None:
        print(self._balance)


class SavingsAccount(BankAccount):
    _interest_rate = 3.5

    def __init__(self):
        super().__init__()

    def calculate_interest(self) -> float:
        return self._balance * self._interest_rate / 100


class CurrentAccount(BankAccount):
    _interest_rate = 1.5

    def __init__(self):
        super().__init__()

    def calculate_interest(self) -> float:
        return self._balance * self._interest_rate / 100


class Customer:
    def __init__(self, name) -> None:
        self._name = name
        self._accounts = []

    def get_name(self) -> str:
        return self._name

    def add_account(self, account: BankAccount) -> None:
        self._accounts.append(account)

    def get_info(self) -> str:
        return f'{self._name}: {len(self._accounts)}'


class PrivateCustomer(Customer):
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        super().__init__(self.set_name())

    def set_name(self):
        return f'{self.first_name} {self.last_name}'


class BusinessCustomer(Customer):
    def __init__(self, company_name):
        self.company_name = f'{company_name} GmbH'
        super().__init__(self.set_name())

    def set_name(self):
        return self.company_name
