import logging.config

from bank.Client import Client
from utils.decorators import log

logging.config.fileConfig("../logging.ini")
logger = logging.getLogger("Bank")


class Bank:
    def __init__(self, clients):
        logger.debug("Starting client class initialization")
        if not isinstance(clients, Client) and not isinstance(clients, list):
            logger.error(
                f'Provided type of clients "{type(clients)}" have '
                f"not valid type"
            )
            raise TypeError("Provided clients have not valid type")
        elif not clients:
            logger.error("Provided no value for client parameter")
            raise ValueError("Clients are not provided")

        self.clients = self._clients_list_to_dict(clients)

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
        if not client_id:
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
    def get_clients_balances(self):
        get_clients = list(self.clients.values())

        clients_balances = []

        for client in get_clients:
            clients_balances.append(client.balance)

        return clients_balances

    @log
    def _clients_list_to_dict(self, clients_list):
        clients_dict = dict()
        for client in clients_list:
            clients_dict[client.id] = client

        return clients_dict
