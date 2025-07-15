import logging.config
from decimal import Decimal

logging.config.fileConfig("../logging.ini")
logger = logging.getLogger("Client")


class Client:
    def __init__(self, name, balance):
        if not Client.validate_name(name):
            logger.error(f'Invalid name "{name}" provided to the constructor')
            raise ValueError("Invalid name")

        if not Client.validate_balance(balance):
            logger.error(
                f"Invalid balance {balance} provided to the constructor"
            )
            raise ValueError("Invalid balance")

        self.name = name
        self.balance = balance

        logger.info("Successfully initialized Client class")

    def depositing(self, deposit: Decimal):
        self.balance += deposit
        return deposit

    @staticmethod
    def validate_name(name):
        try:
            if not isinstance(name, str):
                logger.error(f'Provided name value "{name}" is not a string')
                return False
            elif not name.isalpha():
                logger.error(
                    f'Provided name "{name}" must contain only letters'
                )
                return False
            logger.debug(f'Provided name "{name}" passed validation')
            return True
        except Exception as e:
            logger.error(f"Unexpected error during name validation: {e}")
        finally:
            logger.debug(
                f"Finished name validation with the for input: {name}"
            )

    @staticmethod
    def validate_balance(balance):
        try:
            if not isinstance(balance, Decimal):
                logger.error(
                    f"The provided balance {balance} is not in a valid "
                    f"currency format"
                )
                return False
            elif balance < Decimal("0.00"):
                logger.error(
                    f"Current value of balance {balance} cannot be less than "
                    f"0.00"
                )
                return False
            logger.debug(f"Provided balance {balance} passed validation")
            return True
        except Exception as e:
            logger.error(f"Unexpected error during balance validation: {e}")
        finally:
            logger.debug(
                f"Finished balance validation with the for input: {balance}"
            )
