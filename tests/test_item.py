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
