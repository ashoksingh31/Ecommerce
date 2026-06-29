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

    # Verify discount generation is rejected when fewer than 3 orders exist.
def test_generate_discount_before_threshold(api_client):
    add_keyboard(api_client, 1)
    api_client.post("/checkout", json={})

    response = api_client.post("/admin/discount/generate")
    assert response.status_code == 200
    assert response.json()["code"] == ""


# Verify calling generate twice after 3 orders only creates one coupon.
def test_generate_discount_twice_same_interval(api_client):
    for _ in range(3):
        add_keyboard(api_client, 1)
        api_client.post("/checkout", json={})

    api_client.post("/admin/discount/generate")
    response = api_client.post("/admin/discount/generate")

    assert response.json()["code"] == ""

    discounts = api_client.get("/admin/discounts").json()
    assert len(discounts) == 1


# Verify discount codes used count increments correctly in stats.
def test_stats_discount_codes_used(api_client):
    for _ in range(3):
        add_keyboard(api_client, 1)
        api_client.post("/checkout", json={})

    coupon = api_client.post("/admin/discount/generate").json()["code"]

    add_keyboard(api_client, 2)
    api_client.post("/checkout", json={"discount_code": coupon})

    response = api_client.get("/admin/stats")
    assert response.json()["discount_codes_used"] == 1
    assert response.json()["discount_codes_generated"] == 1



    # Verify orders list returns status field on each order.
def test_orders_have_status(api_client):
    add_keyboard(api_client, 1)
    api_client.post("/checkout", json={})

    response = api_client.get("/admin/orders")
    assert response.json()[0]["status"] == "confirmed"