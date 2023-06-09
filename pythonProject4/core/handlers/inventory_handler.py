from schemas.model import Items
from utility.mongo_utlity import collection


def create_item(item: Items):
    collection.insert_one(item.dict())
    return {"message": "Items added successfully"}


def read_items(item_name=str):
    try:
        item = collection.find_one({"name": item_name})
        if item:
            return {"message": "item is available"}
        return {"error occur": "item is not available"}
    except Exception as e:
        return {"error": str(e)}


# def update_items(item_name: str, item: Items):
#     condition = {"item_name": item_name}
#     update = {"$set": {"name": item.name, "price": item.price}}
#     item_instance.update_one(condition, update)
#     return item

# for index, existing_item in enumerate(inventory):
#     db = client.interns_b2_23
#     item_instance = db.subhash
#     item_instance.update_one(item.dict())
#     if existing_item.name == item_name:
#         inventory[index] = item
#         return {"message": "Items updated successfully"}
#     return {"error": "Items not found"}


def update_item(item_name: str, new_item: Items):
    try:
        result = collection.update_one({"name": item_name}, {"$set": new_item.__dict__})
        if result.modified_count > 0:
            return {"message": "item added successfully"}
        return {"error": "item not found"}
    except Exception as e:
        return {"error": str(e)}


def delete_item(item_name: str):
    result = collection.delete_one({"name": item_name})
    if result.deleted_count > 0:
        return {"message": "Item deleted successfully"}
    else:
        return {"error": "Item not found"}





def pipe_line():
    data = [
        {
            '$group': {
                '_id': None,
                'total': {
                    '$sum': '$price'
                }
            }
        }, {
            '$project': {
                '_id': 0
            }
        }
    ]
    datas = collection.aggregate(data)
    data_1 = list(datas)
    print(data_1)
    return {'total price:': data_1[0]['total']}
