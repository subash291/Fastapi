from fastapi import APIRouter
from schemas.model import Items, Email
from core.handlers.inventory_handler import create_item, read_items, update_item, delete_item, pipe_line
from scripts.constants.app_constants import inventory
from core.handlers.email_handler import send_email

storage_router = APIRouter()


@storage_router.post(inventory.add_items)
def goods(item: Items):
    return create_item(item)


@storage_router.get(inventory.view_items)
def goods(item_name=str):
    return read_items(item_name)


@storage_router.put(inventory.update_items)
def goods(item_name: str, new_item: Items):
    return update_item(item_name, new_item)


@storage_router.delete(inventory.delete_items)
def goods(item_name: str):
    return delete_item(item_name)


@storage_router.post(inventory.send_email)
def feature(email: Email):
    total_item = pipe_line()
    return send_email(email, str(total_item))


@storage_router.get(inventory.total_price)
def pipe():
    return pipe_line()
