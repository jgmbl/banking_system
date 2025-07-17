import logging.config

from bank.Client import Client

logging.config.fileConfig("../logging.ini")
logger = logging.getLogger("Bank")


class Bank:
    def __init__(self, clients):
        logger.debug("Starting client class initialization")
        if isinstance(clients, Client):
            self.clients = list(clients)

        self.clients = clients

        logger.info("Successfully initialized Bank object")

    def add_client(self, client: Client):
        logger.debug("Initialized adding client process")
        if not client:
            logger.error("Provided None value or empty datatype")
            raise ValueError("Provided client object cannot be empty")
        if not isinstance(client, Client):
            logger.error("Provided invalid datatype")
            raise TypeError("Client must be an instance of Client class")

        self.clients.append(client)
