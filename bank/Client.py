import logging.config
import random
import string
from decimal import Decimal
from functools import wraps

logging.config.fileConfig("../logging.ini")
logger = logging.getLogger("Client")


def log(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        logger.debug(f"Starting {func.__name__.replace('_', ' ')}")
        try:
            result = func(*args, **kwargs)
            return result
        except Exception as e:
            logger.error(
                f"Exception raised in {func.__name__}. Exception: {str(e)}"
            )
            raise e
        finally:
            logger.debug(f"Finished {func.__name__.replace('_', ' ')}")

    return wrapper


class Client:
    def __init__(self, name, balance):
        logger.debug("Starting Client class initialization")
        if not self.name_validation(name):
            logger.error(
                "Provided name is not a string or does not have valid format"
            )
            raise ValueError("Invalid name")

        if not self.monetary_value_validation(balance):
            logger.error(
                "Provided name does not have valid monetary data type or does not have valid format"
            )
            raise ValueError("Invalid balance")

        self.name = name
        self.balance = balance
        self.anonymized_name = self.anonymize_name()
        self.anonymized_monetary_value = "***"

        logger.info(
            f"Successfully initialized Client class for name "
            f"{self.anonymized_name} and balance "
            f"{self.anonymized_monetary_value}"
        )

    def deposit(self, amount):
        logger.debug("Initialized deposit process")
        if not Client.monetary_value_validation(amount):
            raise ValueError("Invalid monetary format of amount")

        if amount == Decimal("0.00"):
            logger.info("Skipped depositing due to amount equal 0.00")
            return

        self.balance += amount
        logger.info(f"Deposited {self.anonymized_monetary_value}")

    @staticmethod
    @log
    def name_validation(name):
        if not isinstance(name, str):
            logger.error("Provided name value is not a string")
            raise TypeError(
                "Provided name does not match the correct data type"
            )
        if not name:
            logger.error("Provided name value cannot be empty or None")
            raise ValueError("Name cannot be empty or contain spaces")
        elif not name.isalpha():
            logger.error("Provided name must contain only letters")
            raise ValueError("Provided name must contain only letters")
        return True

    @staticmethod
    @log
    def monetary_value_validation(monetary_value):
        if not isinstance(monetary_value, Decimal):
            logger.error(
                "The provided monetary value is not in a valid currency format"
            )
            raise TypeError(
                "Provided balance does not match the correct data type"
            )
        elif Client.monetary_decimal_places_validator(monetary_value) > 2:
            logger.error("Decimal places must be equal 2")
            raise ValueError("Balance must have 2 decimal places")
        elif monetary_value < Decimal("0.00"):
            logger.error("Monetary value cannot be less than 0.00")
            raise ValueError("Balance must not have negative value")
        return True

    @staticmethod
    @log
    def anonymize_name():
        result = "".join(
            random.choices(string.ascii_letters + string.digits, k=15)
        )
        return result

    @staticmethod
    def monetary_decimal_places_validator(monetary_value: Decimal) -> int:
        return len(str(monetary_value).split(".")[-1])
