"""Описати клас "Банківський рахунок", атрибути якого:

   - ім'я облікового запису - str
   - унікальний id (uuid)
   - баланс float (чи Decimal)
   - транзакції (список)
   Методи

     депозит коштів
     виведення коштів
     отримати баланс


   При зміні балансу записувати в транзакції (сума, тип операції, поточна_дата)

   * Дод. додати та враховувати банківські комісії (1%)"""


import uuid
from datetime import datetime
from decimal import Decimal


class Transaction:
    _deposit = 'deposit'
    _withdrawal = 'withdrawal'

    def __init__(self, amount, transactionType: str):
        if amount < 0:
            raise ValueError('Amount is less than 0')
        if (transactionType != self._deposit) and (transactionType != self._withdrawal):
            raise ValueError('Incorrect transaction type')
        self.amount = amount
        self.transactionType = str(transactionType.lower())
        self.date = datetime.now()

    def __str__(self):
        return f'{self.amount, self.transactionType, self.date.strftime("%d-%m-%Y %h:%m:%s")}'

    def depositType(self) -> str:
        return self._deposit

    def withdrawalType(self) -> str:
        return self._withdrawal


class BankAccount:
    def __init__(self, name):
        self.name = name
        self.uid = uuid.uuid1()
        self.balance = Decimal('0')
        self.transactions = []

    def __str__(self):
        return f'{self.name, str(self.uid), str(self.balance), str(self.transactions)}'

    def getBalance(self) -> Decimal:
        return self.balance

    def changeBalance(self, transaction: Transaction):
        #      if transaction.transactionType == Transaction.depositType():
        if transaction.transactionType == 'deposit':
            self.balance += transaction.amount
        else:
            self.balance -= transaction.amount

    #    def addDeposit(self, transaction: Transaction):
    #        if transaction.transactionType is Transaction.depositType:
    #            self.transactions.append(transaction)
    #            self.changeBalance()
    #        else:
    #            raise ValueError()

    #   def addWithdrawal(self, transaction: Transaction):
    #        if transaction is Transaction.withdrawalType:
    #            self.transactions.append(transaction)
    #            self.changeBalance()
    #        else:
    #            raise ValueError()

    def addTransactions(self, transaction: Transaction):
        self.transactions.append(transaction)
        self.changeBalance(transaction)


account = BankAccount('My account')
transaction1 = Transaction(125, 'deposit')
transaction2 = Transaction(100, 'withdrawal')

account.addTransactions(transaction1)
account.addTransactions(transaction2)

print(account)

