import json
from src.events.handlers_inventory import handle_inventory_event


async def consume_inventory_events(consumer):
    async for msg in consumer:
        event = json.loads(msg.value.decode())
        await handle_inventory_event(event)
