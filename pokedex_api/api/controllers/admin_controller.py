# controllers/admin_controller.py

from django.http import JsonResponse
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from ..services import admin_service
from ..utils.permissions import IsAdminUserCustom


@api_view(['GET'])
@permission_classes([IsAdminUserCustom])
def list_users(request):
    if not request.user.is_authenticated:
        return Response({"message": "Authentication required"}, status=401)
    elif request.user.is_authenticated :
        users = admin_service.get_all_users()
        return JsonResponse(users, safe=False, status=200)
    else:
        return Response({"message": "Unauthorized"}, status=403)
