import pytest

from src.keyboard import Keyboard


@pytest.fixture
def keyboard_factory():
    return Keyboard('testname', 10_000, 5)


def test_keyboard_language(keyboard_factory):
    assert keyboard_factory.language == 'EN'
    keyboard_factory.change_lang()
    assert keyboard_factory.language == 'RU'
