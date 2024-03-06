"""Здесь надо написать тесты с использованием pytest для модуля item."""
from src.item import Item
import pytest


@pytest.fixture
def class_fixture():
    return Item(name='Ноутбук', price=10000, quantity=1000)


@pytest.fixture
def new_fixture():
    value = Item(name='Смартфон', price=10000, quantity=10)
    value.name = 'СуперСмартфон'
    return value


def test_item(class_fixture):
    assert class_fixture.name == 'Ноутбук'
    assert class_fixture.calculate_total_price() == 10000000
    assert class_fixture.all[0] == class_fixture


def test_new_methods(new_fixture):
    assert len(new_fixture.name) == 10
    assert new_fixture.name == 'СуперСмарт'
    assert new_fixture.string_to_number('5') == 5
