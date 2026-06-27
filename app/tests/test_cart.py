from app.services.cart_service import (
    add_item,
    calculate_subtotal,
)
from app.storage import cart


def setup_function():
    cart.clear()


def test_add_item():

    add_item(
        1,
        "Keyboard",
        1000,
        2,
    )

    assert len(cart) == 1


def test_subtotal():

    add_item(
        1,
        "Keyboard",
        1000,
        2,
    )

    assert calculate_subtotal() == 2000