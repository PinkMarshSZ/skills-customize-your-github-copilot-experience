from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="FastAPI Starter")


class Item(BaseModel):
    id: int
    name: str
    description: Optional[str] = None


items = {}


@app.get("/")
def read_root():
    return {"message": "Welcome to FastAPI starter!"}


@app.get("/items/{item_id}")
def read_item(item_id: int):
    return items.get(item_id, {"error": "Not found"})


@app.post("/items/")
def create_item(item: Item):
    items[item.id] = item.dict()
    return items[item.id]


if __name__ == "__main__":
    import uvicorn

    uvicorn.run("starter-code:app", host="127.0.0.1", port=8000, reload=True)
