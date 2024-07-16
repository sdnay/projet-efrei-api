# api/controllers/item_controller.py
from rest_framework.decorators import api_view
from rest_framework.response import Response
from ..services import item_service


@api_view(['GET'])
def item_detail(request, id):
    item = item_service.get_item_by_id(id)
    if item:
        return Response(item, status=200)
    return Response({'message': 'Item not found'}, status=404)


@api_view(['PUT'])
def update_item(request, id):
    result = item_service.update_item(id, request.data)
    return Response(result, status=200 if result['success'] else 400)


@api_view(['DELETE'])
def delete_item(request, id):
    result = item_service.delete_item(id)
    return Response({'message': 'Deleted' if result else 'Item not found'}, status=200 if result else 404)
