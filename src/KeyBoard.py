from src.item import Item
class KeyBoard(Item):
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
        self.__language = 'EN'

    @property
    def language(self) -> str:
        """
        Геттер для атрибута language. Возвращает текущий язык клавиатуры.
        """
        return self.__language

    def change_lang(self) -> 'Keyboard':
        """
        Метод для изменения языка клавиатуры.
        Меняет язык с EN на RU и наоборот.

        :return: Ссылка на текущий экземпляр клавиатуры.
        """
        if self.__language == 'EN':
            self.__language = 'RU'
        else:
            self.__language = 'EN'
        return self

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.name}', {self.price}, {self.quantity})"