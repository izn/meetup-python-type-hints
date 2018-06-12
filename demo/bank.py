""" 4º Meetup Python """

class BankAccount:
    """ BankAccount class """
    def __init__(self, initial_balance = 0.0):
        self.balance = initial_balance

    def deposit(self, amount):
        """ Deposits to a Bank account """
        self.balance += amount

    def withdraw(self, amount):
        """ Withdraws from a Bank account """
        self.balance -= amount

    def overdrawn(self):
        """ Overdrawn? """
        return self.balance < 0


class Bank:
    """ Bank class """
    def __init__(self):
        self.accounts = []

    def create(self, account):
        """ Create a new account """
        self.accounts.append(account)

    def delete(self, account):
        """ Remove a Bank account """
        self.accounts.remove(account)

    def deposit(self, account, amount):
        final_amount = (amount - 0.05) # fee
        account.deposit(final_amount)

    def get_accounts(self):
        return self.accounts
