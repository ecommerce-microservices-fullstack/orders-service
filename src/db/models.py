from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, String


Base = declarative_base()


class Order(Base):
    __tablename__ = "order"

    id = Column(Integer, primary_key=True, index=True)
    item_id = Column(Integer)
    qty = Column(Integer)
    status = Column(String(100))
