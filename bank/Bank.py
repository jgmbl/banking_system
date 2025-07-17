import logging.config

from bank.Client import Client

logging.config.fileConfig("../logging.ini")
logger = logging.getLogger("Bank")


class Bank:
    def __init__(self, clients):
        logger.debug("Starting client class initialization")
        if isinstance(clients, Client):
            self.clients = list(clients)
        else:
            self.clients = clients

        logger.info("Successfully initialized Bank object")
