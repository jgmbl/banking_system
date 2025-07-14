import logging.config
from decimal import Decimal

logging.config.fileConfig("../logging.ini")
logger = logging.getLogger("Client")


class Client:
    def __init__(self, name, balance):
        if not name.isalpha():
            logger.error(f'Provided name "{name}" must contain only letters')
            raise ValueError

        logger.debug("Name passed validation")

        if not isinstance(balance, Decimal):
            logger.error(
                f"The provided balance {balance} is not in a valid currency format"
            )
            raise TypeError
        elif balance < Decimal("0.00"):
            logger.error(
                f"Current value of balance {balance} cannot be less than 0.00"
            )
            raise ValueError

        logger.debug("Balance passed validation")

        logger.info("Successfully initialized Client class")

        self.name = name
        self.balance = balance

    def depositing(self, deposit: Decimal):
        self.balance += deposit
        return deposit
