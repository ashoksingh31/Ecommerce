from fastapi import APIRouter, HTTPException

from app.schemas import (
    CheckoutRequest,
    CheckoutResponse,
)
from app.services.checkout_service import checkout

router = APIRouter()


@router.post("", response_model=CheckoutResponse)
def checkout_cart(request: CheckoutRequest):
    try:
        order = checkout(request.discount_code)

        return CheckoutResponse(
            message="Order placed successfully",
            order_id=order.order_id,
            subtotal=order.subtotal,
            discount=order.discount,
            total=order.total,
        )

    except ValueError as e:
        raise HTTPException(
            status_code=400,
            detail=str(e),
        )