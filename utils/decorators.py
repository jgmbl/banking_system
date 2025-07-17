import logging.config
from functools import wraps

logging.config.fileConfig("../logging.ini")


def log(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        logger_name = func.__module__
        logger = logging.getLogger(str(logger_name).split(".")[-1])
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
