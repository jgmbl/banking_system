import logging.config

import definitions
from bank.Client import Client
from utils.decorators import log
from utils.helpers import object_lists_to_dict

logging.config.fileConfig(definitions.CONFIG_PATH)
logger = logging.getLogger("Bank")


class Bank:
    def __init__(self, clients):
        logger.debug("Starting client class initialization")

        if not isinstance(clients, list):
            logger.error("Provided clients must be a list")
            raise TypeError("Clients must be a list or Client class object")

        dict_of_clients = object_lists_to_dict(
            clients,
            "id",
            validation=True,
            validation_mode=("datatype", "has_attribute"),
            reference=(Client, "id"),
        )

        self.clients = dict_of_clients

        logger.info("Successfully initialized Bank object")

    @log
    def add_client(self, client: Client):
        if not client:
            logger.error("Provided None value or empty datatype for client")
            raise ValueError("Provided client object cannot be empty")
        if not isinstance(client, Client):
            logger.error("Provided invalid datatype")
            raise TypeError("Client must be an instance of Client class")

        self.clients[client.id] = client
        logger.info("Successfully added new client")

    @log
    def remove_client(self, client_id: int):
        if client_id is None:
            logger.error("Provided None value or empty datatype")
            raise ValueError("Provided client id cannot be empty")
        if not isinstance(client_id, int):
            logger.error("Provided invalid datatype")
            raise TypeError("Client id must be an integer")

        if client_id not in self.clients:
            logger.error("Client with provided id does not exist")
            raise KeyError(
                f'Client with provided id "{client_id}" does not exist'
            )

        logger.info("Successfully removed client")
        del self.clients[client_id]

    @log
    def get_client(self, client_id: int):
        if not client_id:
            logger.error("Provided None value or empty datatype")
            raise ValueError("Provided client id cannot be empty")

        if not isinstance(client_id, int):
            logger.error("Provided invalid datatype")
            raise TypeError("Client id must be an integer")

        if client_id not in self.clients.keys():
            logger.error("Client with provided id does not exist")
            raise KeyError(
                f'Client with provided id "{client_id}" does not exist'
            )

        return self.clients[client_id]

    @log
    def get_balances(self):
        get_clients = list(self.clients.values())

        clients_balances = [client.balance for client in get_clients]
        if len(clients_balances) == 0:
            logger.info("Bank does not have clients")

        return clients_balances
