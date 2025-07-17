from decimal import Decimal

import pytest

from bank.Bank import Bank
from bank.Client import Client

INIT_CLIENT = Client("John", Decimal("0.01"))

INIT_CLIENTS = [
    Client("Lisa", Decimal("0.02")),
    Client("Edward", Decimal("50.55")),
    Client("Elisabeth", Decimal("1000000.00")),
]

INIT_INVALID_CLIENTS = [None, "", True, 0, []]


def test_init_bank():
    bank = Bank(INIT_CLIENTS)

    expected_clients = sorted(INIT_CLIENTS.copy(), key=lambda n: n.name)
    actual_clients = sorted(bank.clients, key=lambda n: n.name)

    assert isinstance(bank, Bank)
    assert actual_clients == expected_clients


def test_init_bank_no_clients():
    clients = []

    bank = Bank(clients)

    assert not bank.clients
    assert bank.clients == clients


def test_add_client():
    bank = Bank(INIT_CLIENTS.copy())

    bank.add_client(INIT_CLIENT)

    assert INIT_CLIENT in bank.clients
    assert len(bank.clients) == len(INIT_CLIENTS) + 1


@pytest.mark.parametrize("client", INIT_INVALID_CLIENTS)
def test_add_empty_client(client):
    bank = Bank(INIT_CLIENTS)

    with pytest.raises((TypeError, ValueError)):
        bank.add_client(client)


def test_remove_client():
    initial_clients = INIT_CLIENTS.copy()
    bank = Bank(initial_clients)

    clients_id_list = []
    for client in bank.clients:
        clients_id_list.append(client.id)

    client_id_list_expected = clients_id_list.copy()
    client_id_removed = client_id_list_expected[1]

    removed_client_exists = any(
        client.id == client_id_removed for client in bank.clients
    )

    bank.remove_client(client_id_removed)

    assert len(bank.clients) != len(initial_clients)
    assert not removed_client_exists


def test_remove_non_existent_client():
    bank = Bank([])

    with pytest.raises(ValueError):
        bank.remove_client(10)
