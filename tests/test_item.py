import pytest
from src.item import Item
"""Здесь надо написать тесты с использованием pytest для модуля item."""


@pytest.fixture
def test_item():
    return Item("Ноутбук", 20000, 5)


def test_init(test_item):
    assert test_item.name == "Ноутбук"
    assert test_item.price == 20000
    assert test_item.quantity == 5


def test_calculate_total_price(test_item):
    assert test_item.calculate_total_price() == 100000


def test_apply_discount(test_item):
    test_item.apply_discount()
    assert test_item.price == 20000
    test_item.pay_rate = 0.8
    test_item.apply_discount()
    assert test_item.price == 16000.0
