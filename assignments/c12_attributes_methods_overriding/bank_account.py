# 1. Store the current value of the BankAccount in an attribute named balance (that should start with 0)
# 2. Add a deposit method that receives a value and adds it to balance and prints balance
# 3. Add a withdraw method that receives a value and subtracts it from balance and prints balance

# 1. Add a movements attribute to your class that should be an empty list to start.
# 2. Every time deposit or withdraw methods are called, this movement should be added
#    to movements (eg: deposit(50) should append “DEPOSIT 50” to movements)
# 3. Add a method print_movements to print all the movements

# 1. When the balance is negative (when withdraw method is called), a
#    warning should be printed to the user. Create a display_warning
#    method in your class to do it.

# 1. Add a minimum_balance attribute to your instance (should be 0 by default), and a
#    method to update this value (set_minimum_balance)
# 2. Change the warning check (from exercise 1.) to be shown when balance <=
#    minimum_balance

class BankAccount:

    def __init__(self):
        self.balance = 0
        self.minimum_balance = 0
        self.movement = []

    def get_balance(self):
        return self.balance

    def deposit(self, value):
        if not isinstance(value, int):
            raise ValueError('Deposit amount should be an interger value')
        if value <= 0:
            raise ValueError('Deposit amount should be more than 0')

        self.balance += value
        self.movement.append('DEPOSIT ' + str(value))
        print(f'Balance: {self.balance}')

    def withdraw(self, value):
        if not isinstance(value, int):
            raise ValueError('Withdraw amount should be an interger value')
        if value <= 0:
            raise ValueError('Withdraw amount should be more than 0')

        if self.balance - value < self.minimum_balance:
            return BankAccount.display_warning()

        self.balance -= value
        self.movement.append('WITHDRAW ' + str(value))
        print(f'Balance: {self.balance}')

    def __str__(self):
        return f'Balance: {self.balance}'

    def print_movements(self):
        for move in self.movement:
            print(move)

    def display_warning():
        print('Balance is negative')

    def set_minimum_balance(self, value):
        self.minimum_balance = value


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

    myAccount.print_movements()
    myAccount.withdraw(10)
    myAccount.set_minimum_balance(5)
    myAccount.withdraw(1)
