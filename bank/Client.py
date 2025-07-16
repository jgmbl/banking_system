import logging.config
import random
import string
from decimal import Decimal

logging.config.fileConfig("../logging.ini")
logger = logging.getLogger("Client")


class Client:
    def __init__(self, name, balance):
        logger.debug("Starting Client class initialization")
        if not Client.validate_name(name):
            logger.error("Invalid name provided to the constructor")
            raise ValueError("Invalid name")

        if not Client.validate_monetary_values(balance):
            logger.error("Invalid balance provided to the constructor")
            raise ValueError("Invalid balance")

        self.name = name
        self.balance = balance
        self.anonymized_name = Client.anonymized_name()
        self.anonymized_monetary_value = "***"

        logger.info(
            f"Successfully initialized Client class for name "
            f"{self.anonymized_name} and balance {self.anonymized_monetary_value}"
        )

    def depositing(self, deposit):
        if not Client.validate_monetary_values(deposit):
            logger.error("Invalid amount of deposit")
            raise ValueError("Provided invalid deposit")
        self.balance += deposit
        logger.info(f"Deposited {self.anonymized_monetary_value} to balance")
        return deposit

    @staticmethod
    def validate_name(name):
        logger.debug("Starting name validation")
        validation_result = False
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
            validation_result = True
            return True
        except Exception as e:
            logger.error(f"Unexpected error during name validation: {e}")
        finally:
            logger.debug(
                f"Finished name validation with result: {validation_result}"
            )

    @staticmethod
    def validate_monetary_values(monetary_value):
        logger.debug("Starting monetary values validation")
        validation_result = False
        try:
            if not isinstance(monetary_value, Decimal):
                logger.error(
                    "The provided monetary value is not in a valid currency format"
                )
                return False
            elif monetary_value < Decimal("0.00"):
                logger.error("Monetary value cannot be less than 0.00")
                return False
            logger.debug("Provided monetary value passed validation")
            validation_result = True
            return True
        except Exception as e:
            logger.error(
                f"Unexpected error during monetary values validation: {e}"
            )
        finally:
            logger.debug(
                f"Finished monetary values validation with result: {validation_result}"
            )

    @staticmethod
    def anonymized_name():
        logger.debug("Starting anonymizing name")
        anonymizing_result = False
        try:
            logger.debug("Starting anonymizing name")
            result = "".join(
                random.choices(string.ascii_letters + string.digits, k=15)
            )
            logger.debug(f"Anonymizing name ended with result: {result}")
            anonymizing_result = True
            return result
        except Exception as e:
            logger.error(f"Unexpected error during anonymizing name: {e}")
        finally:
            logger.debug(
                f"Finished anonymizing name with result: {anonymizing_result}"
            )
