class inventory:
    add_items = "/add_items/welcome to grocery"
    view_items = "/getItemByName/{item_name}/"
    update_items = "/item/{item_name}"
    delete_items = "/deleteItemsByName/{item_name}"
    send_email = "/send_email"
    total_price = "/total_price"


from configuration.application_conf import Database

