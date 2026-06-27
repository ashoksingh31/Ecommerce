from app.models import CartItem
from app.storage import cart


def add_item(product_id, name, price, quantity):

    # If product already exists, increase quantity
    for item in cart:
        if item.product_id == product_id:
            item.quantity += quantity
            return item

    new_item = CartItem(
        product_id=product_id,
        name=name,
        price=price,
        quantity=quantity
    )

    cart.append(new_item)

    return new_item


def get_cart():
    return cart


def clear_cart():
    cart.clear()


def calculate_subtotal():
    return sum(item.price * item.quantity for item in cart)