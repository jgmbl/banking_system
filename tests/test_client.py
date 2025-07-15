from decimal import Decimal

import pytest

from bank.Client import Client

init_valid_name_data = ["Adam", "John", "Lisa"]
init_invalid_name_data = ["", "     ", "!@#$%>", 0, None]

init_valid_balance_data = [
    Decimal("0.00"),
    Decimal("10.00"),
    Decimal("100.00"),
]
init_invalid_balance_data = [None, "Hello world!", Decimal("-0.01")]


@pytest.mark.parametrize("name", init_valid_name_data)
def test_valid_name_validation(name):
    assert Client.validate_name(name) is True


@pytest.mark.parametrize("name", init_invalid_name_data)
def test_invalid_name_validation(name):
    assert Client.validate_name(name) is False


@pytest.mark.parametrize("balance", init_valid_balance_data)
def test_valid_balance_validation(balance):
    assert Client.validate_balance(balance) is True


@pytest.mark.parametrize("balance", init_invalid_balance_data)
def test_invalid_balance_validation(balance):
    assert Client.validate_balance(balance) is False


@pytest.mark.parametrize("name", init_valid_name_data)
@pytest.mark.parametrize("balance", init_valid_balance_data)
def test_init_valid_client(name, balance):
    client = Client(name, balance)

    assert isinstance(client, Client)
    assert client.name == name
    assert client.balance == balance


@pytest.mark.parametrize("name", init_invalid_name_data)
@pytest.mark.parametrize("balance", init_valid_balance_data)
def test_init_invalid_name_client(name, balance):
    with pytest.raises(ValueError):
        Client(name, balance)


@pytest.mark.parametrize("name", init_valid_name_data)
@pytest.mark.parametrize("balance", init_invalid_balance_data)
def test_init_invalid_balance_client(name, balance):
    with pytest.raises(ValueError):
        Client(name, balance)


@pytest.mark.parametrize("name", init_valid_name_data)
@pytest.mark.parametrize("balance", init_valid_balance_data)
def test_depositing(name, balance):
    client = Client(name, balance)

    deposit = client.depositing(Decimal("50.00"))

    assert client.balance == balance + deposit


@pytest.mark.parametrize("name", init_valid_name_data)
def test_anonymize_name(name):
    anonymized_name = Client.anonymized_name()

    assert isinstance(anonymized_name, str)
    assert anonymized_name != name
