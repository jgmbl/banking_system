from decimal import Decimal

import pytest

from bank.Client import Client

init_name = "Anna"
init_balance = Decimal("1000.00")

init_valid_name_data = ["Adam", "John", "Lisa"]
init_invalid_name_data = ["", "     ", "!@#$%>", 0, None]

init_valid_monetary_data = [
    Decimal("0.00"),
    Decimal("10.00"),
]
init_invalid_monetary_data = [
    None,
    "Hello world!",
    Decimal("-0.01"),
    Decimal("12.345"),
]


@pytest.mark.parametrize("name", init_valid_name_data)
def test_valid_name_validation(name):
    assert Client.name_validation(name) is True


@pytest.mark.parametrize("name", init_invalid_name_data)
def test_invalid_name_validation(name):
    with pytest.raises(Exception):
        Client.name_validation(name)


@pytest.mark.parametrize("balance", init_valid_monetary_data)
def test_valid_balance_validation(balance):
    assert Client.monetary_value_validation(balance) is True


@pytest.mark.parametrize("balance", init_invalid_monetary_data)
def test_invalid_balance_validation(balance):
    with pytest.raises(Exception):
        Client.monetary_value_validation(balance)


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
    with pytest.raises(Exception):
        Client(name, balance)


@pytest.mark.parametrize("name", init_valid_name_data)
@pytest.mark.parametrize("balance", init_invalid_monetary_data)
def test_init_invalid_balance_client(name, balance):
    with pytest.raises(Exception):
        Client(name, balance)


@pytest.mark.parametrize("name", init_valid_name_data)
def test_anonymize_name(name):
    anonymized_name = Client.anonymize_name()

    assert isinstance(anonymized_name, str)
    assert anonymized_name != name


@pytest.mark.parametrize("amount", [Decimal("0.00"), Decimal("100.12")])
def test_valid_data_deposit(amount):
    client = Client(init_name, init_balance)

    client.deposit(amount)

    if amount == Decimal("0.00"):
        assert client.balance == init_balance

    assert client.balance == init_balance + amount


@pytest.mark.parametrize("amount", init_invalid_monetary_data)
def test_invalid_data_deposit(amount):
    client = Client(init_name, init_balance)
    with pytest.raises(Exception):
        client.deposit(amount)
