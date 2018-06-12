""" 4º Meetup Python """
from bank_mypy import Bank, BankAccount

# Account
account = BankAccount(200.50)
account.deposit(125)

# Bank
bank = Bank()
bank.create(account)
bank.deposit(account, 200)

print('Bank account balance:', account.balance)