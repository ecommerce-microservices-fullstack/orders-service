from fastapi import FastAPI
from prometheus_fastapi_instrumentator import Instrumentator
from src.core.lifespan import lifespan
from src.api.routes_orders import router as orders_router

app = FastAPI(lifespan=lifespan)

app.include_router(orders_router, prefix="/api/v1")

Instrumentator().instrument(app).expose(app)
