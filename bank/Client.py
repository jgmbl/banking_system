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

        logger.info("Successfully initialized Client class")

    def depositing(self, deposit: Decimal):
        self.balance += deposit
        return deposit

    @staticmethod
    def validate_name(name):
        anonymized_name = Client.anonymized_name(name, 10)
        try:
            if not isinstance(name, str):
                logger.error(
                    f"Provided name value {anonymized_name} is not a string"
                )
                return False
            if not name:
                logger.error(
                    f"Provided name value {anonymized_name} cannot be empty "
                    f"or None"
                )
                return False
            elif not name.isalpha():
                logger.error(
                    f"Provided name {anonymized_name} must contain only "
                    f"letters"
                )
                return False
            logger.debug(f"Provided name {anonymized_name} passed validation")
            return True
        except Exception as e:
            logger.error(f"Unexpected error during name validation: {e}")
        finally:
            logger.debug(
                f"Finished name validation with for input: {anonymized_name}"
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
                f"Finished balance validation with for input: {balance}"
            )

    @staticmethod
    def anonymized_name(name, num):
        default_anonymized_name = "*" * num
        try:
            if not isinstance(name, str) or not name:
                return default_anonymized_name
            return "".join(
                random.choices(string.ascii_letters + string.digits, k=num)
            )
        except Exception as e:
            logger.error(f"Unexpected error during anonymizing name: {e}")
        finally:
            logger.debug("Finished anonymizing name")
