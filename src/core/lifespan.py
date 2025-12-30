from fastapi import FastAPI
from aiokafka import AIOKafkaProducer, AIOKafkaConsumer
import asyncio
from contextlib import asynccontextmanager
from src.core.config import Settings
from src.events.consumer import consume_inventory_events

@asynccontextmanager
async def lifespan(app: FastAPI):
    loop = asyncio.get_event_loop()

    producer = AIOKafkaProducer(
        bootstrap_servers=Settings().kafka_bootstrap,
        loop=loop
    )

    consumer = AIOKafkaConsumer(
        "inventory_events",
        bootstrap_servers=Settings().kafka_bootstrap,
        group_id="order-service",
        loop=loop
    )

    await producer.start()
    await consumer.start()
    
    app.state.producer = producer
    app.state.consumer = consumer

    loop.create_task(consume_inventory_events(consumer))
    
    yield
    
    await producer.stop()
    await consumer.stop()