from pydantic import BaseModel

class ItemCreate(BaseModel):
    name: str
    price: float
    description: str

class ItemResponse(ItemCreate):
    id: int

    class Config:
        orm_mode = True
