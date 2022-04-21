# Store the current value of the BankAccount in an attribute named balance that
# should start with 0. (Hint: implement __init__() function)

# Now create some instances of BankAccount and check whether they are
# instances of the said classes or not (Hint: use isinstance() for this)

# Add a deposit method that receives a value and adds it to balance and prints balance
# Add a withdraw method that receives a value and subtracts it from balance and prints balance

# We only want users to be able to deposit and withdraw a positive amount. A ValueError should be raised.
# e.g.: bank_account.deposit(-200) -> ValueError

# A ValueError should be raised if the user inputs anything that can’t be interpreted as an integer.
# e.g.: bank_account.deposit(“Not an integer”) -> ValueError


class BankAccount:
    def __init__(self):
        self.balance = 0

    def get_balance(self):
        return self.balance

    def deposit(self, value):
        if not isinstance(value, int):
            raise ValueError('Deposit amount should be an interger value')
        if value <= 0:
            raise ValueError('Deposit amount should be more than 0')

        self.balance += value
        print(f'Balance: {self.balance}')

    def withdraw(self, value):
        if not isinstance(value, int):
            raise ValueError('Withdraw amount should be an interger value')
        if value <= 0:
            raise ValueError('Withdraw amount should be more than 0')

        self.balance -= value
        print(f'Balance: {self.balance}')

    def __str__(self):
        return f'Balance: {self.balance}'


if __name__ == "__main__":
    myAccount = BankAccount()
    print(myAccount)

    if isinstance(myAccount, BankAccount):
        print('yes')

    myAccount.deposit(5)
    myAccount.withdraw(3)

    try:
        myAccount.deposit('a')
    except Exception as e:
        print(e)

    try:
        myAccount.deposit(-5)
    except Exception as e:
        print(e)
