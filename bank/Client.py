from decimal import Decimal

import logging, logging.config

logging.config.fileConfig("../logging.ini")
logger = logging.getLogger('Client')

class Client:

    def __init__(self, name, balance: Decimal):
        self.name = name

        if balance < 0:
            logger.error(f"Current value of balance {balance} cannot be less than 0.00")
            raise ValueError
        self.balance = balance

    def depositing(self, deposit: Decimal):
        self.balance += deposit
        return deposit
