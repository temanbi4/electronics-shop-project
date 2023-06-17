from src.item import Item
import pytest


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