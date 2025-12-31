from src.db.models import Order
from sqlalchemy.ext.asyncio import AsyncSession
from src.schemas.order_schema import ItemSchema
from src.metrics.database import db_write_latency, db_read_latency


async def create_order(db: AsyncSession, request: ItemSchema):
    with db_write_latency.time():
        order = Order(item_id=request.item_id, qty=request.qty, status="created")
        db.add(order)
        await db.commit()

    with db_read_latency.time():
        await db.refresh(order)

    return order
