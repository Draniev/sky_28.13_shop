import pytest
from src.item import Item
from src.phone import Phone


@pytest.fixture
def phone_factory():
    return Phone('testphone', 10_000, 5, 2)


@pytest.fixture
def item_factory():
    return Item('testname', 10_000, 5)
