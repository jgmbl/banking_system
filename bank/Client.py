import logging.config
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
                "Provided name does not have valid monetary data type or "
                "does not have valid format"
            )
            raise ValueError("Invalid balance")
        Client.standardize_decimal_places(balance)

        self.name = name
        self.balance = balance

        logger.info("Successfully initialized Client class")

    def deposit(self, amount):
        logger.debug("Initialized deposit process")
        if not Client.monetary_value_validation(amount):
            raise ValueError("Invalid monetary format of amount")

        if amount == Decimal("0.00"):
            logger.info("Skipped depositing due to amount equal 0.00")
            return

        Client.standardize_decimal_places(amount)
        self.balance += amount
        logger.info("Successfully deposited money to balance")

    def withdraw(self, amount):
        logger.debug("Initialized withdraw process")
        if not Client.monetary_value_validation(amount):
            raise ValueError("Invalid monetary format of amount")

        if amount == Decimal("0.00"):
            logger.info("Skipped withdrawing due to amount equal 0.00")
            return
        elif amount > self.balance:
            logger.error("Provided amount is greater than balance")
            raise ValueError(
                "Amount if withdrawing cannot be greater than balance"
            )

        Client.standardize_decimal_places(amount)
        self.balance -= amount
        logger.info("Successfully withdrew money from balance")

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
    def monetary_decimal_places_validator(monetary_value: Decimal) -> int:
        return len(str(monetary_value).split(".")[-1])

    @staticmethod
    def standardize_decimal_places(num: Decimal) -> Decimal:
        return num.quantize(Decimal("0.00"))
