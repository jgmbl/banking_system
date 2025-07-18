from decimal import Decimal

import pytest

from bank.Bank import Bank
from bank.Client import Client

INIT_CLIENT = Client("John", Decimal("0.01"))

INIT_CLIENTS_LIST = [
    Client("Lisa", Decimal("0.02")),
    Client("Edward", Decimal("50.55")),
    Client("Elisabeth", Decimal("1000000.00")),
]

INIT_CLIENTS_DICT = {client.id: client for client in INIT_CLIENTS_LIST}

INIT_INVALID_CLIENTS = [None, "", True, []]


def test_init_bank():
    init_bank = Bank(INIT_CLIENTS_LIST.copy())

    assert isinstance(init_bank, Bank)
    assert init_bank.clients == INIT_CLIENTS_DICT


def test_add_client():
    init_bank = Bank(INIT_CLIENTS_LIST.copy())

    init_bank.add_client(INIT_CLIENT)

    assert INIT_CLIENT.id in init_bank.clients
    assert len(init_bank.clients) == len(INIT_CLIENTS_LIST) + 1


@pytest.mark.parametrize("invalid_client", INIT_INVALID_CLIENTS)
def test_add_invalid_clients(invalid_client):
    init_bank = Bank(INIT_CLIENTS_LIST)

    with pytest.raises((TypeError, ValueError)):
        init_bank.add_client(invalid_client)


def test_remove_client():
    init_bank = Bank(INIT_CLIENTS_LIST)

    removed_client_id = next(iter(init_bank.clients.keys()))

    init_bank.remove_client(removed_client_id)

    removed_clients_exists = any(
        client.id == removed_client_id for client in init_bank.clients.values()
    )

    assert len(init_bank.clients) != len(INIT_CLIENTS_LIST)
    assert not removed_clients_exists


def test_remove_non_existent_client():
    init_bank = Bank(INIT_CLIENTS_LIST)
    non_existent_client_id = -1

    with pytest.raises(KeyError):
        init_bank.remove_client(non_existent_client_id)


def test_get_client():
    init_bank = Bank(INIT_CLIENTS_LIST)

    get_client_id = next(iter(init_bank.clients))

    retrieved_client = init_bank.get_client(get_client_id)

    assert len(init_bank.clients) == len(INIT_CLIENTS_DICT)
    assert retrieved_client in init_bank.clients.values()


@pytest.mark.parametrize("client", INIT_CLIENTS_LIST)
def test_get_client_not_present(client):
    init_bank = Bank([client])

    init_non_existent_client_id = -1

    with pytest.raises(KeyError):
        init_bank.get_client(init_non_existent_client_id)


def test_get_clients_balances():
    init_bank = Bank(INIT_CLIENTS_LIST)

    clients_balances = init_bank.get_clients_balances()

    assert isinstance(clients_balances, list)
    assert all(
        isinstance(client_balance, Decimal)
        for client_balance in clients_balances
    )
    assert (
        sorted([client.balance for client in init_bank.clients.values()])
        == clients_balances
    )
