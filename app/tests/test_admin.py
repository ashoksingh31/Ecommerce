from app.tests.helpers import add_keyboard


# Verify admin statistics reflect completed orders.
def test_admin_stats(api_client):

    add_keyboard(api_client, 5)

    api_client.post("/checkout", json={})

    response = api_client.get("/admin/stats")

    assert response.status_code == 200

    data = response.json()

    assert data["total_orders"] == 1
    assert data["total_items_sold"] == 5
    assert data["total_revenue"] == 5000


# Verify generated discount codes are listed correctly.
def test_discount_list(api_client):

    for _ in range(3):
        add_keyboard(api_client, 1)
        api_client.post("/checkout", json={})

    api_client.post("/admin/discount/generate")

    response = api_client.get("/admin/discounts")

    assert response.status_code == 200

    discounts = response.json()

    assert len(discounts) == 1
    assert discounts[0]["percentage"] == 10


# Verify completed orders are returned by the admin API.
def test_orders_list(api_client):

    add_keyboard(api_client, 5)

    api_client.post("/checkout", json={})

    response = api_client.get("/admin/orders")

    assert response.status_code == 200

    orders = response.json()

    assert len(orders) == 1
    assert orders[0]["subtotal"] == 5000
    assert orders[0]["total"] == 5000