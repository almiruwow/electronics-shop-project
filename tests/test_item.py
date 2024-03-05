"""Здесь надо написать тесты с использованием pytest для модуля item."""
from src.item import Item
import pytest


@pytest.fixture
def class_fixture():
    return Item(name='Ноутбук', price=10000, quantity=1000)


def test_item(class_fixture):
    assert class_fixture.name == 'Ноутбук'
    assert class_fixture.calculate_total_price() == 10000000
    assert class_fixture.all[0] == class_fixture
