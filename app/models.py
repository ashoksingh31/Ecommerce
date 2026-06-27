from dataclasses import dataclass
from typing import List, Optional


@dataclass
class CartItem:
    product_id: int
    name: str
    price: float
    quantity: int


@dataclass
class DiscountCode:
    code: str
    percentage: int
    used: bool = False


@dataclass
class Order:
    order_id: int
    items: List[CartItem]
    subtotal: float
    discount: float
    total: float
    discount_code: Optional[str] = None


@dataclass
class Stats:
    total_orders: int = 0
    total_items_sold: int = 0
    total_revenue: float = 0
    total_discount_given: float = 0
    discount_codes_generated: int = 0
    discount_codes_used: int = 0
    last_discount_order: int = 0