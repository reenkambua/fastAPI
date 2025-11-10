from pydantic import BaseModel
from typing import Optional

# ItemBase → shared fields

class ItemBase(BaseModel):
    name: str
    price: float
    description: Optional[str] = None

class ItemCreate(ItemBase):
    pass  # For future use, e.g., additional validations

class ItemResponse(ItemBase):
    id: int  # We'll use this when we have DB entries

    class Config:
        orm_mode = True  # Required to read SQLAlchemy models