# api/controllers/move_controller.py
from rest_framework.decorators import api_view
from rest_framework.response import Response
from ..services import move_service


@api_view(['GET'])
def move_detail(request, id):
    move = move_service.get_move_by_id(id)
    if move:
        return Response(move, status=200)
    return Response({'message': 'Move not found'}, status=404)


@api_view(['PUT'])
def update_move(request, id):
    result = move_service.update_move(id, request.data)
    return Response(result, status=200 if result['success'] else 400)


@api_view(['DELETE'])
def delete_move(request, id):
    result = move_service.delete_move(id)
    return Response({'message': 'Deleted' if result else 'Move not found'}, status=200 if result else 404)
