from decimal import Decimal

import pytest

from bank.Client import Client


@pytest.mark.parametrize(
    "name, balance",
    [
        ("John", Decimal("-1.00")),
        ("Peter", Decimal("0.00")),
        ("Lisa", Decimal("100.00"))
    ]
)
def test_depositing(name, balance):
    if balance < 0:
        with pytest.raises(ValueError):
            Client(name, balance)
    else:
        # Arrange
        client = Client(name, balance)

        # Act
        deposit = client.depositing(Decimal("50.00"))

        # Assert
        assert client.balance == balance + deposit
