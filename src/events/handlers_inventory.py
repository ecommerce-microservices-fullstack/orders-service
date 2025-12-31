from src.db.session import SessionLocal
from src.metrics.orders import orders_failed_total, orders_success_total
from src.metrics.database import db_write_latency, db_read_latency
from src.db.models import Order
import logging


async def handle_inventory_event(event):
    if event["type"] == "InventoryFailed":
        orders_failed_total.inc()
        await _mark_order_failed(event)

    elif event["type"] == "InventoryReserved":
        orders_success_total.inc()


async def _mark_order_failed(event):
    async with SessionLocal() as db:
        with db_read_latency.time():
            order = await db.get(Order, event["order_id"])

        if order:
            with db_write_latency.time():
                order.status = f"Failed. Reason: {event.get('reason', 'Unknown')}"
                await db.commit()
            logging.info(f"Updated order {order.id} to failed")

        else:
            logging.info(f"Order {event['order_id']} not found for rollback")
