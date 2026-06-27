def add_keyboard(client, quantity):

    return client.post(
        "/cart/items",
        json={
            "product_id": 1,
            "name": "Keyboard",
            "price": 1000,
            "quantity": quantity,
        },
    )