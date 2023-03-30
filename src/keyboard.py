from src.item import Item


class MixinLang:

    @property
    def language(self):
        """Возвращает язык клавиатуры"""
        return self.__language

    @language.setter
    def language(self, language):
        print("AttributeError: property 'language' of 'KeyBoard' object has no setter")

    def __init__(self):
        self.__language = 'EN'

    def change_lang(self):
        if self.__language == 'EN':
            self.__language = 'RU'
        else:
            self.__language = 'EN'
        return self


class Keyboard(Item, MixinLang):
    """Класс `Keyboard` для товара 'клавиатура'.
    В отличие от других товаров у него есть атрибут `language` и метод для изменения языка (раскладки клавиатуры),
    реализованные через класс MixinLang.
    """

    pass

# нужен геттер language
# Изменить язык можно только методом `change_lang()`.
#  assert str(kb.language) == "EN"
#
#     kb.change_lang()
#     assert str(kb.language) == "RU"
#
#
#
#
#
#
#
