import pytest
from src.domain.Money import Money


def test_should_create_money_instance():
    money = Money(100)
    assert money.value == 100


def test_should_not_create_negative_money():
    with pytest.raises(Exception, match="Invalid amount"):
        Money(-1)