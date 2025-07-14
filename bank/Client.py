import logging.config
from decimal import Decimal

logging.config.fileConfig("../logging.ini")
logger = logging.getLogger("Client")


class Client:
    def __init__(self, name, balance):
        self._validate_name(name)
        logger.debug("Name passed validation")

        self._validate_balance(balance)
        logger.debug("Balance passed validation")

        self.name = name
        self.balance = balance

        logger.info("Successfully initialized Client class")

    def depositing(self, deposit: Decimal):
        self.balance += deposit
        return deposit

    def _validate_name(self, name):
        if not isinstance(name, str):
            logger.error(f'Provided name value "{name}" is not a string')
            raise TypeError
        elif not name.isalpha():
            logger.error(f'Provided name "{name}" must contain only letters')
            raise ValueError

    def _validate_balance(self, balance):
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
