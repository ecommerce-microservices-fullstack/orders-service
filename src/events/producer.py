from fastapi import FastAPI
from src.db.models import Order
import logging
import json


async def publish_order_created(app: FastAPI, order: Order):
    producer = app.state.producer

    event = {
        "type": "OrderCreated",
        "order_id": order.id,
        "item_id": order.item_id,
        "qty": order.qty,
    }

    await producer.send_and_wait("order_events", json.dumps(event).encode())
    logging.info(f"Order {order.id} event sent successfully")
