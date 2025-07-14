from decimal import Decimal

import pytest

from bank.Client import Client

init_valid_name_data = ["Adam", "John", "Lisa"]
init_invalid_name_data = ["", "     ", "!@#$%>", 0]

init_valid_balance_data = [
    Decimal("0.00"),
    Decimal("10.00"),
    Decimal("100.00"),
]
init_invalid_balance_data = [None, "Hello world!", Decimal("-0.01")]


@pytest.mark.parametrize("name", init_valid_name_data)
@pytest.mark.parametrize("balance", init_valid_balance_data)
def test_init_valid_balance_validation(name, balance):
    client = Client(name, balance)

    assert client.balance == balance


@pytest.mark.parametrize("name", init_valid_name_data)
@pytest.mark.parametrize("balance", init_invalid_balance_data)
def test_init_invalid_balance_validation(name, balance):
    if not isinstance(balance, Decimal):
        with pytest.raises(TypeError):
            Client(name, balance)
    elif balance < Decimal("0.00"):
        with pytest.raises(ValueError):
            Client(name, balance)


@pytest.mark.parametrize("name", init_invalid_name_data)
@pytest.mark.parametrize("balance", init_valid_balance_data)
def test_init_invalid_name_validation(name, balance):
    if not isinstance(name, str):
        with pytest.raises(TypeError):
            Client(name, balance)
    elif not name.isalpha():
        with pytest.raises(ValueError):
            Client(name, balance)


@pytest.mark.parametrize("name", init_valid_name_data)
@pytest.mark.parametrize("balance", init_valid_balance_data)
def test_depositing(name, balance):
    client = Client(name, balance)

    deposit = client.depositing(Decimal("50.00"))

    assert client.balance == balance + deposit
