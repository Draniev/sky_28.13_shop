import pytest


def test_phone_repr(phone_factory):
    assert repr(phone_factory) == "Phone('testphone', 10000, 5, 2)"


def test_add_phone(phone_factory, item_factory):
    assert phone_factory + item_factory == 10
    
    with pytest.raises(ValueError):
        phone_factory + 10000

    with pytest.raises(ValueError):
        item_factory + 10
