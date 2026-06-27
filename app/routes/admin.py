from fastapi import APIRouter

from app.storage import (
    stats,
    orders,
    discount_codes,
)

from app.services.discount_service import (
    generate_discount_code,
    should_generate_discount,
)

router = APIRouter()


@router.post("/discount/generate")
def generate_coupon():

    if not should_generate_discount():
        return {
            "message": "Discount generation condition not met"
        }

    coupon = generate_discount_code()

    return {
        "message": "Coupon generated",
        "coupon": coupon
    }


@router.get("/stats")
def get_stats():
    return stats


@router.get("/orders")
def get_orders():
    return orders


@router.get("/discounts")
def get_discounts():
    return list(discount_codes.values())