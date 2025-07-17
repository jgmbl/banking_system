from decimal import Decimal

import pytest

from bank.Bank import Bank
from bank.Client import Client

INIT_CLIENTS = [
    [Client("Anna", Decimal("0.00")), Client("John", Decimal("1000.00"))],
    [Client("Robert", Decimal("12.12"))],
]


@pytest.mark.parametrize("clients", INIT_CLIENTS)
def test_init_bank(clients):
    bank = Bank(clients)

    if len(bank.clients) == 1:
        assert bank.clients == clients

    bank.clients.sort(key=lambda n: n.name)
    clients.sort(key=lambda n: n.name)

    assert isinstance(bank, Bank)
    assert bank.clients == clients


def test_init_bank_no_clients():
    clients = []

    bank = Bank(clients)

    assert not bank.clients
    assert bank.clients == clients
