from fastapi import APIRouter, HTTPException
from app.schema.item import ItemCreate, ItemResponse
import requests

router = APIRouter(prefix="/items", tags=["Items"])

items_db = []
item_id_counter = 1  


@router.get("/", response_model=list[ItemResponse])
def get_items():
    return items_db


@router.post("/", response_model=ItemResponse)
def create_item(item: ItemCreate):
    global item_id_counter  
    item_data = item.dict()
    item_data["id"] = item_id_counter
    item_id_counter += 1
    items_db.append(item_data)
    return item_data


@router.patch("/{item_id}", response_model=ItemResponse)
def update_item(item_id: int, item: ItemCreate):
    for db_item in items_db:
        if db_item["id"] == item_id:
            db_item.update(item.dict(exclude_unset=True))
            return db_item
    raise HTTPException(status_code=404, detail="Item not found")


@router.delete("/{item_id}")
def delete_item(item_id: int):
    for index, db_item in enumerate(items_db):
        if db_item["id"] == item_id:
            items_db.pop(index)
            return {"message": f"Item {item_id} deleted successfully"}
    raise HTTPException(status_code=404, detail="Item not found")


@router.get("/filter", response_model=list[ItemResponse])
def filter_items(max_price: float | None = None, keyword: str | None = None):
    filtered = items_db

   
    if max_price is not None:
        filtered = [item for item in filtered if item["price"] <= max_price]
    if keyword:
        keyword = keyword.lower()
        filtered = [
            item for item in filtered
            if keyword in item["name"].lower() or keyword in item["description"].lower()
        ]

    print("Filtered results:", filtered)
    return filtered
