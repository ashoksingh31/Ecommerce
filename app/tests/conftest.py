import pytest

from fastapi.testclient import TestClient

from app.main import app
from app.storage import (
    cart,
    orders,
    discount_codes,
    stats,
)

client = TestClient(app)


@pytest.fixture
def api_client():
    return client


@pytest.fixture(autouse=True)
def reset_storage():

    cart.clear()
    orders.clear()
    discount_codes.clear()

    stats.total_orders = 0
    stats.total_items_sold = 0
    stats.total_revenue = 0
    stats.total_discount_given = 0
    stats.discount_codes_generated = 0
    stats.discount_codes_used = 0
    stats.last_discount_order = 0