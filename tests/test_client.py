from decimal import Decimal

import pytest

from bank import Client

@pytest.mark.parametrize(
    "name, balance",
    [
        ("John", Decimal("-1.00")),
        ("Peter", Decimal("0.00")),
        ("Lisa", Decimal("100.00"))
    ]
)

def test_depositing():
    # Arrange
    client = Client(name=name, balance=balance)

    # Act
    deposit = client.depositing(Decimal("50.00"))

    # Assert
    assert client.balance == balance + deposit