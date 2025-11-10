from fastapi import FastAPI
from app.routes import item

app = FastAPI()

#include API router
app.include_router(item.router)

@app.get("/")
async def read_root():
    return {"message": "Hello Maureen, FastAPI is running 🚀"}


