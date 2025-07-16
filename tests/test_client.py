from decimal import Decimal

import pytest

from bank.Client import Client

init_name = "Anna"
init_balance = Decimal("10.11")

init_valid_name_data = ["Adam", "John", "Lisa"]
init_invalid_name_data = ["", "     ", "!@#$%>", 0, None]

init_valid_monetary_data = [
    Decimal("0.00"),
    Decimal("10.00"),
    Decimal("100.00"),
]
init_invalid_monetary_data = [None, "Hello world!", Decimal("-0.01")]


@pytest.mark.parametrize("name", init_valid_name_data)
def test_valid_name_validation(name):
    assert Client.name_validation(name) is True


@pytest.mark.parametrize("name", init_invalid_name_data)
def test_invalid_name_validation(name):
    assert Client.name_validation(name) is False


@pytest.mark.parametrize("balance", init_valid_monetary_data)
def test_valid_balance_validation(balance):
    assert Client.monetary_values_validation(balance) is True


@pytest.mark.parametrize("balance", init_invalid_monetary_data)
def test_invalid_balance_validation(balance):
    assert Client.monetary_values_validation(balance) is False


@pytest.mark.parametrize("name", init_valid_name_data)
@pytest.mark.parametrize("balance", init_valid_monetary_data)
def test_init_valid_client(name, balance):
    client = Client(name, balance)

    assert isinstance(client, Client)
    assert client.name == name
    assert client.balance == balance


@pytest.mark.parametrize("name", init_invalid_name_data)
@pytest.mark.parametrize("balance", init_valid_monetary_data)
def test_init_invalid_name_client(name, balance):
    with pytest.raises(ValueError):
        Client(name, balance)


@pytest.mark.parametrize("name", init_valid_name_data)
@pytest.mark.parametrize("balance", init_invalid_monetary_data)
def test_init_invalid_balance_client(name, balance):
    with pytest.raises(ValueError):
        Client(name, balance)


@pytest.mark.parametrize("name", init_valid_name_data)
def test_anonymize_name(name):
    anonymized_name = Client.anonymize_name()

    assert isinstance(anonymized_name, str)
    assert anonymized_name != name


@pytest.mark.parametrize("deposit", init_valid_monetary_data)
def test_valid_data_epositing(deposit):
    client = Client(init_name, init_balance)

    result = client.depositing(deposit)

    assert client.balance == init_balance + deposit
    assert result == deposit


@pytest.mark.parametrize("deposit", init_invalid_monetary_data)
def test_invalid_data_depositing(deposit):
    client = Client(init_name, init_balance)

    with pytest.raises(ValueError):
        client.depositing(deposit)
