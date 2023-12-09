"""Здесь надо написать тесты с использованием pytest для модуля item."""
import pytest

from src.item import Item


@pytest.fixture
def item_factory():
    return Item('testname', 10_000, 5)


def test_all_len(item_factory):
    assert len(Item.all) == 1


def test_total_price(item_factory):
    assert item_factory.calculate_total_price() == 50_000


def test_payrate(item_factory):
    Item.pay_rate = 0.5
    item_factory.apply_discount()
    assert item_factory.price == 5_000


def test_string_to_number(item_factory):
    assert Item.string_to_number('10.0') == 10
    assert item_factory.string_to_number('20') == 20


def test_name_setter(item_factory):
    item_factory.name = 'shortname'
    assert item_factory.name == 'shortname'
    item_factory.name = 'verylongname'
    assert item_factory.name == 'verylongn'
