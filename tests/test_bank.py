from decimal import Decimal

import pytest

from bank.Bank import Bank
from bank.Client import Client

INIT_CLIENT = Client("John", "0.01")

INIT_CLIENTS = [
    Client("Lisa", Decimal("0.02")),
    Client("Edward", Decimal("50.55")),
    Client("Elisabeth", Decimal("1000000.00")),
]

INIT_IVALID_CLIENTS = [None, "", True, 0, []]


def test_init_bank():
    bank = Bank(INIT_CLIENTS)

    if len(bank.clients) == 1:
        assert bank.clients == INIT_CLIENTS

    bank.clients.sort(key=lambda n: n.name)
    INIT_CLIENTS.sort(key=lambda n: n.name)

    assert isinstance(bank, Bank)
    assert bank.clients == INIT_CLIENTS


def test_init_bank_no_clients():
    clients = []

    bank = Bank(clients)

    assert not bank.clients
    assert bank.clients == clients


def test_add_client():
    bank = Bank(INIT_CLIENTS)

    bank.add_client(INIT_CLIENT)

    assert bank.clients
    assert len(bank.clients) == len(INIT_CLIENTS) + 1


@pytest.mark.parametrize("client", INIT_IVALID_CLIENTS)
def test_add_empty_client(client):
    bank = Bank(INIT_CLIENTS)

    with pytest.raises(TypeError):
        bank.add_client(client)
