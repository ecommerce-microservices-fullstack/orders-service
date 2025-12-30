from fastapi import APIRouter, Depends, Request
from sqlalchemy.ext.asyncio import AsyncSession
from src.schemas.order_schema import ItemSchema
from src.db.session import get_db
from src.db.crud_orders import create_order
from src.events.producer import publish_order_created
from src.metrics.orders import orders_total
import logging

router = APIRouter()

@router.post("/order")
async def make_order(request: Request, body: ItemSchema, db: AsyncSession = Depends(get_db)):
    order = await create_order(db, body)

    orders_total.inc()
    logging.info(f"Order {order.id} was created successfully")
    await publish_order_created(request.app, order)
    
    return {"status": "Order created", "order_id": order.id}