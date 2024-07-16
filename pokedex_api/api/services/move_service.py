# api/services/move_service.py
from ..repositories import move_repository


def get_move_by_id(id):
    return move_repository.get_move_by_id(id)


def update_move(id, data):
    return move_repository.update_move(id, data)


def delete_move(id):
    return move_repository.delete_move(id)
