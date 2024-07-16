# api/services/item_service.py
from ..repositories import item_repository


def get_item_by_id(id):
    return item_repository.get_item_by_id(id)


def update_item(id, data):
    return item_repository.update_item(id, data)


def delete_item(id):
    return item_repository.delete_item(id)
