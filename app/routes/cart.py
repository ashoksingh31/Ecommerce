from fastapi import APIRouter

from app.schemas import AddItemRequest
from app.services.cart_service import (
    add_item,
    get_cart,
    calculate_subtotal,
)

router = APIRouter()


@router.post("/items")
def add_item_to_cart(item: AddItemRequest):

    cart_item = add_item(
        item.product_id,
        item.name,
        item.price,
        item.quantity,
    )

    return {
        "message": "Item added successfully",
        "item": cart_item
    }


@router.get("")
def view_cart():

    return {
        "items": get_cart(),
        "subtotal": calculate_subtotal()
    }