import pytest
from products import Product


def test_create_normal_product():
    product = Product("MacBook Air M2", price=1450, quantity=100)
    assert product.name == "MacBook Air M2"
    assert product.price == 1450
    assert product.quantity == 100
    assert product.is_active()


def test_create_product_with_invalid_details():
    with pytest.raises(ValueError, match="Name cannot be empty."):
        Product("", price=1450, quantity=100)

    with pytest.raises(ValueError, match="Price cannot be negative."):
        Product("MacBook Air M2", price=-10, quantity=100)


def test_product_quantity_becomes_inactive():
    product = Product("MacBook Air M2", price=1450, quantity=1)
    assert product.is_active()
    product.buy(1)
    assert not product.is_active()


def test_product_purchase_modifies_quantity_and_returns_right_output():
    product = Product("MacBook Air M2", price=1450, quantity=100)
    total_price = product.buy(5)
    assert product.quantity == 95
    assert total_price == 1450 * 5


def test_buying_larger_quantity_than_exists_invokes_exception():
    product = Product("MacBook Air M2", price=1450, quantity=100)
    with pytest.raises(ValueError, match="Insufficient quantity available."):
        product.buy(150)
