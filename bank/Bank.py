import logging.config

import definitions
from bank.Client import Client
from utils.decorators import log
from utils.helpers import object_lists_to_dict

logging.config.fileConfig(definitions.CONFIG_PATH)
logger = logging.getLogger("Bank")


class Bank:
    def __init__(self, clients):
        logger.debug("Starting Bank class initialization")
        try:
            Bank.clients_type_and_instances_validation(clients)

            dict_of_clients = object_lists_to_dict(
                clients,
                "id",
                validation=True,
                validation_mode=("datatype", "has_attribute"),
                reference=(Client, "id"),
            )

            self.clients = dict_of_clients
            logger.info("Successfully initialized Bank object")
        except (ValueError, TypeError, AttributeError) as e:
            logger.error(
                f"Unsuccessful initialization of Bank class. "
                f"{type(e).__name__}: {e}"
            )
            raise

    @log
    def add_client(self, client: Client):
        try:
            Bank.client_validation(client)

            self.clients[client.id] = client
            logger.info("Successfully added new client")
        except (TypeError, ValueError):
            logger.error("Adding client to Bank is not successful.")
            raise

    @log
    def remove_client(self, client_id: int):
        try:
            self._client_id_validation(client_id)

            del self.clients[client_id]
            logger.info("Successfully removed client")
        except (TypeError, ValueError, KeyError):
            logger.error("Removing client is not successful.")
            raise

    @log
    def get_client(self, client_id: int):
        try:
            self._client_id_validation(client_id)

            logger.info("Successfully returned client")
            return self.clients[client_id]
        except (TypeError, ValueError, KeyError):
            logger.error("Getting client is not successful")
            raise

    @log
    def get_balances(self):
        get_clients = list(self.clients.values())

        clients_balances = [client.balance for client in get_clients]
        if len(clients_balances) == 0:
            logger.warning("Bank does not have clients")

        logger.info("Successfully returned all balances from the bank")
        return clients_balances

    @staticmethod
    def clients_type_and_instances_validation(clients: list) -> bool:
        if clients is None:
            logger.error("Provided None value for clients")
            raise ValueError("Clients cannot be None")
        if not isinstance(clients, list):
            logger.error("Provided invalid datatype for clients")
            raise TypeError("Clients must be a list")
        if not clients:
            return True
        if not all(isinstance(client, Client) for client in clients):
            logger.error("Provided list contains invalid client instances")
            raise TypeError(
                "Values of the clients list have to be instances "
                "of Client class"
            )

        return True

    @staticmethod
    def client_validation(client: Client) -> bool:
        if not isinstance(client, Client):
            logger.error("Provided incorrect type of client")
            raise TypeError("Client has to be an instance of Client class")
        if not client:
            logger.error("Provided empty client")
            raise ValueError("Provided client cannot be empty")

        return True

    def _client_id_validation(self, client_id: int) -> bool:
        if not isinstance(client_id, int):
            logger.error("Provided invalid datatype of client_id")
            raise TypeError("Client id must be an integer")
        if client_id is None:
            logger.error("Provided None value for client_id")
            raise ValueError("Provided client id cannot be None")
        if client_id not in self.clients:
            logger.error(
                "Provided client id does not match any client in the Bank"
            )
            raise KeyError("Client with provided id does not exist")
        return True
