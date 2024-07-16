# api/repositories/move_repository.py
from ..models import Move


def get_move_by_id(id):
    try:
        return Move.objects.get(pk=id).serialize()
    except Move.DoesNotExist:
        return None


def update_move(id, data):
    try:
        move = Move.objects.get(pk=id)
        for key, value in data.items():
            setattr(move, key, value)
        move.save()
        return {'success': True, 'move': move.serialize(),   'message': 'Move changed'}
    except Move.DoesNotExist:
        return {'success': False, 'message': 'Move not found'}


def delete_move(id):
    try:
        move = Move.objects.get(pk=id)
        move.delete()
        return True
    except Move.DoesNotExist:
        return False
