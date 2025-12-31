from pydantic import BaseModel


class ItemSchema(BaseModel):
    item_id: int
    qty: int
