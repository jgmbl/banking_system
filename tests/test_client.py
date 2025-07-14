from decimal import Decimal

import pytest

from bank.Client import Client

init_valid_name_data = ["Adam",  "John", "Lisa"]
init_invalid_name_data = ["", "     ", "!@#$%>"]

init_valid_balance_data = [Decimal("0.00"), Decimal("10.00"), Decimal("100.00")]
init_invalid_balance_data = [Decimal("-0.01"), Decimal("-10.00"), Decimal("-100.00")]

@pytest.mark.parametrize("name", "balance", init_valid_name_data, init_valid_balance_data)
def test_init_valid_balance_validation(name, balance):
    # Arrange
    client = Client(name, balance)

    # Assert
    assert client.balance == balance

@pytest.mark.parametrize("name", "balance", init_valid_name_data, init_invalid_balance_data)
def test_init_invalid_balance_validation(name, balance):
    if balance < 0:
        with pytest.raises(ValueError):
            Client(name, balance)

@pytest.mark.parametrize("name", "balance", init_invalid_name_data, init_valid_balance_data)
def test_init_invalid_name_validation(name, balance):
    if not all(c.isalpha() for c in name):
        with pytest.raises(ValueError):
            Client(name, balance)

@pytest.mark.parametrize("name", "balance", init_valid_name_data, init_valid_balance_data)
def test_depositing(name, balance):
    # Arrange
    client = Client(name, balance)

    # Act
    deposit = client.depositing(Decimal("50.00"))

    # Assert
    assert client.balance == balance + deposit
