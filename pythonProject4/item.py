from fastapi import FastAPI
from pydantic import BaseModel
from pymongo import MongoClient

# Creating instance of mongo client
client = MongoClient("mongodb://intern_23:intern%40123@192.168.0.220:2717/interns_b2_23")

# Define a Pydantic model for items
class Item(BaseModel):
    name: str
    description: str
    price: float

app = FastAPI()

# POST endpoint for adding items to inventory
@app.post("/add_items")
def create_item(item: Item):
    db = client.interns_b2_23
    item_instance = db.subhash
    item_instance.insert_one(item.dict())
    return {"message": "Item added successfully"}

# GET endpoint for retrieving items by name
@app.get("/getItemByName/{item_name}")
def read_item(item_name: str):
    db = client.interns_b2_23
    item_instance = db.subhash
    item = item_instance.find_one({"name": item_name})
    if item:
        return {"item details": item}
    else:
        return {"error": "Item not found"}

# PUT endpoint for updating items by name
@app.put("/item/{item_name}")
def update_item(item_name: str, item: Item):
    db = client.interns_b2_23
    item_instance = db.subhash
    condition = {"name": item_name}
    update = {"$set": item.dict()}
    result = item_instance.update_one(condition, update)
    if result.modified_count > 0:
        return {"message": "Item updated successfully"}
    else:
        return {"error": "Item not found"}

# DELETE endpoint for deleting items by name
@app.delete("/deleteItemsByName/{item_name}")
def delete_item(item_name: str):
    db = client.interns_b2_23
    item_instance = db.subhash
    result = item_instance.delete_one({"name": item_name})
    if result.deleted_count > 0:
        return {"message": "Item deleted successfully"}
    else:
        return {"error": "Item not found"}
