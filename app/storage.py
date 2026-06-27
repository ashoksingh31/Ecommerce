from app.models import (
    CartItem,
    Order,
    DiscountCode,
    Stats,
)

cart: list[CartItem] = []

orders: list[Order] = []

discount_codes: dict[str, DiscountCode] = {}

stats = Stats()

ORDER_INTERVAL = 3

DISCOUNT_PERCENTAGE = 10