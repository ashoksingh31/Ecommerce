from fastapi import APIRouter, HTTPException

from app.schemas import CheckoutRequest
from app.services.checkout_service import checkout

router = APIRouter()


@router.post("")
def checkout_cart(request: CheckoutRequest):
    try:
        order = checkout(request.discount_code)

        return {
            "message": "Order placed successfully",
            "order": order
        }

    except ValueError as e:
        raise HTTPException(
            status_code=400,
            detail=str(e)
        )