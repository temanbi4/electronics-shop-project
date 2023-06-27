from src.item import Item


class KeyBoardMixin:
    """
    Класс-миксин для хранения и изменения раскладки клавиатуры.
    """

    def __init__(self):
        self._language = 'EN'

    @property
    def language(self):
        """
        Возвращает текущий язык клавиатуры.
        """
        return self._language

    def change_lang(self):
        """
        Метод для изменения языка клавиатуры.
        Меняет язык с EN на RU и наоборот.

        :return: Ссылка на текущий экземпляр клавиатуры.
        """
        if self._language == 'EN':
            self._language = 'RU'
        else:
            self._language = 'EN'
        return self._language


class Keyboard(Item, KeyBoardMixin):
    """
    Класс для товара "клавиатура".
    """

    def __init__(self, name: str, price: float, quantity: int):
        """
        Создание экземпляра класса Keyboard.

        :param name: Название клавиатуры.
        :param price: Цена за единицу клавиатуры.
        :param quantity: Количество клавиатур в магазине.
        """
        super().__init__(name, price, quantity)
        self._language = 'EN'
    def __repr__(self):
        return f"{self.__class__.__name__}('{self.name}', {self.price}, {self.quantity})"

