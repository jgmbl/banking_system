from decimal import Decimal

import pytest

import bank
from bank.Bank import Bank
from bank.Client import Client

INIT_CLIENT = Client("John", Decimal("0.01"))

INIT_CLIENTS_LIST = [
    Client("Lisa", Decimal("0.02")),
    Client("Edward", Decimal("50.55")),
    Client("Elisabeth", Decimal("1000000.00")),
]

INIT_CLIENTS_DICT = {client.id: client for client in INIT_CLIENTS_LIST}

INIT_INVALID_CLIENTS = [None, "", True, 0, []]


def test_init_bank():
    init_bank = Bank(INIT_CLIENTS_LIST.copy())

    assert isinstance(init_bank, Bank)
    assert init_bank.clients == INIT_CLIENTS_DICT


def test_init_bank_no_clients():
    clients = []

    init_bank = Bank(clients)

    assert not init_bank.clients
    assert init_bank.clients == clients


def test_add_client():
    init_bank = Bank(INIT_CLIENTS_LIST.copy())

    init_bank.add_client(INIT_CLIENT)

    assert INIT_CLIENT.id in init_bank.clients
    assert len(init_bank.clients) == len(INIT_CLIENTS_LIST) + 1


@pytest.mark.parametrize("client", INIT_INVALID_CLIENTS)
def test_add_empty_client(client):
    init_bank = Bank(INIT_CLIENTS_LIST)

    with pytest.raises((TypeError, ValueError)):
        init_bank.add_client(client)


def test_remove_client():
    initial_clients = INIT_CLIENTS_LIST.copy()
    init_bank = Bank(initial_clients)

    removed_client_id = next(iter(init_bank.clients))

    bank.remove_client(removed_client_id)

    removed_clients_exits = [
        client.id == removed_client_id for client in init_bank.clients
    ]

    assert len(bank.clients) != len(initial_clients)
    assert not removed_clients_exits


def test_remove_non_existent_client():
    init_bank = Bank([])

    with pytest.raises(ValueError):
        init_bank.remove_client(INIT_CLIENT.id)
