class Bank:
    def __init__(self, account_number, account_holder_name, balance):
        self.account_number = account_number
        self.account_holder_name = account_holder_name
        self.balance = balance

    def withdraw(self, amount: int) -> int:
        if amount > self.balance:
            raise ValueError("Insufficient funds")
        self.balance -= amount
        return self.balance

    def deposit(self, amount: int) -> int:
        self.balance += amount
        return self.balance

    def show_balance(self):
        return self.balance


class SavingsAccount(Bank):
    _interest_rate = 3.5

    def __init__(self, account_number, account_holder_name, balance):
        super().__init__(account_number, account_holder_name, balance)

    def calculate_interest(self):
        return self.balance * self._interest_rate / 100


class CurrentAccount(Bank):
    _interest_rate = 1.5

    def __init__(self, account_number, account_holder_name, balance):
        super().__init__(account_number, account_holder_name, balance)

    def calculate_interest(self):
        return self.balance * self._interest_rate / 100
