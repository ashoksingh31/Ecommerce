from typing import Optional, List
from pydantic import BaseModel, Field


class AddItemRequest(BaseModel):
    product_id: int
    name: str
    price: float = Field(gt=0)
    quantity: int = Field(gt=0)


class CartItemResponse(BaseModel):
    product_id: int
    name: str
    price: float
    quantity: int


class CartResponse(BaseModel):
    items: List[CartItemResponse]
    subtotal: float


class CheckoutRequest(BaseModel):
    discount_code: Optional[str] = None


class CheckoutResponse(BaseModel):
    message: str
    order_id: int
    subtotal: float
    discount: float
    total: float


class DiscountResponse(BaseModel):
    message: str
    code: str
    percentage: int


class StatsResponse(BaseModel):
    total_orders: int
    total_items_sold: int
    total_revenue: float
    total_discount_given: float
    discount_codes_generated: int
    discount_codes_used: int