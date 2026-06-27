from fastapi import APIRouter
from app.schemas import AddItemRequest
from app.services.cart_service import add_item, get_cart

router = APIRouter()


@router.post("/items")
def add_item_to_cart(item: AddItemRequest):
    added_item = add_item(
        product_id=item.product_id,
        name=item.name,
        price=item.price,
        quantity=item.quantity,
    )

    return {
        "message": "Item added to cart",
        "item": added_item
    }


@router.get("")
def view_cart():
    return get_cart()