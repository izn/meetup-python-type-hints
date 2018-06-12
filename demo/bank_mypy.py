""" 4º Meetup Python """
from typing import List

class BankAccount:
    """ BankAccount class """
    def __init__(self, initial_balance: float = 0.0) -> None:
        self.balance = initial_balance

    def deposit(self, amount: float) -> float:
        """ Deposits to a Bank account """
        self.balance += amount
        return self.balance

    def withdraw(self, amount: float) -> None:
        """ Withdraws from a Bank account """
        self.balance -= amount

    def overdrawn(self) -> bool:
        """ Overdrawn? """
        return self.balance < 0


class Bank:
    """ Bank class """
    def __init__(self) -> None:
        self.accounts: List[BankAccount] = []

    def create(self, account: BankAccount) -> None:
        """ Creates a new account """
        self.accounts.append(account)

    def delete(self, account: BankAccount) -> None:
        """ Removes a Bank account """
        self.accounts.remove(account)

    def deposit(self, account: BankAccount, amount: float) -> None:
        final_amount = (amount - 0.05) # fee
        account.deposit(final_amount)

    def get_accounts(self) -> List[BankAccount]:
        return self.accounts
