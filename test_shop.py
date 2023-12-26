"""
Протестируйте классы из модуля homework/models.py
"""
import pytest

from models import Product, Cart


@pytest.fixture
def product():
    return Product("book", 100, "This is a book", 1000)


@pytest.fixture
def cart():
    return Cart()


class TestProducts:
    """
    Тестовый класс - это способ группировки ваших тестов по какой-то тематике
    Например, текущий класс группирует тесты на класс Product
    """

    def test_product_check_quantity(self, product):
        # TODO напишите проверки на метод check_quantity
        assert product.check_quantity(10)
        assert not product.check_quantity(1001)

    def test_product_buy(self, product):
        # TODO напишите проверки на метод buy
        product.buy(10)
        assert product.quantity == 990

    def test_product_buy_more_than_available(self, product):
        # TODO напишите проверки на метод buy,
        #  которые ожидают ошибку ValueError при попытке купить больше, чем есть в наличии
        with pytest.raises(ValueError):
            product.buy(1001)


class TestCart:
    """
    TODO Напишите тесты на методы класса Cart
        На каждый метод у вас должен получиться отдельный тест
        На некоторые методы у вас может быть несколько тестов.
        Например, негативные тесты, ожидающие ошибку (используйте pytest.raises, чтобы проверить это)
    """

    def test_add_product(self, cart, product):
        cart.add_product(product, 5)
        assert cart.products[product] == 5

    def test_remove_product(self, cart, product):
        cart.add_product(product, 20)
        cart.remove_product(product, 5)
        assert cart.products[product] == 15

    def test_remove_all_product(self, cart, product):
        cart.add_product(product, 150)
        cart.remove_product(product, 150)
        assert cart.products.get(product, 0) == 0

    def test_clear_cart(self, cart, product):
        cart.add_product(product)
        cart.clear()
        assert cart.products == {}

    def test_cart_buy_product(self, cart, product):
        cart.add_product(product, 25)
        cart.buy()
        assert product.quantity == 975

    def test_get_total_price(self, cart, product):
        cart.add_product(product, 15)
        assert cart.get_total_price() == 1500

    def test_error(self, cart, product):
        cart.add_product(product, 20000)
        with pytest.raises(ValueError):
            cart.buy()

    def test_cart_buy_more_than_available(self, cart, product):
        cart.add_product(product, 10001)
        with pytest.raises(ValueError):
            cart.buy()
