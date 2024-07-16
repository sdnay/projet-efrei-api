from ..models import Items


def get_item_by_id(id):
    try:
        return Items.objects.get(pk=id).serialize()
    except Items.DoesNotExist:
        return None


def update_item(id, data):
    try:
        item = Items.objects.get(pk=id)
        for key, value in data.items():
            setattr(item, key, value)
        item.save()
        return {'success': True, 'message': 'Item changed', 'item': item.serialize()}
    except Items.DoesNotExist:
        return {'success': False, 'message': 'Item not found'}


def delete_item(id):
    try:
        item = Items.objects.get(pk=id)
        item.delete()
        return True
    except Items.DoesNotExist:
        return False
