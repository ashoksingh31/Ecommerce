import random
import string

from app.models import DiscountCode
from app.storage import (
    discount_codes,
    stats,
    ORDER_INTERVAL,
    DISCOUNT_PERCENTAGE,
)


def _generate_code(length=8):
    return "".join(
        random.choices(
            string.ascii_uppercase + string.digits,
            k=length,
        )
    )


def should_generate_discount():

    current_orders = stats["total_orders"]

    return (
        current_orders != 0
        and current_orders % ORDER_INTERVAL == 0
        and stats["last_discount_order"] != current_orders
    )


def generate_discount_code():

    code = _generate_code()

    while code in discount_codes:
        code = _generate_code()

    coupon = DiscountCode(
        code=code,
        percentage=DISCOUNT_PERCENTAGE,
    )

    discount_codes[code] = coupon

    stats["discount_codes_generated"] += 1
    stats["last_discount_order"] = stats["total_orders"]

    return coupon


def validate_discount(code):

    if code is None:
        return None

    coupon = discount_codes.get(code)

    if coupon is None:
        return None

    if coupon.used:
        return None

    return coupon


def mark_discount_used(code):

    coupon = discount_codes.get(code)

    if coupon:
        coupon.used = True
        stats["discount_codes_used"] += 1