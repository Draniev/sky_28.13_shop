from src.item import Item


class LanguageMixin():
    def __init__(self) -> None:
        self.__language = 'EN'

    @property
    def language(self):
        return self.__language

    def change_lang(self):
        if self.__language == 'EN':
            self.__language = 'RU'
        else:
            self.__language = 'EN'


class Keyboard(Item, LanguageMixin):
    pass
