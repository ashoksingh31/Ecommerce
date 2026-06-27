from fastapi import APIRouter

from app.schemas import (
    StatsResponse,
    DiscountResponse,
)

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


@router.post("/discount/generate", response_model=DiscountResponse)
def generate_coupon():

    if not should_generate_discount():
        return DiscountResponse(
            message="Discount generation condition not met",
            code="",
            percentage=0,
        )

    coupon = generate_discount_code()

    return DiscountResponse(
        message="Coupon generated successfully",
        code=coupon.code,
        percentage=coupon.percentage,
    )


@router.get("/stats", response_model=StatsResponse)
def get_stats():

    return StatsResponse(
        total_orders=stats.total_orders,
        total_items_sold=stats.total_items_sold,
        total_revenue=stats.total_revenue,
        total_discount_given=stats.total_discount_given,
        discount_codes_generated=stats.discount_codes_generated,
        discount_codes_used=stats.discount_codes_used,
    )


@router.get("/orders")
def get_orders():
    return orders


@router.get("/discounts")
def get_discounts():
    return list(discount_codes.values())