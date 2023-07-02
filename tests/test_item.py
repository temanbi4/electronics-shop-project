from src.item import Item
from src.phone import Phone
from src.KeyBoard import Keyboard
import pytest
import os
from src.item import Item, InstantiateCSVError, TypeErrorCsvZero


def test_repr():
    item1 = Item("Смартфон", 10000, 20)
    assert repr(item1) == "Item('Смартфон', 10000, 20)"

def test_str():
    item1 = Item("Смартфон", 10000, 20)
    assert str(item1) == 'Смартфон'


def test_calculate_total_price():
    item1 = Item("Смартфон", 10000, 20)
    item2 = Item("Ноутбук", 20000, 5)

    assert item1.calculate_total_price() == 200000
    assert item2.calculate_total_price() == 100000


def test_apply_discount():
    item1 = Item("Смартфон", 10000, 20)
    item2 = Item("Ноутбук", 20000, 5)

    Item.pay_rate = 0.8

    item1.apply_discount()
    item2.apply_discount()

    assert item1.price == 8000.0
    assert item2.price == 16000.0


def test_instances():
    item1 = Item("Смартфон", 10000, 20)
    item2 = Item("Ноутбук", 20000, 5)

    assert item1 in Item.all
    assert item2 in Item.all


@pytest.fixture
def items_fixture():
    Item.instantiate_from_csv()

def test_instantiate_from_csv(items_fixture):
    # Проверяем, что список экземпляров класса Item заполнился из файла CSV
    assert len(Item.all) == 5

    # Проверяем значения первого элемента в списке
    item1 = Item.all[0]
    assert item1.name == 'Смартфон'
    assert item1.price == 100
    assert item1.quantity == 1

    # Проверяем значения последнего элемента в списке
    item5 = Item.all[-1]
    assert item5.name == 'Клавиатура'
    assert item5.price == 75
    assert item5.quantity == 5

def test_string_to_number():
    # Проверяем преобразование строки в целое число
    assert Item.string_to_number('5') == 5

    # Проверяем преобразование строки с десятичной точкой в целое число
    assert Item.string_to_number('5.0') == 5

    # Проверяем преобразование строки с десятичной точкой и десятичной частью в целое число
    assert Item.string_to_number('5.5') == 5

def test_phone_init():
    phone = Phone('iPhone 17', 123.99, 10, 7)
    assert phone.name == 'iPhone 17'
    assert phone.price == 123.99
    assert phone.quantity == 10
    assert phone.number_of_sim == 7

def test_phone_number_of_sim_setter():
    phone = Phone('iPhone SE', 499.99, 3, 1)
    phone.number_of_sim = 2
    assert phone.number_of_sim == 2

def test_phone_number_of_sim_setter_invalid():
    phone = Phone('Google Pixel 4a', 399.99, 2, 1)
    with pytest.raises(ValueError):
        phone.number_of_sim = 1.5

def test_phone_number_of_sim_setter_zero():
    phone = Phone('OnePlus 8T', 599.99, 4, 2)
    with pytest.raises(ValueError):
        phone.number_of_sim = 0

def test_keyboard_initial_language():
    kb = Keyboard('Blazing Pro RGB', 9600, 5)
    assert kb.language == 'EN'

def test_keyboard_change_language():
    kb = Keyboard('Blazing Pro RGB', 9600, 5)
    kb.change_lang()
    assert kb.language == 'RU'

    kb.change_lang()
    assert kb.language == 'EN'

def test_keyboard_change_language_chain():
    kb = Keyboard('Blazing Pro RGB', 9600, 5)
    kb.change_lang()
    assert kb.language == 'RU'

def test_keyboard_invalid_language():
    kb = Keyboard('Blazing Pro RGB', 9600, 5)
    with pytest.raises(AttributeError):
        kb.language = 'CH'

def test_instantiate_from_csv_exception_FileNotFoundError():
    Item.file_name = 'test'

    with pytest.raises(FileNotFoundError):
        Item.instantiate_from_csv()


def test_instantiate_from_csv_empty_file():
    with pytest.raises(TypeErrorCsvZero):
        Item.file_name = '../tests/test_empty_items.csv'
        Item.instantiate_from_csv()


def test_instantiate_from_csv_bad_file():
    with pytest.raises(InstantiateCSVError):
        Item.file_name = "../tests/test_bad_items.csv"
        Item.instantiate_from_csv()
