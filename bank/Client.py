from decimal import Decimal


class Client:
    def __init__(self, name, balance: Decimal):
        self.name = name

        if balance < 0:
            raise ValueError("Balance should be greater than 0")
        self.balance = balance

    def depositing(self, deposit: Decimal):
        self.balance += deposit
        return deposit
