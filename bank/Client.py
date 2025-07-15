import logging.config
import random
import string
from decimal import Decimal

logging.config.fileConfig("../logging.ini")
logger = logging.getLogger("Client")


class Client:
    def __init__(self, name, balance):
        if not Client.validate_name(name):
            logger.error("Invalid name provided to the constructor")
            raise ValueError("Invalid name")

        if not Client.validate_balance(balance):
            logger.error("Invalid balance provided to the constructor")
            raise ValueError("Invalid balance")

        self.name = name
        self.balance = balance
        self.anonymized_name = Client.anonymized_name()
        self.anonymized_balance = "***"

        logger.info(
            f"Successfully initialized Client class for name "
            f"{self.anonymized_name} and balance {self.anonymized_balance}"
        )

    def depositing(self, deposit: Decimal):
        self.balance += deposit
        return deposit

    @staticmethod
    def validate_name(name):
        try:
            if not isinstance(name, str):
                logger.error("Provided name value is not a string")
                return False
            if not name:
                logger.error("Provided name value cannot be empty or None")
                return False
            elif not name.isalpha():
                logger.error("Provided name must contain only letters")
                return False
            logger.debug("Provided name passed validation")
            return True
        except Exception as e:
            logger.error(f"Unexpected error during name validation: {e}")
        finally:
            logger.debug("Finished name validation")

    @staticmethod
    def validate_balance(balance):
        try:
            if not isinstance(balance, Decimal):
                logger.error(
                    "The provided balance is not in a valid currency format"
                )
                return False
            elif balance < Decimal("0.00"):
                logger.error(
                    "Current value of balance cannot be less than 0.00"
                )
                return False
            logger.debug("Provided balance passed validation")
            return True
        except Exception as e:
            logger.error(f"Unexpected error during balance validation: {e}")
        finally:
            logger.debug("Finished balance validation")

    @staticmethod
    def anonymized_name(length=15):
        try:
            result = "".join(
                random.choices(string.ascii_letters + string.digits, k=length)
            )
            logger.debug(f"Anonymizing name ended with result: {result}")
            return result
        except Exception as e:
            logger.error(f"Unexpected error during anonymizing name: {e}")
