class BankAccount:
    _maximum_loan = 1000000
    _customer_service_address = 'loan@office.com'

    def __init__(self, account_number: int, client_name: str) -> None:
        self.account_number: int = account_number
        self.client_name: str = client_name
        self.balance: int = 0
        self.days_to_pay_loan: int = 0

    def grant_loan(self, amount: int, days_to_pay: int) -> None:
        if amount > BankAccount._maximum_loan:
            raise ValueError('Loan exceeds maximum loan limit')

        if days_to_pay < 30:
            raise ArithmeticError(
                'Pay back period cannot be less than 30 days')

        self.balance += amount
        self.days_to_pay_loan = days_to_pay

    @staticmethod
    def get_customer_service_address() -> str:
        return BankAccount._customer_service_address
