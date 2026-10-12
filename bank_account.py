from typing import Dict, List

class BankAccount:
    """Base Class for a bank Account"""

    def __init__(self, account_number: str, holder_name: str, balance: float = 0.0 ) -> None:
        if balance < 0:
            raise ValueError("Initial Balance cannot be negative. ")

        self.account_number = account_number
        self.holder_name = holder_name
        self._balanace = balance    #private
        self.transaction_histroy: List[Dict[str, object]] = []


    def _add_transaction(self, trasaction_type: str, amount: float) -> None:
        """Store a transaction in the account history"""
        self.transaction_histroy.append({
            'type': trasaction_type,
            'amount': amount,
            'balance': self._balanace
        })


    def deposit(self, amount: float) -> None:
        """Deposit money into the account."""
        if amount <= 0:
            raise ValueError("Deposit money must be greater than ZERO.")

        self._balanace += amount
        self._add_transaction('deposit', amount)


    def withdraw(self, amount: float) -> None:
        """Withdraw Money from the account"""
        if amount <= 0:
            raise ValueError("Withdrawal amount must be greater than Zero.")

        if amount > self._balanace:
            raise ValueError("Insufficient Balance.")

        self._balanace -= amount
        self._add_transaction("withdraw", amount)


    def get_balance(self) -> float:
        """Return the current account Balance"""

        return self._balanace



class SavingsAccount(BankAccount):
    """Savings account with interest"""
    def __init__(self, account_number: str, holder_name: str, balance: float = 0.0, interest_rate: float = 0.0) -> None:
        super().__init__(account_number, holder_name, balance)

        if interest_rate < 0:
            raise ValueError("Interest rate cannot be negative.")

        self.interest_rate = interest_rate


    def apply_interest(self) -> None:
        """Apply interest to the current balance"""
        interest = self._balanace * self.interest_rate / 100

        self._balanace += interest

        self._add_transaction("interest", interest)



class CurrentAccount(BankAccount):
    """Current account with an overdraft limit"""

    def __init__(self, account_number: str, holder_name: str, balance: float = 0.0, overdraft_limit: float = 0.0) -> None:
        super().__init__(account_number, holder_name, balance)

        if overdraft_limit < 0:
            raise ValueError("Overdraft limit cannot be negative.")

        self.overdraft_limit = overdraft_limit



    def withdraw(self, amount: float) -> None:
        """Withdraw money using the availble overdraft limit"""
        if amount < 0:
            raise ValueError("Withdrawal amount must be greater that Zero")

        if amount > self._balanace + self.overdraft_limit :
            raise ValueError("Withdrawal exceeds overdraft limit.")

        self._balanace -= amount
        self._add_transaction('withdraw', amount)       